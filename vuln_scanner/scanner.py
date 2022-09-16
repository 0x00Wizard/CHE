#!/usr/bin/env python3
import requests
import re
from urllib.parse import urljoin

target_url = "https://zsecurity.org/"


class Scanner:
    def __int__(self, url):
        self.target_url = url
        self.target_links = []

    def extract_link(self, url):
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.text)

    def crawl(self, url=None):
        if url is None:
            url = self.target_url
        href_links = self.extract_link(url)
        for link in href_links:
            link = urljoin(url, link)
            if "#" in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)
