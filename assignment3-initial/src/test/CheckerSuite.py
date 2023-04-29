import unittest
from TestUtils import TestChecker
from AST import *
class CheckerSuite(unittest.TestCase):
#  ------------------------------------- [TEST FLOW] --------------------------------------#
    def test_static_10(self):
        input = '''
            main: function void () {
                b: array [5] of integer;
                b[4] = 3;
                printString(b[4]);
            }
        '''
        expect = """Type mismatch in statement: CallStmt(printString, ArrayCell(b, [IntegerLit(4)]))"""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_static_45(self):
        input = '''
            r, s: integer;
            main: function void () {
                a, b: array [5] of integer;
                s = r * r ;
                a[0] = b[2];
                a[0] = b[4]+a[0];
                r = 2.0;
            }
        '''
        expect = """Type mismatch in statement: AssignStmt(Id(r), FloatLit(2.0))"""
        self.assertTrue(TestChecker.test(input, expect, 445))
        
    def test_static_46(self):
        input = '''
            r, s: integer = 5,10;
            main: function void () {
                a, b: array [5] of integer;
                a[0] = s;
                printInt(a[0]);
            }
        '''
        expect = """Undeclared Function: printInt"""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_static_47(self):
        input = '''
            s: string = "2";
            main: function void () {
                a, b: array [5] of integer;
                a[4] = s;
            }
        '''
        expect = """Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(4)]), Id(s))"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_static_48(self):
        input = '''
            main: function void () {
                a, b: array [5] of float;
                a[0] = 2;
                a[3] = 4;
                b[1] = a[1 + a[0]];
            }
        '''
        expect = """Type mismatch in expression: BinExpr(+, IntegerLit(1), ArrayCell(a, [IntegerLit(0)]))"""
        self.assertTrue(TestChecker.test(input, expect, 4482))

    def test_static_49(self):
        input = '''
            main: function void () {
                a: array [5,2] of integer;
                a[0,1] = 2;
                printString(a[0,1] + 2);
                return;
            }
        '''
        expect = """Type mismatch in statement: CallStmt(printString, BinExpr(+, ArrayCell(a, [IntegerLit(0), IntegerLit(1)]), IntegerLit(2)))"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_static_50(self):
        input = '''
            main: function void () {
                a: array [5,2] of float;
                a[0,1] = 2;
                a[0,2] = 5;
                printInteger(a[0,1] + a[0,2]);
            }
        '''
        expect = """Type mismatch in statement: CallStmt(printInteger, BinExpr(+, ArrayCell(a, [IntegerLit(0), IntegerLit(1)]), ArrayCell(a, [IntegerLit(0), IntegerLit(2)])))"""
        self.assertTrue(TestChecker.test(input, expect, 4501))

    def test_static_542(self):
        input = '''
            main: function void () {
                a: auto = {1,2,3};
                a[1,4] = 4;
            }
        '''
        expect = """Type mismatch in expression: ArrayCell(a, [IntegerLit(1), IntegerLit(4)])"""
        self.assertTrue(TestChecker.test(input, expect, 4541))

    def test_static_55(self):
        input = '''
            main: function void () {
                a: auto  = {1,2,3};
                a[2] = "s";
            }
        '''
        expect = """Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(2)]), StringLit(s))"""
        self.assertTrue(TestChecker.test(input, expect, 4551))

    def test_static_60(self):
        input = '''
            main: function void () {
                a: array [5,2] of float;
                a[0] = 2;
                printInteger(a[0,1] + a[0,2]);
            }
        '''
        expect = """Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 4601))
    def test_fl_101(self):
        input = """
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,101))

    def test_fl_102(self):
        input = """
        main: function void (x:float) {}
        main: function void () {}
        """
        expect = """Redeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,102))

    def test_fl_103(self):
        input = """
        main: function void (x:float, x:string) {}
        main: function void () {}
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,103))

    def test_fl_104(self):
        input = """
        foo: function void () {}
        foo: function void () {}    
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,104))

    def test_fl_105(self):
        input = """
        foo: function void () inherit tmp {}
        foo: function void () {}    
        """
        expect = """Undeclared Function: tmp"""
        self.assertTrue(TestChecker.test(input,expect,105))

    def test_fl_106(self):
        input = """
        foo: function void () {}    
        foo: function void () inherit tmp {}
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,106))

    def test_fl_107(self):
        input = """
        tmp: function void (inherit x:integer, x: integer) {}    
        foo: function void () inherit tmp {}
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,107))

    def test_fl_10811(self):
        input = """
        foo: function void () inherit tmp {}
        tmp: function void (inherit x:integer, x: integer) {}    
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,10813))

    def test_fl_10811(self):
        input = """
        foo: function void (x:float) inherit tmp {}
        tmp: function void (inherit x:integer, x: integer) {}    
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,10812))

    def test_fl_109(self):
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

    def test_fl_111(self):
        input = """
        foo: function void(x:integer, x:integer) inherit tmp {}
        tmp: function void(y:integer, y:integer) {}
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,111))

    def test_fl_112(self):
        input = """
        foo: function void(x:integer) inherit tmp {}
        tmp: function void(y:integer, inherit x:integer) {}
        """
        expect = """Invalid Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,112))

    def test_fl_113(self):
        input = """
        x: function void (x:float) {}
        main: function void (x:float) {}
        main: function void () {}
        """
        expect = """Redeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,113))

    def test_fl_114(self):
        input = """
        x: function void (x:float) {}
        main: function void (x:float) {}
        y: function void (a:float, a:float) {}
        """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input,expect,114))

    def test_fl_115(self):
        input = """
        a: function void() {}
        x: function void() {a:integer;} 
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,115))

    def test_fl_116(self):
        input = """
        x: function void() {a:integer;} 
        a: function void() {}
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,116))

    def test_fl_117(self):
        input = """
        x: function void() {a:integer;} 
        a: function void() {}
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,117))

    def test_fl_118(self):
        input = """
        foo: function void (inherit a: integer, a: float) inherit bar {}
        """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input,expect,118))


    def test_fl_119(self):
        input = """
        bar: function void (inherit a: integer){}
        foo: function void (a: integer) inherit bar {
                preventDefault();
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,119))

    def test_fl_120(self):
        input = """
        a: integer = 2.3; 
        b: auto; 
        foo: function void(a: integer, b: float) {} 
        bar: function void() inherit foo {} 
        a: function void() {} 
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(2.3))"""
        self.assertTrue(TestChecker.test(input,expect,120))

    def test_fl_121(self):
        input = """
        b: auto; 
        foo: function void(a: integer, b: float) {} 
        bar: function void() inherit foo {} 
        a: function void() {} 
        """
        expect = """Invalid Variable: b"""
        self.assertTrue(TestChecker.test(input,expect,121))

    def test_fl_122(self):
        input = """
        foo : function auto (inherit n: float, n: integer){} 
        inc : function void (out n : integer, a:float) inherit foo{} 
        """
        expect = """Redeclared Parameter: n"""
        self.assertTrue(TestChecker.test(input,expect,122))

    def test_fl_123(self):
        input = """
        a : integer;
        a : function void (out n : integer, a:float) inherit foo{} 
        """
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input,expect,123))

    def test_fl_124(self):
        input = """
        a : function void (out n : integer, a:float){} 
        a : integer;
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input,expect,124))
# ------------------------------------- [TEST GETENV] --------------------------------------#
    def test_env_0(self): # Success
        input = """
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_env_1(self): # Success
        input = """
        main: function void () {}
        fact: function integer () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_env_3(self): # Success
        input = """
        main: function void () {}
        fact: function integer (x:integer, y: float, z:boolean) {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_env_4(self): # No main
        input = """
        fact: function integer (x:integer, y: float, z:boolean) {}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_env_6(self): # Redeclared function
        input = """
        fact: function integer (x:integer, y: float, z:boolean) {}
        fact: function void (m:integer, n: float) {}
        main: function void () {}
        """
        expect = """Redeclared Function: fact"""
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_env_7(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {}
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void () {}
        """
        expect = """Invalid statement in function: fact"""
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_env_8(self):
        input = """
        fact: function void (m:integer, n: float) inherit foo {}
        main: function void () {}
        """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_env_9(self): # Redecl params
        input = """
        main: function void () {}
        foo: function void (x:integer, y: float, z:string, x: boolean) {}
        fact: function integer (x:integer, y: float, z:boolean) {}
        """
        expect = """Redeclared Parameter: x"""
        self.assertTrue(TestChecker.test(input,expect,409))
# ------------------------------------- [TEST VARDECL PROGRAM] --------------------------------------#
    def test_var_decl_10(self): # Redecl with the params    
        input = """
        x:integer;
        foo: function void (x:integer, y: float, z:string, t:boolean) {
            x:integer;
        }
        main: function void () {}
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_var_decl_11(self):  # Param auto not init -> Invalid(Variable(), varName)
        input = """
        main: function void () {
            a : auto;
        }
        """
        expect = """Invalid Variable: a"""
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_var_decl_12(self): #Success
        input = """
        main: function void () {
            a : auto = 1;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_var_decl_13(self): # Check type float and int #Check
        input = """
        main: function void () {
            a:integer = 5.0;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(5.0))"""
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_var_decl_14(self): # Succesful
        input = """
        main: function void () {
            a :integer = 5;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_var_decl_15(self): # Check
        input = """
        main: function void () {
            a : float = 5;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_var_decl_16(self):  
        input = """
            a : integer ;
            a: function integer() {}
            main: function void () {}
        """
        expect = """Redeclared Function: a"""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_var_decl_17(self): #Type mismatch 
        input = """
        main: function void () {}
        foo: function void (x:integer, y: float, z:string) {
            a : float =  true;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, FloatType, BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_var_decl_18(self): # success
        input = """
        main: function void () {}
        foo: function void (x:integer, y: float, z:string) {
            a:float;
            {
                x:integer;
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_var_decl_19(self): # success
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
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_var_decl_20(self): # success
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
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_var_decl_21(self): # success
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
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_var_decl_22(self): # Success
        input = """
        main: function void (x:integer) {}
        main: function void (x:integer) {}
        """
        expect = """Redeclared Function: main"""
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_var_decl_23(self): # Bien trung ten ham cua no scope 1
        input = """
        main: function void () {}
        foo: function void (x:integer) {
            {
                foo: integer;
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_var_decl_24(self): # # Bien trung ten ham cua no scope 0
        input = """
        main: function void () {}
        foo: function void (x:integer) {
            foo: integer;
            {}
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_var_decl_25(self): # Tham so co ten trung voi ten ham cua no
        input = """
        main: function void () {}
        foo: function void (foo:integer) {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_var_decl_26(self): # Bien trung ten ham khac scope 0
        input = """
        main: function void () {}
        foo: function void (x:integer) {
            main: integer;
            {}
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_var_decl_27(self): 
        input = """
        foo: function void (x:integer) {
            {
                main: integer;
            }
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,427))
# # ------------------------------------- [TEST INHERIT] --------------------------------------#
    def test_ihr_28(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            x:integer;
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        """
        expect = """Invalid statement in function: fact"""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_ihr_29(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            preventDefault();
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_ihr_30(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            preventDefault();
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_ihr_31(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            fact();
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Invalid statement in function: fact"""
        self.assertTrue(TestChecker.test(input,expect,431))


    def test_ihr_32(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super();
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_ihr_33(self): #Success
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_ihr_34(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,2,3);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Type mismatch in expression: IntegerLit(3)"""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_ihr_35(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,1.0,true);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_ihr_36(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1.0,1.0,true);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Type mismatch in expression: FloatLit(1.0)"""
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_ihr_37(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,1.0,true);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_ihr_38(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,1.0,1);
        }
        foo: function integer (x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_ihr_39(self): 
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

    def test_ihr_40(self): 
        input = """
        fact: function void (m:integer, n: float) inherit foo {
            super(1,1.0,true);
            y: integer;
        }
        foo: function integer (inherit x:integer, y: float, z:boolean) {}
        main: function void(){}
        """
        expect = """"""
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
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_ihr_42(self): 
        input = """
        bar: function void (inherit a: integer){}
        foo: function void (a: integer) inherit bar {
        preventDefault();
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_ihr_43(self): 
        input = """
        foo: function void (inherit a: integer, a: float) inherit bar {}
        """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_ihr_44(self): 
        input = """
        inc : function void (out n : integer, a:float) inherit foo{
            super(1,1);
        } 
        foo : function auto (inherit n: float, n: integer){} 
        """
        expect = """Redeclared Parameter: n"""
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_ihr_45(self): 
        input = """
        x: function void() {}
        main: function void() inherit x {
        super(); 
        } 
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_ihr_46(self): 
        input = """
        x, y: integer = 1, foo(1, 2, 3); 
        x, y: string;                           
        foo: function integer (x: integer, y: integer, x:integer){}   
     
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_ihr_47(self): 
        input = """
        a: integer = 2.3; 
        b: auto; 
        foo: function void(a: integer, b: float) {} 
        bar: function void() inherit foo {} 
        a: function void() {} 
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FloatLit(2.3))"""
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_ihr_48(self): 
        input = """
        a: float = 3; 
        b: auto; 
        foo: function void(a: integer, b: float) {} 
        bar: function void() inherit foo {} 
        a: function void() {} 
        """
        expect = """Invalid Variable: b"""
        self.assertTrue(TestChecker.test(input,expect,4481))

    def test_ihr_49(self): 
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
        expect = """Type mismatch in expression: StringLit(Hi)"""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_ihr_50(self): 
        input = """
        foo: function integer(inherit x: integer) inherit bar
        {
            super(2);
            {
                {
                    x:integer;
                    foo(1);
                }
            }
        }

        bar: function integer(inherit y: integer) inherit foo2 
        {
            super(1.0);
        }
        foo2: function integer(inherit z: float){}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,4502))

  # ------------------------------------- [TEST EXPRESSION] --------------------------------------#   
    def test_expr_51(self): # succes
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        main: function void () {
            x: integer;
            x = 1 + 1.0;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(x), BinExpr(+, IntegerLit(1), FloatLit(1.0)))"""
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_expr_52(self): # Undeclared Function Foo
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: integer;
            x = foo();
        }
        """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_expr_53(self): # TypeMismatchInExpression(ctx) -> Void Type
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: integer;
            x = foo4();
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo4, [])"""
        self.assertTrue(TestChecker.test(input,expect,453))
    def test_expr_5422(self):  # TypeMismatchInExpression(ctx), the length of params
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: integer;
            x = foo1();
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo1, [])"""
        self.assertTrue(TestChecker.test(input,expect,4542))

    def test_expr_55(self): #Successful
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void (y: auto) {
            x: integer;
            x = foo1(123,5.0);
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,4550))

    def test_expr_56(self): #Successful
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void (y: auto) {
            x: integer;
            y = x;
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_expr_57(self): #Successful
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void (y: auto) {
            x: integer;
            x = y;
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_expr_58(self): #  TMM Expr --> params 5 for y:float
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: integer;
            x = foo1(5,5);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_expr_59(self):#  TMM Expr 
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: integer;
            x = foo1(5.0,5.0);
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo1, [FloatLit(5.0), FloatLit(5.0)])"""
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_expr_60(self): #success
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            a: integer;
            x: integer = 1;
            y: float = 1.0 ;
            a = foo1(x,y);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,4602))

    def test_expr_61(self):  #Khai báo decl nhưng ko init, nhưng truyền vào function
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            a: integer;
            x: integer = 1;
            y: boolean;
            a = foo1(x,y);
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo1, [Id(x), Id(y)])"""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_expr_62(self): # type mm expr 
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            a: integer;
            x: integer = 1;
            y: float = 1.0 ;
            a = foo1(x,y);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_expr_163(self):  # type mm expr 
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            a: integer;
            x: integer = 1;
            y: float = 1.0 ;
            a = foo1(x,"ABCD");
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo1, [Id(x), StringLit(ABCD)])"""
        self.assertTrue(TestChecker.test(input,expect,4633))

    def test_expr_64(self):  # type mm expr 
        input = """
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            a: integer;
            x: integer = 1;
            y: float = 1.0 ;
            a = foo1(y,y);
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo1, [Id(y), Id(y)])"""
        self.assertTrue(TestChecker.test(input,expect,464))

    # def test_expr_65(self): # 2 auto function expr --> success
    #     input = """
    #     foo1: function auto(x:integer, y:float){}
    #     foo2: function auto(x:integer, y:boolean){}
    #     foo3: function integer(x:integer, y: float, z:boolean, t:string){}
    #     foo4: function void(){}
    #     main: function void () {
    #         x: integer;
    #         x = foo1(1,1.0) + foo2(1,true);
    #         x = foo1(1,1.0);
    #         x = foo2(1,true);
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input,expect,465))

    def test_expr_66(self): # TMM Stmt x
        input = """
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        main: function void () {
            x : integer;
            x = 1.0;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(x), FloatLit(1.0))"""
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_expr_67(self): # TMM Stmt x
        input = """
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        main: function void () {
            x : integer;
            x =  1.0 + foo3(1,1.0,true,"Kien");
            x = foo3(1,1.0,true,"Kien");
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(x), BinExpr(+, FloatLit(1.0), FuncCall(foo3, [IntegerLit(1), FloatLit(1.0), BooleanLit(True), StringLit(Kien)])))"""
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_expr_68(self): # success
        input = """
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        main: function void () {
            x : integer;
            y : float;
            z: integer;
            x =  1 + foo3(1,1.0,true,"Kien");
            x = foo3(1,1.0,true,"Kien");
            y = x;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_expr_69(self): #successs
        input = """
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        main: function void () {
            x : integer;
            y : float;
            z: integer;
            y =  1.0 + foo3(1,1.0,true,"Kien");
            y = foo3(1,1.0,true,"Kien");
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_expr_70(self): #success
        input = """
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: integer;
            y: float;
            x = 1 + foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_expr_71(self): #success
        input = """
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: integer;
            y: float;
            y = 1 + foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_expr_172(self): # type mm STMT
        input = """
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function auto(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: integer;
            y: float;
            z: boolean;
            y = 1.0 + foo();
            z = foo();
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(z), FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 4631))

    def test_expr_73(self): # sucesss
        input = """
        temp: function boolean(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        
        main: function void () {
            x:integer;
            x = foo2(foo(),temp());
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_expr_74(self): # Undeclared ID
        input = """
        temp: function boolean(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        
        main: function void () {
            x:integer;
            x = foo2(foo(),z);
        }
        """
        expect = """Undeclared Identifier: z"""
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_expr_75(self): # Undeclared Function
        input = """ 
        temp: function boolean(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        
        main: function void () {
            x:integer;
            x = foo2(foo(),z());
        }
        """
        expect = """Undeclared Function: z"""
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_expr_76(self): # success
        input = """
        temp: function boolean(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        
        main: function void () {
            x: integer;
            x = foo() % foo2(foo(),temp()); 
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_expr_77(self): 
        input = """
        temp: function boolean(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        
        main: function void () {
            x: integer;
            x = 5 % 2 ;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_expr_78(self): # TMM expr
        input = """
        temp: function boolean(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        
        main: function void () {
            x: integer;
            x = 5 % 2.0 ;
        }
        """
        expect = """Type mismatch in expression: BinExpr(%, IntegerLit(5), FloatLit(2.0))"""
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_expr_79(self): # TMM expr
        input = """
        temp: function boolean(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        
        main: function void () {
            x: integer;
            x = 5 % temp() ;
        }
        """
        expect = """Type mismatch in expression: BinExpr(%, IntegerLit(5), FuncCall(temp, []))"""
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_expr_80(self): # TMM expr
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            x = (temp() == temp1());
        }
        """
        expect = """Type mismatch in expression: BinExpr(==, FuncCall(temp, []), FuncCall(temp1, []))"""
        self.assertTrue(TestChecker.test(input,expect,4800))

    def test_expr_81(self): # success
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            y: integer;
            x = (temp() == foo());
            x = foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_expr_82(self): # TMM STMT
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            y: integer;
            x = (temp() == foo());
            y = foo();
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_expr_83(self): # TMM expr
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            x = (false == 1);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_expr_84(self): # type MM expr
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            x = ("kien" != 1);
        }
        """
        expect = """Type mismatch in expression: BinExpr(!=, StringLit(kien), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_expr_85(self): #Type MM expr
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            x = (temp() > foo());
        }
        """
        expect = """Type mismatch in expression: BinExpr(>, FuncCall(temp, []), FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_expr_86(self):
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function integer(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            x = ( "ABCD" > 1.0);
        }
        """
        expect = """Type mismatch in expression: BinExpr(>, StringLit(ABCD), FloatLit(1.0))"""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_expr_87(self): # Sucesss
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            y: integer;
            x = (1 > foo());
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_expr_88(self): # Type mm STMT
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            y: integer;
            x = (1.0 > foo());
            y = foo();
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_expr_89(self): # success
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            x = (true || true);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 489))


    def test_expr_90(self): # type mm expr
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            x = (true || 1 );
        }
        """
        expect = """Type mismatch in expression: BinExpr(||, BooleanLit(True), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_expr_91(self): # success
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            x = (temp()|| foo());
            x = foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_expr_92(self): # type mm stmt
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            y: integer;
            x = (temp()|| foo());
            x = foo();
            y = foo();
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_expr_93(self): #type mm expr
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            y: integer;
            x = (temp1()|| foo());
        }
        """
        expect = """Type mismatch in expression: BinExpr(||, FuncCall(temp1, []), FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_expr_94(self): 
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: boolean;
            y: integer;
            x = (x || x);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_expr_95(self): # success
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: string;
            x = temp1()::temp1();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_expr_96(self): # sucess
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: string;
            x = foo()::temp1();
            x = foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_expr_special(self): # sucess
        input = """
        temp1: function string(){}
        foo: function auto(){}
        main: function void () {
            x: string;
            x = foo()::temp1;
            x = foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input,expect,999))

    def test_expr_97(self): # type mm stmt
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: string;
            y: integer;
            x = foo()::temp1();
            y = foo();
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_expr_98(self): # Type mm stmt
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x: string;
            y: integer;
            x = foo()::temp1();
            y = foo();
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_expr_99(self): # type mm stmt
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x : integer;
            x = - temp();
        }
        """
        expect = """Type mismatch in expression: UnExpr(-, FuncCall(temp, []))"""
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_expr_100(self): # Type mm expr
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x : integer;
            x = - true;
        }
        """
        expect = """Type mismatch in expression: UnExpr(-, BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input,expect,1100))

    def test_expr_101(self): # Type mm expr
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x : integer;
            x = !1;
        }
        """
        expect = """Type mismatch in expression: UnExpr(!, IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 1101))

    def test_expr_102(self): # tmm stmt
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x : integer;
            x = -foo();
            x = foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1102))

    def test_expr_103(self): # success
        input = """
        x: float = 5;
        main: function void () {
            x = 5.5;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1103))

    def test_expr_1014(self): # success
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x : auto = 1.0;
            x =  -1.0;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 4632))

    def test_expr_105(self): #Type mm expr
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x : integer;
            x = !5.0;
        }
        """
        expect = """Type mismatch in expression: UnExpr(!, FloatLit(5.0))"""
        self.assertTrue(TestChecker.test(input, expect, 1105))

    def test_expr_106(self): # sucesss
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x : boolean;
            x = !foo();
            x = foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1106))

    def test_expr_107(self): #success
        input = """
        temp: function boolean(){}
        temp1: function string(){}
        foo: function auto(){}
        foo1: function auto(x:integer, y:float){}
        foo2: function integer(x:integer, y:boolean){}
        foo3: function integer(x:integer, y: float, z:boolean, t:string){}
        foo4: function void(){}
        main: function void () {
            x : boolean;
            x = !temp();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1107))

    def test_expr_10811(self): #success
        input = """
        foo: function auto(x: float, y:auto){
            y = x;
            y = 5;
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect,110811))

    def test_expr_109(self): #success
        input = """
        foo: function auto(x: float, y:auto){
            y = x;
            y = "Kien";
        }
        main: function void () {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), StringLit(Kien))"""
        self.assertTrue(TestChecker.test(input, expect, 1109))


    def test_expr_110(self): # TMM stmt
        input = """
        foo: function auto(x: integer, y:auto){
            y = 5.0;
            x = y;
        }
        main: function void () {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(x), Id(y))"""
        self.assertTrue(TestChecker.test(input, expect, 1100))

    def test_expr_111(self): # TMM stmt
        input = """
        foo: function auto(x: integer, y:auto){
            {
                y = 5.0;
                {
                    y: boolean;
                    y = true;
                }
            }
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1111))

    def test_expr_112(self): # TMM stmt
        input = """
        foo: function auto(x: integer, y:auto){
            {
                y = 5.0;
                {
                    y: boolean;
                    y = 5.0;
                }
            }
        }
        main: function void () {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), FloatLit(5.0))"""
        self.assertTrue(TestChecker.test(input, expect, 1112))

    def test_expr_113(self): # TMM stmt
        input = """
        foo: function auto(x: integer, y:auto){
            {
                y = 5.0;
                {
                    {
                        {
                            y = true;
                        }
                    }
                }
            }
        }
        main: function void () {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 1113))


    def test_expr_114(self): # TMM stmt
        input = """
        foo: function auto(x: integer, y:auto){
            foo(1,1.0);
            y = 1;
        }
        main: function void () {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1114))

    def test_expr_115(self): # TMM stmt
        input = """
        foo: function auto(x: integer, y:auto){
            foo(1,1.0);
            y = true;
        }
        main: function void () {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 4801))

    def test_expr_116(self): # TMM stmt
        input = """
        foo: function auto(x: integer, y:auto){
            a: integer = foo(1,1.0);
            y = true;
        }
        main: function void () {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 1116))

    def test_expr_117(self): # TMM stmt
        input = """
        foo: function auto(x: integer, y:auto){
        }
        a: integer = foo(1,1);
        main: function void () {
            a: boolean = foo(1,true);
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [IntegerLit(1), BooleanLit(True)])"""
        self.assertTrue(TestChecker.test(input, expect, 1117))

    def test_expr_118(self): # TMM stmt
        input = """
        foo: function auto(x: integer, y:auto){
        }
        a: integer = foo(1,1);
        main: function void () {
            a: boolean = foo(1,1);
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(a, BooleanType, FuncCall(foo, [IntegerLit(1), IntegerLit(1)]))"""
        self.assertTrue(TestChecker.test(input, expect, 1118))

    def test_expr_119(self): # TMM stmt
        input = """
        foo: function auto(x: integer, inherit y:auto){
        }
        bar: function integer () inherit foo {
            super(1,1);
            y = true;
        }
        main: function void () {
            a: boolean = foo(1,1);
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(y), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 1119))
    def test_expr_120(self):
        input = """
        main: function void(){
            x : integer = 5;
            while(x){
                if(x%2 == 0) {y:integer = 3;}
                x = x - 1;      
            }
        }
        """
        expect = """Type mismatch in statement: WhileStmt(Id(x), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(x), IntegerLit(2)), IntegerLit(0)), BlockStmt([VarDecl(y, IntegerType, IntegerLit(3))])), AssignStmt(Id(x), BinExpr(-, Id(x), IntegerLit(1)))]))"""
        self.assertTrue(TestChecker.test(input, expect, 1120))

    def test_expr_121(self):
        input = """
        main: function void(){
            x : integer = 5;
            while(x > 0){
                if(x) {y:integer = 3;}
                x = x - 1;      
            }
        }
        """
        expect = """Type mismatch in statement: IfStmt(Id(x), BlockStmt([VarDecl(y, IntegerType, IntegerLit(3))]))"""
        self.assertTrue(TestChecker.test(input, expect, 1121))
    
    def test_expr_122(self):
        input = """
        main: function void(){
            x : integer = 5;
            while(x > 0){
                if(x>0) {y:integer = 3;}
                else
                {y = x - 1;}      
            }
        }
        """
        expect = """Undeclared Identifier: y"""
        self.assertTrue(TestChecker.test(input, expect, 1122))

    def test_expr_123(self):
        input = """
        main: function void(){
            x : integer = 5;
            while(x > 0) x = y + 1;
        }
        """
        expect = """Undeclared Identifier: y"""
        self.assertTrue(TestChecker.test(input, expect, 1123))

    def test_expr_124(self):
        input = """
        main: function void(){
            x : integer = 5;
            while(0) x = y + 1;
        }
        """
        expect = """Type mismatch in statement: WhileStmt(IntegerLit(0), AssignStmt(Id(x), BinExpr(+, Id(y), IntegerLit(1))))"""
        self.assertTrue(TestChecker.test(input, expect, 1124))

    def test_expr_125(self):
        input = """
        main: function void(){
            do {
                x = x + 1 ;
            }
            while(x < 5);
        }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 1125))

    def test_expr_126(self):
        input = """
        main: function void(){
            x:integer = 0;
            do {
                x = x + 1 ;
            }
            while(x < 5);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1126))

    def test_expr_127(self):
        input = """
        main: function void(){
            x:integer = 0;
            do {
                x = x + 1 ;
            }
            while(x);
        }
        """
        expect = """Type mismatch in statement: DoWhileStmt(Id(x), BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))"""
        self.assertTrue(TestChecker.test(input, expect, 1127))
    
 
    def test_expr_128(self):
        input = """
        main: function void(){
            x:integer = 0;
            do {
                x = x + 1 ;
            }
            while(x < 5);
            break;
        }
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 1128))   

    def test_expr_129(self):
        input = """
        main: function void(){
            x:integer = 0;
            do {
                x = x + 1 ;
            }
            while(x < 5);
            continue;
        }
        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 1129))   

    def test_expr_130(self):
        input = """
        main: function void(){
            x:integer = 0;
            do {
                x = x + 1 ;
                if(x>0){
                    if(x%2==0){
                        break;
                    }
                }
            }
            while(x < 5);

        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1130))   

    def test_expr_131(self):
        input = """
        main: function void(){
            x : integer = 5;
            while(x>0){
                if(x%2 == 0) {y:integer = 3;}
                x = x - 1;      
                {
                    {
                        {
                            break;
                        }
                    }
                }
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1131)) 
  
    def test_expr_132(self):
        input = """
        main: function void(){
            for ( x = 1 , x < 0, x + 1 ){
                y: integer;
            }
        }
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 1132))


    def test_expr_133(self):
        input = """
        x: float;
        main: function void(){
            for ( x = 1 , x < 0, x + 1 ){
                y: integer;
            }
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(<, Id(x), IntegerLit(0)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([VarDecl(y, IntegerType)]))"""
        self.assertTrue(TestChecker.test(input, expect, 1133))
  
    def test_expr_134(self):
        input = """
        main: function void(){
            x: auto = 1;
            for ( x = 1 , x < 5, x + 1 ){
                y : integer;
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1134))

  
    def test_expr_135(self):
        input = """
        main: function void(){
            x: auto = 1.0;
            for ( x = 1 , x < 5, x + 1 ){
                y : integer;
            }
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(<, Id(x), IntegerLit(5)), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([VarDecl(y, IntegerType)]))"""
        self.assertTrue(TestChecker.test(input, expect, 1135))

    def test_expr_136(self):
        input = """
        main: function void(){
            x: auto = 1;
            for ( x = 1 ,5, x + 1 ){
                y : integer;
            }
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(x), IntegerLit(1)), IntegerLit(5), BinExpr(+, Id(x), IntegerLit(1)), BlockStmt([VarDecl(y, IntegerType)]))"""
        self.assertTrue(TestChecker.test(input, expect, 1136))

    def test_expr_137(self):
        input = """
        main: function void(){
            x: auto = 1;
            for ( x = 1 , x > 5, x > 1 ){
                y : integer;
            }
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(x), IntegerLit(1)), BinExpr(>, Id(x), IntegerLit(5)), BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([VarDecl(y, IntegerType)]))"""
        self.assertTrue(TestChecker.test(input, expect, 1137))

    def test_expr_138(self):
        input = """
        main: function void(){
            x: auto = 1;
            for (x = 1 , x > 5, x + 1 ){
                if(x==4){
                continue;
                }
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1138))

    def test_expr_139(self):
        input = """
        main: function void(){
            x: auto = 1;
            while (x < 5){
                if(x==4){
                break;
                }
                x = x + 1;
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1139))

    def test_expr_140(self):
        input = """
        main: function void(){
            x: auto = 1;
            while (x < 5){
                if(x==4){
                    {
                        break;
                    }
                }
                x = x + 1;
            }
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1140))

    def test_expr_141(self):
        input = """
        main: function void(){
            x: auto = 1;
            while (x < 5){
                if(x==4){
                    {
                    }
                }
                x = x + 1;
            }
            break;
        }
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 1141))


    def test_expr_142(self):
        input = """
        foo: function auto(){}
        bar: function integer(x:integer, y:float){}
        main: function void(a:auto){
            x: boolean;
            bar(a,1.0);
            a = true;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 1142))

    def test_expr_143(self):
        input = """
        foo: function auto(){}
        bar: function integer(x:auto, y:float){}
        main: function void(a:integer){
            bar(a,1.0);
            bar(true,1.0);
        }
        """
        expect = """Type mismatch in statement: CallStmt(bar, BooleanLit(True), FloatLit(1.0))"""
        self.assertTrue(TestChecker.test(input, expect, 1143))

    def test_expr_144(self):
        input = """
        foo: function auto(){}
        bar: function integer(x:integer, y:float){}
        main: function void(){
            bar(foo(),1.0);
            z : boolean = foo();
            x : float = foo();
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(z, BooleanType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 1144))

    def test_expr_145(self):
        input = """
        foo: function integer(){}
        bar: function integer(x: auto, y:float){
            bar(foo(),1.0);
            x = 1;
            x = true;
        }
        main: function void(){

        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(x), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 1145))

    def test_expr_146(self):
        input = """
        foo: function auto(){}
        bar: function integer(x:integer, y:float){}
        main: function void(){
            bar(foo(),1.0);
            a : float = foo();
            x : integer = foo();
            z : boolean = foo();
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(z, BooleanType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 1146))

    def test_fl_147(self):
        input = """
        main: function float(){}
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 1147))

    def test_fl_148(self):
        input = """
        main: function float(){}
        main: function void(){}
        """
        expect = """Redeclared Function: main"""
        self.assertTrue(TestChecker.test(input, expect, 1148))

    # def test_fl_149(self):
    #     input = """
    #     main: function void(){
    #         super();
    #     }
    #     """
    #     expect = """Invalid statement in function: main"""
    #     self.assertTrue(TestChecker.test(input, expect, 1149))

