from brownie import SimpleStorage, accounts, config


def read_contract():
    # print(SimpleStorage[0])
    # -1 as array index gets us the most recent deployment
    simple_storage = SimpleStorage[-1]
    # Whenever we work with the smart contract, we need it's
    # ABI
    # ADDRESS
    print(simple_storage.retrieve())


def main():
    read_contract()
