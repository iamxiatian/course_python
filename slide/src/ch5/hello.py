#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Hello world!
'''

import sys

__author__ = 'Tian Xia'


def sayHi():
    args = sys.argv
    if len(args) == 1:
            print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    sayHi()