# ------------------------------------- [TEST RETURN] --------------------------------------#   
    def test_re_150(self): #tmm stmt
        input = """
        foo: function auto(){
            return true;
        }
        main: function void(){
            x:integer = foo();
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 1150))

    def test_re_151(self): #tmm stmt
        input = """
        foo: function auto(){
            return 1;
        }
        main: function void(){
            x:float = foo();
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1151))

    def test_re_152(self): #
        input = """
        main: function void(){
            x:float = foo();
        }
        foo: function auto(){
            return 1;
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1152))

    def test_re_153(self): #tmm stmt
        input = """
        main: function void(){
            x: integer = foo();
        }
        foo: function auto(){
            return 1.0;
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(1.0))"""
        self.assertTrue(TestChecker.test(input, expect, 1153))

    def test_re_154(self): #tmm stmt
        input = """
        main: function void(){
            x: integer = foo();
        }
        foo: function auto(){
            return 1;
            return true;
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 1154))

    def test_re_155(self): #tmm stmt
        input = """
        foo: function auto(){
            return 1.0;
            return 5;
        }
        main: function void(){
            x: integer = foo();
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FuncCall(foo, ))"""
        self.assertTrue(TestChecker.test(input, expect, 1155))

    def test_re_155(self): #tmm stmt
        input = """
        foo: function auto(){
            x: integer = 10;
            if (x>5){
                return 1.0;
            }
            else {
                return 5;
            }
        }
        main: function void(){
            x: integer = foo();
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 4802))

    def test_re_156(self): #tmm stmt
        input = """
        foo: function auto(){
            x: integer = 10;
            if (x>5){
                return 1;
            }
            else {
                return 5.0;
            }
        }
        main: function void(){
            x: integer = foo();
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(5.0))"""
        self.assertTrue(TestChecker.test(input, expect, 1156))


    def test_re_157(self): #tmm stmt
        input = """
        main: function void(){
            x: integer = foo();
        }
        foo: function auto(){
            x: integer = 10;
            if (x>5){
                return 1;
            }
            else {
                return 5.0;
            }
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(5.0))"""
        self.assertTrue(TestChecker.test(input, expect, 1157))

    def test_re_158(self): #tmm stmt
        input = """
        main: function void(){
            x: float = foo();
        }
        foo: function auto(){
            x: integer = 10;
            if (x>5){
                return 1;
            }
            else {
                return true;
            }
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 1158))

    def test_re_159(self): 
        input = """
        x: function integer() {} 
        foo: function void() { 
            x: integer = x();
        } 
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 1159))

    def test_re_160(self): 
        input = """
        x : string = foo();
        foo: function auto () {return 1;} 
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 4803))

