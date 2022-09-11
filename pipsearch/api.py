#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PipSearch API module"""
from typing import List

import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse as datepase

_BASE_URL = 'https://pypi.python.org'


def search(term: str) -> List:
    """ Search for a package in PyPI.

    :param term: search term to look for.
    :return: list of packages found.
    """
    url = f"{_BASE_URL}/search?q={term}"
    response = requests.get(url, timeout=(60, 60))
    soup = None
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        response.raise_for_status()

    package_rows = soup.select('ul.unstyled > li')

    packages = []
    for package in package_rows:
        pkg_name = package.select_one('span.package-snippet__name').text
        pkg_description = package.select_one('p.package-snippet__description').text
        pkg_version = package.select_one('span.package-snippet__version').text
        pkg_url = f"{_BASE_URL}/project/{pkg_name}"
        pkg_date = datepase(package.select_one('time').text.strip('\n\r\t'))

        package_data = {
            'name': pkg_name,
            'link': pkg_url,
            # 'weight': int(package_data_td[1].text),
            'description': pkg_description,
            'version': pkg_version,
            'date': f'{pkg_date:%Y-%m-%d}'
        }
        packages.append(package_data)

    return packages
