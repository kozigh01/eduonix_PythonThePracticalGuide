import functools as ft
from hashlib import sha256
from collections import OrderedDict

from hash_util import hash_string_256, hash_block

MINING_REWARD = 10


genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': [],
    'proof': 100
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Mark'
participants = set()


def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    tx_sender_open = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(tx_sender_open)

    amount_sent = ft.reduce(lambda acc, val: acc + sum(val)
                            if len(val) > 0 else acc, tx_sender, 0)

    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]

    amount_received = ft.reduce(
        lambda acc, val: acc + sum(val) if len(val) > 0 else acc, tx_recipient, 0)

    # return amount_sent, tx_sender, amount_received, tx_recipient
    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Get the last block of the blockchain
        Arguments: 
            None
    """
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1):
    transaction = OrderedDict(
        [('sender', sender), ('recipient', recipient), ('amount', amount)])
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(recipient)
        participants.add(sender)
        return True

    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    reward_transaction = OrderedDict(
        [('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
    combined_transactions = open_transactions[:]
    combined_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': combined_transactions,
        'proof': proof
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))

    # returning a tuple, could also use (tx_recipient, tx_amount)
    return tx_recipient, tx_amount


def get_user_choice():
    return input('Your choice: ')


def print_blockchain_elements():
    for block in blockchain:
        print(block)
    # else:
    print('-' * 50)


def print_menu():
    print('Please Choose:')
    print('1: Add a new transactioin value')
    print('2: Mine a new block')
    print('3: Output the blockchain')
    print('4: Display participant')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit loop')
    return get_user_choice()


def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if hash_block(blockchain[index-1]) != block['previous_hash']:
            return False
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of work is invalid')
            return False

    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True
while waiting_for_input:
    user_choice = print_menu()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data  # tuple unpacking
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        print('=== Transactions are all valid: ' + str(verify_transactions()))
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': 'abcd',
                             'index': 99, 'transactions': []}
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick from the list')

    if not verify_chain():
        print('Invalid blockchain')
        waiting_for_input = False

    print(get_balance('Mark'))
    # print('Balance of {}: {:6.2f}'.format('Mark', get_balance('Mark')))
else:
    print('User left!')

print('Done!')
