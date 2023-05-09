#!/usr/bin/python3
"""
Module to query the Reddit API and return a list containing the titles of all
hot articles for a given subreddit.
If no results are found for the given subreddit, None is returned.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles for a given
    subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "dr8c00"}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params={"after": after})
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        after = response.json().get("data").get("after")
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
