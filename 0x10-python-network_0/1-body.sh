#!/bin/bash
# This script sends a GET request to a URL and displays the body of a 200 status code response
curl -sX GET $1 -L
