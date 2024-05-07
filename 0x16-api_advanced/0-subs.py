#!/usr/bin/python3

"""
This script queries the Reddit API to retrieve the number of subscribers for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively query the Reddit API and return a list containing the titles
    of all hot articles for a given subreddit.
    If no results are found for the given subreddit, return None.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]
        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        return None

subreddit_name = "python"
hot_articles = recurse(subreddit_name)
if hot_articles is not None:
    print("Hot articles in r/{}:".format(subreddit_name))
    for title in hot_articles:
        print(title)
else:
    print("No results found for r/{}.".format(subreddit_name))
