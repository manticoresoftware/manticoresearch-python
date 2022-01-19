# Manticore Search Client
# Copyright (c) 2020-2021, Manticore Software LTD (https://manticoresearch.com)
#
# All rights reserved
 
import unittest

class ParametrizedTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', settings=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.settings = settings

    @staticmethod
    def parametrize(testcase_class, settings=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_class)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_class(name, settings=settings))
        return suite

