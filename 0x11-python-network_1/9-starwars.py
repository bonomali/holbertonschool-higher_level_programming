#!/usr/bin/python3
"""takes in a string and sends a search request to the Star Wars API"""


import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get("https://swapi.co/api/people/?search={}"
                       .format(argv[1]))
    rjson = req.json()
    print("Number of results: {}".format(rjson["count"]))

    for item in rjson["results"]:
        print(item["name"])
