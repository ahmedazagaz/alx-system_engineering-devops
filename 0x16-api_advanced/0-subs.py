#!/usr/bin/python3
"""
queries the Reddit API
returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that return the number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Curious_Salt3631)"
    }
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
