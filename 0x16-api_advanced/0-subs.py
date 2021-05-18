#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """gets the number of subscribers"""
    try:
        subs = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
               headers={'User-agent': 'Mozilla/5.0'}, allow_redirects=False).json()
        return subs.get('data').get('subscribers') if not None else 0
    except:
        return 0
