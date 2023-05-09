#!/usr/bin/python3
"""Module to query the Reddit API and return the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, 0 is returned.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "dr8c00"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
