#!/usr/bin/python3
"""description"""

import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as response:
    rd = response.info()
    print(rd['X-Request-Id'])
