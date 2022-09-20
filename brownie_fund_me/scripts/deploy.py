from brownie import FundMe, network, config
from brownie import MockV3Aggregator

from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
# from scripts.helpful_scripts import deploy_mocks, get_account


def deploy_fund_me():
    print("Inside deploy_fund_me")
    account = get_account()
    # Pass the price feed address to our fundme contract
    # If we are on a persistent network like Rinkeby, use the associated address
    # Otherwise deploy mocks
    print(f"From deploy.py. Current network is {network.show_active()}")
    # if network.show_active() != "development":
    print(network.show_active())
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # price_feed_address = "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"
        # The below says: Hey! if we are not in development network, poll the address from the config
        price_feed_address = config['networks'][network.show_active(
        )]["eth_usd_price_feed"]

    # There is a different price feedaddress for different network
    # But what if we want to work with development chain
    # The way is called Mocking
    # We have to deploy a new contract and we must have the associated Solidity code for it

    else:
        print("deploy_fund_me : else block")
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        # print(f"Mocks Depoyed!!")
        # print(f"Mocks Depoyed at {price_feed_address}")

    # fund_me = FundMe.deploy(price_feed_address, {'from': account}, publish_source=True)

    fund_me = FundMe.deploy(price_feed_address, {
                            'from': account}, publish_source=config["networks"][network.show_active()].get(
        "verify"))

    print(f"Contract deployed to {fund_me.address}")


def main():
    print("main")
    deploy_fund_me()


# Add a development network in the persistent network list Ethereum
# displayed by below command
# $ brownie networks list
# so that the mock contract we deploy remain in the : build > deployment.
#
# brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=1337
