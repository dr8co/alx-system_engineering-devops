#!/usr/bin/python3
"""Module to query the Reddit API and print the titles of the first 10
hot posts listed for a given subreddit.
If a subreddit is invalid, None is printed.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given
    subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "dr8c00"}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params={"limit": 10})
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
