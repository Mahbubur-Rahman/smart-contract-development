from brownie import FundMe
from scripts.helpful_scripts import get_account


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    price = fund_me.getPrice()
    # 20000000000000000000000000000000
    print(price)
    entrance_fee = fund_me.getEntranceFee()
    print(f'The current entry fee is {entrance_fee}')
    print("Funding....")
    fund_me.fund({"from": account, "value": entrance_fee})


def main():
    fund()
    withdraw()
