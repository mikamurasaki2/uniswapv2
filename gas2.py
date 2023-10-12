
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

def get_tx(tx):
    chainName = 'eth-mainnet'
    url = f'https://api.covalenthq.com/v1/{chainName}/transaction_v2/{tx}/?&key={API_KEY}'
    return url


if __name__ == '__main__':


    # covalent
    API_KEY = 'ckey_1dcbb4def6f5447493e30f100ea'

    nn = ['tx_offset',
          'gas_offered',
          'gas_spent',
          'gas_price',
          'fees_paid',
          'gas_quote',
          'pretty_gas_quote',
          'gas_quote_rate',
          'block_height',
          'tx_hash',
          ]
    out = ','.join(nn) + '\n'

    tx1 = '0xe1082f2e207dc241f96dd9de2eb3f9ce3957b14e5c862ce52f5fe3843582a659'
    tx2 = '0xa34754ef7e21852ccce0da82d11a68c5cd1345bd4d5ba12484885498155211b3'
    tt = [tx1, tx2]
    for i, tx in enumerate(tt):
        url = get_tx(tx)
        response = requests.get(url)
        res = response.json()
        rr = res['data']['items'][0]
        out1 = ''
        vv = []
        for name in nn:
            vv += [str(rr[name])]
            print(i, name, rr[name])
            print
        out1 = ','.join(vv)
        out += out1 + '\n'
        fn_add('gas2.csv', out)

    pass



