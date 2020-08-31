from hash_util import hash_string_256, hash_block

class Verification:
    @staticmethod
    def valid_proof(transactions, last_hash, proof):
        tx_ordered = [tx.to_ordered_dict() for tx in transactions]
        guess = (str(tx_ordered) + str(last_hash) + str(proof)).encode()
        guess_hash = hash_string_256(guess)
        return guess_hash[:2] == '00'

    @classmethod
    def verify_chain(cls, blockchain):
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if hash_block(blockchain[index-1]) != block.prev_hash:
                return False
            if not cls.valid_proof(block.transactions[:-1], block.prev_hash, block.proof):
                print('Proof of work is invalid')
                return False

        return True

    @staticmethod
    def verify_transaction(transaction, get_balance):
        sender_balance = get_balance()
        return sender_balance >= transaction.amount

    @classmethod
    def verify_transactions(cls, open_transactions, get_balance):
        return all([cls.verify_transaction(tx, get_balance) for tx in open_transactions])
