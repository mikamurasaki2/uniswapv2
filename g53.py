
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

if __name__ == '__main__':

    df = pd.read_csv('fr1_all.csv')
    pass

    N = 0
    name = f'TX21/0.csv'
    df = pd.read_csv(name)
    for i in range(1000):
        name = f'TX21/{i}.csv'
        if not os.path.exists(name):
            continue
        dfi = pd.read_csv(name)
        df = pd.concat([df, dfi])
        print(i, len(dfi), len(df))

    for i in range(3652):
        name = f'TX22/{i}.csv'
        if not os.path.exists(name):
            continue
        dfi = pd.read_csv(name)
        df = pd.concat([df, dfi])
        print(i, len(dfi), len(df))

    df.to_csv(f'fr_all.csv', index=False)

    pass