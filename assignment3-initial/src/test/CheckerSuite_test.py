import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_TypeMismatchInSTMT_for1(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                for (i = 12, i >= 0, i - 0.5){
                
                } 
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 4000))  