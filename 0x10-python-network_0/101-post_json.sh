#!/bin/bash
# Pass a JSON file to post
curl -sH "Content-Type: application/json" -d @"$2" "$1"
