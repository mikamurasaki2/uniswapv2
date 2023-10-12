
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

def tx_rf(name):
    df = pd.read_csv(f'TX21/{name}.csv')
    df_block = df['block'].values
    df_ts = df['ts'].values
    df_pool = df['pool'].values
    df_usd = df['usd'].values
    df_tx = df['tx'].values
    N = len(df)
    hh = []
    new = 0
    old = set()
    for i in range(N):
        ts = df_ts[i]
        pool = df_pool[i]
        h = f'{ts}-{pool}'
        hh += [h]
    for i in range(N):
        h = hh[i]
        if h in old:
            continue
        hh2 = hh.copy()
        hh2[i] = ''
        if h in hh2:
            new += 1
            old.add(h)
            print(new, i, h, df_usd[i])
            while h in hh2:
                j = hh2.index(h)
                print(new, j, hh[j], df_usd[j])
                hh2[j] = ''

    return new

if __name__ == '__main__':
    N = 0
    for i in range(1):
        try:
            new = tx_rf(i)
        except:
            continue
        N += new
        print(i, new, N)
    print('N=', N)
    pass