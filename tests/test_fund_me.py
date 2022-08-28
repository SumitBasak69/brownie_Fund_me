from brownie import FundMe, accounts, exceptions
from scripts.functions import get_account, get_address, live_or_not
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    Fund_Me = FundMe.deploy(get_address(account), {"from": account})
    entrance_fee = Fund_Me.getEntranceFee()
    tx = Fund_Me.fund({"value": entrance_fee, "from": account})
    tx.wait(1)
    assert Fund_Me.getaddresstoamt(account.address) == entrance_fee
    tx2 = Fund_Me.withdraw({"from": account})
    tx2.wait(1)
    assert Fund_Me.getaddresstoamt(account.address) == 0


def test_only_onwer_can_withdarw():
    if live_or_not():
        pytest.skip("Only For Local Testing...")
    account = get_account()
    Fund_Me = FundMe.deploy(get_address(account), {"from": account})
    entrance_fee = Fund_Me.getEntranceFee()
    tx = Fund_Me.fund({"value": entrance_fee, "from": account})
    tx.wait(1)
    account2 = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        tx2 = Fund_Me.withdraw({"from": account2})
        tx2.wait(1)
