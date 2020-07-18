#!/usr/bin/python
import sys, json, re
from pybitcointools import *
from pybitcointools.mnemonic import *
import python_sha3

def sha3(x):
    return python_sha3.sha3_256(x).digest()

def eth_addr(x):
    p = encode_pubkey(privtopub(x), 'bin_electrum')
    return sha3(p)[12:].encode('hex')

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
    print "0x0" + eth_addr(key)
    
elif sys.argv[1] == 'decode':
    key_string = sys.argv[2]
    key = sha256(key_string)
    print ("wif", encode_privkey(key, 'wif'))
    print ("hex", encode_privkey(key, 'hex'))         
    print privtoaddr(key)
    print "0x0" + eth_addr(key)

