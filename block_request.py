#!/usr/bin/env python3

import requests

base_url = 'https://mempool.space/api/blocks'
first_block = 700000
last_block = 700001

for i in range(first_block, last_block):

    headers = {'Authorization': 'Bearer Variable1', }
    files = [('server', '*'), ]

    url = ''.join([base_url, str(i)])
    res = requests.put(url, headers=headers, files=files, verify=True)