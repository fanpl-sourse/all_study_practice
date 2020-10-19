# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 07:39
# @Author  : 饭盆里
# @File    : test_unittest.py
# @Software: PyCharm
# @desc    :
import unittest

class TestMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        print('>>>>>>>>>>>method setUpClass')
    @classmethod
    def tearDownClass(self) -> None:
        print('>>>>>>>>>>>method tearDownClass')

    def test_upper(self):
        print('upper')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print('isupper')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

class TestMethods1(unittest.TestCase):

    def setUp(self):
        print('method1 setup')
    def tearDown(self) -> None:
        print('method1 tearDown')

    def test_upper1(self):
        print('upper1')
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper1(self):
        print('isupper1')
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split1(self):
        s = 'hello world1'
        print(s)
        self.assertEqual(s.split(), ['hello', 'world1'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_assertEqual(self):
        print('assertEqual')
        self.assertEqual(1,1)

    def test_assertNotEqual(self):
        print('assertNotEqual')
        self.assertNotEqual(1,2)

    def test_assertTrue(self):
        print('assertTrue')
        self.assertTrue(1)

    def test_assertFault(self):
        print('assertFault')
        self.assertFalse(None)

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestMethods1)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
