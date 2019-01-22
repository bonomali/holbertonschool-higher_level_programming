#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""


import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        info = html.decode("utf-8")
        print("Body Response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf-8 content: {}".format(info))
