
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



def run_query(uri, query):
    request = requests.post(uri, json={'query': query}, headers={"Content-Type": "application/json"})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(f"Unexpected status code returned: {request.status_code}")



if __name__ == '__main__':

    url = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"
    query0 = '''{ 
        transactions( 
            first: 1000 
            skip: 0 
            where: { 
                blockNumber_gt: "15800000",  
                blockNumber_lt: "15800050" 
            } 
        ) { 
            id 
            blockNumber 
            swaps { 
                amountUSD 
                pair { 
                    token0 { 
                        symbol 
                    } 
                    token1 { 
                        symbol 
                    } 
                } 
            } 
            timestamp 
        } 
  }'''

    #START = 15800500
    START = 15850500
    for i in range(10000):

        b1 = START + i * 50
        b2 = START + i * 50 + 50
        query = query0
        query = re.sub('15800000', str(b1), query)
        query = re.sub('15800050', str(b2), query)

        result = run_query(url, query)

        df = pd.DataFrame(result['data']['transactions'])
        df.to_csv(f'TX2/tx_{i}.csv', index=False)
        print(i, b1, b2, len(df))

    pass