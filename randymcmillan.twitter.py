#!/usr/bin/env python3
# https://github.com/geduldig/TwitterAPI
import sys
import os
import shutil
import importlib as imp
from importlib.resources import read_text
import time
import blockcypher
os.environ['PYTHONPATH']
sys.path.append('.')
sys.path.append("/usr/local/lib/python3.7/site-packages")
from TwitterAPI import TwitterAPI

millis = int(round(time.time() * 1000))
seconds = int(round(time.time()))

print(os.getcwd())

try:
    # shutil.move(os.path.join(filedir, "pages.html"), os.getcwd())
    shutil.move(os.getcwd()+"/BLOCK_TIME", os.getcwd()+"/OLD_BLOCK_TIME")
except:
    f = open("BLOCK_TIME", "w")
    f.write("" + 0 + "\n")
    f.close()

try:
    block_time = blockcypher.get_latest_block_height(coin_symbol='btc')
    block_height = repr(block_time)
    f = open("BLOCK_TIME", "w")
    f.write("" + block_height + "\n")
    f.close()
    # print(block_time)
    print(block_height)
except:
    block_time = 0
    pass

def getData(filename):
    f = open(filename)
    global data
    data = f.read()
    f.close()
    return data

# def tweetBlockTime():
#     r = api.request('statuses/update', {'status': block_height })
#     if (r.status_code == 200):
#         print('SUCCESS')
#     else:
#         print('FAILURE')

def tweetBlockTime():
    print(block_height)
    print(obt)
    if (block_height != obt):
        r = api.request('statuses/update', {'status': block_height })
        if (r.status_code == 200):
            print('api.request SUCCESS')
        else:
            print('api.request FAILURE')
    else:
        print('tweetBlockTime() FAILURE')

OLD_BLOCK_TIME = os.path.expanduser('./OLD_BLOCK_TIME')

ACCESS_TOKEN_SECRET = os.path.expanduser('./twitter_access_tokens/access_token_secret.txt')
ACCESS_TOKEN = os.path.expanduser('./twitter_access_tokens/access_token.txt')
CONSUMER_API_KEY = os.path.expanduser('./twitter_access_tokens/consumer_api_key.txt')
CONSUMER_API_SECRET_KEY = os.path.expanduser('./twitter_access_tokens/consumer_api_secret_key.txt')
# print(ACCESS_TOKEN_SECRET)

cak  = getData(CONSUMER_API_KEY)
cask = getData(CONSUMER_API_SECRET_KEY)
at   = getData(ACCESS_TOKEN)
ats  = getData(ACCESS_TOKEN_SECRET)
obt  = getData(OLD_BLOCK_TIME)

api  = TwitterAPI(cak,cask,at,ats)

# r = api.request('search/tweets', {'q':'bitcoin'})
# for item in r:
#         print(item)

tweetBlockTime()
