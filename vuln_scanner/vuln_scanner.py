#!/usr/bin/env python3

import scanner

target_url = "https://zsecurity.org/"

vuln_scanner = scanner.Scanner()

vuln_scanner.crawl(target_url)