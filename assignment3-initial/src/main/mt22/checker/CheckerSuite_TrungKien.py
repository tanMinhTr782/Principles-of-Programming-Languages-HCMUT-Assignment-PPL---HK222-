import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_101(self):
        input = """
        main: function void () {}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,101))

    def test_102(self):
        input = """
        main: function void (x:float) {}
        main: function void () {}
        """
        expect = """Redeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,102))

    def test_103(self):
        input = """
        main: function void (x:float, x:string) {}
        main: function void () {}
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,103))

    def test_104(self):
        input = """
        foo: function void () {}
        foo: function void () {}    
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,104))

    def test_105(self):
        input = """
        foo: function void () inherit tmp {}
        foo: function void () {}    
        """
        expect = """Undeclared Function: tmp"""
        self.assertTrue(TestChecker.test(input,expect,105))

    def test_106(self):
        input = """
        foo: function void () {}    
        foo: function void () inherit tmp {}
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,106))

    def test_107(self):
        input = """
        tmp: function void (inherit x:integer, x: integer) {}    
        foo: function void () inherit tmp {}
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,107))

    def test_108(self):
        input = """
        foo: function void () inherit tmp {}
        tmp: function void (inherit x:integer, x: integer) {}    
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,108))

    def test_108(self):
        input = """
        foo: function void (x:float) inherit tmp {}
        tmp: function void (inherit x:integer, x: integer) {}    
        """
        expect = """Invalid Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,108))

    def test_109(self):
        input = """
        foo: function void (a:float, a:string) inherit tmp {}
        tmp: function void (inherit x:integer, x: integer) {}    
        """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input,expect,109))

    def test_110(self):
        input = """
        tmp: function void (inherit x:integer, x: integer) {}    
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,110))

    def test_111(self):
        input = """
        foo: function void(x:integer, x:integer) inherit tmp {}
        tmp: function void(y:integer, y:integer) {}
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,111))

    def test_112(self):
        input = """
        foo: function void(x:integer) inherit tmp {}
        tmp: function void(y:integer, inherit x:integer) {}
        """
        expect = """Invalid Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,112))

    def test_113(self):
        input = """
        x: function void (x:float) {}
        main: function void (x:float) {}
        main: function void () {}
        """
        expect = """Redeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,113))

    def test_114(self):
        input = """
        x: function void (x:float) {}
        main: function void (x:float) {}
        y: function void (a:float, a:float) {}
        """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input,expect,114))

    def test_115(self):
        input = """
        a: function void() {}
        x: function void() {a:integer;} 
        main: function void () {}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,115))

    def test_116(self):
        input = """
        x: function void() {a:integer;} 
        a: function void() {}
        main: function void () {}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,116))

    def test_117(self):
        input = """
        x: function void() {a:integer;} 
        a: function void() {}
        main: function void () {}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,117))

    def test_118(self):
        input = """
        foo: function void (inherit a: integer, a: float) inherit bar {}
        """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input,expect,118))


    def test_119(self):
        input = """
        bar: function void (inherit a: integer){}
        foo: function void (a: integer) inherit bar {
                preventDefault()
        }
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input,expect,119))

    def test_120(self):
        input = """
        a: integer = 2.3; 
        b: auto; 
        foo: function void(a: integer, b: float) {} 
        bar: function void() inherit foo {} 
        a: function void() {} 
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(2.3))"""
        self.assertTrue(TestChecker.test(input,expect,120))

    def test_121(self):
        input = """
        b: auto; 
        foo: function void(a: integer, b: float) {} 
        bar: function void() inherit foo {} 
        a: function void() {} 
        """
        expect = """Invalid Variable: b"""
        self.assertTrue(TestChecker.test(input,expect,121))

    def test_122(self):
        input = """
        foo : function auto (inherit n: float, n: integer){} 
        inc : function void (out n : integer, a:float) inherit foo{} 
        """
        expect = """Redeclared Parameter: n"""
        self.assertTrue(TestChecker.test(input,expect,122))

    def test_123(self):
        input = """
        a : integer;
        a : function void (out n : integer, a:float) inherit foo{} 
        """
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input,expect,123))

    def test_124(self):
        input = """
        a : function void (out n : integer, a:float){} 
        a : integer;
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input,expect,124))

    def test_0(self): # Success
        input = """
        main: function void () {}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_1(self): # Success
        input = """
        main: function void () {}
        fact: function integer () {}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_3(self): # Success
        input = """
        main: function void () {}
        fact: function integer (x:integer, y: float, z:boolean) {}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_4(self): # No main
        input = """
        fact: function integer (x:integer, y: float, z:boolean) {}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_6(self): # Redeclared function
        input = """
        fact: function integer (x:integer, y: float, z:boolean) {}
        fact: function void (m:integer, n: float {}
        main: function void () {}
        """
        expect = """Redeclared Function: fact"""
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_7(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {}
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void () {}
        """
        expect = """Invalid statement in function: fact"""
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_8(self):
        input = """
        fact: function void (m:integer, n: float) inherit foo {}
        main: function void () {}
        """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_9(self): # Redecl params
        input = """
        main: function void () {}
        foo: function void (x:integer, y: float, z:string, x: boolean) {}
        fact: function integer (x:integer, y: float, z:boolean) {}
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,409))
# ------------------------------------- [TEST VARDECL PROGRAM] --------------------------------------#
    def test_10(self): # Redecl with the params    
        input = """
        x:integer;
        foo: function void (x:integer, y: float, z:string, t:boolean) {
            x:integer;
        }
        main: function void () {}
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_11(self):  # Param auto not init -> Invalid(Variable(), varName)
        input = """
        main: function void () {
            a : auto;
        }
        """
        expect = """Invalid Variable: a"""
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_12(self): #Success
        input = """
        main: function void () {
            a : auto = 1;
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_13(self): # Check type float and int #Check
        input = """
        main: function void () {
            a:integer = 5.0;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(5.0))"""
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_14(self): # Succesful
        input = """
        main: function void () {
            a :integer = 5;
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_15(self): # Check
        input = """
        main: function void () {
            a : float = 5;
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_16(self):  
        input = """
            a : integer ;
            a: function integer() {}
            main: function void () {}
        """
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_17(self): #Type mismatch 
        input = """
        main: function void () {}
        foo: function void (x:integer, y: float, z:string) {
            a : float =  true;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, FloatType, BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_18(self): # success
        input = """
        main: function void () {}
        foo: function void (x:integer, y: float, z:string) {
            a:float;
            {
                x:integer;
            }
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_19(self): # success
        input = """
        main: function void () {}
        foo: function void (x:integer, y: float, z:string) {
            a:float;
            {
                {
                    x:integer;
                }
            }
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_20(self): # success
        input = """
        main: function void () {}
        x : auto = "Kien";
        foo: function void (x:integer, y: float, z:string) {
            a:float;
            {
                b: integer;
                {
                    b: integer;
                    x:integer;
                }
            }
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_21(self): # success
        input = """
        x : auto = "Kien";
        main: function void () {}
        foo: function void (x:integer, y: float, z:string) {
            a:float;
            {
                b: integer;
                {
                    b: integer;
                    x:integer;
                }
            }
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_22(self): # Success
        input = """
        main: function void (x:integer) {}
        main: function void (x:integer) {}
        """
        expect = """Redeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_23(self): # Bien trung ten ham cua no scope 1
        input = """
        main: function void () {}
        foo: function void (x:integer) {
            {
                foo: integer;
            }
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_24(self): # # Bien trung ten ham cua no scope 0
        input = """
        main: function void () {}
        foo: function void (x:integer) {
            foo: integer;
            {}
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_25(self): # Tham so co ten trung voi ten ham cua no
        input = """
        main: function void () {}
        foo: function void (foo:integer) {}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_26(self): # Bien trung ten ham khac scope 0
        input = """
        main: function void () {}
        foo: function void (x:integer) {
            main: integer;
            {}
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_27(self): # Bien trung ten ham cua no scope 1
        input = """
        main: function void () {}
        foo: function void (x:integer) {
            {
                main: integer;
            }
        }
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,427))
# ------------------------------------- [TEST INHERIT] --------------------------------------#
    def test_28(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            x:integer;
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        """
        expect = """Invalid statement in function: fact"""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_29(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            preventDefault();
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_30(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            preventDefault();
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_31(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            fact();
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Invalid statement in function: fact"""
        self.assertTrue(TestChecker.test(input,expect,431))


    def test_32(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super();
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Type mismatch in statement: CallStmt(super, )"""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_33(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Type mismatch in statement: CallStmt(super, IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_34(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,2,3);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Type mismatch in statement: CallStmt(super, IntegerLit(1), IntegerLit(2), IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_35(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,1.0,true);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_36(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Type mismatch in statement: CallStmt(super, FloatLit(1.0), FloatLit(1.0), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_37(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,1.0,true);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_38(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,1.0,1);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Type mismatch in statement: CallStmt(super, IntegerLit(1), FloatLit(1.0), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_39(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,1.0,true);
            x: integer;
        }
        foo: function integer (inherit x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_40(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,1.0,true);
            y: integer;
        }
        foo: function integer (inherit x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_41(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,1.0,true);
            {
                x:integer;
            }
        }
        foo: function integer (inherit x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_42(self): 
        input = """
        bar: function void (inherit a: integer){}
        foo: function void (a: integer) inherit bar {
        preventDefault()
        }
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_43(self): 
        input = """
        foo: function void (inherit a: integer, a: float) inherit bar {}
        """
        expect = """Undeclared Function: bar"""
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_44(self): 
        input = """
        inc : function void (out n : integer, a:float) inherit foo{
            super(1,1);
        } 
        foo : function auto (inherit n: float, n: integer){} 
        """
        expect = """Invalid Parameter: n"""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_45(self): 
        input = """
        x: function void() {}
        main: function void() inherit x {
        super(); //
        } 
        """
        expect = """[]"""
        self.assertTrue(TestChecker.test(input,expect,445))

    # def test_42(self): 
    #     input = """
    #     x, y: integer: 1, foo(1, 2, 3); 
    #     x, y: string;                           
    #     foo: function integer (x: integer, y: integer, x:integer){}   
     
    #     """
    #     expect = """[]"""
    #     self.assertTrue(TestChecker.test(input,expect,407))

    def test_47(self): 
        input = """
        a: integer = 2.3; 
        b: auto; 
        foo: function void(a: integer, b: float) {} 
        bar: function void() inherit foo {} 
        a: function void() {} 
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(2.3))"""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_48(self): 
        input = """
        a: float = 3; 
        b: auto; 
        foo: function void(a: integer, b: float) {} 
        bar: function void() inherit foo {} 
        a: function void() {} 
        """
        expect = """Invalid Variable: b"""
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_49(self): 
        input = """
        foo: function integer(inherit x: integer) inherit bar
        {
            super(2);
        }

        bar: function integer(inherit y: integer) inherit foo2 
        {
            super("Hi");
        }
        foo2: function integer(inherit z: float){}
        """
        expect = """Type mismatch in statement: CallStmt(super, StringLit(Hi))"""
        self.assertTrue(TestChecker.test(input,expect,449))