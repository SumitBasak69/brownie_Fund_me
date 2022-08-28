from brownie import FundMe
from scripts.functions import get_account


def fund():
    Fund_Me = FundMe[-1]
    account = get_account()
    entrance_fee = Fund_Me.getEntranceFee({"from": account})
    print(f" Current Entery Fee is {entrance_fee}")
    Fund_Me.fund({"from": account, "value": entrance_fee})


def withdraw():
    Fund_Me = FundMe[-1]
    account = get_account()
    Fund_Me.withdraw({"from": account})


def main():
    fund()
    withdraw()
