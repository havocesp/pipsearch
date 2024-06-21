#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pipsearch

 - File: main.py
 - Author: Havocesp <https://github.com/havocesp/pipsearch>
 - Created: 2022-09-10
 -
"""
import sys
from argparse import ArgumentParser

from tabulate import tabulate

from pipsearch import ps


def main(term: str, page, max_pages, brief=False):
    """ Main function

    :param page: Page number to start searching
    :param max_pages: Max pages to search.
    :param brief: Show less information about results.
    :param term: search term to look for in PyPI.
    """
    results = ps.search(term, page, max_pages, brief)
    print(tabulate(results, headers='keys', tablefmt='fancy_grid'))


def run():
    """ Main function """
    parser = ArgumentParser(description='PyPI.org packages search app')
    parser.add_argument('term', type=str, help='Search term to look for in PyPI')
    parser.add_argument('--page', '-p', type=int, default=1, help='Page number to start searching.')
    parser.add_argument('--max-pages', '-m', type=int, default=10, help='Max pages to search')
    parser.add_argument('--brief', '-b', action='store_true', help='Show less information about results')
    args = parser.parse_args()
    main(args.term, args.page, args.max_pages)
    return 0


if __name__ == '__main__':
    sys.exit(run())
