#!/usr/bin/env python3

# https://github.com/geduldig/TwitterAPI
import sys
import os
import hashlib
# import importlib
# from importlib.resources import read_text
# import json
# import pickle
import shutil
import time
import requests
import blockcypher
# import pyjq
# import gnupg

# os.environ['PYTHONPATH']
sys.path.append('.')
sys.path.append("/usr/local/lib/python3.7/site-packages")
from TwitterAPI import TwitterAPI

global CONFIG
CONFIG                  = str('twitter_access_tokens')
global BLOCK_TIP_HEIGHT
BLOCK_TIP_HEIGHT        = os.path.expanduser(os.getcwd()+'/BLOCK_TIP_HEIGHT')
global DIFFICULTY
DIFFICULTY              = os.path.expanduser(os.getcwd()+'/DIFFICULTY')
global OLD_BLOCK_TIME
OLD_BLOCK_TIME          = os.path.expanduser(os.getcwd()+'/OLD_BLOCK_TIME')
global ACCESS_TOKEN_SECRET
ACCESS_TOKEN_SECRET     = os.path.expanduser(os.getcwd()+'/'+CONFIG+'/access_token_secret.txt')
global ACCESS_TOKEN
ACCESS_TOKEN            = os.path.expanduser(os.getcwd()+'/'+CONFIG+'/access_token.txt')
global CONSUMER_API_KEY
CONSUMER_API_KEY        = os.path.expanduser(os.getcwd()+'/'+CONFIG+'/consumer_api_key.txt')
global CONSUMER_API_SECRET_KEY
CONSUMER_API_SECRET_KEY = os.path.expanduser(os.getcwd()+'/'+CONFIG+'/consumer_api_secret_key.txt')
global DIGEST
DIGEST = ""
global DATA
DATA = ""


def getData(filename):
    f = open(filename)
    DATA = f.read()
    f.close()
    return DATA


cak  = getData(CONSUMER_API_KEY)
cask = getData(CONSUMER_API_SECRET_KEY)
at   = getData(ACCESS_TOKEN)
ats  = getData(ACCESS_TOKEN_SECRET)
obt  = getData(OLD_BLOCK_TIME)

api  = TwitterAPI(cak,cask,at,ats)

def moveBlockTime():
    try:
        shutil.move(os.getcwd()+"/BLOCK_TIME", os.getcwd()+"/OLD_BLOCK_TIME")
    except:
        f = open("BLOCK_TIME", "w")
        f.write("" + 0 + "\n")
        f.close()

def getMillis():
    global millis
    millis = int(round(time.time() * 1000))
    return millis

def getSeconds():
    global seconds
    seconds = int(round(time.time()))
    return seconds

def blockTime():
    global block_time
    global block_height
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

def BTC_UNIX_TIME_MILLIS():
    global btc_unix_time_millis
    btc_unix_time_millis = str(blockTime())+":"+str(getMillis())
    return btc_unix_time_millis

def BTC_UNIX_TIME_SECONDS():
    global btc_unix_time_seconds
    btc_unix_time_seconds = str(blockTime())+":"+str(getSeconds())
    return btc_unix_time_seconds

def UNIX_TIME_MILLIS():
    global unix_time_millis
    unix_time_millis = str(getMillis())
    return unix_time_millis

def UNIX_TIME_SECONDS():
    global unix_time_seconds
    unix_time_seconds = str(getSeconds())
    return unix_time_seconds

def BTC_TIME():
    global btc_time
    btc_time = str(blockTime())
    return btc_time

def tweet_blocktime():
    if BTC_TIME() != obt:
        request = api.request('statuses/update', {'status': BTC_UNIX_TIME_MILLIS()})
        if (request.status_code == 200):
            print('api.request SUCCESS')
        else:
            print('api.request FAILURE')
    else:
        print('tweetBlockTime() FAILURE')

def getMempoolAPI(url,DATA):
    # print(url)
    with open(DATA, 'wb') as f:
        request = requests.get(url, stream=True)
        f.writelines(request.iter_content(1024))
        response = getData(DATA)
        # print(getData(DATA))
        # print(response)

def searchGPGR(GPGR):
    try:
        global r
        request = api.request('search/tweets', {'q':GPGR})
        try:
            with open(GPGR+"_"+btc_unix_time_millis, 'w+') as f:
                f.write(request.text)
                f.close
        except:
            print("TRY GPGR FAILED!")
            pass
    except:
        print("GPGR SEARCH FAILED!")
        pass

