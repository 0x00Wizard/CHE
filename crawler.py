#!/usr/bin/env python3
import requests

URL = "https://mmmm.google.com"

def request(url):
    try:
        response = requests.get(url=URL)
        print(response)


    except requests.exceptions.ConnectionError:
        pass

