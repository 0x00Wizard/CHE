#!/usr/bin/env python3
import requests
import argparse

URL = "google.com"


def request(url):
    try:
        return requests.get("http://" + url)

    except requests.exceptions.ConnectionError:
        pass


def get_subdomain():
    with open("subdomains-wodlist.txt", "r") as wordlist_file:
        words = [line.strip() for line in wordlist_file]
        for word in words:
            print(f"{word}.{URL}")
            test_url = f"{word}.{URL}"
            response = request(test_url)
            if response:
                print(f"[+] Discovered subdomain --> {test_url}")


parser = argparse.ArgumentParser(description='To find subdomain')
parser.add_argument('-d', '--domain', dest='url', help='[+] write domain google.com')

args = parser.parse_args()
print(args.domain)


# with open("files-and-dirs-wordlist.txt", "r") as wordlist_file:
#     words = [line.strip() for line in wordlist_file]
#     for word in words:
#         test_url = f"{URL}/{word}"
#         response = request(test_url)
#         if response:
#             print(f"[+] Discovered URL --> {test_url}")
