#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad status codes

        data = response.json()
        for post in data["data"]["children"]:
            title = post["data"]["title"]
            print(title)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print(None)

subreddit_name = "python"
print(f"Top 10 hot posts in r/{subreddit_name}:")
top_ten(subreddit_name)
