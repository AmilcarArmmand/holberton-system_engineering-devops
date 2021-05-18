#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """gets the number of subscribers"""
    try:
        subs = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
               headers={'User-agent': 'my user agent'}, allow_redirects=False).json()
        return subs.get('data').get('subscribers')
    except:
        return 0
