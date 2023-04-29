import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test401(self):
        input = """
            a: integer;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test402(self):
        input = """"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test403(self):
        input = """
        a: integer;
        b: float;
        a: string;
        main: function void () {}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test404(self):
        input = """
        a: integer;
        b: auto;
        main: function void () {}
        """
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test405(self):
        input = """
        recur: function integer (a:integer,b:integer,a:integer) {
        }
        main: function void () {}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test406(self):
        input = """
            a: integer = 1;
            b: float = 1;
            c: string = "1";
            d: boolean = true;
            f: string;
            g: boolean;
            h: float;
            i: integer;
            main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test407(self):
        input = """
            a: integer = 1.0;
            main: function void () {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test408(self):
        input = """
            fibo: function integer (n: integer) {}
            main: function void () {}
            fibo: function float (n: integer) {}
        """
        expect = """Redeclared Function: fibo"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test409(self):
        input = """ 
            a: integer = fibo(5);
            main: function void () {}
        """
        expect = """Undeclared Function: fibo"""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test410(self):
        input = """ 
            a: integer = fibo(5);
            fibo: function integer (n: integer) {}
            main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test411(self):
        input = """ 
            a: integer = fibo(5.2);
            fibo: function integer (n: integer) {}
            main: function void () {}
        """
        expect = """Type mismatch in expression: FloatLit(5.2)"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test412(self):
        input = """ 
            a: integer = fibo();
            fibo: function integer (n: integer) {}
            main: function void () {}
        """
        expect = """Type mismatch in expression: FuncCall(fibo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test413(self):
        input = """
        fibo: function integer (n: integer) {
            n: integer = 1;
        }
        main: function void () {}
        """
        expect = """Redeclared Variable: n"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test414(self):
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
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test415(self):
        input = """
        fibo: function integer (n: integer) {
            continue;
        }
        main: function void () {}
        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test416(self):
        input = """
        fibo: function integer (n: integer) {
            {break;}
        }
        main: function void () {}
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test417(self):
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
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test418(self):
        input = """
        fibo: function integer (n: integer) {
            return a;
        }
        main: function void () {}
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test419(self):
        input = """
        fibo: function auto (n: integer) {
            return false;
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test420(self):
        input = """
        a: integer;
        fibo: function integer (n: integer) {
            return a;
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test421(self):
        input = """
        test: function integer () {
            return !true;
        }
        main: function void () {}
        """
        expect = """Type mismatch in statement: ReturnStmt(UnExpr(!, BooleanLit(True)))"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test422(self):
        input = """
        test: function integer () {
            return -true;
        }
        main: function void () {}
        """
        expect = """Type mismatch in expression: UnExpr(-, BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test423(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[2] of integer = {1,2,3};
        main: function void () {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test424(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[3] of float = {1,2,3};
        main: function void () {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, ArrayType([3], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test425(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[3] of integer = {1,2,3.2};
        main: function void () {}
        """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.2)])"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test426(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[1,2,1] of integer = {{{69},{420}}};
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test427(self):
        input = """
        main: function void () {
            while (true) {
                break;
            }
            if(1<2){
                a: integer = 1;
            }
            //i:integer = 1;
            for(i=3,i<5,i+2){
                continue;
            }
        }
        """
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test428(self):
        input = """
        main: function void () {
            i:auto = 1+2.0;
            for(i=3,i<5,i+2){
                continue;
            }
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(i), IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test429(self):
        input = """
        a: float;
        b: integer;
        main: function void () {
            a = 1 + b;
            b = 1.5 + a;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(b), BinExpr(+, FloatLit(1.5), Id(a)))"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test430(self):
        input = """
        a: float;
        b: string;
        main: function void () {
            a = 1 + b;
        }
        """
        expect = """Type mismatch in expression: BinExpr(+, IntegerLit(1), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test431(self):
        input = """
        a: integer;
        foo: function integer (c: integer, d: integer) {}
        main: function void () {
            b: integer;
            foo(b,a);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test432(self):
        input = """
        foo: function integer (c: integer, d: integer) {}
        main: function void () {
            b: integer = foo+1;
        }
        """
        expect = """Type mismatch in expression: BinExpr(+, Id(foo), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test433(self):
        input = """
        a: auto = foo(1,2)+3.1;
        foo: function integer (c: integer, d: integer) {}
        main: function void () {
            foo(a,a);
        }
        """
        expect = """Type mismatch in expression: Id(a)"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test434(self):
        input = """
        x : auto = {4,5,6};
        y : auto = x[1,2];
        main: function void () {
        }
        """
        expect = """Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test435(self):
        input = """
        a: array[2,2] of integer;
        b: array[2] of integer = a[0];
        main: function void () {
        
        }
        
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test436(self):
        input = """
        foo: function integer() inherit bar{preventDefault();}
        main: function void () {}
        """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test437(self):
        input = """
        main: function void () {
            i:integer;
            for(i=1,i<10,i+1){
                if(i==5)
                    break;
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test438(self):
        input = """
        main: function void () {
            i:integer;
            for(i=1,i<10,i+1){
                if(i==5)
                    continue;
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test439(self):
        input = """
        foo: function integer() inherit bar{preventDefault();}
        bar: function integer(inherit out n:integer,inherit a:float) {preventDefault();}
        fizz: function integer(inherit sixty9:auto) inherit Bar {preventDefault();}
        buzz: function integer() inherit fizz{preventDefault();}
        main: function void () {}
        """
        expect = """Undeclared Function: Bar"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test440(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer () inherit foo {
            preventDefault();
            a = foo(1);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test441(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer () inherit foo {
            preventDefault();
            foo(true,1);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test442(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer () inherit foo {
            preventDefault();
            foo();
        }
        """
        expect = """Type mismatch in statement: CallStmt(foo, )"""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test443(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer () inherit foo {
            preventDefault();
            a = foo();
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test444(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer () inherit foo {
            preventDefault();
            a = foo(true,1);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test445(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer (p: boolean) inherit foo {
            preventDefault();
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test446(self):
        input = """
        a: integer;
        foo: function integer (inherit p: boolean) {}
        bar: function integer (p: boolean) inherit foo {
            preventDefault();
        }
        main: function void () {}
        """
        expect = """Invalid Parameter: p"""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test447(self):
        input = """
        a: integer;
        foo: function integer (inherit p: boolean) {}
        bar: function integer (k: boolean) inherit foo {
        }
        main: function void () {}
        """
        expect = """Invalid statement in function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test448(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer (p: boolean) inherit foo {
            super(true);
        }
        main: function void () {}
        """
        expect = """Invalid statement in function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test449(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer (p: boolean) inherit foo {
            super();
        }
        main: function void () {}
        """
        expect = """Invalid statement in function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test450(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer (p: boolean) inherit foo {
            preventDefault();
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 450))