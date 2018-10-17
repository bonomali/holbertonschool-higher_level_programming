#!/usr/bin/python3
import json
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    list = load_from_json_file(filename)
except (ValueError, FileNotFoundError):
    list = []
for i in argv[1:]:
    list.append(i)
save_to_json_file(list, filename)
