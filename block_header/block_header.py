#!/usr/bin/env python
#
# Author: Zhenxing Xu <xzxlnmail@163.com>
#

import sys
import hashlib


# Block header datas: 4 + 32 + 32 + 4 + 4 + 4 = 80bytes
'''
header_hex = ("00000020" +
"117a5813c103b385340912c1c1d5ca7ec49f3d59102978000000000000000000" +
"dc6b41e7e7e21d13b0dc36bbbcb869dc765c66185436eb1fbe0e286f88b890f7" +
"95514c5a" +
"c1910018" +
"aaad4e7e")

header_hex = ("00000020" +
"fbe2538fd33364ebd1921c9e223286957aaa6c8905a92f000000000000000000" +
"d9707628d7f11d7ee979c9388e368f0a85489980c73cb7804c3ecc4bb000016d" +
"22f5b15a" +
"494a5117" +
"e516ba04")

header_hex = ("00000020" +
"fbe2538fd33364ebd1921c9e223286957aaa6c8905a92f000000000000000000" +
"de6a25f9e751f90f77c1dcd64a776bc0b528a3e897b545ff4af9a90ba0b14e50" +
"22f5b15a" +
"494a5117" +
"fa2fac0a")
'''

header_hex = ("01000000" +
"81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000" +
"e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b" +
"c7f5d74d" +
"f2b9441a" +
"42a14695")

# Only using sha256 test
def sha256_test():
    header_bin = header_hex.decode('hex')
    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    print(hash.encode('hex_codec'))
    #'1dbd981fe6985776b644b173a4d0385ddc1aa2a829688d1e0000000000000000'
    print(hash[::-1].encode('hex_codec'))
    #'00000000000000001e8d6829a8a21adc5d38d0a473b144b6765798e61f98bd1d'


def calc_hash(header):
    header_bin = header.decode('hex')
    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    print('\033[1;32mhash big endian:    \033[0m' + hash.encode('hex_codec'))
    print('\033[1;32mhash little endian: \033[0m' + hash[::-1].encode('hex_codec'))


def big_little_endian(string):
    return string.decode('hex')[::-1].encode('hex_codec')


def run(path, endian):
    try:
        with open(path) as f:
            tmp = f.read().split()
    except:
        print("Open file failed.")
        sys.exit()

    version = tmp[1]
    prehash = tmp[3]
    merkle = tmp[5]
    ntimes = tmp[7]
    bits = tmp[9]
    nonce = tmp[11]

    if (endian == '0'):
        header_tmp = version + prehash + merkle + ntimes + bits + nonce
    else:
        header_tmp = big_little_endian(version) \
                        + big_little_endian(prehash) \
                        + big_little_endian(merkle) \
                        + big_little_endian(ntimes) \
                        + big_little_endian(bits) \
                        + big_little_endian(nonce)

    print(header_tmp)
    calc_hash(header_tmp)


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        endian = sys.argv[2]
    except:
        print("Please input paramter: file name.")
        sys.exit()

    run(path, endian)
