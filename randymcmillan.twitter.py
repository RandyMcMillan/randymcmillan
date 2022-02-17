#!/usr/bin/env python3
# https://github.com/geduldig/TwitterAPI
import sys
import os
import requests
import shutil
import importlib as imp
from importlib.resources import read_text
import time
import blockcypher
import pyjq
os.environ['PYTHONPATH']
sys.path.append('.')
sys.path.append("/usr/local/lib/python3.7/site-packages")
from TwitterAPI import TwitterAPI

# print(os.getcwd())
def moveBlockTime():
    try:
        # shutil.move(os.path.join(filedir, "pages.html"), os.getcwd())
        shutil.move(os.getcwd()+"/BLOCK_TIME", os.getcwd()+"/OLD_BLOCK_TIME")
    except:
        f = open("BLOCK_TIME", "w")
        f.write("" + 0 + "\n")
        f.close()

def blockTime():
    try:
        block_time = blockcypher.get_latest_block_height(coin_symbol='btc')
        block_height = repr(block_time)
        f = open("BLOCK_TIME", "w")
        f.write("" + block_height + "\n")
        f.close()
        return block_time
    except:
        return 0
        pass

def getData(filename):
    f = open(filename)
    global data
    data = f.read()
    f.close()
    return data

def tweetBlockTime(block_time):
    if (block_time != obt):
        r = api.request('statuses/update', {'status': block_time })
        if (r.status_code == 200):
            print('api.request SUCCESS')
        else:
            print('api.request FAILURE')
    else:
        print('tweetBlockTime() FAILURE')

# Example: curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/asdfasdfasdf
#
# import requests
#
# headers = {
#     'Content-type': 'application/json',
# }
#
# data = '{"text":"Hello, World!"}'
#
# response = requests.post('https://hooks.slack.com/services/asdfasdfasdf', headers=headers, data=data)

DIFFICULTY          = os.path.expanduser('./DIFFICULTY')

print(pyjq.all( ".members[] | [.name]", {"members": [ {"name": "foo"} ]} ))

def getMempoolAPI(url,DATA):
    # print(url)
    with open(DATA, 'wb') as f:
        r = requests.get(url, stream=True)
        f.writelines(r.iter_content(1024))
        response = getData(DATA)
        print(getData(DATA))
        print(response)

BLOCK_TIP_HEIGHT        = os.path.expanduser('./BLOCK_TIP_HEIGHT')
DIFFICULTY              = os.path.expanduser('./DIFFICULTY')
OLD_BLOCK_TIME          = os.path.expanduser('./OLD_BLOCK_TIME')
ACCESS_TOKEN_SECRET     = os.path.expanduser('./twitter_access_tokens/access_token_secret.txt')
ACCESS_TOKEN            = os.path.expanduser('./twitter_access_tokens/access_token.txt')
CONSUMER_API_KEY        = os.path.expanduser('./twitter_access_tokens/consumer_api_key.txt')
CONSUMER_API_SECRET_KEY = os.path.expanduser('./twitter_access_tokens/consumer_api_secret_key.txt')

millis  = int(round(time.time() * 1000))
seconds = int(round(time.time()))

cak  = getData(CONSUMER_API_KEY)
cask = getData(CONSUMER_API_SECRET_KEY)
at   = getData(ACCESS_TOKEN)
ats  = getData(ACCESS_TOKEN_SECRET)
obt  = getData(OLD_BLOCK_TIME)

api  = TwitterAPI(cak,cask,at,ats)

def searchBitcoin():
    r = api.request('search/tweets', {'q':'bitcoin'})
    for item in r:
        print(item)

# searchBitcoin()
# print(blockTime())
tweetBlockTime(blockTime())
getMempoolAPI('https://mempool.space/api/v1/difficulty-adjustment', DIFFICULTY)
getMempoolAPI('https://mempool.space/api/blocks/tip/height',        BLOCK_TIP_HEIGHT)
