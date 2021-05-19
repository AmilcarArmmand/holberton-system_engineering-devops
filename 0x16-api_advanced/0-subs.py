#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """gets the number of subscribers"""
    resp = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers={'User-agent': 'Mozilla/5.0'}, allow_redirects=False)
    data = resp.json().get('data', {'subscribers': 0})
    subs = data.get('subscribers', 0)
    return subs
