#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """Query the Reddit API to print titles of the first 10 hot posts for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyRedditApp/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print(None)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        print(None)

subreddit_name = "python"
print(f"Top 10 hot posts in r/{subreddit_name}:")
top_ten(subreddit_name)
