#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Query the Reddit API to get the number of subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditApp/1.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return 0

subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"Subscribers of r/{subreddit_name}: {subscribers_count}")
