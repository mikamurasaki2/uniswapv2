
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


def fn_write(file_name: str, html: str) -> None:
   with open (file_name, 'w', encoding='utf-8') as f:
       f.write(html)

def fn_add(file_name: str, html: str) -> None:
   with open (file_name, 'a', encoding='utf-8') as f:
       f.write(html)




if __name__ == '__main__':

    sg = Subgrounds()

    #aave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')

    us2 =  sg.load_subgraph('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2')

#    latest = aave_v2.Query.markets(
#        orderBy=aave_v2.Market.totalValueLockedUSD,
#        orderDirection='desc',
#        first=5,
#    )

    latest = us2.Query.transactions(
        first=5,
    )


    df = sg.query_df([
        latest.id,
    ])

    print(df)

    df.to_csv('us2.csv', index=False)

    pass


