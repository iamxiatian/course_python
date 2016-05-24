# coding: utf-8


class Student(object):
    '''   学生的基类    '''

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def sayHi(self):
        print('我是学生%s' % self.name)


class Postgraduate(Student):
    '''研究生'''
    def sayHi(self):
        print('我是研究生%s' % self.name)


def meet(student):
    student.sayHi()


if __name__ == '__main__':
    han = Student('韩寒', 85)
    wang = Postgraduate('王小二', 80)
    meet(han)
    meet(wang)
