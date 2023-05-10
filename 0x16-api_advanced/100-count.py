#!/usr/bin/python3
"""
Module to query the Reddit API, parse the title of all hot articles, and
print a sorted count of given keywords (case-insensitive, delimited by spaces.
"""

import requests


def count_words(subreddit, word_list, words_found=[], after=None):
    """
    Prints a sorted count of given keywords (case-insensitive, delimited by
    spaces.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "dr8c00"}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params={"after": after})
    if after is None:
        word_list = [word.lower() for word in word_list]

    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            title = post.get("data").get("title").lower()
            for word in title.split(' '):
                if word in word_list:
                    words_found.append(word)
        aft = response.json().get("data").get("after")
        if aft is not None:
            count_words(subreddit, word_list, words_found, aft)
        else:
            result = {}
            for word in words_found:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda x: x[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
