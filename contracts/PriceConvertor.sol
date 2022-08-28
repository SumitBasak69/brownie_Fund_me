//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

library PriceConvertor {
    function getprice(AggregatorV3Interface priceFeed)
        internal
        view
        returns (uint256)
    {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return uint256(price * 1e10);
    }

    function getconversionrate(uint256 ethamt, AggregatorV3Interface priceFeed)
        internal
        view
        returns (uint256)
    {
        uint256 ethprice = getprice(priceFeed);
        uint256 ethtot = (ethprice * ethamt) / 1e18;
        return ethtot;
    }

    function getentrancefee(uint256 MIN_USD, AggregatorV3Interface priceFeed) internal view returns (uint256) {
        uint256 ethprice = getprice(priceFeed);
        uint256 precision = 1e18;
        return ((MIN_USD * precision) / ethprice) + 1;

    }
}
