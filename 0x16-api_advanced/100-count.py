#!/usr/bin/python3
"""
Module to query the Reddit API, parse the title of all hot articles, and
print a sorted count of given keywords (case-insensitive, delimited by spaces.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Prints a sorted count of given keywords (case-insensitive, delimited by
    spaces.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "dr8c00"}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params={"after": after})
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            for word in word_list:
                title = post.get("data").get("title").lower()
                if word.lower() in title:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        after = response.json().get("data").get("after")
        if after is None:
            if not len(word_count) > 0:
                print()
                return
            for key, value in sorted(word_count.items(),
                                     key=lambda x: (-x[1], x[0])):
                print("{}: {}".format(key, value))
            return
        return count_words(subreddit, word_list, after, word_count)
    else:
        return
