#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

target_url = "localhost"
target_links = []


def extract_link(url):
    response = requests.get(url=url)
    data = response.text

    soup = BeautifulSoup(data, "html.parser")
    return soup.find_all("a")
    # links = [link.get("href") for link in soup.find_all("a")]


def crawl(url):
    href_links = extract_link(url)
    for link in href_links:
        link = urljoin(target_url, link.get("href"))
        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_url:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)

