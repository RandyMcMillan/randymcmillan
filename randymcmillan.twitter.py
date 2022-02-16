#!/usr/bin/env python3

import sys
import os
import importlib as imp
from importlib.resources import read_text
os.environ['PYTHONPATH']
sys.path.append('.')
# sys.path.append('./twitter')
# sys.path.append('./twitter/build')
sys.path.append("/usr/local/lib/python3.7/site-packages")
# sys.path.append("/usr/local/lib/python3.8/site-packages")
# sys.path.append("/usr/local/lib/python3.9/site-packages")
from TwitterAPI import TwitterAPI
# help()

ACCESS_TOKEN_SECRET = os.path.expanduser('./twitter_access_tokens/access_token_secret.txt')
ACCESS_TOKEN = os.path.expanduser('./twitter_access_tokens/access_token.txt')
CONSUMER_API_KEY = os.path.expanduser('./twitter_access_tokens/consumer_api_key.txt')
CONSUMER_API_SECRET_KEY = os.path.expanduser('./twitter_access_tokens/consumer_api_secret_key.txt')
print(ACCESS_TOKEN_SECRET)


def getCredentials(filename):
    f = open(filename)
    global data
    data = f.read()
    f.close()
    return data

cask = getCredentials(CONSUMER_API_SECRET_KEY)
print(cask)
cak  = getCredentials(CONSUMER_API_KEY)
print(cak)
ats  = getCredentials(ACCESS_TOKEN_SECRET)
print(ats)
at   = getCredentials(ACCESS_TOKEN)
print(at)

# https://github.com/geduldig/TwitterAPI
api = TwitterAPI(
    cak,
    cask,
    at,
    ats
)
r = api.request('search/tweets', {'q':'bitcoin'})
for item in r:
        print(item)
