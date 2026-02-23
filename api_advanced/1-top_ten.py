#!/usr/bin/python3
"""
function that queries the 'Reddit API'
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'linux:alu.api.advanced:v1.0 (by /u/alu_student)'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json().get('data', {})
        children = data.get('children', [])
        for post in children:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)
