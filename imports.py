#!/usr/bin/env python3

#from future.standard_library import install_aliases
#install_aliases()

#import site; site.getsitepackages()
#import subprocess, sys, re, os,platform, shutil, stat, os.path, time, datetime, string, gmpy2, math, random, json, time, logging, codecs, locale, urllib, requests

import sys
#print(sys.path)
#sys.path.append('.')
#sys.path.append('./libs')#TODO in setup.sh clone depends to libs and add to path
sys.path.append("/usr/local/lib/python3.7/site-packages")
#sys.path.append("/usr/local/lib/python3.8/site-packages")
#sys.path.append("/Users/git/bin/python3")
#sys.path.append("/Users/git/fulcrum/bs/bs4")
#print(sys.path)


#sys.path.insert(0, "/Users/git/pycoin/pycoin")
#sys.path.insert(0, "/Users/git/gmpy2")

import os
os.environ["PYTHONIOENCODING"] = "utf-8";
import subprocess
import requests

import time
from time import sleep

import re

#myLocale=locale.setlocale(locale.LC_ALL, "en_GB.UTF-8");
from bs4 import BeautifulSoup as bs
#from urllib.request import urlopen
from itertools import permutations
from io import BytesIO

import math

from gmpy2 import *

import psutil
import logging
import codecs
from datetime          import datetime
from unix_time         import *
from url_ok            import *
#cProfile
import cProfile, pstats, io
#from pstats import SortKey

