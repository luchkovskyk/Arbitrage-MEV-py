import math
import json
import os
import shlex
import subprocess






def sqrtPricex96toQuote(sqrtPriceX96):
    ratiox192=math.pow(sqrtPriceX96, 2)
    quote=ratiox192/(math.pow(2,192))
    return quote


def find_last_index(data):
  last_seen = {}
  for i, value in enumerate(data):
    last_seen[value] = i  # Update last seen index for the value
  return last_seen





def get_max_excluding_none(data):

  # Filter out None values using filter
  if data == [None]*len(data):
    zeroLength = True
    return [None, zeroLength]
  else:
     zeroLength = False 

  filtered_data = filter(lambda x: x is not None, data)
  filtered_data = list(filtered_data)
  # Use max() on the filtered list, handling potential emptiness
  
  return [max(filtered_data, default=None), zeroLength]
    


def load_json(ruta):
    ruta_real = os.path.join(os.getcwd(), ruta)
    with open(ruta_real, "r") as f:
        datos = json.load(f)
    return datos

def to_readable_amount(amount, decimals):
   readableAmount= amount/(10**decimals)
   return readableAmount

def from_readable_amount(amount, decimals):
   wei= int(amount * (10**decimals))
   return wei


def _as_bool(value):
   if isinstance(value, bool):
      return value
   if value is None:
      return None
   if isinstance(value, (int, float)):
      return bool(value)
   if isinstance(value, str):
      return value.strip().lower() in {"1", "true", "yes", "on"}
   return bool(value)


def resolve_private_key(config=None):
   env_key = os.getenv("PRIVATE_KEY")
   if env_key:
      return env_key.strip()

   key_file = os.getenv("PRIVATE_KEY_FILE") or os.getenv("PRIVATE_KEY_PATH")
   if key_file:
      with open(key_file, "r") as handle:
         return handle.read().strip()

   key_cmd = os.getenv("PRIVATE_KEY_CMD")
   if key_cmd:
      return subprocess.check_output(shlex.split(key_cmd), text=True).strip()

   if config and "wallets" in config and "from_key" in config["wallets"]:
      return config["wallets"]["from_key"]

   raise ValueError("Private key not found. Set PRIVATE_KEY, PRIVATE_KEY_FILE, PRIVATE_KEY_CMD, or config wallets.from_key.")


def resolve_read_only(config=None, cli_value=None):
   cli_bool = _as_bool(cli_value)
   if cli_bool is not None:
      return cli_bool

   env_value = os.getenv("READ_ONLY")
   env_bool = _as_bool(env_value)
   if env_bool is not None:
      return env_bool

   if config and "mode" in config and "read_only" in config["mode"]:
      return _as_bool(config["mode"]["read_only"])

   return False


def resolve_read_only_from(config=None):
   env_value = os.getenv("READ_ONLY_FROM")
   if env_value:
      return env_value

   if config and "mode" in config and "read_only_from" in config["mode"]:
      return config["mode"]["read_only_from"]

   return None
