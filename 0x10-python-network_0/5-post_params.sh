#!/bin/bash
# takes a URL, sends a POST request, displays the body of the response
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
