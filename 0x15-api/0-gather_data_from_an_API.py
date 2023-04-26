#!/usr/bin/python3
"""
A script that returns information using REST API
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        name = req.json().get("name")
        if name is not None:
            jreq = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            allTasks = len(jreq)
            completed = []
            for t in jreq:
                if t.get("completed") is True:
                    completed.append(t)
            count = len(completed)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, allTasks))
            for title in completed:
                print("\t {}".format(title.get("title")))