def searchGPGS(GPGS):
    try:
        global s
        s = api.request('search/tweets', {'q':GPGS})
        try:
            with open(GPGS+"_"+btc_unix_time_millis, 'w+') as f:
                f.write(s.text)
                f.close
        except:
            print("TRY GPGS FAILED!")
            pass
    except:
        print("GPGS SEARCH FAILED!")
        pass


getMempoolAPI('https://mempool.space/api/v1/difficulty-adjustment', DIFFICULTY)
getMempoolAPI('https://mempool.space/api/blocks/tip/height',        BLOCK_TIP_HEIGHT)
# searchBitcoin()
# print(blockTime())
# print(getMillis())
# print(getSeconds())
# tweetBlockTime(blockTime())

def test_hash_lib():
    global TEST_256
    TEST_256 = hashlib.sha256()
    # empty string test
    # SHA-256 has the input message size < 2^64-bits. Block size is 512-bits, and it has a word size of 32-bits.
    # The output is a 256-bit digest.
    # REF: SHA-256 e3b0c442 98fc1c14 9afbf4c8 996fb924 27ae41e4 649b934c a495991b 7852b855
    # print(bytes(TEST_256.digest()))
    # b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'

    # digest_size 256 bits = 32 (bytes) per nist standard REF: NIST.FIPS.180-4
    print(TEST_256.digest_size)
    print(str(pow(2,5))+" (bytes)")
    assert TEST_256.digest_size == pow(2,5)
    # 32

    print(TEST_256.block_size)
    print(pow(2,6))
    assert TEST_256.block_size == pow(2,6)
    # 64

    assert "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" == TEST_256.hexdigest()
    print("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    print(TEST_256.hexdigest())

def HEX_MESSAGE_DIGEST(recipient, message, sender):

    n_256 = hashlib.sha256()
    print(n_256.digest())
    print(n_256.hexdigest())
    print(n_256.digest_size)
    print(n_256.block_size)
    n_256.update(bytes(recipient, 'utf-8'))
    print(n_256.digest())
    print(n_256.hexdigest())
    print(n_256.digest_size)
    print(n_256.block_size)
    n_256.update(bytes(message, 'utf-8'))
    print(n_256.digest())
    print(n_256.hexdigest())
    print(n_256.digest_size)
    print(n_256.block_size)
    n_256.update(bytes(btc_unix_time_millis, 'utf-8'))
    print(n_256.digest())
    print(n_256.hexdigest())
    print(n_256.digest_size)
    print(n_256.block_size)
    n_256.update(bytes(sender, 'utf-8'))
    print(n_256.digest())
    print(n_256.hexdigest())
    print(n_256.digest_size)
    print(n_256.block_size)

    # print(n_256.hexdigest())

    return n_256.hexdigest()

def message_header():
        DIGEST = HEX_MESSAGE_DIGEST(GPGR, MESSAGE ,GPGS)
        global BODY
        # BODY = str(":GPGR:"+GPGR+':DIGEST:'+DIGEST+':BTC:UNIX:'+BTC_UNIX_TIME_MILLIS()+":GPGS:"+GPGS+":")
        BODY = str(":"+GPGR+':'+DIGEST+':'+BTC_UNIX_TIME_MILLIS()+":"+GPGS+":")
        print(BODY)
        return BODY
def message_body():
        DIGEST = HEX_MESSAGE_DIGEST(GPGR, MESSAGE ,GPGS)
        global BODY
        # BODY = str(":GPGR:"+GPGR+':DIGEST:'+DIGEST+':BTC:UNIX:'+BTC_UNIX_TIME_MILLIS()+":GPGS:"+GPGS+":")
        BODY = str(":"+GPGR+':'+DIGEST+':'+BTC_UNIX_TIME_MILLIS()+":"+GPGS+":")
        print(BODY)
        return BODY

def tweet_message_digest(block_time):
    body = message_body()
    if (block_time != obt):
        request = api.request('statuses/update', {'status': body})
        if (request.status_code == 200):
            print('api.request SUCCESS')
        else:
            print('api.request FAILURE')
    else:
        print('tweetBlockTime() FAILURE')

# print(BTC_UNIX_TIME_MILLIS())

global GPGR
GPGR='BB06757B' #RECIPIENT
# print(GPGR)
global GPGS
GPGS='BB06757B' #SENDER
# print(GPGS)
global MESSAGE
MESSAGE='text human readable message'
# HEX_MESSAGE_DIGEST(GPGR, MESSAGE, GPGS)
# tweet_message_digest(blockTime())
# print(str(message_body()))
test_hash_lib()
# tweet_blocktime()
# searchGPGR(GPGR)
# searchGPGS(GPGS)

