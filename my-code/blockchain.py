import functools as ft
import pickle

from hash_util import hash_block
from block import Block
from transaction import Transaction
from verification import Verification


MINING_REWARD = 10


class Blockchain:
    def __init__(self, hosting_node_id):
        self.__chain = [Block(index=0, prev_hash='', transactions=[], proof=100)]
        self.__open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id

    def get_chain(self):
        return self.__chain[:]

    def get_open_transactions(self):
        return self.__open_transactions[:]

    def load_data(self):
        try:
            with open('blockchain.p', mode='rb') as f:
                content = pickle.loads(f.read())
                self.__chain = content['chain']
                self.__open_transactions = content['ot']
        except (IOError, IndexError):
            print('File not found or Index error!')
        except (FileExistsError, ValueError):
            print('Handle multiple Error!')
        except:
            print('Wildcard')
        finally:
            print('this always runs')

    def save_data(self):
        try:
            with open('blockchain.p', mode="wb") as f:
                f.write(pickle.dumps(
                    {'chain': self.__chain, 'ot': self.__open_transactions}))
        except IOError:
            print('Save failed!')

    def proof_of_work(self):
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof

    def get_balance(self):
        participant = self.hosting_node
        tx_sender = [[tx.amount for tx in block.transactions
                      if tx.sender == participant] for block in self.__chain]
        tx_sender_open = [
            tx.amount for tx in self.__open_transactions if tx.sender == participant]
        tx_sender.append(tx_sender_open)

        amount_sent = ft.reduce(lambda acc, val: acc +
                                sum(val) if len(val) > 0 else acc, tx_sender, 0)

        tx_recipient = [[tx.amount for tx in block.transactions if tx.recipient ==
                         participant] for block in self.__chain]

        amount_received = ft.reduce(
            lambda acc, val: acc + sum(val) if len(val) > 0 else acc, tx_recipient, 0)

        # return amount_sent, tx_sender, amount_received, tx_recipient
        return amount_received - amount_sent

    def add_transaction(self, recipient, sender, amount=1):
        transaction = Transaction(sender, recipient, amount)
        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            self.save_data()
            return True

        return False

    def mine_block(self):
        last_block = self.__chain[-1]
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        reward_transaction = Transaction(
            'MINING', self.hosting_node, MINING_REWARD)
        combined_transactions = self.__open_transactions[:]
        combined_transactions.append(reward_transaction)
        block = Block(
            index=len(self.__chain),
            prev_hash=hashed_block,
            transactions=combined_transactions,
            proof=proof
        )
        self.__chain.append(block)
        self.__open_transactions = []
        self.save_data()
        return True
