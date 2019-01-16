#!/bin/bash
# takes a URL, send GET request, displays body of response
curl -sLX GET "$1"
