'''
    单元测试：
        1.unittest单元组件
        1.1 继承TestCase测试用例
        1.2 测试用例方法命名必须是testXXXX
        1.3 使用assertEqual()来断言

'''
import unittest

from Calc import Calc


class TestCalc(unittest.TestCase):

    def testAdd(self):
        # 1.准备数据
        a = 6
        b = 5
        c = 11
        # 2.调用被测程序
        calc = Calc()
        sum = calc.add(a,b)

        # 3.断言
        self.assertEqual(c,sum)

    def testAdd1(self):
        # 1.准备数据
        a = -6
        b = -5
        c = -11
        # 2.调用被测程序
        calc = Calc()
        sum = calc.add(a, b)

        # 3.断言
        self.assertEqual(c, sum)


    def testsubs(self):
        # 1.准备数据
        a = 6
        b = 5
        c = 1
        # 2.调用被测程序
        calc = Calc()
        sum = calc.subs(a, b)

        # 3.断言
        self.assertEqual(c, sum)

    def testmulti(self):
            # 1.准备数据
            a = 6
            b = 5
            c = 30
            # 2.调用被测程序
            calc = Calc()
            sum = calc.multi(a, b)

            # 3.断言
            self.assertEqual(c, sum)

    def testdevision(self):
            # 1.准备数据
            a = 6
            b = 2
            c = 3
            # 2.调用被测程序
            calc = Calc()
            sum = calc.devision(a, b)

            # 3.断言
            self.assertEqual(c, sum)

    def testdevision1(self):
        a = 10
        b = 5
        c = 2
        calc = Calc()
        sum = calc.devision(a,b)
        self.assertEqual(c,sum)






















