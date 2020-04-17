#!/usr/bin/python3
"""Use the package request"""
if __name__ == "__main__":
    import requests
    import sys

    dic = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=dic)
    print(r.text)
