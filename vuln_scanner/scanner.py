#!/usr/bin/env python3
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class Scanner:
    def __init__(self, url, link_to_ignore):
        self.session = requests.session()
        self.target_url = url
        self.target_links = []
        self.link_to_ignore = link_to_ignore

    def extract_link(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', response.text)

    def crawl(self, url=None):
        if url is None:
            url = self.target_url
        href_links = self.extract_link(url)
        for link in href_links:
            link = urljoin(url, link)
            if "#" in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links and link not in self.link_to_ignore:
                self.target_links.append(link)
                print(link)
                self.crawl(link)

    def extract_forms(self, url):
        response = self.session.get(url)
        html_response = BeautifulSoup(response.text, "html.parser")
        return html_response.find_all("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        post_url = urljoin(url, action)
        print(post_url)
        method = form.get("method")
        inputs_list = form.find_all("input")
        post_data = {}
        for inputs in inputs_list:
            input_name = inputs.get("name")
            input_type = inputs.get("type")
            input_value = inputs.get("value")
            if input_type == "text":
                input_value = value

            post_data[input_name] = input_value
        if method == "post":
            return requests.post(url=post_url, data=post_data)
        return self.session.get(post_url, params=post_data)

    def run_scanner(self):
        for link in self.target_links:
            forms = self.extract_forms(link)
            for form in forms:
                print(f"[+] Testing form in {form}")

    def test_xss_in_form(self, form, url):
        xss_test_script = "<sCript> alert('test') </scriPt>"
        response = self.submit_form(form, xss_test_script, url)
        if xss_test_script in response.text:
            return True
