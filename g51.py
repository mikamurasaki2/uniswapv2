
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
import json
import requests

from subgrounds import Subgrounds
from covalent import Client


def fn_write(file_name: str, html: str) -> None:
   with open (file_name, 'w', encoding='utf-8') as f:
       f.write(html)

def fn_add(file_name: str, html: str) -> None:
   with open (file_name, 'a', encoding='utf-8') as f:
       f.write(html)

def tx_df(name):
    df = pd.read_csv(f'TX2/tx_{name}.csv')
    df_block = df['blockNumber'].values
    df_ts = df['timestamp'].values
    df_tx = df['id'].values
    block_ = []
    ts_ = []
    tx_ = []
    usd_ = []
    pool_ = []
    num = 0
    ss = df['swaps'].values
    for i, s in enumerate(ss):
        s = re.sub("'", '"', s)
        j = json.loads(s)
        if not len(j):
            continue
        j = j[0]
        usd = round(float(j['amountUSD']),1)
        pair = j['pair']
        t0 = pair['token0']['symbol']
        t1 = pair['token1']['symbol']
        pool = f'{t0}-{t1}'
        pool_ += [pool]
        usd_ += [usd]
        block_ += [df_block[i]]
        ts_ += [df_ts[i]]
        tx_ += [df_tx[i]]
        num += 1

    df2 = pd.DataFrame({'block': block_,
                           'ts': ts_,
                           'pool': pool_,
                           'usd': usd_,
                           'tx': tx_,
                           })

    df2.to_csv(f'TX22/{name}.csv', index=False)
    return num


if __name__ == '__main__':
    N = 0
    for i in range(3652):
        try:
            num = tx_df(i)
        except:
            continue
        N += num
        print(i, num, N)
    print('N=', N)
    pass