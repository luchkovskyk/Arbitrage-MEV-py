// SPDX-License-Identifier: Unlicensed
pragma solidity ^0.8.4;

contract MockUniswapV2Router {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256,
        address[] calldata,
        address,
        uint256
    ) external pure returns (uint256[] memory amounts) {
        amounts = new uint256[](2);
        amounts[0] = amountIn;
        amounts[1] = amountIn + 1;
    }
}
