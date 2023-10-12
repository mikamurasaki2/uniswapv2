
# python3 knd_1.py

# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/tutorial/errors.html

import os
import sys
import re
import time
import datetime
import numpy as np
import pandas as pd
import requests

from subgrounds import Subgrounds

from covalent import Client


def fn_write(file_name: str, html: str) -> None:
   with open (file_name, 'w', encoding='utf-8') as f:
       f.write(html)

def fn_add(file_name: str, html: str) -> None:
   with open (file_name, 'a', encoding='utf-8') as f:
       f.write(html)

"""
- `get_pools()`: Get all the pools of a particular DEX. 
    Supports most common DEXs (Uniswap, SushiSwap, etc), 
    and returns detailed trading data (volume, liquidity, 
    swap counts, fees, LP token prices).
    
- `get_pool_by_address()`: Get the 7 day and 30 day time-series data 
    (volume, liquidity, price) of a particular liquidity pool in a DEX. 
    Useful for building time-series charts on DEX trading activity.

- `get_pools_for_token_address()`: Get all pools and the supported DEX 
    for a token. Useful for building a table of top pairs across 
    all supported DEXes that the token is trading on.
    
- `get_address_exchange_balances()`: Return balance of a wallet/contract 
        address on a specific DEX.
        
- `get_network_exchange_tokens()`: Get the balance of a wallet address in a DEX. 
        Useful for finding out user balances locked up in DEX pools.

- `get_supported_dexes()`: Get all the supported DEXs available for the xy=k 
        endpoints, along with the swap fees and factory addresses.
        
- `get_dex_for_pool_address()`: Get the supported DEX given a pool address, 
    along with the swap fees, DEX's logo url, and factory addresses. 
    Useful to identifying the specific DEX to which a pair address is associated.
    
- `get_single_network_exchange_token()`: Get historical daily swap count 
        for a single network exchange token.
        
- `get_transactions_for_account_address()`: Get all the DEX transactions 
    of a wallet. Useful for building tables of DEX activity segmented by wallet.
    
- `get_transactions_for_token_address()`: Get all the transactions of a token 
    within a particular DEX. Useful for getting a per-token view of DEX activity.
    
- `get_transactions_for_exchange()`: Get all the transactions of a particular DEX 
    liquidity pool. Useful for building a transactions history table 
    for an individual pool.
    
- `get_ecosystem_chart_data()`: Get a 7d and 30d time-series chart of DEX activity. 
    Includes volume and swap count.
    
- `get_health_data()`: Ping the health of xy=k endpoints to get the synced 
    block height per chain.

"""


def pools():
    chainName = 'eth-mainnet'
    dexName = 'uniswap_v2'
    url = f'https://api.covalenthq.com/v1/{chainName}/xy=k/{dexName}/pools/?&key={API_KEY}'
    return url

def run_query(uri, query):
    request = requests.post(uri, json={'query': query}, headers={"Content-Type": "application/json"})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Unexpected status code returned: {request.status_code}")



if __name__ == '__main__':

    url = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"
    query = """{
        pairs(first: 1000, skip: 6000, where: {txCount_gt: "1000"}) {
            reserveUSD
            id
            txCount
            volumeUSD
            token0 {
                symbol
            }
            token1 {
                symbol
            }
        }
    }"""

    result = run_query(url, query)

    df = pd.DataFrame(result['data']['pairs'])
    df.to_csv('us1.csv', index=False)

    pass