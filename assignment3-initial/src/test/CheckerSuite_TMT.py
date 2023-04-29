import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *
from abc import ABC
from Visitor import Visitor
class CheckerSuite(unittest.TestCase):
    def test_basicUndeclared_Identifier(self):
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType(), IntegerLit(65)), AssignStmt(Id("a"), BinExpr("+", Id("a"), Id("b")))]))
])    
        # expect = """main: function void () {
        #     a: integer = 65; 
        #     a = a + b;
        # }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 401))
    def test_basicUndeclared_Identifier_Param(self):
        """Test basicUndeclared_Identifier_Param"""
        input = """
            bds: function integer () {
                return a; 
            }
            main: function void () {
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 402))
    def test_basicCallStmt(self):
        """Test basicUndeclared_Function"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([CallStmt("helloWorld",[])]))
])
        expect = "Undeclared Function: helloWorld"
# main: function void () {
#                 helloWorld(); 
#         }
        self.assertTrue(TestChecker.test(input, expect, 403))
    def test_InvaildVariableDecl_AutoNoInit(self):
        """Test InvaildVariableDecl_AutoNoInit"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("x", AutoType())]))
])
        expect = "Invalid Variable: x"
        # expect = """
        #     main: function void () {
        #         x:auto; 
        # }"""
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test_TypeMismatchInBinExp_SCOPE(self):
        """Test TypeMismatchInBinExp_SCOPE"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", StringType()), AssignStmt(Id("a"), BinExpr("::", StringLit("HCMUT"), IntegerLit(2023)))]))
])
        expect = "Type mismatch in expression: BinExpr(::, StringLit(HCMUT), IntegerLit(2023))"
#  main: function void () {
#                 a: string; 
#                 a = "HCMUT"::2023; 
#         }
        self.assertTrue(TestChecker.test(input, expect, 405))


#################################### RELATIONAL BASIC TEST #################################
    def test_TypeMismatchInBinExp_EQUAL(self):
        """test_TypeMismatchInBinExp_EQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        # expect = """
        #     main: function void () {
        #         a: boolean; 
        #         a = (12.25 == 12); 
        # }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", BooleanType()), AssignStmt(Id("a"), BinExpr("==", FloatLit(12.25), IntegerLit(12)))]))
])
        expect = "Type mismatch in expression: BinExpr(==, FloatLit(12.25), IntegerLit(12))"
        self.assertTrue(TestChecker.test(input, expect, 406)) 
    def test_TypeMismatchInBinExp_EQUAL1(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        # expect = """
        #     main: function void () {
        #         a: boolean; 
        #         a = (12.25 < "12.25"); 
        # }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a",BooleanType()), AssignStmt(Id("a"), BinExpr("<", FloatLit(12.25), StringLit("12.25")))]))
])
        expect = "Type mismatch in expression: BinExpr(<, FloatLit(12.25), StringLit(12.25))"
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_TypeMismatchInBinExp_GREATERTHAN(self):
        """test_TypeMismatchInBinExp_GREATERTHAN""" 
        # OPERAND TYPE: INT/FLOAT
        # expect = """
        #     main: function void () {
        #         a: boolean; 
        #         a = (12.25 > true); 
        # }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", BooleanType()), AssignStmt(Id("a"), BinExpr(">", FloatLit(12.25), BooleanLit(True)))]))
])
        expect = "Type mismatch in expression: BinExpr(>, FloatLit(12.25), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_TypeMismatchInBinExp_LESSTHAN(self):
        """test_TypeMismatchInBinExp_LESSTHAN""" 
        # OPERAND TYPE: INT/FLOAT
        # expect = """
        #     main: function void () {
        #         a: boolean;
        #         b: array [3] of boolean;  
        #         a = (12.25 < b); 
        # }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", BooleanType()), VarDecl("b", ArrayType([3], BooleanType())), AssignStmt(Id("a"), BinExpr("<", FloatLit(12.25), Id("b")))]))
])
        expect = "Type mismatch in expression: BinExpr(<, FloatLit(12.25), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_TypeMismatchInBinExp_LESSTHAN1(self):
        """test_TypeMismatchInBinExp_LESSTHANEQ""" 
        # OPERAND TYPE: INT/FLOAT
        # expect = """
        #     main: function void () {
        #         a: boolean;
        #         b: array [3] of boolean;  
        #         a = (12.25 <= b); 
        # }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", BooleanType()), VarDecl("b", ArrayType([3], BooleanType())), AssignStmt(Id("a"), BinExpr("<=", FloatLit(12.25), Id("b")))]))
])
        expect = "Type mismatch in expression: BinExpr(<=, FloatLit(12.25), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test_TypeMismatchInBinExp_GREATTHANEQ(self):
        """test_TypeMismatchInBinExp_GREATTHANEQ""" 
        # OPERAND TYPE: INT/FLOAT
        # expect = """
        #     main: function void () {
        #         a: boolean;
        #         c:string = "11.11";
        #         a = (11.11 >= c); 
        # }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", BooleanType()), VarDecl("c", StringType(), StringLit(11.11)), AssignStmt(Id("a"), BinExpr(">=", FloatLit(11.11), Id("c")))]))
])
        expect = "Type mismatch in expression: BinExpr(>=, FloatLit(11.11), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 411))   
