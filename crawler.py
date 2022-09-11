#!/usr/bin/env python3
import requests

URL = "google.com"


def request(url):
    try:
        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass

# with open("subdomains-wodlist.txt", "r") as wordlist_file:
#     words = [line.strip() for line in wordlist_file]
#     for word in words:
#         test_url = f"{word}.{URL}"
#         response = request(test_url)
#         if response:
#             print(f"[+] Discovered subdomain --> {test_url}")


with open("files-and-dirs-wordlist.txt", "r") as wordlist_file:
    words = [line.strip() for line in wordlist_file]
    for word in words:
        test_url = f"{URL}/{word}"
        response = request(test_url)
        if response:
            print(f"[+] Discovered URL --> {test_url}")
