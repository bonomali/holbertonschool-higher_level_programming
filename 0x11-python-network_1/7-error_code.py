#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
the body of the response"""


import requests
from sys import argv


if __name__ == "__main__":
    try:
        req = requests.get(argv[1])
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(req.status_code))