# #################################### RELATIONAL BASIC TEST #################################


# #################################### BOOLEAN OPERATOR BASIC TEST #################################
    def test_TypeMismatchInUnExp_NOT(self):
        """test_TypeMismatchInBinExp_GREATTHANEQ""" 
        # OPERAND TYPE: BOOLEAN
        # expect = """
        #     main: function void () {
        #         a: boolean; 
        #         a = !11.11; 
        # }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", BooleanType()), AssignStmt(Id("a"), UnExpr("!", FloatLit(11.11)))]))
])
        expect = "Type mismatch in expression: UnExpr(!, FloatLit(11.11))"
        self.assertTrue(TestChecker.test(input, expect, 412))
#     def test_TypeMismatchInBinExp_AND(self):
#         """test_TypeMismatchInBinExp_GREATTHANEQ""" 
#         # OPERAND TYPE: BOOLEAN
#         # expect = """
#         #     main: function void () {
#         #         a: boolean; 
#         #         a = (11.11 && true); 
#         # }"""
#         input = Program([
# 	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", BooleanType()), AssignStmt(Id("a"), BinExpr("&&", FloatLit(11.11), BooleanLit(True)))]))
# ])
#         expect = "Type mismatch in expression: BinExpr(&&, FloatLit(11.11), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test_TypeMismatchInBinExp_OR(self):
        """test_TypeMismatchInBinExp_GREATTHANEQ""" 
        # OPERAND TYPE: BOOLEAN
        # expect = """
        #     main: function void () {
        #         a: boolean; 
        #         a = (2801 || true); 
        # }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", BooleanType()), AssignStmt(Id("a"), BinExpr("||", IntegerLit(2801), BooleanLit(True)))]))
])
        expect = "Type mismatch in expression: BinExpr(||, IntegerLit(2801), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 414))
# #################################### BOOLEAN OPERATOR TEST #################################

