from brownie import accounts, Arbitrage, MockERC20, MockUniswapV2Router


def test_deploys_arbitrage_contract():
    arbitrage = Arbitrage.deploy({"from": accounts[0]})
    assert arbitrage.address


def test_approve_handlers_sets_allowance():
    owner = accounts[0]
    arbitrage = Arbitrage.deploy({"from": owner})
    token = MockERC20.deploy("Mock", "MCK", 18, {"from": owner})
    router = MockUniswapV2Router.deploy({"from": owner})

    arbitrage.approveHandlers([token.address], [router.address], {"from": owner})

    assert token.allowance(arbitrage.address, router.address) == 2**256 - 1


def test_profit_swap_simulates_uniswap_v2():
    owner = accounts[0]
    arbitrage = Arbitrage.deploy({"from": owner})
    token_in = MockERC20.deploy("TokenIn", "TIN", 18, {"from": owner})
    token_out = MockERC20.deploy("TokenOut", "TOUT", 18, {"from": owner})
    router = MockUniswapV2Router.deploy({"from": owner})

    amount_in = 100
    swap_params = (
        0,
        router.address,
        token_in.address,
        token_out.address,
        0,
        amount_in,
        ([], [], []),
    )

    arbitrage.profitSwap([swap_params], amount_in, {"from": owner})
