#!/usr/bin/python3
"""
parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, posts=[], count=0, after=''):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    if after:
        query += '&after={}'.format(after)

    url = '?show="all"&limit=100&count={}&after={}'.format(count,
                                                           after)
    headers = {'User-Agent': 'user agent 1.0'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if not response.ok:
        return None

    data = response.json()['data']

    for post in data['children']:
        posts.append(post['data']['title'])

    after = data.get('after')
    dist = data['dist']
    if after:
        count_words(subreddit, word_list, posts, count + dist, after)

    if count == 0:
        result = {}
        word_list = [word.lower() for word in word_list]
        posts = ' '.join(hot_list).lower().split(' ')
        for words in posts:
            for search_word in word_list:
                if word == search_word:
                    result.setdefault(search_word, 0)
                    result[search_word] += 1
        for word, count in sorted(result.items()):
            print("{}: {}".format(word, count))