######################################## CALCULATE OPERATOR TEST ########################################
    def test_TypeMismatchInUnExp_MINUS0(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        # expect = """
        #     main: function void () {
        #         a: string; 
        #         a = -"0301"; 
        # }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", StringType()), AssignStmt(Id("a"), UnExpr("-", StringLit("0301")))]))
])
        expect = "Type mismatch in expression: UnExpr(-, StringLit(0301))"
        self.assertTrue(TestChecker.test(input, expect, 415))    

    def test_TypeMismatchInBinExp_MINUS(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        expect = """
            main: function void () {
                a: integer; 
                a = "0301" - 73; 
        }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType), AssignStmt(Id("a"), BinExpr("-", StringLit("0301"), IntegerLit(73)))]))
])
        expect = "Type mismatch in expression: BinExpr(-, StringLit(0301), IntegerLit(73))"
        self.assertTrue(TestChecker.test(input, expect, 416))   
    def test_TypeMismatchInBinExp_ADD(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        expect = """
            main: function void () {
                a: integer; 
                a = 73  + true; 
        }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType), AssignStmt(Id("a"), BinExpr("+", IntegerLit(73), BooleanLit(True)))]))
])
        expect = "Type mismatch in expression: BinExpr(+, IntegerLit(73), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 417))  
    def test_TypeMismatchInBinExp_DIV(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        expect = """
            main: function void () {
                a: integer;

                a = {1,2,3} / 73; 
        }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType), AssignStmt(Id("a"), BinExpr("/", ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(73)))]))
])
        expect = "Type mismatch in expression: BinExpr(/, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(73))"
        self.assertTrue(TestChecker.test(input, expect, 418)) 
    def test_TypeMismatchInBinExp_MUL(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        expect = """
            main: function void () {
                a: integer;
                a = 73 * "2"; 
        }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType), AssignStmt(Id("a"), BinExpr("*", IntegerLit(73), StringLit("2")))]))
])
        expect = "Type mismatch in expression: BinExpr(*, IntegerLit(73), StringLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 419))  
    def test_TypeMismatchInBinExp_REMAINDER(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        expect = """
            main: function void () {
                a: integer;
                a = 73 % true; 
        }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType), AssignStmt(Id("a"), BinExpr("%", IntegerLit(73), BooleanLit(True)))]))
])
        expect = "Type mismatch in expression: BinExpr(%, IntegerLit(73), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 420))
# ######################################## CALCULATE OPERATOR TEST ########################################

    def test_TypeMismatchInFunc_voidFunc(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        expect = """
            foo: function void (){}
            main: function void () {
                a: integer;
                a = 73 + foo(); 
        }"""
        input = Program([
	FuncDecl("foo", VoidType(), [], None, BlockStmt([])),
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType), AssignStmt(Id("a"), BinExpr("+", IntegerLit(73), FuncCall("foo", [])))]))
])
        expect = "Type mismatch in expression: BinExpr(+, IntegerLit(73), FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_TypeMismatchInSTMT_FuncCallNotVoid(self):
        """test_TypeMismatchInSTMT_FuncCallNotVoid"""
        # Da bo rang buoc CallStmt phai la voidType: 
        # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8322
        # OPERAND TYPE: INT
        expect = """
            foo: function integer (){}
            main: function void () {
                foo(); 
        }"""
        input = Program([
	FuncDecl("foo", IntegerType(),[], None, BlockStmt([])),
	FuncDecl("main", VoidType(), [], None, BlockStmt([CallStmt("foo",[] )]))
])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))
    def test_TypeMismatchInSTMT_ifCond(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        # Type in condition must be boolean
        expect = """
            main: function void () {
                if (3 + 4) {
                    
                }
        }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([IfStmt(BinExpr("+", IntegerLit(3), IntegerLit(4)), BlockStmt([]))]))
])
        expect = "Type mismatch in statement: IfStmt(BinExpr(+, IntegerLit(3), IntegerLit(4)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test_TypeMismatchInSTMT_whileCond(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        expect = """
            main: function void () {
                while (2 / 4) {
                
                }
        }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([WhileStmt(BinExpr("/", IntegerLit(2), IntegerLit(4)), BlockStmt([]))]))
])
        expect = "Type mismatch in statement: WhileStmt(BinExpr(/, IntegerLit(2), IntegerLit(4)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 424))
    def test_TypeMismatchInSTMT_dowhileCond(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        expect = """
            main: function void () {
                do {
                
                }
                while ("HCMUT"::"K22"); 
        }"""
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([DoWhileStmt(BinExpr("::", StringLit("HCMUT"), StringLit("K22")), BlockStmt([]))]))
])
        expect = "Type mismatch in statement: DoWhileStmt(BinExpr(::, StringLit(HCMUT), StringLit(K22)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test_TypeMismatchInSTMT_for(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                i:float;
                for (i = 9.5, i >= 0, i - 1){
                
                } 
        }"""
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), FloatLit(9.5)), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 426))
    def test_TypeMismatchInSTMT_for1(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                i:integer = 10; 
                for (i = 12, i >= 0, i - 0.5){
                } 
        }"""
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(12)), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), FloatLit(0.5)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 427))
    def test_TypeMismatchInSTMT_for11(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                i:integer; 
                for (i = true, i >= 0, i - 1){
                
                } 
        }"""
        expect = """Type mismatch in statement: AssignStmt(Id(i), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 428))
    def test_TypeMismatchInSTMT_for2(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:array [3] of integer = {1,2,3}; 
                x = {4,5,6}; 
                
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(x), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]))"
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test_TypeMismatchInSTMT_intAssFloat(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:integer; 
                x = 1.5; 
                
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(x), FloatLit(1.5))"
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_TypeMismatchInSTMT_floatAssInt(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:float; 
                x = 1; 
                
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test_TypeMismatchInSTMT_000(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:boolean; 
                x = 1; 
                
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(x), IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 432))  
    def test_inherit1(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo: function integer(a:integer,b:integer) {}
            foo1: function void() inherit foo {
                super();
            }
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_inherit2(self):
        input = """
            foo: function integer(a:integer,b:integer) {}
            foo1: function void() inherit foo {
                preventDefault();
            }
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Type mismatch in statement: CallStmt(foo1, BooleanLit(True), IntegerLit(12))"
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test_inherit3(self):
        input = """
            foo: function integer() {}
            foo1: function void() inherit foo {
                preventDefault();
            }
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Type mismatch in statement: CallStmt(foo1, BooleanLit(True), IntegerLit(12))"
        self.assertTrue(TestChecker.test(input, expect, 435))
    def test_inherit4(self):
        input = """
            foo: function integer() {
                readInteger();
            }
            foo1: function void() inherit foo {
                super();
            }
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Type mismatch in statement: CallStmt(foo1, BooleanLit(True), IntegerLit(12))"
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test_inherit5(self):
        input = """
            foo: function integer(inherit a:float) {
                readInteger();
            }
            foo1: function void(a:float) inherit foo {
                super();
            }
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_inherit6(self):
        input = """
            foo1: function void(b:float) inherit foo {
                super(1.1);
                a:integer = 7; 
            }
            foo: function integer(inherit a:float) {
                readInteger();
            }
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_inherit7(self):
        input = """
            foo: function integer(inherit a:float) {
                readInteger();
            }
            foo1: function void(b:float) inherit foo {
                super(true);
            }
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Type mismatch in statement: CallStmt(super, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test_inherit8(self):
        input = """
        foo1: function void (inherit x: string){}
        foo: function void() inherit foo1{
            x = 2;
            foo1(2);
        }
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Invalid statement in function: AssignStmt(Id(x), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test_inherit9(self):
        input = """
        foo1: function void (inherit x: string){}
        foo: function void() inherit foo1{
            super("HCMUT");
            x = 2;
        }
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(x), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test_inherit10(self):
        input = """
        foo1: function void (inherit x: string){}
        foo: function void() inherit foo1{
            super("HCMUT");
            foo(2);
        }
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Type mismatch in expression: IntegerLit(2)"
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test_inherit11(self):
        input = """
        foo: function void() inherit foo1{
            super("HCMUT",true);
            x = 7;
        }
        foo1: function void (inherit x: string, inherit x:boolean){}
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test_inherit12(self):
        input = """
        foo: function void() inherit foo1{
            super("HCMUT",true);
            x = 7;
        }
        foo1: function void (inherit x: string, inherit y:boolean){}
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = "Type mismatch in statement: AssignStmt(Id(x), IntegerLit(7))"
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test_inherit13(self):
        input = """
       foo: function integer(inherit x: integer) inherit bar {super(2);}
bar: function integer(inherit y: integer) inherit foo2 {super("Hi");}
foo2: function integer(inherit z: float) {}
"""
        expect = "Type mismatch in statement: CallStmt(super, StringLit(Hi))"
        self.assertTrue(TestChecker.test(input, expect, 445))    
    def test_inherit14(self): # xet lai sau. 
        input = """
       foo: function integer(inherit x: integer) inherit bar {
        super(2);
        y = 1; 
        z = 1.5;
        }
bar: function integer(inherit y: integer) inherit foo2 {super("Hi");}
foo2: function integer(inherit z: float) {}
"""
        expect = "Undeclared Identifier: z"
        self.assertTrue(TestChecker.test(input, expect, 446))  
    def test_inherit15(self): # xet lai sau. 
        input = """
a: integer = 2; //1
b: auto; //2
foo: function void(a: integer, b: float) {} //3
bar: function void() inherit foo {} //4
a: function void() {} //5

"""
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 447))
    def test_inherit16(self):
        input = """
foo: function integer(y: integer) inherit foo1 {super(69);}
       foo1: function integer(inherit x: auto){
            x = x + 1;
            x = x + 1.5; 
        }
"""
        expect = "Type mismatch in statement: AssignStmt(Id(x), BinExpr(+, Id(x), FloatLit(1.5)))"
        self.assertTrue(TestChecker.test(input, expect, 448))  
    def test_inherit17(self):
        input = """
foo: function integer(y: integer) inherit foo1 {
    super(69);
    x = x + 0.1;
    }
       foo1: function integer(inherit x: auto){
            readInteger(x);
        }
"""
        expect = "Type mismatch in statement: AssignStmt(Id(x), BinExpr(+, Id(x), FloatLit(0.1)))"
        self.assertTrue(TestChecker.test(input, expect, 449))  
    def test_inherit18(self):
        input = """
foo: function integer(y: auto) inherit foo1 {
    super(69);
    x = x + y;
    y = y + 0.1;
    }
       foo1: function integer(inherit x: auto){
            x = x + 1;
            x = x + 1.5; 
        }
"""
        expect = "Type mismatch in statement: AssignStmt(Id(y), BinExpr(+, Id(y), FloatLit(0.1)))"
        self.assertTrue(TestChecker.test(input, expect, 450))  
    def test_inherit19(self): # ask the teacher. 
        input = """
foo: function integer(y: auto) inherit foo1 {
    super(y);
    y = y + true;
    }
       foo1: function integer(inherit x: integer){
            x = x + 1;
            x = x + 1.5; 
        }
"""
        expect = "Type mismatch in expression: BinExpr(+, Id(y), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_inherit20(self):
        input = """
foo: function integer(y: integer) inherit foo1 {
    super(69);
    }
       foo1: function integer(inherit x: auto){
            printInteger(x); 
            foo1(x); 
        }
"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 452))  
    def test_inherit21(self): 
        input = """
       foo1: function integer(inherit x: auto){
            printInteger(x); 
            foo1(x); 
        }
        foo: function integer(y: integer) inherit foo1 {
        super(1.5);
    }
        """
        expect = "Type mismatch in statement: CallStmt(super, FloatLit(1.5))"
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_inherit22(self): 
        input = """
       foo1: function integer(inherit x: auto){
            printInteger(x); 
            foo1(x); 
        }
        foo: function integer(y: integer) inherit foo1 {
        y = 69; 
    }
        """
        expect = "Invalid statement in function: AssignStmt(Id(y), IntegerLit(69))"
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test_inherit23(self): 
        input = """
       foo1: function integer(inherit x: auto){
            printInteger(x); 
            foo1(x); 
        }
        foo: function integer(y: integer) inherit foo1 {
        super(1); 
    }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_FuncBody2(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) printInteger(x);
            while (1111) printInteger(x); 

        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Type mismatch in statement: WhileStmt(IntegerLit(1111), CallStmt(printInteger, Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 456))
    def test_FuncBody3(self): 
        input = """
        foo: function boolean(x:integer) {
            do {printInteger(x);}
            while (x > 1);
            do {printInteger(x);}
            while (1111);
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Type mismatch in statement: DoWhileStmt(IntegerLit(1111), BlockStmt([CallStmt(printInteger, Id(x))]))"
        self.assertTrue(TestChecker.test(input, expect, 457))
    def test_infer_1(self): 
        input = """
        main: function void () { 
            a : auto = 10;
            b : auto = "hello";
            c : auto = a < 100;
            if (c) { 
                printString(b);
            }
            else {
                writeFloat(a); 
            }
        }
        """
        expect = "Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_infer_14(self): 
        input = """
        a:integer = foo(78); 
        foo: function auto (x:integer) {
            return 1; 
        }
        b:boolean = foo(1); 
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, BooleanType, FuncCall(foo, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test_infer_3(self): 
        input = """
        foo_: function void() {
            foo(69); 
        } 
        foo: function auto (x:integer) {
            x = x + foo(10); 
            return 1; 
        }
        """
        expect = "Type mismatch in expression: BinExpr(+, Id(x), FuncCall(foo, [IntegerLit(10)]))"
        self.assertTrue(TestChecker.test(input, expect, 460))
    def test_infer_4(self): 
        input = """
        a:integer = foo(78) + 15 ; 
        foo: function auto (x:integer) {
            return 1; 
        }
        b:boolean = foo(1); 
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, BooleanType, FuncCall(foo, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_FuncBody_11(self): 
        input = """
foo: function void(out x: integer){}
main: function void(){
         foo(2);
}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test_FuncBody_12(self): 
        # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988
        input = """
 x: integer = foo();
    foo: function integer (){}

        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test_FuncBody_13(self): 
        # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=7988
        input = """
foo: function void(){
       {
            x = 5;
        }
        x: integer;
 }
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 464)) 
    def test_FuncBody_14(self): 
        # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8110
        input = """
main: function void () {printInteger(a);}
a: integer = 1;
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 465))  
    def test_FuncBody_15(self): 
        # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8317
        input = """
a: integer;
main: function void() {
   b: integer = a;
}

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466)) 
    def test_infer7(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
    a: auto = foo(1, 2);

    foo: function auto() { }
        }"""
        expect = """Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 467)) 
    def test_FuncBody_16_epKieu(self):
        # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=8051
        input = """
    foo: function void (a: float, b: integer) {}
    main: function void () {
        foo(1,2);
    }
                
        }"""
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 468))
    def test_infer8(self):
        # a = a + b; // Line này liệu có bị TypeMismatchInExpression không
        input = """
        foo: function void(a: auto, b: integer) {
        a = a + b;
        a = 1.5; 
}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), FloatLit(1.5))"""
        self.assertTrue(TestChecker.test(input, expect, 469))
    def test_variable(self):
        # OPERAND TYPE: INT
        input = """
        a: integer = 5.4;
