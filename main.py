#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pipsearch

 - File: /main.py
 - Author: Havocesp <https://github.com/havocesp/pipsearch>
 - Created: 2022-09-10
 -
"""
from argparse import ArgumentParser

from tabulate import tabulate

from pipsearch import ps

if __name__ == '__main__':
    ap = ArgumentParser(description='Search for packages in PyPI')
    ap.add_argument('term', help='Search term')
    args = ap.parse_args()
    results = ps.search(args.term)
    print(tabulate(results, headers='keys', tablefmt='fancy_grid'))
