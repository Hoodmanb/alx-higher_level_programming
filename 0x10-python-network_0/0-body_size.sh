#!/usr/bin/bash
# takes a url send a request to it
# display the size of the body of the response
curl -s -I "$1" | grep "Content-Length" | cut -d " " -f 2