# ------------------------------------- [TEST UPDATE CODE] --------------------------------------# 
    def test_up_161(self): 
        input = """
        main: function void(){
            foo();
            x: integer = foo();
            x:integer = 1 + 2 + 3 + foo();
        }
        foo: function auto () {return true;} 
        """
        expect = """Redeclared Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 1161))

    def test_up_162(self): 
        input = """
        main: function void(){
            foo();
            //x: integer = foo();
        }
        foo: function auto () {return true;} 
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1162))

    # def test_up_163(self): 
    #     input = """
    #     main: function void(){
    #         foo();
    #         x: auto = foo();
    #         x: integer = foo();
    #     }
    #     foo: function auto () {} 
    #     """
    #     expect = """Type mismatch in expression: FuncCall(foo, [])"""
    #     self.assertTrue(TestChecker.test(input, expect, 1163))

    def test_up_164(self): 
        input = """
        foo: function auto(a:integer){}
        main: function void(){
        x: float = foo(1);
        foo(1);
        }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1164))

    def test_up_165(self): 
        input = """
        foo: function void(a:auto){
        a = foo();
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 4805))

    def test_up_166(self): 
        input = """
        foo: function void(a:auto){
            a = foo(1);
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [IntegerLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect, 1166))

    def test_up_167(self): 
        input = """
        bar: function void(inherit a:integer){}
        foo: function void(a:integer) inherit bar{
            preventDefault();
        }
        main: function void(){}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 1167))

    def test_up_168(self): 
        input = """
        bar: function void(inherit x:integer){}
        foo: function void(a:integer) inherit bar{
            preventDefault();
            x = 5;
        }
        main: function void(){}
        """
        expect = """Undeclared Identifier: x"""
        self.assertTrue(TestChecker.test(input, expect, 1168))

    # def test_up_169(self): 
    #     input = '''
    #         foo1: function void() inherit foo{
    #             z = 4;
    #         }
    #         foo: function void(inherit x:integer, inherit y: float, inherit x: string){}
    #         main : function void() {
 
    #         }
    #     '''
    #     expect = """Invalid statement in function: foo1"""
    #     self.assertTrue(TestChecker.test(input, expect, 1169))

    def test_up_170(self): 
        input = '''
            foo: function void() inherit foo1{
                super(1);
            }
            foo1: function integer (inherit a:integer, inherit b:integer){}
        '''
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input, expect, 1170))
    
    def test_up_171(self): 
        input = '''
        a: float = foo(1,2);
        foo: function float (a:auto,b:auto){
            a = "abc";
            b = "bcd";
            return a + b;
        }
        '''
        expect = """Type mismatch in statement: AssignStmt(Id(a), StringLit(abc))"""
        self.assertTrue(TestChecker.test(input, expect, 1171))

    def test_up_172(self): 
        input = '''
        foo: function integer(){}
        main: function void(){
            foo: integer = 3;
            a : integer;
            a = foo();
        }
        '''
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 1172))

