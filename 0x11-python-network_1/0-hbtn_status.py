#!/usr/bin/python3
"""my body header"""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        ty = response.read()
        print("\t- type: {}".format(type(response.read())))
        print("\t- content: {}".format(ty))
        print("\t- utf8 content: {}".format(ty.decode('utf-8')))
