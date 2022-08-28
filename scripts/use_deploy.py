from brownie import FundMe


def use_FundMe():
    Fund_Me = FundMe[-1]
    print(Fund_Me.owner())


def main():
    use_FundMe()
