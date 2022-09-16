#!/usr/bin/env python3

import requests
import re
from urllib.parse import urljoin

target_url = "https://zsecurity.org"
target_links = []


def extract_link(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.text)


def crawl(url):
    href_links = extract_link(url)
    for link in href_links:
        link = urljoin(target_url, link)
        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_url:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)
