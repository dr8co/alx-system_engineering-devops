#!/usr/bin/python3
"""
Module to query the Reddit API, parse the title of all hot articles, and
print a sorted count of given keywords (case-insensitive, delimited by spaces.
"""

import requests


def count_words(subreddit, word_list, after="", word_dict={}):
    """
    Prints a sorted count of given keywords (case-insensitive, delimited by
    spaces.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "dr8c00"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")
    for child in children:
        title = child.get("data").get("title")
        for word in word_list:
            if word.lower() not in word_dict.keys():
                word_dict[word.lower()] = 0
            word_count = title.lower().split().count(word.lower())
            word_dict[word.lower()] += word_count

    if after is None:
        if len(word_dict) == 0:
            return
        for key, value in sorted(word_dict.items(),
                                 key=lambda x: (-x[1], x[0])):
            if value != 0:
                print("{}: {}".format(key, value))
    else:
        return count_words(subreddit, word_list, after, word_dict)