"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(5.4))"""
        self.assertTrue(TestChecker.test(input, expect, 470)) 
    def test_FuncBody17(self): 
        input = """
        bar: function void (inherit a: integer){}
foo: function void (a: integer) inherit bar {
preventDefault();
}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 471))
    def test_FuncBody18(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                
            }
            continue; 
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 472))
    def test_FuncBody19(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                continue; 
                // a = 7; 
            }
            continue; 
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test_FuncBody19(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                continue;   
            }
            continue; 
            x = 1.2;
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 474))
    def test_FuncBody20(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                continue;   
                a = 69;
            }
            continue; 
            x = 1.2;
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 475))
    def test_FuncBody21(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                continue;   
                a = 69; 
                continue; 
            }
            x = 1.2;
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 476))
    def test_FuncBody22(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                a:integer = 69; 
            }
            a = 7;
            x = 1.2;
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 477))
    def test_infer_15(self): 
        input = """
        foo1: function integer(y:integer) { 
            y = y + foo(12); 
            return y;
        }
        foo: function auto (x:integer) {
            return 1; 
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test_FuncBody23(self): 
        input = """
        inc : function void (out n : integer, a:float) inherit foo {}
        foo : function auto (inherit n: float, n: integer){} 
        """
        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test_FuncBody24(self): 
        input = """
        inc : function void (out n : integer, a:float) inherit foo {}
        foo : function auto (inherit n: float, c: integer){} 
        """
        expect = "Invalid Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 480))
    def test_FuncBody25(self): 
        input = """
        inc : function void (out n : integer, a:float) inherit foo {}
        foo : function auto (inherit f: float, c: integer){} 
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 481))
    def test_infer_16(self): 
        input = """
        foo: function auto() {}
        a: float = -foo();
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 482))
    def test_FuncBody26(self): 
        input = """
                foo: function void() inherit foo1{
                    super("HCMUT",true);
                    {
                        x = 7;
                    }
                }
                foo1: function void (inherit x: string, inherit x:boolean){}
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 483))
    def test_infer_17(self): 
        input = """
                a:  integer = 5;
                b : auto = a  == true;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 484))
    def test_infer_18(self):
        input = """
        x: integer = foo();
        foo: function integer (){}

            main: function void () {                
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_TypeMismatchInSTMT_1(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            M: function void (a: integer) inherit N {} 
N: function void (inherit a: integer) {}

                
        }"""
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 486))   
    def test_Throw_lhs_or_rhs(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        main: function void() {
    a = b;
}
"""
        expect = """Undeclared Identifier: b"""
        self.assertTrue(TestChecker.test(input, expect, 487))
    def test_FuncBody28(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function boolean (inherit a: integer, b: float, c: string) {}

bar: function void(a: float) inherit foo {

        super(12, 2.0);

}
"""
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test_FuncBody29(self):
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
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 489))
    def test_FuncBody30(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        main: function auto() { return; }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test_FuncBody31(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        main: function auto() { return 1; }"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test_FuncBody32(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function void (a: integer) inherit bar { super(1,2); }
bar: function void (inherit a: string, inherit a: integer) { }
"""
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 492))
    def test_FuncBody33(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9192
        input = """a:function boolean() {a:integer;} """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test_FuncBody34(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # https://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=9192
        input = """ x: function integer() {} 
 foo: function float() { x: integer = x(); } 
"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_FuncBody35(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                continue;
                a = 7; 
            }
            continue; 
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test_FuncBody365(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                continue;
                a = 7;
                continue; 
            }
            continue; 
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 496))
    def test_FuncBody36(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                {
                    a:integer = 12; 
                } 
                a = 9; 
            }
            continue; 
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test_FuncBody37(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                {
                    return true; 
                } 
                a = 9; 
            }
            continue; 
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test_FuncBody38(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                {
                    continue;
                } 
                a = 9; 
            }
            continue; 
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 499))
    def test_FuncBody39(self): 
        input = """
        foo: function boolean(x:integer) {
            while (x > 1) {
                {
                    while (x < 5) {
                    continue; 
                    }
                    x = 1.4;
                } 
                a = 9; 
            }
            continue; 
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), FloatLit(1.4))"
        self.assertTrue(TestChecker.test(input, expect,500))
    def test_FuncBody39(self): 
        input = """
        foo: function boolean(x:integer) {
            if (x > 1) {
                while (x < 2) {
                continue; 
                    }
                x = 1.1; 
                }
            }
            continue; 
        }
        main: function void() {
            foo(1.5);
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(x), FloatLit(1.1))"
        self.assertTrue(TestChecker.test(input, expect,501))
        # Trang 58
    def test_Vardecl1(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
a: integer = foo();
foo: function string() { }
"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 502))
    def test_FuncBody40(self): 
        input = """
        inc : function void (out n : integer, n: float) inherit foo{
      super(0.1, 1);
      n: string = 124;    
} 
foo : function auto (inherit n: float, b: integer){}

        """
        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input, expect,503))
    # Trang 58
