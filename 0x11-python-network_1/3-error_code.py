#!/usr/bin/python3
"""description"""

import urllib.request
from sys import argv
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            rd = response.read().decode('utf-8')
            print(rd)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
