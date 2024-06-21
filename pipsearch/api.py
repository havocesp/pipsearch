#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PipSearch API module"""
from textwrap import wrap
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
# noinspection PyPackageRequirements
from dateutil.parser import parse as datepase

from pipsearch.utils import wait

_BASE_URL = 'https://pypi.python.org'


def searh_parse(resp: requests.Response, brief=False) -> List[Dict]:
    """Do the parsing of the search response from PyPI.

    :param resp: Response object from requests.
    :param brief: if true, show less information about results.
    :return: List of packages found.
    """
    pkgs = []

    if resp.ok:
        soup = BeautifulSoup(resp.text, 'lxml')
        package_rows = soup.select('ul.unstyled > li')

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
                'description': "\n".join(wrap(pkg_description, width=60, max_lines=5)),
                # 'version': pkg_version,
                # 'date': f'{pkg_date:%Y-%m-%d}'
            }
            if not brief:
                package_data['version'] = pkg_version
            if not brief:
                package_data['date'] = f'{pkg_date:%Y-%m-%d}'

            pkgs.append(package_data)
    return pkgs


def search(term: str, page=1, max_pages=10, brief=False) -> List:
    """ Search for a package in PyPI.

    :param page: page number to start to.
    :param max_pages: max pages to search.
    :param brief: show less information about results.
    :return: list of packages found.
    """
    packages = []

    last_page = 0

    print(f" - [INFO] Searching packages on PyPI that matchs term: \"{term}\"")

    url = f"{_BASE_URL}/search?q={term}&page={page}"

    response = requests.get(url, timeout=(60, 60))
    if response.ok:
        bs = BeautifulSoup(response.text, 'lxml')
        select_result = bs.select_one('a.button:nth-child(6)')
        if select_result:
            last_page = int(select_result.text)

    if last_page and last_page == 0:
        last_page = 1

    if max_pages >= last_page:
        max_pages = last_page

    max_pages += page - 1

    print(f" - [INFO] Page: {page}/{max_pages} - Last page: {last_page}")
    entries = searh_parse(response, brief=brief)

    packages.extend(entries)

    wait()

    while response.ok and page < max_pages:
        page += 1
        print(f" - [INFO] Page: {page}/{max_pages} - Last page: {last_page}")
        url = f"{_BASE_URL}/search?q={term}&page={page}"
        response = requests.get(url, timeout=(60, 60))
        entries = searh_parse(response)
        packages.extend(entries)
        if response.ok:
            wait()
    return sorted(packages, key=lambda k: k['date'], reverse=True)
