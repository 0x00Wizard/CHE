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

html_response = BeautifulSoup(response.text, "html.parser")

form_list = html_response.find_all("form")

for form in form_list:
    action = form.get("action")
    method = form.get("method")
    input_name = [item.get("name") for item in form.find_all("input")]
    print(input_name)


