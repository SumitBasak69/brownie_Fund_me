from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIORNMENT = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIORMENTS = ["development", "ganache-local"]
DECIMALS = 1
STARTING_PRICE = Web3.toWei(2000, "ether")


def live_or_not():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIORMENTS:
        return True
    else:
        return False


def get_account():
    if not (live_or_not()) or network.show_active() in FORKED_LOCAL_ENVIORNMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def get_address(account):
    if not (live_or_not()):
        print(f"Active Network : {network.show_active()}")
        print("Deploying Mocks...")
        if len(MockV3Aggregator) <= 0:
            mock_aggregator = MockV3Aggregator.deploy(
                DECIMALS, STARTING_PRICE, {"from": account}
            )
            print("Mock Deployed...")
        else:
            print("Mock Already Deployed\nUsing Already Deployed Aggregator...")
            mock_aggregator = MockV3Aggregator[-1]
        return mock_aggregator
    else:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
