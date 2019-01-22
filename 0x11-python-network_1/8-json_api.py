#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


import requests
from sys import argv


if __name__ == "__main__":
    if argv[1] is None:
        letter = ""
    else:
        letter = argv[1]

    values = {'q': letter}
    req = requests.post("http://0.0.0.0:5000/search_user", data=values)

    try:
        rjson = req.json()
        if json:
            print("[{}] {}".format(rjson["id"], rjson["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
