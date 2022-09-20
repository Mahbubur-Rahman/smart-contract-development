from brownie import network
from brownie import accounts
from brownie import config
from brownie import MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

# DECIMALS = 18
# STARTING_PRICE = 2000

DECIMALS = 8
STARTING_PRICE = 200000000000


def deploy_mocks():
    print("Inside deploy_mocks")
    print(f"The active network is  {network.show_active()}")
    print(f"Deploying from Mocks....")
    # If we already have a Mock deployed on whatever network we are working on, we dont need two Mocks deployed
    # So we should check if there is a Mock already deployed
    if len(MockV3Aggregator) <= 0:
        # mock_aggregator = MockV3Aggregator.deploy(18, 2000000000000000000000, {"from": account})
        # mock_aggregator = MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": get_account()})
        mock_aggregator = MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
        print(f"aggregator Object is {mock_aggregator}")
    # price_feed_address = mock_aggregator.address
    # MockV3Aggregator[-1] means the latest deployed MockV3Aggregator contract
    # price_feed_address = MockV3Aggregator[-1].address
    print(f"Mocks Depoyed!!")
    # print(f"Mocks Depoyed at {price_feed_address}")


def get_account():
    print("Inside get_account")
    print(
        f"From helpful_script.py. Current network is {network.show_active()}")
    # if(network.show_active() == "development"):
    # if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
