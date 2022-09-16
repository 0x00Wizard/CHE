#!/usr/bin/env python3

import scanner

target_url = "https://zsecurity.org/"

vuln_scanner = scanner.Scanner(target_url)

vuln_scanner.crawl()