#     def test_TypeMismatchInSTMT_2(self):

    def test_array1(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                a:array [3] of integer = {1,3,4.5};
                
        }"""
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(3), FloatLit(4.5)])"""
        self.assertTrue(TestChecker.test(input, expect, 504))
    def test_TypeMismatchInExpression_array33(self):
        """Test TypeMismatchInExpression_array"""
        # Can list of integer consist of ID . This is an example 
        input = """
            main: function void () {
                x: integer = 11;
                a:array [12] of float;  
                b: integer;
                b = a[x]; 
        }"""
        expect = """Type mismatch in statement: AssignStmt(Id(b), ArrayCell(a, [Id(x)]))"""
        self.assertTrue(TestChecker.test(input, expect, 505))   
    def test_TypeMismatchInExpression_array44(self):
        """Test TypeMismatchInExpression_array"""
        # Can list of integer consist of ID . This is an example 
        input = """
            main: function void () {
                x: integer = 11;
                a:array [12] of integer;  
                b: integer;
                b = a[x]; 
        }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 506))   
    def test_array5(self):
        """Test TypeMismatchInExpression_array2"""
        input = """
            main: function void () {
                a:array [12] of integer;
                b: integer;
                b = a[1.1]; 
        }"""
        expect = """Type mismatch in expression: ArrayCell(a, [FloatLit(1.1)])"""
        self.assertTrue(TestChecker.test(input, expect, 507)) 
    def test_array6(self):
        """Test TypeMismatchInExpression_array"""
        input = """
            main: function void () {
                b: integer; 
                b = a[11]; 
        }"""
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 508))
    def test_array7(self):
        """Test TypeMismatchInExpression_array"""
        input = """
            main: function void () {
                a:array [4] of integer = {1}; 
                // a: array [0] of integer; // khong can bat
        }"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([4], IntegerType), ArrayLit([IntegerLit(1)]))"""
        self.assertTrue(TestChecker.test(input, expect, 509))
    def test_array8(self): 
        """Test TypeMismatchInExpression_array"""
        input = """
            main: function void () {
                a: array[2] of integer = { {1}, {2} };
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)])]))"
        self.assertTrue(TestChecker.test(input, expect, 510)) 
    def test_array9(self): 
        """Test TypeMismatchInExpression_array"""
        input = """
            main: function void () {
                a: auto = { 1,2 };
                printInteger(a[0]); 
        }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 511)) 
    def test_array10(self): 
        """Test TypeMismatchInExpression_array"""
        input = """
            main: function void () {
                a:array [1,2,3] of integer; 
                printInteger(a[1]); 
        }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 512)) 
    def test_SuccessFirstStatement22(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function integer () {
                return 1.5;
        }
       """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(1.5))"""
        self.assertTrue(TestChecker.test(input, expect, 513))
    def test_For1(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        i:string;
        foo: function integer (a:integer, b: float) {
            for(i = "Hello World", i < 10, i + 1) {
                return 0;
            }
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), StringLit(Hello World)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(0))]))"""
        self.assertTrue(TestChecker.test(input, expect, 514))
    def test_FuncBody40(self): 
        input = """
        foo1: function integer(y:integer) { 
            y = y + foo(12); 
            return y;
        }
        foo: function auto (x:integer) {
            return 10; 
            return true; 
        }
        """
        expect = "Type mismatch in statement: ReturnStmt(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 515))
    def test_TypeMismatchInSTMT_voidFunc2(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo: function integer (){}
            main: function void () {
                a: integer = 2.3 + foo(); 
        }"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, FloatLit(2.3), FuncCall(foo, [])))"
        self.assertTrue(TestChecker.test(input, expect, 516))
    def test_FuncBody41(self): 
        input = """
        foo: function boolean(x:integer) {
            do {
                    if (x == 11) break; 
                    else {
                        x = x  + 1; 
                        continue;
                        } 
                }
            while (x > 1); 
            continue; 
        }
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 517))
    def test_array_11(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
               array [2, 3, 2] of integer = {{{1, 2}, {1, 2}}, {{1, 2}, {1, "2"}, {1, 2}}};
                
        }"""
        expect = """Program([
	FuncDecl("foo", () [Param(x, FloatType)], None, BlockStmt([]))
	FuncDecl("foo"1, VoidType(), [Param(a, IntegerType), InheritParam(x, FloatType)], foo, BlockStmt([CallStmt(super, FloatLit(11.11)), VarDecl(x, () IntegerLit(2023)), ReturnStmt()]))
	FuncDecl("main", VoidType(), [], None, BlockStmt([CallStmt(foo1, IntegerLit(21), FloatLit(21.12))]))
])"""
        self.assertTrue(TestChecker.test(input, expect, 518)) 
    def test_array_12(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
               a:array [2, 2] of integer =  { {1 , 2}, {1,1.5} };
                
        }"""
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(1.5)])"""
        self.assertTrue(TestChecker.test(input, expect, 519)) 
    def test_array_13(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
               a: array[2] of integer = { {1}, {2} }; 
                
        }"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 520)) 
    def test_array_14(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
          foo: function integer () {return 1;}  
          x: array [1,2,3] of integer; 
          y: auto = x[1,foo()];
          """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 521)) 
    def test_array_15(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                arr:array[2,2] of integer = {{1,2}, {1,2}};
                
        }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 522)) 
    def test_array_16(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                arr: array [6] of integer = {1, 2, 3, 4, 5};
                
        }"""
        expect = """Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([6], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))"""
        self.assertTrue(TestChecker.test(input, expect, 523)) 
    def test_array_17(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                a: array [3] of integer = {1,2,3};
                a[0.1] = 8; 
                
        }"""
        expect = """Type mismatch in expression: ArrayCell(a, [FloatLit(0.1)])"""
        self.assertTrue(TestChecker.test(input, expect, 524)) 
    def test_array_18(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                a: array [2,2] of integer = {{1,2},{3,4}};
                a[1,0.1] = 8; 
                
        }"""
        expect = """Type mismatch in expression: ArrayCell(a, [IntegerLit(1), FloatLit(0.1)])"""
        self.assertTrue(TestChecker.test(input, expect, 525)) 
    def test_array_19(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo1:function auto() {}
            foo2:function auto() {}
            main: function void () {
                a: array [2] of integer = { foo1(), foo2() };
                b: integer = 1; 

        }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 526)) 
    def test_array_20(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo1:function integer(a:auto, b:auto) {
                arr: array [2] of integer = { a, b };
                a = a + 0.1; 
            }
        }"""
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 527)) 
    def test_FuncBody50(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        expect = """
        foo: function integer (x: float) {}
        """
        input = """Program([
	FuncDecl("foo", () [Param(x, FloatType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestChecker.test(input, expect, 528))
    def test_409(self):
        input = """ 
            a: integer = fibo(5);
            main: function void () {}
        """
        expect = """Undeclared Function: fibo"""
        self.assertTrue(TestChecker.test(input, expect, 529))
    def test_411(self):
        input = """ 
            a: integer = fibo(5.2);
            fibo: function integer (n: integer) {}
            main: function void () {}
        """
        expect = """Type mismatch in expression: FloatLit(5.2)"""
        self.assertTrue(TestChecker.test(input, expect, 530))
    def test_412(self):
        input = """ 
            a: integer = fibo();
            fibo: function integer (n: integer) {}
            main: function void () {}
        """
        expect = """Type mismatch in expression: FuncCall(fibo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 531))
    def test_413(self):
        input = """
        fibo: function integer (n: integer) {
            {
                n: integer = 1;
                k: integer = 1;
            }
            k: integer = 1;
            {
                n: integer = 1;
                k: integer = 1;
            }
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 532))
    def test_415(self):
        input = """
        fibo: function integer (n: integer) {
            continue;
        }
        main: function void () {}
        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 533))
    def test_416(self):
        input = """
        fibo: function integer (n: integer) {
            {break;}
        }
        main: function void () {}
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 534))
    def test_417(self):
        input = """
        fibo: function integer (n: integer) {
            {return 1;}
            {return 2.2;}
            {return 3;}
            {return 4;}
        }
        main: function void () {}
        """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(2.2))"""
        self.assertTrue(TestChecker.test(input, expect, 535))
    def test_419(self):
        input = """
        fibo: function auto (n: integer) {
            return !false;
        }
        main: function void () {
            b:boolean = fibo(69); 
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 536))
    def test_422(self):
        input = """
        test: function integer () {
            return -true;
        }
        main: function void () {}
        """
        expect = """Type mismatch in expression: UnExpr(-, BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 537))
    def test_21212(self):
        input = """
        aaaaa: array[3] of integer = {1,2,3};
        baaaa: array[2] of integer = {1,2,3};
        main: function void () {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(baaaa, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 538))
    def test_424(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[3] of float = {1,2,3};
        main: function void () {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, ArrayType([3], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 539))
    def test_427(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[1,2,1] of integer = {{{69},{420}}};
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 540))
    def test_428(self):
        input = """
        main: function void () {
            i:auto = 1+2.0;
            for(i=3,i<5,i+2){
                continue;
            }
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ContinueStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, 541))
#     def test_SuccessFirstStatement2(self):
#         """test_TypeMismatchInBinExp_REMAINDER""" 
#         # OPERAND TYPE: INT
#         expect = """
#         foo: function integer () {}
#         foo1: function void (a:integer) inherit foo {
#                 preventDefault();  
#         }
#             main: function void () {
#                 foo1(69); 
#         }"""
#         input = """Program([
# 	FuncDecl("foo", () [], None, BlockStmt([]))
# 	FuncDecl("foo"1, VoidType(), [Param(a, IntegerType)], foo, BlockStmt([CallStmt(preventDefault, )]))
# 	FuncDecl("main", VoidType(), [], None, BlockStmt([CallStmt(foo1, IntegerLit(69))]))
# ])"""
#         self.assertTrue(TestChecker.test(input, expect, 446))
 

