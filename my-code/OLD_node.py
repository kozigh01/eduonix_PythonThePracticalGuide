from uuid import uuid4

from utility.verification import Verification
from blockchain import Blockchain

class Node:
    def __init__(self):
        # self.id = str(uuid4())
        self.id = 'MARK'
        self.blockchain = Blockchain(self.id)

    def get_transaction_value(self):
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('Your transaction amount please: '))

        # returning a tuple, could also use (tx_recipient, tx_amount)
        return tx_recipient, tx_amount

    def get_user_choice(self):
        return input('Your choice: ')

    def print_blockchain_elements(self):
        for block in self.blockchain.get_chain():
            print(block)
        # else:
        print('-' * 50)

    def print_menu(self):
        print('Please Choose:')
        print('1: Add a new transactioin value')
        print('2: Mine a new block')
        print('3: Output the blockchain')
        print('4: Check transaction validity')
        print('q: Quit loop')
        return self.get_user_choice()

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            user_choice = self.print_menu()

            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data  # tuple unpacking
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                print('=== Transactions are all valid: ' +
                      str(Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance)))
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Input was invalid, please pick from the list')

            if not Verification.verify_chain(self.blockchain.get_chain()):
                print('Invalid blockchain')
                waiting_for_input = False

            print(f'Balance for {self.id}: {self.blockchain.get_balance()}')
        else:
            print('User left!')

        print('Done!')


node = Node()
node.listen_for_input()