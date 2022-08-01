from tkinter import PROJECTING
from brownie import accounts, network
# from brownie.network import account

import os
from brownie import config

from brownie import SimpleStorage


def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


# Work with Rinkeby test network through Infura
# VIDEO TIME: 04:53:45 [https://www.youtube.com/watch?v=M576WGiDBdQ]
def deploy_simple_storage_rinkeby_infura():
    print("Inside deploy_simple_storage_rinkeby_infura()")
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    print(simple_storage.retrieve())


# Deploy smart contract with ganache-cli
# Brownie always defaultsto using local ganache cli
# If we dont give Brownie a network to use,
# it will spin up a local Ganache and at the end of the script execution,
# it will tear the Ganache network back down
def deploy_simple_storage_with_ganache_cli():
    # Account created via ganache-cli
    account = accounts[0]
    print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    # brownie is smart enough and it knows that retrieve() is a view function. So it makes a call() not transact()
    print(stored_value)
    # Now lets creates a transaction
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    print(simple_storage.retrieve())

# Create a new account with Brownie:
    # $brownie accounts new my_account
    # Now it will prompt for the private key and password
    # Using this new account from script:
    # account = accounts.load(my_account)
    # It will prompt for the password while executing the script
# Delete an account:
    # $brownie accounts delete testAccount


# Account created via brownie cli
    # account = accounts.load("my_account")
    # print(account)

# Account loaded from brownie-config file using environment variable. It uses "import os"
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)

# Account loaded from brownie-config file without importing  Python's os package
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    # print(config)

def main():
    # deploy_simple_storage()
    deploy_simple_storage_rinkeby_infura()