#     def test_FuncDeclAfterCalledByAnotherFunction(self):
#         """test_TypeMismatchInBinExp_REMAINDER""" 
#         # OPERAND TYPE: INT
#         expect = """
#         foo: function integer (x: float) {return foo1(69);}
#         foo1: function integer (x: integer) {return 0;}
#         main: function void () {

#         }
#         """
#         input = """Program([
# 	FuncDecl("foo", () [Param(x, FloatType)], None, BlockStmt([ReturnStmt(FuncCall(foo1, [IntegerLit(69)]))]))
# 	FuncDecl("foo"1, () [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
# 	FuncDecl("main", VoidType(), [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestChecker.test(input, expect, 449))  
                                         

#     def test_TypeMismatchInBinExp_EQUAL0(self):
#         """test_TypeMismatchInBinExp_NOTEQUAL""" 
#         # OPERAND TYPE: INT/BOOLEAN
#         expect = """
#             main: function void () {
#                 a: boolean; 
#                 a = (12.25 != 12); 
#         }"""
#         input = """Program([
# 	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", BooleanType()), AssignStmt(Id("a"), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
# ])"""
#         self.assertTrue(TestChecker.test(input, expect, 456))


#     def test_TypeMismatchInSTMT_voidFunc2(self):
#         """test_TypeMismatchInBinExp_REMAINDER""" 
#         # OPERAND TYPE: INT
#         expect = """
#             foo: function integer (){}
#             main: function void () {
#                 a: integer = 2.3 + foo(); 
#         }"""
#         input = Program([
# 	FuncDecl("foo", IntegerType(), [], None, BlockStmt([])),
# 	FuncDecl("main", VoidType(), [], None, BlockStmt([CallStmt("foo",[] )]))
# ])
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 422))

    # def test_FuncBody4(self): 
    #     input = """
    #     foo: function boolean(x:integer) {
    #         if (x > 1) printInteger(x); 
    #         if (x + 28) {
    #             printInteger(x); 
    #         } 
    #     }
    #     main: function void() {
    #         foo(1.5);
    #     }
    #     """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(y), BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input, expect, 456))

    # def test_FuncBody6(self): 
    #     input = """
    #     foo: function boolean(x:integer) {
    #         while (x < 111) {
    #                 if (x == 11) break; 
    #                 else {
    #                     x = x  + 1; 
    #                     continue;
    #                     } 
    #         }
    #         continue; 
    #     }
    #     main: function void() {
    #         foo(1.5);
    #     }
    #     """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(y), BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input, expect, 458))


    # def test_FuncBody10(self): 
    #     input = """
    #     foo: function boolean(x:auto) {
    #         for (x = 1, x < 100,x + 1) printInteger(x);

    #     }
    #     main: function void() {
    #         foo(1.5);
    #     }
    #     """
    #     expect = "Type mismatch in expression: BinExpr(+, Id(y), BooleanLit(True))"
    #     self.assertTrue(TestChecker.test(input, expect, 462))
