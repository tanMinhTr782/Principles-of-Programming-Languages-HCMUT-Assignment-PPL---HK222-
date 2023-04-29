import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_basicUndeclared_Identifier(self):
        """Test basicUndeclared_Identifier"""
        input = """main: function void () {
            a: integer = 65; 
            a = a + b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_basicUndeclared_Identifier_Param(self):
        """Test basicUndeclared_Identifier_Param"""
        input = """
            bds: function integer () {
                return a; 
            }
            main: function void () {
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_basicUndeclared_Function(self):
        """Test basicUndeclared_Function"""
        input = """main: function void () {
                helloWorld(); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_InvaildVariableDecl_AutoNoInit(self):
        """Test InvaildVariableDecl_AutoNoInit"""
        input = """
            main: function void () {
                x:auto; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_InvaildParamDecl(self):
        """Test InvaildVariable_AutoNoInit"""
        input = """
            foo: function integer(a:integer) {}
            main: function void (){
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))   
    def test_TypeMismatchInExpression_array1(self):
        """Test TypeMismatchInExpression_array"""
        input = """
            main: function void () {
                b: integer; 
                b = a[11]; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_TypeMismatchInExpression_array2(self):
        """Test TypeMismatchInExpression_array2"""
        input = """
            main: function void () {
                a:array [12] of integer;
                b: integer;
                b = a[1.1]; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207)) 
    def test_TypeMismatchInBinExp_SCOPE(self):
        """Test TypeMismatchInBinExp_SCOPE"""
        input = """
            main: function void () {
                a: string; 
                a = "HCMUT"::2023; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
#################################### RELATIONAL BASIC TEST #################################
    def test_TypeMismatchInBinExp_EQUAL(self):
        """test_TypeMismatchInBinExp_EQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 == 12); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209)) 
    def test_TypeMismatchInBinExp_EQUAL0(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_TypeMismatchInBinExp_EQUAL1(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 < "12.25"); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_TypeMismatchInBinExp_GREATERTHAN(self):
        """test_TypeMismatchInBinExp_GREATERTHAN""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 > true); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test_TypeMismatchInBinExp_LESSTHAN(self):
        """test_TypeMismatchInBinExp_LESSTHAN""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: boolean;
                b: array [3] of boolean;  
                a = (12.25 < b); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))
    def test_TypeMismatchInBinExp_LESSTHAN1(self):
        """test_TypeMismatchInBinExp_LESSTHANEQ""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: boolean;
                b: array [3] of boolean;  
                a = (12.25 <= b); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test_TypeMismatchInBinExp_GREATTHANEQ(self):
        """test_TypeMismatchInBinExp_GREATTHANEQ""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: boolean;
                c:string = "11.11";
                a = (11.11 >= c); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))   
#################################### RELATIONAL BASIC TEST #################################


#################################### BOOLEAN OPERATOR TEST #################################
    def test_TypeMismatchInUnExp_NOT(self):
        """test_TypeMismatchInBinExp_GREATTHANEQ""" 
        # OPERAND TYPE: BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = !11.11; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_TypeMismatchInBinExp_AND(self):
        """test_TypeMismatchInBinExp_GREATTHANEQ""" 
        # OPERAND TYPE: BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (11.11 && true); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test_TypeMismatchInBinExp_OR(self):
        """test_TypeMismatchInBinExp_GREATTHANEQ""" 
        # OPERAND TYPE: BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (2801 || true); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
#################################### BOOLEAN OPERATOR TEST #################################

######################################## CALCULATE OPERATOR TEST ########################################
    def test_TypeMismatchInUnExp_MINUS0(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: string; 
                a = -"0301"; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))    

    def test_TypeMismatchInBinExp_MINUS(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: integer; 
                a = "0301" - 73; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))   
    def test_TypeMismatchInBinExp_ADD(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: integer; 
                a = 73  + true; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))  
    def test_TypeMismatchInBinExp_DIV(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: integer;

                a = {1,2,3} / 73; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221)) 
    def test_TypeMismatchInBinExp_MUL(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: integer;
                a = 73 * "2"; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))  
    def test_TypeMismatchInBinExp_REMAINDER(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                a: integer;
                a = 73 % true; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
######################################## CALCULATE OPERATOR TEST ########################################

    def test_TypeMismatchInFunc_voidFunc(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo: function void (){}
            main: function void () {
                a: integer;
                a = 73 + foo(); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_TypeMismatchInSTMT_voidFunc2(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo: function integer (){}
            main: function void () {
                foo(); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    def test_TypeMismatchInSTMT_FuncCallNotVoid(self):
        """test_TypeMismatchInSTMT_FuncCallNotVoid""" 
        # OPERAND TYPE: INT
        input = """
            foo: function integer (){}
            main: function void () {
                foo(); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test_TypeMismatchInSTMT_ifCond(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                if (3 + 4) {
                    
                }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test_TypeMismatchInSTMT_whileCond(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                while (2 / 4) {
                
                }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test_TypeMismatchInSTMT_dowhileCond(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                do {
                
                }
                while ("HCMUT"::"K22"); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
    def test_TypeMismatchInSTMT_for(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                for (i = "12", i >= 0, i - 1){
                
                } 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
    def test_TypeMismatchInSTMT_for1(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                for (i = 12, i >= 0, i - 0.5){
                
                } 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test_TypeMismatchInSTMT_for11(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                for (i = true, i >= 0, i - 1){
                
                } 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_TypeMismatchInSTMT_for2(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:array [3] of integer = {1,2,3}; 
                x = {4,5,6}; 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test_TypeMismatchInSTMT_intAssFloat(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:integer; 
                x = 1.5; 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_TypeMismatchInSTMT_floatAssInt(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:float; 
                x = 1; 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    def test_TypeMismatchInSTMT_000(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:boolean; 
                x = 1; 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))  
    def test_TypeMismatchInSTMT_00(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo: function integer() {}
            foo1: function void(a:integer,b:integer) inherit foo {}
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
    def test_TypeMismatchInSTMT_0(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo: function integer() {
                return "Hello world"; 
            }
            main: function void () {
                foo(); 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238)) 
    def test_TypeMismatchInSTMT_1(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo: function integer() {
                return "Hello world"; 
            }
            main: function void () {
                foo(); 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))   
    def test_TypeMismatchInSTMT_2(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                break; 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))   
    def test_TypeMismatchInSTMT_3(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                continue; 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))  
    def test_TypeMismatchInSTMT_4(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                a:array [3] of integer = {1,3,4.5};
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_InvaildFirstStatement(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function integer (a:integer, b:boolean) {}
        foo1: function void () inherit foo{
                return; 
        }
            main: function void () {
                foo1(); 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_SuccessFirstStatement(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function integer (a:integer, b:boolean) {}
        foo1: function void () inherit foo {
                super(12,true);  
        }
            main: function void () {
                foo1(); 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_SuccessFirstStatement2(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function integer () {}
        foo1: function void (a:integer) inherit foo  {
                preventDefault();  
        }
            main: function void () {
                foo1(69); 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    def test_SuccessFirstStatement2(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function integer () {}
        foo1: function void (a:integer) inherit foo {
                preventDefault();  
        }
            main: function void () {
                foo1(69); 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
    def test_RedeclaredInherit(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function integer (x: float) {}
        foo1: function void (a:integer, inherit x: float) inherit foo{
                super(11.11); 
                x: integer = 2023; 
                return;  
        }
            main: function void () {
                foo1(21,21.12); 
                
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))  
    def test_NoEntryPoint(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function integer (x: float) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248)) 
    def test_FuncDeclAfterCalledByAnotherFunction(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function integer (x: float) {return foo1(69);}
        foo1: function integer (x: integer) {return 0;}
        main: function void () {

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))  
    def test_mainReturnInteger(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        main: function integer () {
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))                                             
    def test_TypeMismatchInExpression_array3(self):
        """Test TypeMismatchInExpression_array"""
        # Can list of integer consist of ID . This is an example 
        input = """
            main: function void () {
                x: integer = 11;
                a:array [12] of integer;  
                b: integer;
                b = a[x]; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))   
    def test_TypeMismatchInExpression_array4(self):
        """Test TypeMismatchInExpression_array"""
        # Can list of integer consist of ID . This is an example 
        input = """
            main: function void () {
                x: integer = 11;
                a:array [12] of integer;  
                b: integer;
                b = a[x]; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))   
    def test_TypeMismatchInExpression_array3(self):
        """Test TypeMismatchInExpression_array"""
        # Can list of integer consist of ID . This is an example 
        input = """
            main: function void () {
                x: integer = 11;
                a:array [12] of integer;  
                b: integer;
                b = a[x]; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))
    def test_TypeMismatchInExpression_array3(self):
        """Test TypeMismatchInExpression_array"""
        # Can list of integer consist of ID . This is an example 
        input = """
            main: function void () {
                x: integer = 11;
                a:array [12] of integer;  
                b: integer;
                b = a[x]; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_TypeMismatchInExpression_array3(self):
        """Test TypeMismatchInExpression_array"""
        # Can list of integer consist of ID . This is an example 
        input = """
            main: function void () {
                x: integer = 11;
                a:array [12] of integer;  
                b: integer;
                b = a[x]; 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))         
    def test_full_program(self):
        """Test full program"""
        input = """x: integer = 65;
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
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
