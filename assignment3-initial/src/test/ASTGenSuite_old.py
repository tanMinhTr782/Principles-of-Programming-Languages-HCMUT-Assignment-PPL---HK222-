import unittest
from TestUtils import TestAST
from AST import *
# py run.py test ParserSuite
# py run.py test ASTGenSuite
class ASTGenSuite(unittest.TestCase):
    def test_basicUndeclared_Identifier(self):
        """Test basicUndeclared_Identifier"""
        input = """main: function void () {
            a: integer = 65; 
            a = a + b;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(65)), AssignStmt(Id(a), BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))
    def test_basicUndeclared_Identifier_Param(self):
        """Test basicUndeclared_Identifier_Param"""
        input = """
            bds: function integer () {
                return a; 
            }
            main: function void () {
        }"""
        expect = """Program([
	FuncDecl(bds, IntegerType, [], None, BlockStmt([ReturnStmt(Id(a))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))
    def test_basicUndeclared_Function(self):
        """Test basicUndeclared_Function"""
        input = """main: function void () {
                helloWorld(); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(helloWorld, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))
    def test_InvaildVariableDecl_AutoNoInit(self):
        """Test InvaildVariableDecl_AutoNoInit"""
        input = """
            main: function void () {
                x:auto; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, AutoType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))
    def test_InvaildParamDecl(self):
        """Test InvaildVariable_AutoNoInit"""
        input = """
            foo: function integer(a:integer) {}
            main: function void (){
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))   
    def test_TypeMismatchInExpression_array1(self):
        """Test TypeMismatchInExpression_array"""
        input = """
            main: function void () {
                b: integer; 
                b = a[11]; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(b, IntegerType), AssignStmt(Id(b), ArrayCell(a, [IntegerLit(11)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    def test_TypeMismatchInExpression_array2(self):
        """Test TypeMismatchInExpression_array2"""
        input = """
            main: function void () {
                a:array [12] of integer;
                b: integer;
                b = a[1.1]; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([12], IntegerType)), VarDecl(b, IntegerType), AssignStmt(Id(b), ArrayCell(a, [FloatLit(1.1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307)) 
    def test_TypeMismatchInBinExp_SCOPE(self):
        """Test TypeMismatchInBinExp_SCOPE"""
        input = """
            main: function void () {
                a: string; 
                a = "HCMUT"::2023; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType), AssignStmt(Id(a), BinExpr(::, StringLit(HCMUT), IntegerLit(2023)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))
#################################### RELATIONAL BASIC TEST #################################
    def test_TypeMismatchInBinExp_EQUAL(self):
        """test_TypeMismatchInBinExp_EQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 == 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(==, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309)) 
    def test_TypeMismatchInBinExp_EQUAL1(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 < "12.25"); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(<, FloatLit(12.25), StringLit(12.25)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    def test_TypeMismatchInBinExp_GREATERTHAN(self):
        """test_TypeMismatchInBinExp_GREATERTHAN""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 > true); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(>, FloatLit(12.25), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))
    def test_TypeMismatchInBinExp_LESSTHAN(self):
        """test_TypeMismatchInBinExp_LESSTHAN""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: boolean;
                b: array [3] of boolean;  
                a = (12.25 < b); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), VarDecl(b, ArrayType([3], BooleanType)), AssignStmt(Id(a), BinExpr(<, FloatLit(12.25), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))
    def test_TypeMismatchInBinExp_LESSTHAN1(self):
        """test_TypeMismatchInBinExp_LESSTHANEQ""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: boolean;
                b: array [3] of boolean;  
                a = (12.25 <= b); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), VarDecl(b, ArrayType([3], BooleanType)), AssignStmt(Id(a), BinExpr(<=, FloatLit(12.25), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))
    def test_TypeMismatchInBinExp_GREATTHANEQ(self):
        """test_TypeMismatchInBinExp_GREATTHANEQ""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: boolean;
                c:string = "11.11";
                a = (11.11 >= c); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), VarDecl(c, StringType, StringLit(11.11)), AssignStmt(Id(a), BinExpr(>=, FloatLit(11.11), Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))   
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
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), UnExpr(<class 'str'>, FloatLit(11.11)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))
    def test_TypeMismatchInBinExp_AND(self):
        """test_TypeMismatchInBinExp_GREATTHANEQ""" 
        # OPERAND TYPE: BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (11.11 && true); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(&&, FloatLit(11.11), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))
    def test_TypeMismatchInBinExp_OR(self):
        """test_TypeMismatchInBinExp_GREATTHANEQ""" 
        # OPERAND TYPE: BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (2801 || true); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(||, IntegerLit(2801), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
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
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType), AssignStmt(Id(a), UnExpr(<class 'str'>, StringLit(0301)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))    

    def test_TypeMismatchInBinExp_MINUS(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: integer; 
                a = "0301" - 73; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(-, StringLit(0301), IntegerLit(73)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))   
    def test_TypeMismatchInBinExp_ADD(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: integer; 
                a = 73  + true; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(+, IntegerLit(73), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))  
    def test_TypeMismatchInBinExp_DIV(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: integer;

                a = {1,2,3} / 73; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(/, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(73)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321)) 
    def test_TypeMismatchInBinExp_MUL(self):
        """test_TypeMismatchInBinExp_MINUS""" 
        # OPERAND TYPE: INT/FLOAT
        input = """
            main: function void () {
                a: integer;
                a = 73 * "2"; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(*, IntegerLit(73), StringLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))  
    def test_TypeMismatchInBinExp_REMAINDER(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                a: integer;
                a = 73 % true; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(%, IntegerLit(73), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
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
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(a), BinExpr(+, IntegerLit(73), FuncCall(foo, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
    def test_TypeMismatchInSTMT_voidFunc2(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo: function integer (){}
            main: function void () {
                foo(); 
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
    def test_TypeMismatchInSTMT_FuncCallNotVoid(self):
        """test_TypeMismatchInSTMT_FuncCallNotVoid""" 
        # OPERAND TYPE: INT
        input = """
            foo: function integer (){}
            main: function void () {
                foo(); 
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
    def test_TypeMismatchInSTMT_ifCond(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                if (3 + 4) {
                    
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(+, IntegerLit(3), IntegerLit(4)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
    def test_TypeMismatchInSTMT_whileCond(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                while (2 / 4) {
                
                }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(/, IntegerLit(2), IntegerLit(4)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    def test_TypeMismatchInSTMT_dowhileCond(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                do {
                
                }
                while ("HCMUT"::"K22"); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(::, StringLit(HCMUT), StringLit(K22)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
    def test_TypeMismatchInSTMT_for(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                for (i = "12", i >= 0, i - 1){
                
                } 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), StringLit(12)), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
    def test_TypeMismatchInSTMT_for1(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                for (i = 12, i >= 0, i - 0.5){
                
                } 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(12)), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), FloatLit(0.5)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
    def test_TypeMismatchInSTMT_for11(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                for (i = true, i >= 0, i - 1){
                
                } 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), BooleanLit(True)), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
    def test_TypeMismatchInSTMT_for2(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:array [3] of integer = {1,2,3}; 
                x = {4,5,6}; 
                
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), AssignStmt(Id(x), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
    def test_TypeMismatchInSTMT_intAssFloat(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:integer; 
                x = 1.5; 
                
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), FloatLit(1.5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
    def test_TypeMismatchInSTMT_floatAssInt(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:float; 
                x = 1; 
                
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType), AssignStmt(Id(x), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
    def test_TypeMismatchInSTMT_000(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                x:boolean; 
                x = 1; 
                
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, BooleanType), AssignStmt(Id(x), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))  
    def test_TypeMismatchInSTMT_00(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            foo: function integer() {}
            foo1: function void(a:integer,b:integer) inherit foo {}
            main: function void () {
                foo1(true,12); 
                
        }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([]))
	FuncDecl(foo1, VoidType, [Param(a, IntegerType), Param(b, IntegerType)], foo, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo1, BooleanLit(True), IntegerLit(12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
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
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([ReturnStmt(StringLit(Hello world))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338)) 
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
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([ReturnStmt(StringLit(Hello world))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))   
    def test_TypeMismatchInSTMT_2(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                break; 
                
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))   
    def test_TypeMismatchInSTMT_3(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                continue; 
                
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))  
    def test_TypeMismatchInSTMT_4(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
            main: function void () {
                a:array [3] of integer = {1,3,4.5};
                
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(3), FloatLit(4.5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
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
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, BooleanType)], None, BlockStmt([]))
	FuncDecl(foo1, VoidType, [], foo, BlockStmt([ReturnStmt()]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo1, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
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
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType), Param(b, BooleanType)], None, BlockStmt([]))
	FuncDecl(foo1, VoidType, [], foo, BlockStmt([CallStmt(super, IntegerLit(12), BooleanLit(True))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo1, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
    def test_SuccessFirstStatement22(self):
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
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([]))
	FuncDecl(foo1, VoidType, [Param(a, IntegerType)], foo, BlockStmt([CallStmt(preventDefault, )]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo1, IntegerLit(69))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
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
        expect = """Program([
	FuncDecl(foo, IntegerType, [], None, BlockStmt([]))
	FuncDecl(foo1, VoidType, [Param(a, IntegerType)], foo, BlockStmt([CallStmt(preventDefault, )]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo1, IntegerLit(69))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
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
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, FloatType)], None, BlockStmt([]))
	FuncDecl(foo1, VoidType, [Param(a, IntegerType), InheritParam(x, FloatType)], foo, BlockStmt([CallStmt(super, FloatLit(11.11)), VarDecl(x, IntegerType, IntegerLit(2023)), ReturnStmt()]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo1, IntegerLit(21), FloatLit(21.12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))  
    def test_NoEntryPoint(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function integer (x: float) {}
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, FloatType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348)) 
    def test_FuncDeclAfterCalledByAnotherFunction(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        foo: function integer (x: float) {return foo1(69);}
        foo1: function integer (x: integer) {return 0;}
        main: function void () {

        }
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, FloatType)], None, BlockStmt([ReturnStmt(FuncCall(foo1, [IntegerLit(69)]))]))
	FuncDecl(foo1, IntegerType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))  
    def test_mainReturnInteger(self):
        """test_TypeMismatchInBinExp_REMAINDER""" 
        # OPERAND TYPE: INT
        input = """
        main: function integer () {
        } 
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))                                             
    def test_TypeMismatchInExpression_array33(self):
        """Test TypeMismatchInExpression_array"""
        # Can list of integer consist of ID . This is an example 
        input = """
            main: function void () {
                x: integer = 11;
                a:array [12] of integer;  
                b: integer;
                b = a[x]; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(11)), VarDecl(a, ArrayType([12], IntegerType)), VarDecl(b, IntegerType), AssignStmt(Id(b), ArrayCell(a, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))   
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
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(11)), VarDecl(a, ArrayType([12], IntegerType)), VarDecl(b, IntegerType), AssignStmt(Id(b), ArrayCell(a, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))   
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
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(11)), VarDecl(a, ArrayType([12], IntegerType)), VarDecl(b, IntegerType), AssignStmt(Id(b), ArrayCell(a, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
    def test_TypeMismatchInExpression_array35(self):
        """Test TypeMismatchInExpression_array"""
        # Can list of integer consist of ID . This is an example 
        input = """
            main: function void () {
                x: integer = 11;
                a:array [12] of integer;  
                b: integer;
                b = a[x]; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(11)), VarDecl(a, ArrayType([12], IntegerType)), VarDecl(b, IntegerType), AssignStmt(Id(b), ArrayCell(a, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
    def test_TypeMismatchInExpression_array36(self):
        """Test TypeMismatchInExpression_array"""
        # Can list of integer consist of ID . This is an example 
        input = """
            main: function void () {
                x: integer = 11;
                a:array [12] of integer;  
                b: integer;
                b = a[x]; 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(11)), VarDecl(a, ArrayType([12], IntegerType)), VarDecl(b, IntegerType), AssignStmt(Id(b), ArrayCell(a, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))         
    def test_TypeMismatchInBinExp_EQUAL0(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def privatetest_basicExp(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_TypeMismatchInBinExp_EQUAL0(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_TypeMismatchInBinExp_EQUAL0(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_TypeMismatchInBinExp_EQUAL0(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_TypeMismatchInBinExp_EQUAL0(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_TypeMismatchInBinExp_EQUAL0(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_TypeMismatchInBinExp_EQUAL0(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_TypeMismatchInBinExp_EQUAL0(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    def test_TypeMismatchInBinExp_EQUAL0(self):
        """test_TypeMismatchInBinExp_NOTEQUAL""" 
        # OPERAND TYPE: INT/BOOLEAN
        input = """
            main: function void () {
                a: boolean; 
                a = (12.25 != 12); 
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, BooleanType), AssignStmt(Id(a), BinExpr(!=, FloatLit(12.25), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))