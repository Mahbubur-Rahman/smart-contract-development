from __future__ import nested_scopes
import json
from eth_typing import Address
from web3 import Web3
from solcx import compile_standard, install_solc
import os
from dotenv import load_dotenv

load_dotenv()


with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)


# @Compile Our Solidity
install_solc("0.6.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

print(compiled_sol)

print("########################################################")
# os.system.exit(0)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = json.loads(
    compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"])["output"]["abi"]

# For connecting to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
# "0xc75f3F4C506A6444Ea40A4325B19f2Fb487262b1"
my_address = "0xc75f3F4C506A6444Ea40A4325B19f2Fb487262b1"
private_key = os.getenv("PRIVATE_KEY")


# Using infura

# w3 = Web3(Web3.HTTPProvider(
#     "https://rinkeby.infura.io/v3/f782d626cb43463e954b7e6ed31d11a8"))
# chain_id = 4
# my_address = "0xAd3d20282088AE9A7b531f359e2294e837CD3EB0"
# # This is metamask account1 private key accuired from account details
# private_key = "11ad9efa6bdb6f060a0f9f10416e66e0864e9826528148a44f99f89dca48d6c4"
# print(private_key)


# Create the contract in Python
# To learn More: https: // web3py.readthedocs.io/en/latest/contracts.html
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorage)
print("########################################################")

# Get the latest transaction
# Getting nonce via the address my_address means:
#  The account address is in a blockchain network
#  There are transactions belonging to the account in that network
#  The below getTransactionCount() function gets the total number of transaction from that ACCOUNT into that NETWORK
#  The Network might be in local Ganache blockchain network or any other public test/main network
#  In case we use any public test/main network. we use the corresponding web3.py's httpprovider for that network
nonce = w3.eth.getTransactionCount(my_address)
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)
print(transaction)
print("########################################################t1")

signed_txn = w3.eth.account.sign_transaction(
    transaction, private_key=private_key)
# print("Deploying Contract!")
# print(transaction)

# Send Transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


# Working with the contract, you always need
# Contract Address
# Contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(simple_storage)
print("########################################################")

# Call -> Simulate making the call and return a value. It does not make a state change in the blockchain
# Transact -> Actually makes state change to the blockchain

# Initial value of a favorite number = 0
print(simple_storage.functions.retrieve().call())

# Call store function to store a value of 15 as a favorite number
print(simple_storage.functions.store(15).call())

# Show the stored favorite number will still be 0 as there was no transaction made
print(simple_storage.functions.retrieve().call())


# Make a store transaction now
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce+1
    }
)
# Sign the transaction
signed_store_transaction = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)

send_store_tx = w3.eth.send_raw_transaction(
    signed_store_transaction.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print(simple_storage.functions.retrieve().call())
