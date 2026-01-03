import argparse
from brownie import config, accounts, Arbitrage

from .helpful_scripts import resolve_private_key, resolve_read_only




def deploy(read_only=None):
    if resolve_read_only(config, read_only):
        print("Read-only mode enabled: skipping deploy.")
        return
    account = accounts.add(resolve_private_key(config))
    #print(Arb.abi)
    #mock = web3.eth.contract(address=config["Arb"]["polygon-main"] , abi=Arb.abi)

    #estimated_gas = mock.functions.recoverTokens('0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6').estimateGas({'from':account.address})
    Arbitrage.deploy({'from':account})
    #print(estimated_gas)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--read-only", action="store_true", help="Run without sending transactions.")
    args = parser.parse_args()
    deploy(read_only=args.read_only)
    #print(Arbitrage[0])
