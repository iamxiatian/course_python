mport sys
from pprint import pprint

import hello
# ImportError: No module named 'hello'

pprint(sys.path)
sys.path.append('/home/xiatian/Documents/git/teaching/python/slide/src/ch5')

import hello
hello.sayHi()
# Hello, world!

