#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Hello world!
'''

import sys

__author__ = 'Tian Xia'


def _sayInChinese():
    return '你好'


def _sayInEnglish():
    return 'hello'


def sayHi():
    args = sys.argv
    if len(args) == 1:
            print(_sayInChinese())
    elif len(args) == 2:
        print('%s, %s!' % (_sayInEnglish(), args[1]))
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    sayHi()
