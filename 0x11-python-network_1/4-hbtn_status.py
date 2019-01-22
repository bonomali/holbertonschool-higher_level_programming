#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status using the requests package"""


import requests


if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(req.text))
    print("\t- content: {}".format(type(req.text)))
