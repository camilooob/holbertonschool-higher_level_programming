#!/usr/bin/python3
"""connect to the github api"""
if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    import sys

    user = sys.argv[1]
    pwd = sys.argv[2]

    r = requests.get(
        'https://api.github.com/user',
        auth=HTTPBasicAuth(user, pwd)
    )

    try:
        data = r.json()
        print(data.get('id'))
    except:
        print("Not a valid JSON")
