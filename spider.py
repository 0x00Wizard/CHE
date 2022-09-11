#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

TARGET_URL = "https://zsecurity.org"


def extract_link(url):
    response = requests.get(url=url)
    data = response.text

    soup = BeautifulSoup(data, "html.parser")
    links = soup.find_all("a")
    # links = [link.get("href") for link in soup.find_all("a")]

    for link in links:
        joined_links = urljoin(TARGET_URL, link.get("href"))
        link_text = [new_item for item in joined_links if TARGET_URL in link and link not in TARGET_URL]

        if TARGET_URL in link and link not in TARGET_URL:
            print(link)


extract_link(TARGET_URL)
