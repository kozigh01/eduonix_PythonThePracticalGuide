blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Adds a value to the blockchain 

        Arguments:
            :transaction_amount: the amount to save in the bc
    """
    if last_transaction == None:
        blockchain.append([[1], transaction_amount])
    else:
        blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return float(input('Your transaction amount please: '))


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
    print('2: Output the blockchain')
    print('h: Manipulate the chain')
    print('q: Quit loop')
    return get_user_choice()


def verify_chain():
    previous_block = []
    for block in blockchain:
        if previous_block == []:
            previous_block = block
            continue
        elif previous_block != block[0]:
            return False
        previous_block = block
    return True


waiting_for_input = True
while waiting_for_input:
    user_choice = print_menu()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick from the list')

    if not verify_chain():
        print('Invalid blockchain')
        waiting_for_input = False
else:
    print('User left!')

print('Done!')
