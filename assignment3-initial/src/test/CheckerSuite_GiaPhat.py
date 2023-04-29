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
        expect = """"""
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

    def test451(self):
        input = """
        a: array[3] of integer = {1,2,3};
        b: array[1,2,1] of integer = {{{69},{420,69}}};
        main: function void () {}
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(69)]), ArrayLit([IntegerLit(420), IntegerLit(69)])])"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test452(self):
        input = """
        foo: function void (a:auto) {}
        a: function void () {}
        main: function void () {
                foo(a);
        }
        """
        expect = """Type mismatch in expression: Id(a)"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test453(self):
        input = """
        a: function void () { super();}
        main: function void () {
        }
        """
        expect = """Invalid statement in function: a"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test454(self):
        input = """
        a: function void () { preventDefault();}
        main: function void () {
        }
        """
        expect = """Invalid statement in function: a"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test455(self):
        input = """
        x : auto={4,5,6};
        y:  auto=x[1,2];
        """
        expect = """Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test456(self):
        input = """
        x:float;
        y:float;
        main: function void () {
            a: boolean = x==y;
        }
        """
        expect = """Type mismatch in expression: BinExpr(==, Id(x), Id(y))"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test457(self):
        input = """a: integer = 5.4;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(5.4))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test458(self):
        input = """
        foo: function void(out a: auto, out b: integer) {
         a = a + b; 
        }
        main: function void () {
            foo(1,2);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test459(self):
        input = """foo: function void(){

       {

            x = 5;

        }

        x: integer;
 }
 """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test460(self):
        input = Program([
            FuncDecl('main', VoidType(), [], None, BlockStmt(
                [CallStmt('printInteger', [Id('a')])])),
            VarDecl('a', IntegerType(), IntegerLit(1))])
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test461(self):
        input = """
        b: integer;
        foo: function void(out a: integer, out b:boolean){}
        main: function void () {
            foo(b,2);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(2)"""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test462(self):
        input = """
        b: integer;
        foo: function void(out a: integer, out b:boolean){}
        main: function void () {
            foo(b,true);
        }
        """
        expect = """Type mismatch in expression: BooleanLit(True)"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test463(self):
        input = """
            a: function void (p : array [1] of integer) {}
            main: function void () {
            a({1});
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test464(self):
        input = """
            a: function void (p : array [1] of integer) {}
            main: function void () {
            a({1,2});
            }
        """
        expect = """Type mismatch in expression: ArrayLit([IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test465(self):
        input = """
            a: function void (p : array [1] of integer) {}
            main: function void () {
            a({1.0});
            }
        """
        expect = """Type mismatch in expression: ArrayLit([FloatLit(1.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test466(self):
        input = """
            a: function integer (p : array [1] of integer) {}
            main: function void () {
            b: integer = a({0});
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test467(self):
        input = """
            a: function integer (p : array [1] of integer) {}
            main: function void () {
            b: integer = a({{0}});
            }
        """
        expect = """Type mismatch in expression: ArrayLit([ArrayLit([IntegerLit(0)])])"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test468(self):
        input = """
        
        foo: function auto() {}
        main: function void () {
            a: integer = foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test469(self):
        input = """
        foo:function auto() {}
         a: integer = foo();
        main: function void () {
            b: boolean = foo();
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, BooleanType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test470(self):
        input = """
        foo:function auto() {}
        main: function void () {
            a: boolean = foo();
            b: boolean = foo();
            c: string = foo();
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, StringType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test471(self):
        input = """
        foo:function auto() {}
        main: function void () {
        
            b: array[1] of integer = {foo()};
            c: integer = foo();
            d: array[1] of float = {foo()+1.2};
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test472(self):
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
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test473(self):
        input = """
        a: array[2] of integer = { {1}, {2} };
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1)]), ArrayLit([IntegerLit(2)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test474(self):
        input = """
        bar: function void (inherit a: integer){
        
        }

        foo: function void (a: integer) inherit bar {
            preventDefault();
            }
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test475(self):
        input = """
        foo: function void (inherit a: integer, a: float) inherit bar {}
        """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test476(self):
        input = """
        foo: function integer(){}
        main: function void(){
            m: integer;
            m = foo + 1;
        }
        """
        expect = """Type mismatch in expression: BinExpr(+, Id(foo), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test477(self):
        input = """
        foo: function auto(){}
        bar: function boolean(){
            return foo();
        }
        main: function void(){
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test478(self):
        input = """
        bar: function boolean(a:integer){
            if (a==5)
                return a;
        }
        main: function void(){
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test479(self):
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
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test480(self):
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
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test481(self):
        input = """
        func: function void(a: integer, b: float) {}
        main: function void() { func(1);}
        """
        expect = """Type mismatch in statement: CallStmt(func, IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test482(self):
        input = """
        func: function void(a: integer, b: float) {}
        main: function void() { func(1,2.0,3);}
        """
        expect = """Type mismatch in expression: IntegerLit(3)"""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test483(self):
        input = """x, y: integer = 1, foo(1, 2, 3); 
                    x, y: string;                      
                    foo: function integer (x: integer, y: integer, x:integer){}
                """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test484(self):
        input = """
        foo: function integer (inherit x: integer,inherit y: integer,inherit out z:integer){}
        bar: function integer () inherit foo{
            super(1,2);
        }
        main: function void(){}
        """
        expect = """Type mismatch in statement: CallStmt(super, IntegerLit(1), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test485(self):
        input = """
        foo: function integer (inherit x: integer,inherit y: integer,inherit out z:integer){}
        bar: function integer () inherit foo{
            super(1,2,3);
        }
        main: function void(){}
        """
        expect = """Type mismatch in expression: IntegerLit(3)"""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test486(self):
        input = """
        a: integer;
        main: function void(){
            a = 3.5;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), FloatLit(3.5))"""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test487(self):
        input = """
        a: boolean;
        main: function void(){
            a = true && false || (1==2);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test488(self):
        input = """
        a: boolean;
        main: function void(){
            a = true && false || (1+2);
        }
        """
        expect = """Type mismatch in expression: BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), BinExpr(+, IntegerLit(1), IntegerLit(2)))"""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test489(self):
        input = """
        a: boolean;
        main: function void(){
            a = true && false || (1==2)>0;
        }
        """
        expect = """Type mismatch in expression: BinExpr(>, BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), BinExpr(==, IntegerLit(1), IntegerLit(2))), IntegerLit(0))"""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test490(self):
        input = """
         a: string = "Ligma";
         b: auto = "ball";
         main: function void(){
            a = a::" "::b;
         }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test491(self):
        input = """
         a: string = "Ligma";
         b: auto = "ball";
         main: function void(){
            a = a::" "::b::" "::1;
         }
        """
        expect = """Type mismatch in expression: BinExpr(::, BinExpr(::, BinExpr(::, BinExpr(::, Id(a), StringLit( )), Id(b)), StringLit( )), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test492(self):
        input = """
        foo: function integer (inherit x: integer){}
        bar: function integer () inherit foo{
            super(1);
            return x;
        }
        main: function void(){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test493(self):
        input = """
        foo: function integer (inherit x: integer){}
        bar: function integer () inherit foo{
            super(1);
            return x*1.4;
        }
        main: function void(){}
        """
        expect = """Type mismatch in statement: ReturnStmt(BinExpr(*, Id(x), FloatLit(1.4)))"""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test494(self):
        input = """
        foo: function integer (inherit x: integer){}
        bar: function integer () inherit foo{
            super(1);
            return x::"1";
        }
        main: function void(){}
        """
        expect = """Type mismatch in expression: BinExpr(::, Id(x), StringLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test495(self):
        input = """
        foo: function string (inherit x: auto){}
        bar: function string () inherit foo{
            super(1);
            return;
        }
        main: function void(){}
        """
        expect = """Type mismatch in statement: ReturnStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test496(self):
        input = """
        foo: function string (inherit out x: auto){}
        bar: function string () inherit foo{
            super(1);
            return x;
        }
        main: function void(){}
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test497(self):
        input = """
        foo: function string (inherit out x: auto){}
        bar: function string () inherit foo{
           preventDefault();
           return x;
        }
        main: function void(){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test498(self):
        input = """
        foo: function string (inherit out x: auto){}
        bar: function string () inherit foo{
        }

        main: function void(){}
        """
        expect = """Invalid statement in function: bar"""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test499(self):
        input = """
        a: auto = foo();
        foo: function string (){}
        main: function void(){
        a = "Lick my balls";
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test500(self):
        input = """
        a: auto = foo();
        foo: function float (){}
        main: function void(){
        a = 1+1;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 500))
