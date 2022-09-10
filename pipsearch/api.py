#! /usr/bin/python

import re

import requests
from bs4 import BeautifulSoup


def search(term):
	url = f"https://pypi.python.org/pypi?:action=search&term={term}"
	req = requests.get(url)

	soup = BeautifulSoup(req.text, 'html.parser')

	packagestable = soup.table
	packagerows = packagestable.find_all('tr', {'class': re.compile('[odd|even]')})

	packages = list()
	for package in packagerows:
		packagedatatd = package.find_all('td')
		packagedata = {
			'name': packagedatatd[0].text.replace(u'\xa0', ' '),
			'link': f"https://pypi.python.org{packagedatatd[0].find('a')['href']}",
			'weight': int(packagedatatd[1].text),
			'description': packagedatatd[2].text
		}
		packages.append(packagedata)

	return packages
