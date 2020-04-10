#!/bin/bash
# Print only the http code
curl -so /dev/null -w "%{http_code}" "$1"
