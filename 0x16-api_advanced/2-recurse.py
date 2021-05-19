#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """Refactored prototype to make recursive"""
    try:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        res = get(url, headers={'User-agent': 'Mozilla/5.0'},
                  params={'after': after},
                  allow_redirects=False).json()
        after = res['data']['after']
        for item in res['data']['children']:
            hot_list.append(item['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list if len(hot_list).__gt__(0) else None
    except:
        return None
