#!/usr/bin/env python3

import json, requests
from requests import Request, Session
from django.http import HttpResponse


base_url = 'https://mempool.space/api/blocks/'
first_block = 700000
last_block = 700020

for i in range(first_block, last_block):
    headers = {'Authorization': 'mempool mempool', }
    files = [('server', '*'), ]
    url = ''.join([base_url, str(i)])
    #res = requests.get(url, headers=headers, files=files, verify=True)
    r = Request('GET', url, headers=headers, files=files)
    prepped = r.prepare()
    #print(prepped.url)
    #print(prepped.headers)
    s = Session()
    res = s.send(prepped)
    #print(res.status_code)
    #print(res.json)
    mempoolDATA = json.loads(str(res.text))
    print(mempoolDATA)
