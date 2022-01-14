#!/usr/bin/env python3

import json, requests
from requests import Request, Session
from django.http import HttpResponse
from pprint import pprint

# curl example
# curl -sSL "https://mempool.space/api/blocks/700000"

base_url_blocks = 'https://mempool.space/api/blocks/'
first_block = 700000 # find the block heights you need
last_block = 700020

for i in range(first_block, last_block):
    headers = {'Authorization': 'mempool mempool', }
    files = [('server', '*'), ]
    url = ''.join([base_url_blocks, str(i)])
    # res = requests.get(url, headers=headers, files=files, verify=True)
    block_info = Request('GET', url, headers=headers, files=files)
    prepped = block_info.prepare()
    # print(prepped.url)
    # print(prepped.headers)
    s = Session()
    res = s.send(prepped)
    # print(res.status_code)
    block_DATA = json.loads(res.text)

    # pprint(mempoolDATA)

    # get tags from json
    tags = []
    for tag in block_DATA:
        tags.append(tag)


    base_url_block = 'https://mempool.space/api/block/'
    # print each tag name e your content
    for i in range(len(tags)):
        # print(tags[i] + ': ' + str(json[tags[i]]))
        print(tags[i].get('id'))
        url = ''.join([base_url_block, tags[i].get('id')])
        # res = requests.get(url, headers=headers, files=files, verify=True)
        block_info = Request('GET', url, headers=headers, files=files)
        prepped = block_info.prepare()
        # print(prepped.url)
        # print(prepped.headers)
        s = Session()
        res = s.send(prepped)
        # print(res.status_code)
        block_DATA = json.loads(res.text)

# curl example
# curl -sSL "https://mempool.space/api/block/000000000000000015dc777b3ff2611091336355d3f0ee9766a2cf3be8e4b1ce/txs"

