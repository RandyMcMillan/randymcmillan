#!/usr/bin/env python3

import json, requests
from requests import Request, Session
from django.http import HttpResponse
from pprint import pprint

# curl example
# curl -sSL "https://mempool.space/api/blocks/700000"

base_url_blocks = 'https://mempool.space/api/blocks/'
base_url_block = 'https://mempool.space/api/block/'
base_url_tx = 'https://mempool.space/api/tx/'

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
    # print(block_info.status_code)
    block_DATA = json.loads(res.text)

    # pprint(mempoolDATA)

    # get tags from json
    txids = []
    for txid in block_DATA:
        txids.append(txid)

    # print each tag name e your content
    for i in range(len(txids)):

        print(txids[i].get('id'))

        url = ''.join([base_url_block, txids[i].get('id')])
        # res = requests.get(url, headers=headers, files=files, verify=True)
        tx_info = Request('GET', url, headers=headers, files=files)
        prepped = tx_info.prepare()
        # print(prepped.url)
        # print(prepped.headers)
        s = Session()
        res = s.send(prepped)
        # print(res.status_code)
        txid_DATA = json.loads(res.text)

# curl example
# curl -sSL "https://mempool.space/api/block/000000000000000015dc777b3ff2611091336355d3f0ee9766a2cf3be8e4b1ce/txs"

