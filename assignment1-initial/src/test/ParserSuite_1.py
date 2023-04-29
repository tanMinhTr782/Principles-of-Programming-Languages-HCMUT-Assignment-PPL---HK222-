import unittest
from TestUtils import TestParser
class ParserSuite(unittest.TestCase):
    def test1(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful" 
        self.assertTrue(TestParser.test(input, expect, 201))
        # py run.py test ParserSuite
        # py run.py test LexerSuite
    def test2(self):
        """Simple program: int main() {} """
        input = """a, b, c, d: integer = 3, 4, 6, 5;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test3(self):
        input = """a: integer = 10;
        if (a > 2) return 0;
        else return 1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test4(self):
        input = """"x = -3"""
        expect = ",=,-,3,<EOF>"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test5(self):
        """Simple program: int main() {} """
        input = """a, b, c = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test6(self): 
        """test indentifiers"""
        self.assertTrue(TestParser.test("{1,3,4,5}", "{1,3,4,5}", 206))
    def test7(self): 
        self.asssertTrue(TestParser.test("""a, b, c: integer = 3, 4, 6;""","successful",207))
    def test8(self): 
        self.asssertTrue(TestParser.test("""a, b, c: integer = 3, 4, 6, 7;""","Error on line 1 col 29: ;",208))
    def test9(self): 
        self.assertTrue(TestParser.test("""x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }""","successful",220))
    def test10(self):
        """test identifiers"""
        self.assertTrue(TestParser.test("""3 + 1;""", "Error on line 1 col 0: 3", 209))
    def test11(self):
        input = "a,b: integer"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,210))
    def test12(self):
        input = "inherit out fun: integer"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,211))
    def test13(self):
        input = "arr : array [1] of float = {};"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,212))
    def test14(self):
        input = "a: array[3] of integer = {1,2,3};"
        output = "successful"
        self.assertTrue(TestParser.test(input,output,213))
    def test15(self):
        input = "a: array[3] of integer;"
        output = "successful"
        self.assertTrue(TestParser.test(input,output,214))
    def test16(self):
        input = "if(a==1); else a = 1 + 1;"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,215))
    def test17(self):
        input = "arr: array [1_0] of string;"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,216))
    def test18(self):
        input = "return true;;"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,217))
    def test19(self): 
        input = "a : integer = {1,2,3};"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,218))
    def test20(self): 
        self.assertTrue(TestParser.test("""a,b: integer = 35,36;""","successful",219))
    def test21(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test22(self):
        """Simple program: int main() {} """
        input = """a, b, c, d: integer = 3, 4, 6, 5;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test23(self):
        input = """a: integer = 10;
        if (a > 2) return 0;
        else return 1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test24(self):
        input = """"x = -3"""
        expect = ",=,-,3,<EOF>"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test25(self):
        """Simple program: int main() {} """
        input = """a, b, c = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test26(self): 
        """test indentifiers"""
        self.assertTrue(TestParser.test("{1,3,4,5}", "{1,3,4,5}", 226))
    def test27(self): 
        self.asssertTrue(TestParser.test("""a, b, c: integer = 3, 4, 6;""","successful",227))
    def test28(self): 
        self.asssertTrue(TestParser.test("""a, b, c: integer = 3, 4, 6, 7;""","Error on line 1 col 29: ;",228))
    def test29(self): 
        self.assertTrue(TestParser.test("""x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }""","successful",230))
    def test30(self):
        """test identifiers"""
        self.assertTrue(TestParser.test("""3 + 1;""", "Error on line 1 col 0: 3", 229))
    def test31(self):
        input = "a,b: integer"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,240))
    def test32(self):
        input = "inherit out fun: integer"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,241))
    def test33(self):
        input = "arr : array [1] of float = {};"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,242))
    def test34(self):
        input = "a: array[3] of integer = {1,2,3};"
        output = "successful"
        self.assertTrue(TestParser.test(input,output,243))
    def test35(self):
        input = "a: array[3] of integer;"
        output = "successful"
        self.assertTrue(TestParser.test(input,output,244))
    def test36(self):
        input = "if(a==1); else a = 1 + 1;"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,245))
    def test37(self):
        input = "arr: array [1_0] of string;"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,246))
    def test38(self):
        input = "return true;;"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,247))
    def test39(self): 
        input = "a : integer = {1,2,3};"
        output = "successful"
        self.asssertTrue(TestParser.test(input,output,248))
    def test40(self): 
        self.assertTrue(TestParser.test("""a,b: integer = 35,36;""","successful",249))  