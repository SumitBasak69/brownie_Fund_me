from brownie import FundMe, accounts, network, config
from scripts.functions import get_account, get_address, live_or_not


def deploy_FundMe():
    account = get_account()
    price_feed = get_address(account)

    print("Deploying Contract...")
    Fund_Me = FundMe.deploy(
        price_feed,
        {"from": account},
    )
    print(Fund_Me)


def main():
    deploy_FundMe()
