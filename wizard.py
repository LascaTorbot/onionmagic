#!/usr/bin/python

import sys
import base64
import sha
import binascii

if len(sys.argv) != 2:
    print "usage: %s <public key pem file>"
    exit()

filename = sys.argv[1]

def main(filename):
    with open(filename) as file:
        #obtaining key from file
        key64 = ""
        firstLine = file.readline()
        if "BEGIN RSA PUBLIC KEY" not in firstLine:
            print "invalid file format"
            exit()

        for line in file:
            if "END RSA PUBLIC KEY" in line:
                break
            key64 += line

    #Key from B64 to BIN
    key = base64.b64decode(key64.strip())

    #SHA1 HASH
    sha1 = sha.new(key)
    sha1Str = sha1.digest()

    #Finally converts the first 10 bytes to base32.
    #Substring of 20 in hex means substring of 10 in bin
    print base64.b32encode(sha1Str[:10]).lower() + ".onion"


main(filename)