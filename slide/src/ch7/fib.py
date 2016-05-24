# coding: utf-8


class Fib(object):
    '''
    生成指定数量并满足斐波那契数列的数字序列
    '''
    def __init__(self, total):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b
        self.count, self.total = 0, total  # 初始化已经输出的数量和需要输出的总数量

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        self.count += 1
        if self.count > self.total:
            raise StopIteration()
        return self.a

if __name__ == '__main__':
    for n in Fib(10):
        print(n)
