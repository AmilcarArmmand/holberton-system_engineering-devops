#!/usr/bin/python3
"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""
from requests import get


def top_ten(subreddit):
    try:
        resp = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
                   headers={'User-agent': 'Mozilla/5.0'}, params={'limit': 10},
                   allow_redirects=False).json()
        for item in resp['data']['children']:
            print(item['data']['title'])
    except:
        print('None')
