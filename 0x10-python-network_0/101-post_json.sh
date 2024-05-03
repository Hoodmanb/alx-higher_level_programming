#!/bin/bash
# sends a JSON POST request to a URLs first argument and displays the body of response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
