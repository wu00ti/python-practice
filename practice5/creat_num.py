#!/usr/bin/python
#-*- conding:UTF-8 -*-

import string 
import random

KEY_LEN = 20
KEY_ALL = 200

def base_str():
    return(string.letters+string.digits)

def key_gen():
    keylist = [random.choice(base_str())for i in range(KEY_LEN)]
    return("".join(keylist) + '\n')


def print_key(func):
    def _print_key(num):
        for i in func(num):
            print (i) 
    return _print_key

def key_num(num,result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(key_gen())
    print (result)

if __name__ == "__main__":
    key_num(KEY_ALL)
