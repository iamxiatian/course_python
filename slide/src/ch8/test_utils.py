# coding: utf-8

import unittest
from utils import average


class UtilsTest(unittest.TestCase):
    '''
    utils模块的单元测试
    '''
    def setUp(self):
        print('测试准备处理...')

    def tearDown(self):
        print('测试收尾工作.')

    def test_average(self):
        self.assertEqual(average(1, 2, 3), 2)
        self.assertNotEqual(average(2, 2.4), 2)

if __name__ == '__main__':
    unittest.main()
