#!/usr/bin/env python3

import scanner


target_url = "http://testphp.vulnweb.com/"
data_dict = {"username": "admin", "password": "password", "Login": "submit"}
links_to_ignore = ["logout.php"]
vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post(target_url, data=data_dict)

# vuln_scanner.crawl()

forms = vuln_scanner.extract_forms("http://localhost")
response = vuln_scanner.submit_form(forms[0], "test")