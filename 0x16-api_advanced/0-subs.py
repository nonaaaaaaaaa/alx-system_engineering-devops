#!/usr/bin/python3

"""
This script queries the Reddit API to retrieve the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 for an invalid subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Add a custom user agent to prevent Too Many Requests error

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

if __name__ == "__main__":
    subreddit = 'learnprogramming'
    print(f"Number of subscribers in r/{subreddit}: {number_of_subscribers(subreddit)}")
