#!/usr/bin/python3
"""Use the package request"""
if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
