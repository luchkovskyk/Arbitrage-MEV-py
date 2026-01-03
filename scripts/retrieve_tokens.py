import argparse
from brownie import config, accounts, interface, Arbitrage
from .helpful_scripts import load_json, resolve_private_key, resolve_read_only


base_tokens = load_json('base_tokens.json')
#Arbitrage = interface.Arb(config["Arb"]["polygon-main"]) 


PROTOCOLS = [
    "UniswapV2", #IUniswapV2Router02
    "UniswapV3",  #ISwapRouter
    "SushiswapV2",
    "SushiswapV3",
    "CamelotV2",
    "CamelotV3", #ISwapRouter_Algebra
    "RamsesV3",
    "TraderjoeV2" #ILBRouter
]

def retrieve(read_only=None):
    if resolve_read_only(config, read_only):
        print("Read-only mode enabled: skipping recoverMyTokens.")
        return
    account = accounts.add(resolve_private_key(config))
    tokens = []
    for token in base_tokens["tokens"]:
        tokens.append(token["address"])

    
    Arbitrage[0].recoverMyTokens(tokens, {"from":account})



def approve_handlers(read_only=None):
    if resolve_read_only(config, read_only):
        print("Read-only mode enabled: skipping approveHandlers.")
        return
    tokens_list = []
    protocols_list = []
    account = accounts.add(resolve_private_key(config))

    for token in base_tokens["tokens"]:
        tokens_list.append(token["address"])

    for protocol in PROTOCOLS:
        protocols_list.append(config["router"][protocol])

    Arbitrage[0].approveHandlers(tokens_list, protocols_list, {"from": account})



def send(read_only=None):
    if resolve_read_only(config, read_only):
        print("Read-only mode enabled: skipping transfers.")
        return
    account = accounts.add(resolve_private_key(config))
    for token in base_tokens["tokens"]:
        IERC20 = interface.IERC20(token["address"])

        balance = IERC20.balanceOf(account.address)
        print(balance)

        if balance !=0:
            tx = IERC20.transfer(Arbitrage[0], balance, {'from': account })
            tx.wait(4)
        else:
            pass


def retrieve_one(read_only=None):
    if resolve_read_only(config, read_only):
        print("Read-only mode enabled: skipping recovermyTokens.")
        return
    account = accounts.add(resolve_private_key(config))
    address = base_tokens["tokens"][5]["address"]
    tx = Arbitrage[0].recovermyTokens(address, {'from': account})



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--read-only", action="store_true", help="Run without sending transactions.")
    args = parser.parse_args()
    send(read_only=args.read_only)
