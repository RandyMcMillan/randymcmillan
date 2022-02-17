#!/usr/bin/env python3

from imports    import *
from socket     import *
from psutil     import *
from gmpy2      import *
from unixTime   import *
from sys        import *
from os         import *

USER       = psutil.Process().username()
IS_MACOS   = psutil.MACOS
IS_LINUX   = psutil.LINUX
IS_WINDOWS = psutil.WINDOWS
PATH = getcwd()

def sys_info():

    print("sys.path:%s",sys.path)
    print(sys.path)
    print("Python version")
    print (sys.version)
    print("Version info.")
    print (sys.version_info)

def insertPaths():

    sys.path.append("/usr/local/lib/python3.7/site-packages")
    sys.path.append("/usr/local/lib/python3.8/site-packages")
    sys.path.append("/usr/local/lib/python3.9/site-packages")
    sys.path.append(PATH)
    # print("sys.path:%s",sys.path)
    # print(sys.path)

def systemType():
    if (IS_MACOS):
        # print("IS_MACOS="+str(psutil.MACOS))
        # print(str(os.uname()))
        return str("IS_MACOS")
        # DEFAULT_WALLET_FOLDER = "~/Library/ApplicationSupport/Bitcoin/wallets/"
        # DEFAULT_WALLET = "wallet.dat"

    if (IS_LINUX):
        return str("IS_LINUX")
        # DEFAULT_WALLET_FOLDER = ""
        # DEFAULT_WALLET = "wallet.dat"

    if (IS_WINDOWS):
        return str("IS_WINDOWS")
        # DEFAULT_WALLET_FOLDER = ""
        # DEFAULT_WALLET = "wallet.dat"

GOLDEN_RATIO = 1.6180339887498948482045868343656381177203091798057628621354486227
#report flags
TEST                = False
REPORT              = True
KEY_REPORT          = True
SLEEP_REPORT        = True # uses SLEEP_AMOUNT to pause report

PROFILE             = False
#usage
#check imports.py
#import cProfile, pstats, io
#from pstats import SortKey

#cProfile Usage
#if (PROFILE):
    #pr = cProfile.Profile()
    #pr.enable()

    # ... do something ...

    #pr.disable()
    #s = io.StringIO()
    #sortby = SortKey.CUMULATIVE
    #ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    #ps.print_stats()
    #print(s.getvalue())

NOTIFY              = True
TIME_OUT            = 5
#primes only
CHECK_ADDRESSES     = True

#push test targets to address array
TEST_TARGETS        = True

EXTENSION           = "wif"

#address array
addresses = []
count = 0
custom_count = 0

# Setup logging
logging.basicConfig(level=logging.INFO ,format='%(asctime)s %(message)s', datefmt='%j.%Y %I:%M:%S %p')
logger = logging.getLogger()
UTF8Writer = codecs.getwriter('utf8')
# sys.stdout = UTF8Writer(sys.stdout)

POWMOD_GMP_SIZE = pow(2, 256)

START_TIME = TimestampMillisec64()
CAFFEINATE = 18600

if __name__ == "__main__":

    from imports    import *
    from psutil     import *
    from gmpy2      import *
    from unixTime   import *
    from sys        import *
    import argparse
    insertPaths()
    parser = argparse.ArgumentParser()
    parser.add_argument("-arg1", action="store_true", help="-arg1 example")
    parser.add_argument("-arg2", action="store_true", help="-arg2 example")

    int_group = parser.add_argument_group('integer args')
    int_group.add_argument("-x", action="store_true", help="x arg example")
    int_group.add_argument("-y", action="store_true", help="y arg example")

    mutex_group = parser.add_mutually_exclusive_group()
    mutex_group.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    mutex_group.add_argument("-q", "--quiet", action="store_true")

    subparsers = parser.add_subparsers(title='sys_info', description='sys info commands', help='get sys info')
    parser_sys_info = subparsers.add_parser('sys_info')
    parser_sys_info.add_argument("sys_info", action="store_true", help="sys_info example")
    parser_sys_info.add_argument("-sys1", action="store_true", help="-sys1 example")
    parser_sys_info.add_argument("-sys2", action="store_true", help="-sys2 example")
    parser_sys_info.set_defaults(func=sys_info)

    args = parser.parse_args()
    if args.verbose:
        logger.info("args.verbose = %s",args.verbose)
        pass
    if args.arg1:
        logger.info("args.arg1 = %s",args.arg1)
        pass
    if args.arg2:
        logger.info("args.arg2 = %s",args.arg2)
        pass

#    args = parser_sys_info.parse_args()

    if args.sys_info:
        if args.sys1:
            logger.info("args.sys1 = %s",args.sys1)
            pass
        if args.sys2:
            logger.info("args.sys2 = %s",args.sys2)
            pass

