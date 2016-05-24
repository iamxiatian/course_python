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
        if(args[1] == 'en'):
            print(_sayInEnglish())
        else:
            print(_sayInChinese())
    elif len(args) == 3:
        msg = _sayInEnglish() if args[1] == 'en' else _sayInChinese()
        print('%s, %s!' % (msg, args[2]))
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    sayHi()
