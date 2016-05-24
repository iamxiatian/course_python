# coding: utf-8

from optparse import OptionParser
parser = OptionParser()

parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
print(options)

if not options.filename:
    parser.error('未指定-f参数')

f = open(options.filename, 'r')
lineno = 1
for line in f:
    print(lineno, '\t', line, end='')
    lineno += 1
print('---FINISH---')
