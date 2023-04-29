import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    def test300(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test301(self):
        input = """x, y, z: integer;"""
        expect = str(Program([VarDecl("x", IntegerType()), VarDecl(
            "y", IntegerType()), VarDecl("z", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test302(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = str(Program([VarDecl("x", IntegerType(), IntegerLit(1)), VarDecl(
            "y", "IntegerType", IntegerLit(2)), VarDecl("z", IntegerType(), IntegerLit(3))
        ]))
        self.assertTrue(TestAST.test(input, expect, 302))

    def test303(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = str(Program([
            VarDecl('x', IntegerType(), IntegerLit(1)),
            VarDecl('y', IntegerType(), IntegerLit(2)),
            VarDecl('z', IntegerType(), IntegerLit(3)),
            VarDecl('a', FloatType()),
            VarDecl('b', FloatType())]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test304(self):
        input = """main: function void () {
        }"""
        expect = str(Program([
            FuncDecl('main', VoidType(), [], None, BlockStmt([]))]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test305(self):
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = str(Program([
            FuncDecl('main', VoidType(), [], None, BlockStmt(['CallStmt(printInteger, IntegerLit(4))']))]))
        self.assertTrue(TestAST.test(input, expect, 305))

    def test306(self):
        input = """
            main: function void () {
                n = 3;
                k = 4;
                readInteger();
                printInteger(n);
                readFloat();
                writeFloat(3.14);
                readString();
                printString("Hello World");
                readBoolean();
                printBoolean(true);
                super(1,2);
                super();
            }
        """
        expect = str(Program([FuncDecl('main', VoidType(), [], None, BlockStmt([
            AssignStmt(Id('n'), IntegerLit(3)), AssignStmt(
                Id('k'), IntegerLit(4)),
            CallStmt('readInteger', []),
            CallStmt('printInteger', [Id('n')]),
            CallStmt('readFloat', []),
            CallStmt('writeFloat', [FloatLit(3.14)]),
            CallStmt('readString', []),
            CallStmt('printString', [StringLit('Hello World')]),
            CallStmt('readBoolean', []),
            CallStmt('printBoolean', [BooleanLit(True)]),
            CallStmt('super', [IntegerLit(1), IntegerLit(2)]),
            CallStmt('super', [])
        ]))]))
        self.assertTrue(TestAST.test(input, expect, 306))

    def test307(self):
        input = """ do_something(3.14); 
                    did_something(3.14);
                    super(); """
        expect = str(Program([CallStmt('do_something', [FloatLit(3.14)]),
                              CallStmt('did_something', [FloatLit(3.14)]),
                              CallStmt('super', [])]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test308(self):
        input = """continue; return; break;"""
        expect = str(Program([ContinueStmt(), ReturnStmt(), BreakStmt()]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test309(self):
        input = """foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
                main: function void () {
                printInteger(4);
                }"""
        expect = str(Program([
            FuncDecl('foo', VoidType(),
                     [ParamDecl('a', IntegerType(), False, True), ParamDecl('b', FloatType(), True, True)], 'bar', BlockStmt([])),
            FuncDecl('main', VoidType(), [], None, BlockStmt(
                [CallStmt('printInteger', [IntegerLit(4)])]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test310(self):
        input = """
        for (i = 0, i < 10,  i + 1) {
            printInteger(i);
        }
        for(j = 10, j > 0, j - 1) {
            printInteger(j);
        }
        """
        expect = str(Program([
            ForStmt(AssignStmt(Id('i'), IntegerLit(0)), BinExpr('<', Id('i'), IntegerLit(10)), BinExpr(
                '+', Id('i'), IntegerLit(1)), BlockStmt([CallStmt('printInteger', [Id('i')])])),
            ForStmt(AssignStmt(Id('j'), IntegerLit(10)), BinExpr('>', Id('j'), IntegerLit(0)), BinExpr(
                '-', Id('j'), IntegerLit(1)), BlockStmt([CallStmt('printInteger', [Id('j')])]))

        ]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test311(self):
        input = """
        while (i < 10) {
            printInteger(i);
            i = i + 1;
            }    
        while(true)
            get_API();
        for (i = 0, i < 10,  i + 1) {
            printInteger(i);
        }
        """
        expect = str(Program([
            WhileStmt(BinExpr('<', Id('i'), IntegerLit(10)), BlockStmt([CallStmt(
                'printInteger', [Id('i')]), AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1)))])),
            WhileStmt(BooleanLit(True), CallStmt('get_API', [])),
            ForStmt(AssignStmt(Id('i'), IntegerLit(0)), BinExpr('<', Id('i'), IntegerLit(10)), BinExpr(
                '+', Id('i'), IntegerLit(1)), BlockStmt([CallStmt('printInteger', [Id('i')])]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 311))

    def test312(self):
        input = """
            do {get_API();} while (true);
            do get_API(); while (true);
            if (n==0){
                return 1;
            }
        """
        expect = str(Program([
            DoWhileStmt(BooleanLit(True), BlockStmt(
                [CallStmt('get_API', [])])),
            DoWhileStmt(BooleanLit(True), CallStmt('get_API', [])),
            IfStmt(BinExpr('==', Id('n'), IntegerLit(0)),
                   BlockStmt([ReturnStmt(IntegerLit(1))]), None)
        ]))
        self.assertTrue(TestAST.test(input, expect, 312))

    def test313(self):
        input = """
            if (n==0)
                return 1;
            else 
                return n * factorial(n-1);
            
        """
        expect = str(Program([
            IfStmt(BinExpr('==', Id('n'), IntegerLit(0)),
                   ReturnStmt(IntegerLit(1)),
                   ReturnStmt(BinExpr('*', Id('n'), FuncCall('factorial', [BinExpr('-', Id('n'), IntegerLit(1))]))))
        ]))
        self.assertTrue(TestAST.test(input, expect, 313))

    def test314(self):
        input = """
            if (n==0)
            {
                return 1;
                if (n==1)
                    return 2;
            }
            else
                return n * factorial(n-1);
            
        """
        expect = str(Program([
            IfStmt(BinExpr('==', Id('n'), IntegerLit(0)),
                     BlockStmt([ReturnStmt(IntegerLit(1)),
                                IfStmt(BinExpr('==', Id('n'), IntegerLit(1)),
                                       ReturnStmt(IntegerLit(2)), None)]),
                     ReturnStmt(
                         BinExpr('*', Id('n'), FuncCall('factorial', [BinExpr('-', Id('n'), IntegerLit(1))])))
                     )
        ]))
        self.assertTrue(TestAST.test(input, expect, 314))

    def test315(self):
        input = """
            a,b,c : array [1, 2] of integer;
        """
        expect = str(
            Program([
                VarDecl('a', ArrayType([1, 2], IntegerType())),
                VarDecl('b', ArrayType([1, 2], IntegerType())),
                VarDecl('c', ArrayType([1, 2], IntegerType()))
            ])
        )

        self.assertTrue(TestAST.test(input, expect, 315))

    def test316(self):
        input = """
        a[0,1]=0;
        a[1]=1.5;
        """
        expect = str(Program([
            AssignStmt(
                ArrayCell('a', [IntegerLit(0), IntegerLit(1)]), IntegerLit(0)),
            AssignStmt(ArrayCell('a', [IntegerLit(1)]), FloatLit(1.5))
        ]))
        self.assertTrue(TestAST.test(input, expect, 316))

    def test317(self):
        input = """
        a:array[1] of integer = {1,2,3};
        """
        expect = str(Program([
            VarDecl('a', ArrayType([1], IntegerType()), ArrayLit(
                [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 317))

    def test318(self):
        input = """
        a,b,c:array[3] of integer = {1,2,3},{4,5,6},{7,8,9};
        """
        expect = str(Program([
            VarDecl('a', ArrayType([3], IntegerType()), ArrayLit(
                [IntegerLit(1), IntegerLit(2), IntegerLit(3)])),
            VarDecl('b', ArrayType([3], IntegerType()), ArrayLit(
                [IntegerLit(4), IntegerLit(5), IntegerLit(6)])),
            VarDecl('c', ArrayType([3], IntegerType()), ArrayLit(
                [IntegerLit(7), IntegerLit(8), IntegerLit(9)]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 318))

    def test319(self):
        input = """
        a: integer = 5+7;
        b: float = 5.5 + 7.7;
        c:string= "Hello" :: "World";
        """
        expect = str(Program([
            VarDecl('a', IntegerType(), BinExpr(
                '+', IntegerLit(5), IntegerLit(7))),
            VarDecl('b', FloatType(), BinExpr(
                '+', FloatLit(5.5), FloatLit(7.7))),
            VarDecl('c', StringType(), BinExpr(
                '::', StringLit('Hello'), StringLit('World')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 319))

    def test320(self):
        input = """
        n = 5;
        a: array [1] of integer;
        b: array [2] of float = {1.3,3.14};
        c: array [3] of string = {"Hello", "World", "!"};
        d: array [4] of boolean = {true, false, true, false};
        """
        expect = str(Program([
            AssignStmt(Id('n'), IntegerLit(5)),
            VarDecl('a', ArrayType([1], IntegerType())),
            VarDecl('b', ArrayType([2], FloatType()),
                    ArrayLit([FloatLit(1.3), FloatLit(3.14)])),
            VarDecl('c', ArrayType([3], StringType()), ArrayLit(
                [StringLit('Hello'), StringLit('World'), StringLit('!')])),
            VarDecl('d', ArrayType([4], BooleanType()), ArrayLit(
                [BooleanLit(True), BooleanLit(False), BooleanLit(True), BooleanLit(False)]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 320))

    def test321(self):
        input = """
        a,b: array[2] of integer={1+5,2-3},{1,3};
        c=(1+2)*(4-5)/6;
        """
        expect = str(Program([
            VarDecl('a', ArrayType([2], IntegerType()), ArrayLit([BinExpr(
                '+', IntegerLit(1), IntegerLit(5)), BinExpr('-', IntegerLit(2), IntegerLit(3))])),
            VarDecl('b', ArrayType([2], IntegerType()),
                    ArrayLit([IntegerLit(1), IntegerLit(3)])),
            AssignStmt(Id('c'), BinExpr('/', BinExpr('*', BinExpr('+', IntegerLit(1),
                       IntegerLit(2)), BinExpr('-', IntegerLit(4), IntegerLit(5))), IntegerLit(6)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 321))

    def test322(self):
        input = """
         {}
         {n=1;}
         {
            get_int();
            put_int(n);
         }
        """
        expect = str(Program([
            BlockStmt([]),
            BlockStmt([AssignStmt(Id('n'), IntegerLit(1))]),
            BlockStmt([CallStmt('get_int', []),
                      CallStmt('put_int', [Id('n')])])
        ]))
        self.assertTrue(TestAST.test(input, expect, 322))

    def test323(self):
        input = """
        fact: function integer (n:integer){
                    if(n==0) return 1;    
                    return n*fact(n-1);         
                    } 
        """
        expect = str(Program([
            FuncDecl('fact',
                     IntegerType(),
                     [ParamDecl('n', IntegerType())],
                     "",
                     BlockStmt([
                         IfStmt(BinExpr('==', Id('n'), IntegerLit(0)),
                                ReturnStmt(IntegerLit(1)), None),
                         ReturnStmt(
                             BinExpr('*', Id('n'), FuncCall('fact', [BinExpr('-', Id('n'), IntegerLit(1))])))
                     ]))
        ]))

        self.assertTrue(TestAST.test(input, expect, 323))

    def test324(self):
        input = """
        {r, s: integer;
                  r = 2.0;
                  a, b: array [5] of integer;
                  s = r * r * myPI; 
                 a[0] = s; }
        """
        expect = str(Program([
            BlockStmt([
                VarDecl('r', IntegerType()),
                VarDecl('s', IntegerType()),
                AssignStmt(Id('r'), FloatLit(2.0)),
                VarDecl('a', ArrayType([5], IntegerType())),
                VarDecl('b', ArrayType([5], IntegerType())),
                AssignStmt(Id('s'), BinExpr(
                    '*', BinExpr('*', Id('r'), Id('r')), Id('myPI'))),
                AssignStmt(ArrayCell('a', [IntegerLit(0)]), Id('s'))
            ])
        ]))
        self.assertTrue(TestAST.test(input, expect, 324))

    def test325(self):
        input = """
        inc: function void(out n: integer, delta: integer) inherit add {
            /*do something*/
            }
        """
        expect = str(Program([
            FuncDecl('inc', VoidType(), [ParamDecl('n', IntegerType(), True, False), ParamDecl(
                'delta', IntegerType())], 'add', BlockStmt([]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 325))

    def test326(self):
        input = """
        b: function array [2] of integer (){
            if(a[0]!=0) 
                a[0]=0; 
            else a[0]=1; 
            return a;
            }
        """
        expect = str(Program([
            FuncDecl('b', ArrayType([2], IntegerType()), [], "", BlockStmt([
                IfStmt(BinExpr('!=', ArrayCell('a', [IntegerLit(0)]), IntegerLit(0)), AssignStmt(ArrayCell(
                    'a', [IntegerLit(0)]), IntegerLit(0)), AssignStmt(ArrayCell('a', [IntegerLit(0)]), IntegerLit(1))),
                ReturnStmt(Id('a'))
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 326))

    def test327(self):
        input = """
        I : boolean = true&&true&&true;
        """
        expect = str(Program([
            VarDecl('I', BooleanType(), BinExpr('&&', BinExpr(
                '&&', BooleanLit(True), BooleanLit(True)), BooleanLit(True)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 327))

    def test328(self):
        input = """
        a = a||b > 5 && c < 3;
        """
        expect = str(Program([
            AssignStmt(Id('a'), BinExpr('<', BinExpr('>', BinExpr(
                '||', Id('a'), Id('b')), BinExpr('&&', IntegerLit(5), Id('c'))), IntegerLit(3)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 328))

    def test329(self):
        input = """
        a = concur * 4 * fact(5);
        """
        expect = str(Program([
            AssignStmt(Id('a'), BinExpr('*', BinExpr('*', Id('concur'),
                       IntegerLit(4)), FuncCall('fact', [IntegerLit(5)])))
        ]))
        self.assertTrue(TestAST.test(input, expect, 329))

    def test330(self):
        input = """
        fact: function integer (n:integer){
                    if(n==0) return 1;
                    else return n*fact(n-1);
                    }
        main: function void(){
                    printInteger(fact(5));
                    }
        """
        expect = str(Program([
            FuncDecl('fact', IntegerType(), [ParamDecl('n', IntegerType())], "", BlockStmt([
                IfStmt(BinExpr('==', Id('n'), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(
                    BinExpr('*', Id('n'), FuncCall('fact', [BinExpr('-', Id('n'), IntegerLit(1))]))))
            ])),
            FuncDecl('main', VoidType(), [], "", BlockStmt([
                CallStmt('printInteger', [FuncCall('fact', [IntegerLit(5)])])
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 330))

    def test331(self):
        input = """
        a = b + c * d;
        """
        expect = str(Program([
            AssignStmt(Id('a'), BinExpr('+', Id('b'), BinExpr('*', Id('c'), Id('d'))))
        ]))
        self.assertTrue(TestAST.test(input, expect, 331))

    def test332(self):
        input = """king: function auto (inherit throne: string)
        {rule(country);}"""

        expect = str(Program([
            FuncDecl('king', AutoType(), [ParamDecl('throne', StringType(
            ), False, True)], "", BlockStmt([CallStmt('rule', [Id('country')])]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 332))

    def test333(self):
        input = """
        a,b:integer = 1,2; c:integer = a%b; d:integer = c*2; e:integer = d/2;
        """
        expect = str(Program([
            VarDecl('a', IntegerType(), IntegerLit(1)),
            VarDecl('b', IntegerType(), IntegerLit(2)),
            VarDecl('c', IntegerType(), BinExpr('%', Id('a'), Id('b'))),
            VarDecl('d', IntegerType(), BinExpr('*', Id('c'), IntegerLit(2))),
            VarDecl('e', IntegerType(), BinExpr('/', Id('d'), IntegerLit(2)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 333))

    def test334(self):
        input = """
        a[0,1] = \"Hey you\";
        """
        expect = str(Program([
            AssignStmt(
                ArrayCell('a', [IntegerLit(0), IntegerLit(1)]), StringLit('Hey you'))
        ]))
        self.assertTrue(TestAST.test(input, expect, 334))

    def test335(self):
        input = """
        a: boolean = true || (true && false) != !false;
        """
        expect = str(Program([
            VarDecl('a', BooleanType(), BinExpr('!=', BinExpr('||', BooleanLit(True), BinExpr(
                '&&', BooleanLit(True), BooleanLit(False))), UnExpr('!', BooleanLit(False))))
        ]))
        self.assertTrue(TestAST.test(input, expect, 335))

    def test336(self):
        input = """
        call(call(2,3,4),xtv(),4);
        """
        expect = str(Program([
            CallStmt('call', [FuncCall('call', [IntegerLit(2), IntegerLit(3), IntegerLit(4)]), FuncCall(
                'xtv', []), IntegerLit(4)])
        ]))
        self.assertTrue(TestAST.test(input, expect, 336))

    def test337(self):
        input = """
        a = 1+2+n*x()+3-8*9%3;
        """
        expect = str(Program([
            AssignStmt('a', BinExpr('-', BinExpr('+', BinExpr('+', IntegerLit(1), IntegerLit(2)), BinExpr('*', 'n', CallStmt(
                'x', []))), BinExpr('%', BinExpr('*', IntegerLit(8), IntegerLit(9)), IntegerLit(3))))
        ]))

    def test338(self):
        input = """
        a = love()&&hate();
        """
        expect = str(Program([
            AssignStmt(Id('a'), BinExpr('&&', FuncCall(
                'love', []), FuncCall('hate', [])))
        ]))
        self.assertTrue(TestAST.test(input, expect, 338))

    def test339(self):
        input = """
        a:integer = 1;
        b:integer = 2;
        climb: function integer (a:integer, b:integer){
            for(a=1, a<10, a+1){
                if(a==b) return a;
                else return b;
            }
        }
        while(b<10){
            b = b+1;
            print(b);
        }
        goo(a/b + climb(a,b));
        main: function void(){
        }
        """
        expect = str(Program([
            VarDecl('a', IntegerType(), IntegerLit(1)),
            VarDecl('b', IntegerType(), IntegerLit(2)),
            FuncDecl('climb', IntegerType(), [ParamDecl('a', IntegerType()), ParamDecl('b', IntegerType())], "", BlockStmt([
                ForStmt(AssignStmt(Id('a'), IntegerLit(1)), BinExpr('<', Id('a'), IntegerLit(10)),  BinExpr(
                    '+', Id('a'), IntegerLit(1)), BlockStmt([IfStmt(BinExpr('==', Id('a'), Id('b')), ReturnStmt(Id('a')), ReturnStmt(Id('b')))]))
            ])),
            WhileStmt(BinExpr('<', Id('b'), IntegerLit(10)), BlockStmt([
                AssignStmt(Id('b'), BinExpr('+', Id('b'), IntegerLit(1))),
                CallStmt('print', [Id('b')])
            ])),
            CallStmt(
                'goo', [BinExpr('+', BinExpr('/', Id('a'), Id('b')), FuncCall('climb', [Id('a'), Id('b')]))]),
            FuncDecl('main', VoidType(), [], "", BlockStmt([]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 339))

    def test340(self):
        input = """
        e = -4; f = !true; g = (1+2); j = 2+3+4; h = 1+2.3-4e-5; k = (1+2)*3-4;
        """
        expect = str(Program([
            AssignStmt(Id('e'), UnExpr('-', IntegerLit(4))),
            AssignStmt(Id('f'), UnExpr('!', BooleanLit(True))),
            AssignStmt(Id('g'), BinExpr('+', IntegerLit(1), IntegerLit(2))),
            AssignStmt(Id('j'), BinExpr(
                '+', BinExpr('+', IntegerLit(2), IntegerLit(3)), IntegerLit(4))),
            AssignStmt(Id('h'), BinExpr(
                '-', BinExpr('+', IntegerLit(1), FloatLit(2.3)), FloatLit(4e-5))),
            AssignStmt(Id('k'), BinExpr('-', BinExpr('*', BinExpr('+',
                       IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 340))

    def test341(self):
        input = """
         a = n();
            b = n(1);
        """
        expect = str(Program([
            AssignStmt(Id('a'), FuncCall('n', [])),
            AssignStmt(Id('b'), FuncCall('n', [IntegerLit(1)]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 341))

    def test342(self):
        input = """
        greedy: function auto (a:integer, b:integer){
            if(a==b) return a;
            return "Hey you";
            }
        """
        expect = str(Program([
            FuncDecl('greedy', AutoType(), [ParamDecl('a', IntegerType()), ParamDecl('b', IntegerType())], "", BlockStmt([
                IfStmt(BinExpr('==', Id('a'), Id('b')), ReturnStmt(
                    Id('a'))), ReturnStmt(StringLit('Hey you'))
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 342))

    def test343(self):
        input = """
        a,b : integer = 1-5, 2+3;
        """
        expect = str(Program([
            VarDecl('a', IntegerType(), BinExpr(
                '-', IntegerLit(1), IntegerLit(5))),
            VarDecl('b', IntegerType(), BinExpr(
                '+', IntegerLit(2), IntegerLit(3)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 343))

    def test344(self):
        input = """
        a,b, c : string = "Hello", "World", "Hello"::"World"::"!";
        """
        expect = str(Program([
            VarDecl('a', StringType(), StringLit('Hello')),
            VarDecl('b', StringType(), StringLit('World')),
            VarDecl('c', StringType(), BinExpr('::', BinExpr(
                '::', StringLit('Hello'), StringLit('World')), StringLit('!')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 344))

    def test345(self):
        input = """
        a,b,c : boolean = true&&false, false!=true, true||false;
        """
        expect = str(Program([
            VarDecl('a', BooleanType(), BinExpr(
                '&&', BooleanLit(True), BooleanLit(False))),
            VarDecl('b', BooleanType(), BinExpr(
                '!=', BooleanLit(False), BooleanLit(True))),
            VarDecl('c', BooleanType(), BinExpr(
                '||', BooleanLit(True), BooleanLit(False)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 345))

    def test346(self):
        input = """
        a: function integer (a:integer, b:integer){
        
        }
        b: function integer (a:integer, b:integer){
        }
        """
        expect = str(Program([
            FuncDecl('a', IntegerType(), [ParamDecl('a', IntegerType()), ParamDecl(
                'b', IntegerType())], "", BlockStmt([])),
            FuncDecl('b', IntegerType(), [ParamDecl('a', IntegerType()), ParamDecl(
                'b', IntegerType())], "", BlockStmt([]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 346))

    def test347(self):
        input = """
            if(a==b) return a;
            if(a!=b) return b;
        """
        expect = str(Program([
            IfStmt(BinExpr('==', Id('a'), Id('b')), ReturnStmt(Id('a'))),
            IfStmt(BinExpr('!=', Id('a'), Id('b')), ReturnStmt(Id('b')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 347))

    def test348(self):
        input = """
         while(a==b) return a;
            while(a!=b) return b;

        """
        expect = str(Program([
            WhileStmt(BinExpr('==', Id('a'), Id('b')), ReturnStmt(Id('a'))),
            WhileStmt(BinExpr('!=', Id('a'), Id('b')), ReturnStmt(Id('b')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 348))

    def test349(self):
        input = """
        for(i=0, i<10, i+1) return i;
        for(i=0, i>10, i-1) return i;
        do return i; while(i<10);
        """
        expect = str(Program([
            ForStmt(AssignStmt(Id('i'), IntegerLit(0)), BinExpr('<', Id('i'), IntegerLit(
                10)), BinExpr('+', Id('i'), IntegerLit(1)), ReturnStmt(Id('i'))),
            ForStmt(AssignStmt(Id('i'), IntegerLit(0)), BinExpr('>', Id('i'), IntegerLit(
                10)), BinExpr('-', Id('i'), IntegerLit(1)), ReturnStmt(Id('i'))),
            DoWhileStmt(BinExpr('<', Id('i'), IntegerLit(10)), ReturnStmt(Id('i')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 349))

    def test350(self):
        input = """
        for(i=0, i<10, i+1) return i;
        for(i=0, i>10, i-1) {return i;}
        """
        expect = str(Program([
            ForStmt(AssignStmt(Id('i'), IntegerLit(0)), BinExpr('<', Id('i'), IntegerLit(
                10)), BinExpr('+',Id('i'), IntegerLit(1)), ReturnStmt(Id('i'))),
            ForStmt(AssignStmt(Id('i'), IntegerLit(0)), BinExpr('>', Id('i'), IntegerLit(
                10)), BinExpr('-', Id('i'), IntegerLit(1)), BlockStmt([ReturnStmt(Id('i'))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 350))

    def test351(self):
        input = """
        if(a==b) return a;
        if(a!=b) {return b;}
        """
        expect = str(Program([
            IfStmt(BinExpr('==', Id('a'), Id('b')), ReturnStmt(Id('a'))),
            IfStmt(BinExpr('!=', Id('a'), Id('b')),
                   BlockStmt([ReturnStmt(Id('b'))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 351))

    def test352(self):
        input = """
        if(a==b) return a;
        else return b;
        if(a!=b) {return b;}
        else {return a;}
        """
        expect = str(Program([
            IfStmt(BinExpr('==', Id('a'), Id('b')), ReturnStmt(Id('a')), ReturnStmt(Id('b'))),
            IfStmt(BinExpr('!=', Id('a'), Id('b')), BlockStmt(
                [ReturnStmt(Id('b'))]), BlockStmt([ReturnStmt(Id('a'))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 352))

    def test353(self):
        input = """
        do return i; while(i<10);
        do {return i;} while(i<10);
        """
        expect = str(Program([
            DoWhileStmt(BinExpr('<', Id('i'), IntegerLit(10)),
                        ReturnStmt(Id('i'))),
            DoWhileStmt(BinExpr('<', Id('i'), IntegerLit(10)),
                        BlockStmt([ReturnStmt(Id('i'))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 353))

    def test354(self):
        input = """
            a= 1+2*3/4-5;
        """
        expect = str(Program([
            AssignStmt(Id('a'), BinExpr('-', BinExpr('+', IntegerLit(1), BinExpr('/',
                       BinExpr('*', IntegerLit(2), IntegerLit(3)), IntegerLit(4))), IntegerLit(5)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 354))

    def test355(self):
        input = """
        foo: function integer (inherit out a:integer, b:integer)inherit bar{
            a = a + b;
            return a;
        }
        """
        expect = str(Program([
            FuncDecl('foo', IntegerType(), [ParamDecl('a', IntegerType(), True, True), ParamDecl(
                'b', IntegerType())], 'bar', BlockStmt([AssignStmt(Id('a'), BinExpr('+', Id('a'), Id('b'))), ReturnStmt(Id('a'))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 355))

    def test356(self):
        input = """
        climbstairs: function integer(n:integer) {
            if(n==1) return 1;
            if(n==2) return 2;
            return climbstairs(n-1)+climbstairs(n-2);
        }
        """
        expect = str(Program([
            FuncDecl('climbstairs', IntegerType(), [ParamDecl('n', IntegerType())], "", BlockStmt([
                IfStmt(BinExpr('==', Id('n'), IntegerLit(1)),
                       ReturnStmt(IntegerLit(1))),
                IfStmt(BinExpr('==', Id('n'), IntegerLit(2)),
                       ReturnStmt(IntegerLit(2))),
                ReturnStmt(BinExpr('+', FuncCall('climbstairs', [BinExpr('-', Id('n'), IntegerLit(
                    1))]), FuncCall('climbstairs', [BinExpr('-', Id('n'), IntegerLit(2))])))
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 356))

    def test357(self):
        input = """
        while(a==b) {
            a = a + b;
            return a;
        }
        if (a==b) {
            a = a + b;
            return a;
        }
        """
        expect = str(Program([
            WhileStmt(BinExpr('==', Id('a'), Id('b')), BlockStmt(
                [AssignStmt(Id('a'), BinExpr('+', Id('a'), Id('b'))), ReturnStmt(Id('a'))])),
            IfStmt(BinExpr('==', Id('a'), Id('b')), BlockStmt(
                [AssignStmt(Id('a'), BinExpr('+', Id('a'), Id('b'))), ReturnStmt(Id('a'))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 357))

    def test358(self):
        input = """
        binarysearch: function void (l:integer, r:integer, x:integer) {
            if (r>=l) {
                mid = l + (r - l)/2;
                if (arr[mid] == x) return mid;
                if (arr[mid] > x) return binarysearch(l, mid-1, x);
                return binarysearch(mid+1, r, x);
                }
        }
        """
        expect = str(Program([
            FuncDecl('binarysearch', VoidType(), [ParamDecl('l', IntegerType()), ParamDecl('r', IntegerType()), ParamDecl('x', IntegerType())], "", BlockStmt([
                IfStmt(BinExpr('>=', Id('r'), Id('l')), BlockStmt([
                    AssignStmt(Id('mid'), BinExpr(
                        '+', Id('l'), BinExpr('/', BinExpr('-', Id('r'), Id('l')), IntegerLit(2)))),
                    IfStmt(BinExpr('==', ArrayCell(
                        'arr', [Id('mid')]),  Id('x')), ReturnStmt(Id('mid'))),
                    IfStmt(BinExpr('>', ArrayCell('arr', [Id('mid')]),  Id('x')), ReturnStmt(
                        FuncCall('binarysearch', [Id('l'), BinExpr('-', Id('mid'), IntegerLit(1)),  Id('x')]))),
                    ReturnStmt(FuncCall('binarysearch', [
                               BinExpr('+', Id('mid'), IntegerLit(1)), Id('r'), Id('x')]))
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 358))

    def test359(self):
        input = """
        foo: function integer (inherit out a:integer, b:integer)inherit bar{
            return a;
        }
        if (a==b) {
            a = a + b;
            return a;
        }
        main: function void () {
            a = 1;
            b = 2;
            c = foo(a,b);
            return 0;
        }
        """
        expect = str(Program([
            FuncDecl('foo', IntegerType(), [ParamDecl('a', IntegerType(), True, True), ParamDecl(
                'b', IntegerType())], 'bar', BlockStmt([ReturnStmt(Id('a'))])),
            IfStmt(BinExpr('==', Id('a'), Id('b')), BlockStmt(
                [AssignStmt(Id('a'), BinExpr('+', Id('a'), Id('b'))), ReturnStmt(Id('a'))])),
            FuncDecl('main', VoidType(), [], "", BlockStmt([

                AssignStmt(Id('a'), IntegerLit(1)),
                AssignStmt(Id('b'), IntegerLit(2)),
                AssignStmt(Id('c'), FuncCall('foo', [Id('a'), Id('b')])),
                ReturnStmt(IntegerLit(0))
            ]))

        ]))
        self.assertTrue(TestAST.test(input, expect, 359))

    def test360(self):
        input = """
        inc: function void(out n: integer, delta: integer){}
        """
        expect = str(Program([
            FuncDecl('inc', VoidType(), [ParamDecl('n', IntegerType(), True, False), ParamDecl(
                'delta', IntegerType())], "", BlockStmt([]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 360))

    def test361(self):
        input = """
            {}{}{}
        """
        expect = str(Program([
            BlockStmt([]),
            BlockStmt([]),
            BlockStmt([])
        ]))
        self.assertTrue(TestAST.test(input, expect, 361))

    def test362(self):
        input = """
        a = -4.5 + 5.0 + 6.4;
        """
        expect = str(Program([
            AssignStmt(Id('a'), BinExpr(
                '+', BinExpr('+', UnExpr('-', FloatLit(4.5)), FloatLit(5.0)), FloatLit(6.4)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 362))

    def test363(self):
        input = """
        if(n==NULL) return;
        """
        expect = str(Program([
            IfStmt(BinExpr('==', Id('n'), Id('NULL')), ReturnStmt())
        ]))
        self.assertTrue(TestAST.test(input, expect, 363))

    def test364(self):
        input = """
        this_year: boolean = bad_year>2020;
        """
        expect = str(Program([
            VarDecl('this_year', BooleanType(), BinExpr(
                '>', Id('bad_year'), IntegerLit(2020)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 364))

    def test365(self):
        input = """
        a: array [5,3] of integer;
        a[0,0] = s;
        a = None;
        """
        expect = str(Program([
            VarDecl('a', ArrayType([5, 3], IntegerType())),
            AssignStmt(
                ArrayCell('a', [IntegerLit(0), IntegerLit(0)]), Id('s')),
            AssignStmt(Id('a'), Id('None'))
        ]))
        self.assertTrue(TestAST.test(input, expect, 365))

    def test366(self):
        input = """
        foo: function integer (inherit out a:integer, b:integer)inherit bar{
            return a;
        }
        bar: function integer (inherit out a:integer, b:integer)inherit foo{
            return a;
        }
        main: function void () {
            foo(bar(1,2),3);
            }
        """
        expect = str(Program([
            FuncDecl('foo', IntegerType(), [ParamDecl('a', IntegerType(), True, True), ParamDecl(
                'b', IntegerType())], 'bar', BlockStmt([ReturnStmt(Id('a'))])),
            FuncDecl('bar', IntegerType(), [ParamDecl('a', IntegerType(), True, True), ParamDecl(
                'b', IntegerType())], 'foo', BlockStmt([ReturnStmt(Id('a'))])),
            FuncDecl('main', VoidType(), [], "", BlockStmt([
                CallStmt(
                    'foo', [FuncCall('bar', [IntegerLit(1), IntegerLit(2)]), IntegerLit(3)])
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 366))

    def test367(self):
        input = """
        a,b,c,d: float = e,f,g,h;
        printInteger(reduce(a,b,c,d));
        """
        expect = str(Program([
            VarDecl('a', FloatType(), Id('e')),
            VarDecl('b', FloatType(), Id('f')),
            VarDecl('c', FloatType(), Id('g')),
            VarDecl('d', FloatType(), Id('h')),
            CallStmt('printInteger', [FuncCall(
                'reduce', [Id('a'), Id('b'), Id('c'), Id('d')])])
        ]))
        self.assertTrue(TestAST.test(input, expect, 367))

    def test368(self):
        input = """
        if (a==b) {
            a = a + b;
            return "No";
        }
        else {
            a = a - b;
            return "Yes";
        }
        """
        expect = str(Program([
            IfStmt(BinExpr('==', Id('a'), Id('b')), BlockStmt([
                AssignStmt(Id('a'), BinExpr('+', Id('a'), Id('b'))),
                ReturnStmt(StringLit('No'))
            ]), BlockStmt([
                AssignStmt(Id('a'), BinExpr('-', Id('a'), Id('b'))),
                ReturnStmt(StringLit('Yes'))
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 368))

    def test369(self):
        input = """
        a = a + b + c + d;
        """
        expect = str(Program([
            AssignStmt(Id('a'), BinExpr(
                '+', BinExpr('+', BinExpr('+', Id('a'), Id('b')), Id('c')), Id('d')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 369))

    def test370(self):
        input = """
        for(i=0, i<10, i+1) {
            print(i);
        }
        while(i<10) {
            print(i);
            i = i + 1;
        }
        if(i<10) {
            print(i);
            i = i + 1;
        }
        """
        expect = str(Program([
            ForStmt(AssignStmt(Id('i'), IntegerLit(0)), BinExpr('<', Id('i'), IntegerLit(10)), BinExpr('+', Id('i'), IntegerLit(1)), BlockStmt([
                CallStmt('print', [Id('i')])
            ])),
            WhileStmt(BinExpr('<', Id('i'), IntegerLit(10)), BlockStmt([
                CallStmt('print', [Id('i')]),
                AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1)))
            ])),
            IfStmt(BinExpr('<', Id('i'), IntegerLit(10)), BlockStmt([
                CallStmt('print', [Id('i')]),
                AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1)))
            ]), None)
        ]))
        self.assertTrue(TestAST.test(input, expect, 370))

    def test371(self):
        input = """
            if (a==b) return "No";
            else return "Yes";
            while(true)
                ddos(server);
        """
        expect = str(Program([
            IfStmt(BinExpr('==', Id('a'), Id('b')), ReturnStmt(
                StringLit('No')), ReturnStmt(StringLit('Yes'))),
            WhileStmt(BooleanLit(True), CallStmt('ddos', [Id('server')]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 371))

    def test372(self):
        input = """
        complex: function integer (a:integer, b:integer) {
                return complex(a,b);
            }
        """
        expect = str(Program([
            FuncDecl('complex', IntegerType(), [ParamDecl('a', IntegerType()), ParamDecl(
                'b', IntegerType())], "", BlockStmt([ReturnStmt(FuncCall('complex', [Id('a'), Id('b')]))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 372))

    def test373(self):
        input = """
            e: float = 2.83;
            pi: float = 3.14;

        """
        expect = str(Program([
            VarDecl('e', FloatType(), FloatLit(2.83)),
            VarDecl('pi', FloatType(), FloatLit(3.14))
        ]))
        self.assertTrue(TestAST.test(input, expect, 373))

    def test374(self):
        input = """
        return n*(n-1)/n;
        """
        expect = str(Program([
            ReturnStmt(
                BinExpr('/', BinExpr('*', Id('n'), BinExpr('-', Id('n'), IntegerLit(1))), Id('n')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 374))

    def test375(self):
        input = """
        n: function integer (a:integer, b:integer) {
            if (a==b) return 1;
            return n(n(n(a-b,b),1),2);
        }
        """
        expect = str(Program([
            FuncDecl('n', IntegerType(), [ParamDecl('a', IntegerType()), ParamDecl(
                'b', IntegerType())], "", BlockStmt([IfStmt(BinExpr('==', Id('a'), Id('b')), ReturnStmt(IntegerLit(1)), None), ReturnStmt(FuncCall('n', [FuncCall('n', [FuncCall('n', [BinExpr('-', Id('a'), Id('b')), Id('b')]), IntegerLit(1)]), IntegerLit(2)]))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 375))

    def test376(self):
        input = """
            a: integer = 1+2/3*4;
        """
        expect = str(Program([
            VarDecl('a', IntegerType(), BinExpr('+', IntegerLit(1), BinExpr('*',
                    BinExpr('/', IntegerLit(2), IntegerLit(3)), IntegerLit(4))))
        ]))
        self.assertTrue(TestAST.test(input, expect, 376))

    def test377(self):
        input = """
        a = a||b <= 0;
        """
        expect = str(Program([
            AssignStmt(Id('a'), BinExpr('<=', BinExpr(
                '||', Id('a'), Id('b')), IntegerLit(0)))
        ]))

        self.assertTrue(TestAST.test(input, expect, 377))

    def test378(self):
        input = """
        
        """
        expect = str(Program([
        ]))
        self.assertTrue(TestAST.test(input, expect, 378))

    def test379(self):
        input = """
        a: array [5,3] of integer;
                 a[0,0] = s;
        """
        expect = str(Program([
            VarDecl(Id('a'), ArrayType([5, 3], IntegerType())),
            AssignStmt(ArrayCell('a', [IntegerLit(0), IntegerLit(0)]), Id('s'))
        ]))

    def test380(self):
        input = """
        i:integer = 0; do {getAPI(); i = i+1;} while (i<5);
        """
        expect = str(Program([
            VarDecl('i', IntegerType(), IntegerLit(0)),
            DoWhileStmt(BinExpr('<', Id('i'), IntegerLit(5)), BlockStmt(
                [CallStmt('getAPI', []), AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1)))]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 380))

    def test381(self):
        input = """
            for (i=0, i<10, i+1){  
                     a[i] = i;           
                }
        """
        expect = str(Program([
            ForStmt(AssignStmt('i', IntegerLit(0)), BinExpr('<', 'i', IntegerLit(10)), BinExpr(
                '+', 'i', IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell('a', ['i']), 'i')]))
        ]))

    def test382(self):
        input = """while(true){
                for(i=0, i<10 ,i+1)
                    dfs(graph[i]);
                
                break;
            }
            """
        expect = str(Program([
            WhileStmt(BooleanLit(True), BlockStmt([
                ForStmt(AssignStmt(Id('i'), IntegerLit(0)), BinExpr('<', Id('i'), IntegerLit(10)), BinExpr(
                    '+', Id('i'), IntegerLit(1)), CallStmt('dfs', [ArrayCell('graph', [Id('i')])])),
                BreakStmt()
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 382))

    def test383(self):
        input = """
        n = cal(cal(cal(2)));
        """
        expect = str(Program([
            AssignStmt(Id('n'), FuncCall(
                'cal', [FuncCall('cal', [FuncCall('cal', [IntegerLit(2)])])]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 383))

    def test384(self):
        input = """
        n = a&&b||c>d<=e;
        """
        expect = str(Program([
            AssignStmt(Id('n'), BinExpr('<=', BinExpr('>', BinExpr(
                '||', BinExpr('&&', Id('a'), Id('b')), Id('c')), Id('d')), Id('e')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 384))

    def test385(self):
        input = """
        /*this is a comment */
        n = bullshit[0];
        """
        expect = str(Program([
            AssignStmt(Id('n'), ArrayCell('bullshit', [IntegerLit(0)]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 385))

    def test386(self):
        input = """
        {
        // this is a comment
        }
        """
        expect = str(Program([
            BlockStmt([])
        ]))
        self.assertTrue(TestAST.test(input, expect, 386))

    def test387(self):
        input = """
        main: function void(){
            add(1,2);
            sub(1,2);
            n: integer = add(1,2)+sub(1,2)/sub(2,1);
        }
        """
        expect = str(Program([
            FuncDecl('main', VoidType(), [], "", BlockStmt([
                CallStmt('add', [IntegerLit(1), IntegerLit(2)]),
                CallStmt('sub', [IntegerLit(1), IntegerLit(2)]),
                VarDecl('n', IntegerType(), BinExpr('+', FuncCall('add', [IntegerLit(1), IntegerLit(2)]), BinExpr(
                    '/', FuncCall('sub', [IntegerLit(1), IntegerLit(2)]), FuncCall('sub', [IntegerLit(2), IntegerLit(1)]))))
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 387))

    def test388(self):
        input = """
            terminate: function void(){
                preventDefault();
            }
            main: function void(){
                terminate();
            }
        """
        expect = str(Program([
            FuncDecl('terminate', VoidType(), [], "", BlockStmt([
                CallStmt('preventDefault', [])
            ])),
            FuncDecl('main', VoidType(), [], "", BlockStmt([
                CallStmt('terminate', [])
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 388))

    def test389(self):
        input = """
        dp: function array[2,2] of integer (a:integer, b:integer){
            for(a=1, a<10, a+1){
                if(a==b) return a;
                else return b;
            }
        }
        """
        expect = str(Program([
            FuncDecl('dp', ArrayType([2, 2], IntegerType()), [ParamDecl('a', IntegerType()), ParamDecl('b', IntegerType())], "", BlockStmt([
                ForStmt(AssignStmt(Id('a'), IntegerLit(1)), BinExpr('<', Id('a'), IntegerLit(10)),  BinExpr(
                    '+', Id('a'), IntegerLit(1)), BlockStmt([IfStmt(BinExpr('==', Id('a'), Id('b')), ReturnStmt(Id('a')), ReturnStmt(Id('b')))]))
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 389))

    def test390(self):
        input = """
        a,b : array[1,3] of boolean;
        """
        expect = str(Program([
            VarDecl('a', ArrayType([1, 3], BooleanType())),
            VarDecl('b', ArrayType([1, 3], BooleanType()))
        ]))
        self.assertTrue(TestAST.test(input, expect, 390))

    def test391(self):
        input = """
        n = call(0);
        print(call(1,2,3));
        """
        expect = str(Program([
            AssignStmt(Id('n'), FuncCall('call', [IntegerLit(0)])),
            CallStmt(
                'print', [FuncCall('call', [IntegerLit(1), IntegerLit(2), IntegerLit(3)])])
        ]))
        self.assertTrue(TestAST.test(input, expect, 391))

    def test392(self):
        input = """
        a: array[2] of string = {\"TungCua\",\"TauCong\"};
        """
        expect = str(Program([
            VarDecl('a', ArrayType([2], StringType()), ArrayLit(
                [StringLit('TungCua'), StringLit('TauCong')]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 392))

    def test393(self):
        input = """"""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input, expect, 393))

    def test394(self):
        input = """
        return (1+2);
        """
        expect = str(Program([
            ReturnStmt(BinExpr('+', IntegerLit(1), IntegerLit(2)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test395(self):
        input = """{{{}}}"""
        expect = str(Program([
            BlockStmt([BlockStmt([BlockStmt([])])])
        ]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test396(self):
        input = """
        a: integer = 1; b:float = get_pi();
        """
        expect = str(Program([
            VarDecl('a', IntegerType(), IntegerLit(1)),
            VarDecl('b', FloatType(), FuncCall('get_pi', []))
        ]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test397(self):
        input = """
        b: string = a::c;
        """
        expect = str(Program([
            VarDecl('b', StringType(), BinExpr('::', Id('a'), Id('c')))
        ]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test398(self):
        input = """
        a[0,0] = s; a[0,1] = -5;
        """
        expect = str(Program([
            AssignStmt(
                ArrayCell('a', [IntegerLit(0), IntegerLit(0)]), Id('s')),
            AssignStmt(ArrayCell('a', [IntegerLit(0), IntegerLit(1)]), UnExpr(
                '-', IntegerLit(5)))
        ]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test399(self):
        input = """
        main: function void(){
            if(a==1) return;
            else return 1;
            while(a<10){
                a = a+1;
                print(a);
                }
        }
        """
        expect = str(Program([
            FuncDecl('main', VoidType(), [], "", BlockStmt([
                IfStmt(BinExpr('==', Id('a'), IntegerLit(1)),
                       ReturnStmt(), ReturnStmt(IntegerLit(1))),
                WhileStmt(BinExpr('<', Id('a'), IntegerLit(10)), BlockStmt([
                    AssignStmt(Id('a'), BinExpr('+', Id('a'), IntegerLit(1))),
                    CallStmt('print', [Id('a')])
                ]))
            ]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 399))

    def test400(self):
        input = """
        while (true) run(py);
        """
        expect = str(Program([
            WhileStmt(BooleanLit(True), CallStmt('run', [Id('py')]))
        ]))
        self.assertTrue(TestAST.test(input, expect, 400))
