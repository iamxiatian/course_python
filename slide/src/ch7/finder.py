# coding: utf-8

import os


class Finder(object):
    '''
    把指定后缀名的文件名称保存到一个文本文件中
    '''

    def __init__(self, start_path, ext_name):
        self.start_path = start_path
        self.ext_name = ext_name

    def save(self, out_filename):
        filenames = self._scan(self.start_path)
        f = open(out_filename, 'w')
        f.writelines([name+'\n' for name in filenames])
        f.close()

    def _scan(self, path):
        lst = []
        for f in os.listdir(path):
            fullname = os.path.join(path, f)
            if os.path.isdir(fullname):
                lst.extend(self._scan(fullname))
            elif fullname.endswith(self.ext_name):
                lst.append(f)
        return lst

if __name__ == '__main__':
    finder = Finder('/home/xiatian/Documents/books', '.pdf')
    finder.save('/tmp/books.txt')
