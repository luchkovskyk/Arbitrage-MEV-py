# Arbitrage bot for Arbitrum chain

This repository uses [brownie-eth](https://eth-brownie.readthedocs.io/en/stable/install.html) and python 3.9.

This arbitrage bot is intended to work on Arbitrum L2 chain.

Please make sure you understand the code before executing it, it is not commented as of now.

## Installation

1. Install Python 3.9
2. Install dependencies: `pip install -r requirements.txt`
3. Verify Brownie is installed: `brownie --version`

## Setup

1. Copy `.env.example` to `.env` and fill in the deployment addresses for the quoter and router contracts referenced in `brownie-config.yaml`
2. Add your private key and RPC URL to the `.env` file
3. Configure the arbitrum-main network using brownie networks
4. Set the amount you want to trade with each token in "amount_min" - [base_tokens.json](base_tokens.json) 

## Security practices

- Use a hardware wallet whenever possible, and keep hot-wallet balances minimal.
- Store secrets in a vault or external secret manager instead of in the repo.
- Never commit private keys or seed phrases to Git. Treat `.env` as a local-only file.
- Prefer environment-based secrets:
  - `PRIVATE_KEY` (direct value).
  - `PRIVATE_KEY_FILE` or `PRIVATE_KEY_PATH` (path to a file containing the key).
  - `PRIVATE_KEY_CMD` (command that returns the key, e.g. a Vault CLI call).

## Usage

1. Deploy the Arbitrage contract with [deploy](scripts/deploy.py)  -> brownie run scripts/deploy.py
2. Send the base tokens with [retrieve_tokens](scripts/retrieve_tokens.py) 
3. Approve handlers using the function approve_handlers in [retrieve_tokens](scripts/retrieve_tokens.py) 
4. Start doing arbitrage with [Arbitrage_detector](scripts/Arbitrage_detector.py)  ->brownie run scripts/Arbitrage_detector.py
5. Once done, retrieve tokens with the function retrieve in [retrieve_tokens](scripts/retrieve_tokens.py) 

### Read-only (simulation) mode

Set `READ_ONLY=true` or pass `--read-only` to scripts that send transactions. This will skip on-chain writes and only simulate/estimate costs. You can also set `READ_ONLY_FROM` (or `mode.read_only_from` in `brownie-config.yaml`) to control the `from` address used for gas estimation.
 

