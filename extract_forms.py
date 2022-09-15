#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "http://128.198.49.198:8102/mutillidae/index.php?page=dns-lookup.php"

response = request(target_url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.prettify())
