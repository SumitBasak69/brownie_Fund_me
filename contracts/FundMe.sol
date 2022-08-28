//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./PriceConvertor.sol";

error NotOwner();

contract FundMe {
    using PriceConvertor for uint256;

    uint256 public constant MIN_USD = 50 * 1e18;

    address public immutable owner;
    address[] public funders;
    mapping(address => uint256) public addresstoamt;

    AggregatorV3Interface public priceFeed;

    constructor(address priceFeedAddress) {
        owner = msg.sender;
        priceFeed = AggregatorV3Interface(priceFeedAddress);
    }

    receive() external payable {
        fund();
    }

    fallback() external payable {
        fund();
    }

    function fund() public payable {
        require(
            msg.value.getconversionrate(priceFeed) >= MIN_USD,
            "Not Enough ETH"
        );
        funders.push(msg.sender);
        addresstoamt[msg.sender] = msg.value;
    }

    function withdraw() public onlyowner {
        for (uint256 i = 0; i < funders.length; i++)
            addresstoamt[funders[i]] = 0;

        funders = new address[](0);

        (bool callsuccess, ) = payable(msg.sender).call{
            value: address(this).balance
        }("");
        require(callsuccess, "Call Failed");
    }

    function getaddresstoamt(address _sender) public view returns (uint256) {
        return (addresstoamt[_sender]);
    }

    function getEntranceFee() public view returns (uint256) {
        return MIN_USD.getentrancefee(priceFeed);
    }

    modifier onlyowner() {
        //require(owner == msg.sender, "ERROR : SENDER NOT OWNER!!!!!");
        if (msg.sender != owner) {
            revert NotOwner();
        }
        _; //Whole Functions code
    }
}
