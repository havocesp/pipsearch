#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PipSearch API module"""
import re
from typing import List

import requests
from bs4 import BeautifulSoup

_BASE_URL = 'https://pypi.python.org'


def search(term: str) -> List:
    """ Search for a package in PyPI.

    :param term: search term to look for.
    :return: list of packages found.
    """
    url = f"{_BASE_URL}/pypi?:action=search&term={term}"
    response = requests.get(url, timeout=(60, 60))
    soup = None
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        response.raise_for_status()

    package_stable = soup.table
    package_rows = package_stable.find_all('tr', {'class': re.compile(r'odd|even')})

    packages = []
    for package in package_rows:
        package_data_td = package.find_all('td')
        package_data = {
            'name': package_data_td[0].text.replace('\xa0', ' '),
            'link': f"{_BASE_URL}{package_data_td[0].find('a')['href']}",
            'weight': int(package_data_td[1].text),
            'description': package_data_td[2].text
        }
        packages.append(package_data)

    return packages
