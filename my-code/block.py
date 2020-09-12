from time import time
from utility.printable import Printable

class Block(Printable):
    def __init__(self, index, prev_hash, transactions, proof, time=time()):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof

    # inherit from Printable
    # def __repr__(self):
    #     # return f'Index: {self.index}, Prev Hash: {self.prev_hash}, Proof: {self.proof}, Transactions: {self.transactions}'

