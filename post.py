#!/usr/bin/env python3

import requests

target_url = "http://testphp.vulnweb.com/login.php"

data = {
    "uname": "test",
    "pass": "test",
    "login": "submit"
}

response = requests.post(target_url, data=data)
print(response.text)
