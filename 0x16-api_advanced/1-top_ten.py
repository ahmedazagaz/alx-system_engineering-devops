#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts
listed for a given subreddit
"""

import requests
import sys


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'user agent 1.0'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        children = response.json().get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
    else:
        print("None")
