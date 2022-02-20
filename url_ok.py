#!/usr/bin/env python

from imports import *
from configs import *

def urlOK(url):
    r = requests.head(url)
    return r.status_code == 200

