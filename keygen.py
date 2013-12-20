#!/usr/bin/python
import sys, json, re
from pybitcointools import *
from pybitcointools.mnemonic import *

if len(sys.argv) == 1:
    print "keygen <command> ..."
elif sys.argv[1] == 'generate':
    # 40 = 160/8*2
    # this gives us 160 bits of entropy
    random_bits = random_key()[:40] 
    key_string = ' '.join(mn_encode(random_bits))
    key = sha256(key_string)
    print '"' + key_string + '"'
    print privtoaddr(key)
elif sys.argv[1] == 'decode':
    key_string = sys.argv[2]
    key = sha256(key_string)
    print encode_privkey(key, 'wif')
    print privtoaddr(key)

