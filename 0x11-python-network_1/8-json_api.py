#!/usr/bin/python3
"""python package request"""
if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 1:
        dic = {'q': ""}
    else:
        dic = {'q': sys.argv[1]}

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=dic)
        data = r.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
