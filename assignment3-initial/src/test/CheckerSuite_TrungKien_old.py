import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_401(self):
        input = """
            a: integer;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 601))

    def test_402(self):
        input = """"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 602))

    def test_403(self):
        input = """
        a: integer;
        b: float;
        a: string;
        main: function void () {}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 603))

    def test_404(self):
        input = """
        a: integer;
        b: auto;
        main: function void () {}
        """
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 604))

    def test_405(self):
        input = """
        recur: function integer (a:integer,b:integer,a:integer) {
        }
        main: function void () {}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 605))

    def test_406(self):
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
        self.assertTrue(TestChecker.test(input, expect, 606))

    def test_407(self):
        input = """
            a: integer = 1.0;
            main: function void () {}
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 607))

    def test_408(self):
        input = """
            fibo: function integer (n: integer) {}
            main: function void () {}
            fibo: function float (n: integer) {}
        """
        expect = """Redeclared Function: fibo"""
        self.assertTrue(TestChecker.test(input, expect, 608))

    def test_409(self):
        input = """ 
            a: integer = fibo(5);
            main: function void () {}
        """
        expect = """Undeclared Function: fibo"""
        self.assertTrue(TestChecker.test(input, expect, 609))

    def test_410(self):
        input = """ 
            a: integer = fibo(5);
            fibo: function integer (n: integer) {}
            main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 610))

    def test_411(self):
        input = """ 
            a: integer = fibo(5.2);
            fibo: function integer (n: integer) {}
            main: function void () {}
        """
        expect = """Type mismatch in expression: FloatLit(5.2)"""
        self.assertTrue(TestChecker.test(input, expect, 611))

    def test_412(self):
        input = """ 
            a: integer = fibo();
            fibo: function integer (n: integer) {}
            main: function void () {}
        """
        expect = """Type mismatch in expression: FuncCall(fibo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 612))

    def test_413(self):
        input = """
        fibo: function integer (n: integer) {
            n: integer = 1;
        }
        main: function void () {}
        """
        expect = """Redeclared Variable: n"""
        self.assertTrue(TestChecker.test(input, expect, 613))

    def test_414(self):
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
        self.assertTrue(TestChecker.test(input, expect, 614))

    def test_415(self):
        input = """
        fibo: function integer (n: integer) {
            continue;
        }
        main: function void () {}
        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 615))

    def test_416(self):
        input = """
        fibo: function integer (n: integer) {
            {break;}
        }
        main: function void () {}
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 616))

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
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(1.2))"""
        self.assertTrue(TestChecker.test(input, expect, 617))

    def test_418(self):
        input = """
        fibo: function integer (n: integer) {
            return a;
        }
        main: function void () {}
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 618))

    def test_419(self):
        input = """
        fibo: function auto (n: integer) {
            return false;
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 619))

    def test_420(self):
        input = """
        a: integer;
        fibo: function integer (n: integer) {
            return a;
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 620))

    def test_421(self):
        input = """
        test: function integer () {
            return !true;
        }
        main: function void () {}
        """
        expect = """Type mismatch in statement: ReturnStmt(UnExpr(!, BooleanLit(T1ue)))"""
        self.assertTrue(TestChecker.test(input, expect, 621))

    def test_422(self):
        input = """
        test: function integer () {
            return -true;
        }
        main: function void () {}
        """
        expect = """Type mismatch in expression: UnExpr(-, BooleanLit(T1ue))"""
        self.assertTrue(TestChecker.test(input, expect, 622))

    def test_423(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[2] of integer = {1,2,3};
        main: function void () {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(1)]))"""
        self.assertTrue(TestChecker.test(input, expect, 623))

    def test_424(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[3] of float = {1,2,3};
        main: function void () {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, ArrayType([3], FloatType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(1)]))"""
        self.assertTrue(TestChecker.test(input, expect, 624))

    def test_425(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[3] of integer = {1,2,3.2};
        main: function void () {}
        """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.2)])"""
        self.assertTrue(TestChecker.test(input, expect, 625))

    def test_426(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[1,2,1] of integer = {{{69},{420}}};
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 626))

    def test_427(self):
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
        self.assertTrue(TestChecker.test(input, expect, 627))

    def test_428(self):
        input = """
        main: function void () {
            i:auto = 1+2.0;
            for(i=3,i<5,i+2){
                continue;
            }
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(i), IntegerLi1(3))"""
        self.assertTrue(TestChecker.test(input, expect, 628))

    def test_429(self):
        input = """
        a: float;
        b: integer;
        main: function void () {
            a = 1 + b;
            b = 1.5 + a;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(b), BinExpr(+, FloatLit(1.5), I1(a)))"""
        self.assertTrue(TestChecker.test(input, expect, 629))

    def test_430(self):
        input = """
        a: float;
        b: string;
        main: function void () {
            a = 1 + b;
        }
        """
        expect = """Type mismatch in expression: BinExpr(+, IntegerLit(1), I1(b))"""
        self.assertTrue(TestChecker.test(input, expect, 630))

    def test_431(self):
        input = """
        a: integer;
        foo: function integer (c: integer, d: integer) {}
        main: function void () {
            b: integer;
            foo(b,a);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 631))

    def test_432(self):
        input = """
        foo: function integer (c: integer, d: integer) {}
        main: function void () {
            b: integer = foo+1;
        }
        """
        expect = """Type mismatch in expression: BinExpr(+, Id(foo), IntegerLi1(1))"""
        self.assertTrue(TestChecker.test(input, expect, 632))

    def test_433(self):
        input = """
        a: auto = foo(1,2)+3.1;
        foo: function integer (c: integer, d: integer) {}
        main: function void () {
            foo(a,a);
        }
        """
        expect = """Type mismatch in expression: Id(a)"""
        self.assertTrue(TestChecker.test(input, expect, 633))

    def test_434(self):
        input = """
        x : auto = {4,5,6};
        y : auto = x[1,2];
        main: function void () {
        }
        """
        expect = """Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 634))

    def test_435(self):
        input = """
        a: array[2,2] of integer;
        b: array[2] of integer = a[0];
        main: function void () {
        
        }
        
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 635))

    def test_436(self):
        input = """
        foo: function integer() inherit bar{preventDefault();}
        main: function void () {}
        """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 636))

    def test_437(self):
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
        self.assertTrue(TestChecker.test(input, expect, 637))

    def test_438(self):
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
        self.assertTrue(TestChecker.test(input, expect, 638))

    def test_439(self):
        input = """
        foo: function integer() inherit bar{preventDefault();}
        bar: function integer(inherit out n:integer,inherit a:float) {preventDefault();}
        fizz: function integer(inherit sixty9:auto) inherit Bar {preventDefault();}
        buzz: function integer() inherit fizz{preventDefault();}
        main: function void () {}
        """
        expect = """Undeclared Function: Bar"""
        self.assertTrue(TestChecker.test(input, expect, 639))

    def test_440(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer () inherit foo {
            preventDefault();
            a = foo(1);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 640))

    def test_441(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer () inherit foo {
            preventDefault();
            foo(true,1);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 641))

    def test_442(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer () inherit foo {
            preventDefault();
            foo();
        }
        """
        expect = """Type mismatch in statement: CallStmt(foo, )"""
        self.assertTrue(TestChecker.test(input, expect, 642))

    def test_443(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer () inherit foo {
            preventDefault();
            a = foo();
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 643))

    def test_444(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer () inherit foo {
            preventDefault();
            a = foo(true,1);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 644))

    def test_445(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer (p: boolean) inherit foo {
            preventDefault();
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 645))

    def test_446(self):
        input = """
        a: integer;
        foo: function integer (inherit p: boolean) {}
        bar: function integer (p: boolean) inherit foo {
            preventDefault();
        }
        main: function void () {}
        """
        expect = """Invalid Parameter: p"""
        self.assertTrue(TestChecker.test(input, expect, 646))

    def test_447(self):
        input = """
        a: integer;
        foo: function integer (inherit p: boolean) {}
        bar: function integer (k: boolean) inherit foo {
        }
        main: function void () {}
        """
        expect = """Invalid statement in function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 647))

    def test_448(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer (p: boolean) inherit foo {
            super(true);
        }
        main: function void () {}
        """
        expect = """Invalid statement in function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 648))

    def test_449(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer (p: boolean) inherit foo {
            super();
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 649))

    def test_450(self):
        input = """
        a: integer;
        foo: function integer (p: boolean) {}
        bar: function integer (p: boolean) inherit foo {
            preventDefault();
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 650))

    def test_451(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[1,2,1] of integer = {{{69},{420,69}}};
        main: function void () {}
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(69)]), ArrayLit([IntegerLit(420), IntegerLit(69)])])"""
        self.assertTrue(TestChecker.test(input, expect, 651))

    def test_452(self):
        input = """
        foo: function void (a:auto) {}
        a: function void () {}
        main: function void () {
                foo(a);
        }
        """
        expect = """Type mismatch in expression: Id(a)"""
        self.assertTrue(TestChecker.test(input, expect, 652))

    def test_453(self):
        input = """
        a: function void () { super();}
        main: function void () {
        }
        """
        expect = """Invalid statement in function: a"""
        self.assertTrue(TestChecker.test(input, expect, 653))

    def test_454(self):
        input = """
        a: function void () { preventDefault();}
        main: function void () {
        }
        """
        expect = """Invalid statement in function: a"""
        self.assertTrue(TestChecker.test(input, expect, 653))

    def test_455(self):
        input = """
        x : auto={4,5,6};
        y:  auto=x[1,2];
        """
        expect = """Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 655))

    def test_456(self):
        input = """
        x:float;
        y:float;
        main: function void () {
            a: boolean = x==y;
        }
        """
        expect = """Type mismatch in expression: BinExpr(==, Id(x), I1(y))"""
        self.assertTrue(TestChecker.test(input, expect, 656))

    def test_457(self):
        input = """a: integer = 5.4;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(1.4))"
        self.assertTrue(TestChecker.test(input, expect, 657))

    def test_458(self):
        input = """
        foo: function void(out a: auto, out b: integer) {
         a = a + b; 
        }
        main: function void () {
            foo(1,2);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 658))

    def test_459(self):
        input = """foo: function void(){

       {

            x = 5;

        }

        x: integer;
 }
 """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 659))

    def test_461(self):
        input = """
        b: integer;
        foo: function void(out a: integer, out b:boolean){}
        main: function void () {
            foo(b,2);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(2)"""
        self.assertTrue(TestChecker.test(input, expect, 661))

    def test_462(self):
        input = """
        b: integer;
        foo: function void(out a: integer, out b:boolean){}
        main: function void () {
            foo(b,true);
        }
        """
        expect = """Type mismatch in expression: BooleanLit(True)"""
        self.assertTrue(TestChecker.test(input, expect, 662))

    def test_463(self):
        input = """
            a: function void (p : array [1] of integer) {}
            main: function void () {
            a({1});
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 663))

    def test_464(self):
        input = """
            a: function void (p : array [1] of integer) {}
            main: function void () {
            a({1,2});
            }
        """
        expect = """Type mismatch in expression: ArrayLit([IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 664))

    def test_465(self):
        input = """
            a: function void (p : array [1] of integer) {}
            main: function void () {
            a({1.0});
            }
        """
        expect = """Type mismatch in expression: ArrayLit([FloatLit(1.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 665))

    def test_466(self):
        input = """
            a: function integer (p : array [1] of integer) {}
            main: function void () {
            b: integer = a({0});
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 666))

    def test_467(self):
        input = """
            a: function integer (p : array [1] of integer) {}
            main: function void () {
            b: integer = a({{0}});
            }
        """
        expect = """Type mismatch in expression: ArrayLit([ArrayLit([IntegerLit(0)])])"""
        self.assertTrue(TestChecker.test(input, expect, 667))

    def test_468(self):
        input = """
        
        foo: function auto() {}
        main: function void () {
            a: integer = foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 668))

    def test_469(self):
        input = """
        foo:function auto() {}
         a: integer = foo();
        main: function void () {
            b: boolean = foo();
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, BooleanType, FuncCall(foo,1[]))"""
        self.assertTrue(TestChecker.test(input, expect, 669))

    def test_470(self):
        input = """
        foo:function auto() {}
        main: function void () {
            a: boolean = foo();
            b: boolean = foo();
            c: string = foo();
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, StringType, FuncCall(foo,1[]))"""
        self.assertTrue(TestChecker.test(input, expect, 670))

    def test_471(self):
        input = """
        foo:function auto() {}
        main: function void () {
        
            b: array[1] of integer = {foo()};
            c: integer = foo();
            d: array[1] of float = {foo()+1.2};
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 671))

    def test_472(self):
        input = """
        foo:function auto() {}
        main: function void () {
        
            b: array[1] of integer = {foo()};
            c: integer = foo();
            d: array[1] of float = {foo()+1.2};
            e: float = foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 672))

    def test_473(self):
        input = """
        a: array[2] of integer = { {1}, {2} };
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)1)]))"""
        self.assertTrue(TestChecker.test(input, expect, 673))

    def test_474(self):
        input = """
        bar: function void (inherit a: integer){
        
        }

        foo: function void (a: integer) inherit bar {
            preventDefault();
            }
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 674))

    def test_475(self):
        input = """
        foo: function void (inherit a: integer, a: float) inherit bar {}
        """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 675))

    def test_476(self):
        input = """
        foo: function integer(){}
        main: function void(){
            m: integer;
            m = foo + 1;
        }
        """
        expect = """Type mismatch in expression: BinExpr(+, Id(foo), IntegerLi1(1))"""
        self.assertTrue(TestChecker.test(input, expect, 676))

    def test_477(self):
        input = """
        foo: function auto(){}
        bar: function boolean(){
            return foo();
        }
        main: function void(){
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 677))

    def test_478(self):
        input = """
        bar: function boolean(a:integer){
            if (a==5)
                return a;
        }
        main: function void(){
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(I1(a))"""
        self.assertTrue(TestChecker.test(input, expect, 678))

    def test_479(self):
        input = """
        bar: function boolean(a:integer){
            
            k:boolean = 5==4;
            {
                a: string = "Yo Mr. White";
            }
            return k;
            k: integer = 5;

        }
        main: function void(){
        }
        """
        expect = """Redeclared Variable: k"""
        self.assertTrue(TestChecker.test(input, expect, 679))

    def test_480(self):
        input = """func: function integer() {
            a: integer = 1;
            while(a < 10) {
            a = a + 1;
            continue;
            a: float = 12.0;
            }  
            }
        main: function void() {}
            """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 680))

    def test_481(self):
        input = """
        func: function void(a: integer, b: float) {}
        main: function void() { func(1);}
        """
        expect = """Type mismatch in statement: CallStmt(func, IntegerLi1(1))"""
        self.assertTrue(TestChecker.test(input, expect, 681))

    def test_482(self):
        input = """
        func: function void(a: integer, b: float) {}
        main: function void() { func(1,2.0,3);}
        """
        expect = """Type mismatch in expression: IntegerLit(3)"""
        self.assertTrue(TestChecker.test(input, expect, 682))

    def test_483(self):
        input = """x, y: integer = 1, foo(1, 2, 3); 
                    x, y: string;                      
                    foo: function integer (x: integer, y: integer, x:integer){}
                """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 683))

    def test_484(self):
        input = """
        foo: function integer (inherit x: integer,inherit y: integer,inherit out z:integer){}
        bar: function integer () inherit foo{
            super(1,2);
        }
        main: function void(){}
        """
        expect = """Type mismatch in statement: CallStmt(super, IntegerLit(1), IntegerLi1(2))"""
        self.assertTrue(TestChecker.test(input, expect, 684))

    def test_485(self):
        input = """
        foo: function integer (inherit x: integer,inherit y: integer,inherit out z:integer){}
        bar: function integer () inherit foo{
            super(1,2,3);
        }
        main: function void(){}
        """
        expect = """Type mismatch in expression: IntegerLit(3)"""
        self.assertTrue(TestChecker.test(input, expect, 685))

    def test_486(self):
        input = """
        a: integer;
        main: function void(){
            a = 3.5;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), FloatLit(1.5))"""
        self.assertTrue(TestChecker.test(input, expect, 686))

    def test_487(self):
        input = """
        a: boolean;
        main: function void(){
            a = true && false || (1==2);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 687))

    def test_488(self):
        input = """
        a: boolean;
        main: function void(){
            a = true && false || (1+2);
        }
        """
        expect = """Type mismatch in expression: BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(Fa1se)), BinExpr(+, IntegerLit(1), IntegerLi1(2)))"""
        self.assertTrue(TestChecker.test(input, expect, 688))

    def test_489(self):
        input = """
        a: boolean;
        main: function void(){
            a = true && false || (1==2)>0;
        }
        """
        expect = """Type mismatch in expression: BinExpr(>, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(Fa1se)), BinExpr(==, IntegerLit(1), IntegerLi1(2))), IntegerLi1(0))"""
        self.assertTrue(TestChecker.test(input, expect, 689))

    def test_490(self):
        input = """
         a: string = "Ligma";
         b: auto = "ball";
         main: function void(){
            a = a::" "::b;
         }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 690))

    def test_491(self):
        input = """
         a: string = "Ligma";
         b: auto = "ball";
         main: function void(){
            a = a::" "::b::" "::1;
         }
        """
        expect = """Type mismatch in expression: BinExpr(::, BinExpr(::, BinExpr(::, BinExpr(::, Id(a), StringLi1( )), I1(b)), StringLi1( )), IntegerLi1(1))"""
        self.assertTrue(TestChecker.test(input, expect, 691))

    def test_492(self):
        input = """
        foo: function integer (inherit x: integer){}
        bar: function integer () inherit foo{
            super(1);
            return x;
        }
        main: function void(){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 692))

    def test_493(self):
        input = """
        foo: function integer (inherit x: integer){}
        bar: function integer () inherit foo{
            super(1);
            return x*1.4;
        }
        main: function void(){}
        """
        expect = """Type mismatch in statement: ReturnStmt(BinExpr(*, Id(x), FloatLit(1.4)))"""
        self.assertTrue(TestChecker.test(input, expect, 693))

    def test_494(self):
        input = """
        foo: function integer (inherit x: integer){}
        bar: function integer () inherit foo{
            super(1);
            return x::"1";
        }
        main: function void(){}
        """
        expect = """Type mismatch in expression: BinExpr(::, Id(x), StringLi1(1))"""
        self.assertTrue(TestChecker.test(input, expect, 694))

    def test_495(self):
        input = """
        foo: function string (inherit x: auto){}
        bar: function string () inherit foo{
            super(1);
            return;
        }
        main: function void(){}
        """
        expect = """Type mismatch in statement: ReturnStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 695))

    def test_496(self):
        input = """
        foo: function string (inherit out x: auto){}
        bar: function string () inherit foo{
            super(1);
            return x;
        }
        main: function void(){}
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 696))

    def test_497(self):
        input = """
        foo: function string (inherit out x: auto){}
        bar: function string () inherit foo{
           preventDefault();
           return x;
        }
        main: function void(){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 697))

    def test_498(self):
        input = """
        foo: function string (inherit out x: auto){}
        bar: function string () inherit foo{
        }

        main: function void(){}
        """
        expect = """Invalid statement in function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 698))

    def test_499(self):
        input = """
        a: auto = foo();
        foo: function string (){}
        main: function void(){
        a = "Lick my balls";
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 699))

    def test500(self):
        input = """
        a: auto = foo();
        foo: function float (){}
        main: function void(){
        a = 1+1;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 700))
 