# ------------------------------------- [RAISE IN CALLSTMT, FUNCALL AND SUPER] --------------------------------------# 
    def test_up_173(self): # Funcall with != len
        input = '''
        foo: function integer(x:integer, y:float){}
        main: function void(){
            x: integer = foo(t);
        }
        '''
        expect = """Type mismatch in expression: FuncCall(foo, [Id(t)])"""
        self.assertTrue(TestChecker.test(input, expect, 1173))

    def test_up_174(self): # Funcall with != type
        input = '''
        foo: function integer(x:integer, y:float){}
        main: function void(){
            x: integer = foo(1,true);
        }
        '''
        expect = """Type mismatch in expression: FuncCall(foo, [IntegerLit(1), BooleanLit(True)])"""
        self.assertTrue(TestChecker.test(input, expect, 1174))

    def test_up_175(self): # Funcall with undecl
        input = '''
        foo: function integer(x:integer, y:float){}
        main: function void(){
            x: integer = foo(1,t);
        }
        '''
        expect = """Undeclared Identifier: t"""
        self.assertTrue(TestChecker.test(input, expect, 1175))

    def test_up_176(self): # CallStmt with undecl
        input = '''
        foo: function integer(x:integer, y:float){}
        main: function void(){
            foo(1,t);
        }
        '''
        expect = """Undeclared Identifier: t"""
        self.assertTrue(TestChecker.test(input, expect, 1176))

    def test_up_177(self): # CallStmt with != len
        input = '''
        foo: function integer(x:integer, y:float){}
        main: function void(){
            foo(t);
        }
        '''
        expect = """Type mismatch in statement: CallStmt(foo, Id(t))"""
        self.assertTrue(TestChecker.test(input, expect, 1177))

    def test_up_178(self): # Callstmt with != type
        input = '''
        foo: function integer(x:integer, y:float){}
        main: function void(){
            foo(1,true);
        }
        '''
        expect = """Type mismatch in statement: CallStmt(foo, IntegerLit(1), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 1178))

    def test_up_179(self): # For super, len(arg) > len(param) -> TMM expr arg du dau tien
        input = '''
        foo: function integer(x:integer, y:float){}
        bar: function integer () inherit foo{
            super(1,2,3,5,6);
        }
        main: function void(){}
        '''
        expect = """Type mismatch in expression: IntegerLit(3)"""
        self.assertTrue(TestChecker.test(input, expect, 1179))

    def test_up_180(self): # For super, len(arg) < len(param) -> TMM ctx rong
        input = '''
        foo: function integer(x:integer, y:float){}
        bar: function integer () inherit foo{
            super(1);
        }
        main: function void(){}
        '''
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input, expect, 1180))

    def test_up_181(self): # For super, != type -> tra ve element tai do
        input = '''
        foo: function integer(x:integer, y:float){}
        bar: function integer () inherit foo{
            super(1,true);
        }
        main: function void(){}
        '''
        expect = """Type mismatch in expression: BooleanLit(True)"""
        self.assertTrue(TestChecker.test(input, expect, 1181))

    def test_up_182(self): 
        input = '''
        a : integer = b;
        b : function void() {}
        main: function void(){}
        '''
        expect = """Undeclared Identifier: b"""
        self.assertTrue(TestChecker.test(input, expect, 1182))

    def test_up_183(self): 
        input = '''
        foo: integer = 1;
        foo1: function auto () inherit foo {}
        '''
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 1183))


    def test_up_1184(self): 
        input = '''
        foo: integer = 1;
        foo1: function auto () 
        {foo();}
        '''
        expect = """Type mismatch in statement: CallStmt(foo, )"""
        self.assertTrue(TestChecker.test(input, expect, 1184))


    def test_up_1184(self): 
        input = '''
        foo: integer = 1;
        foo1: function auto () 
        {foo();}
        '''
        expect = """Type mismatch in statement: CallStmt(foo, )"""
        self.assertTrue(TestChecker.test(input, expect, 1184))
