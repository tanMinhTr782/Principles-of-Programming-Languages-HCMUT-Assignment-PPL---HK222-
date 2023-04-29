import unittest
from TestUtils import TestParser

# py run.py test ParserSuite
class ParserSuite(unittest.TestCase):
#----------------- [TEST VARIABLE DECLARATION] -----------------#
    # def test_0(self):
    #     input = """foo: function void (inherit a: integer, inherit out b: float) inherit bar {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 311))
    def test_0(self):
        input = """x  : integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))
    def test_1(self):
        input = """x : string; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_2(self):
        input = """x : float;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_3(self):
        input = """x : boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_4(self):
        input = """x : float;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_5(self):
        # Test declaration array
        input = """test_array: array [2,3] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_6(self):
        # Test declaration array
        input = """tes1, test2 : array [3,4] of string;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_7(self):
        input = """x,y,z : integer = 1,2,3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_8(self):
        input = """x,y : float = 1.1 , 0.1 ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_9(self):
        input = """x,y : boolean = true, false;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_10(self):
        input = """x,y : string = "Kien","Ha";  """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_11(self): #false
        #Miss SEMI
        input = """x: integer"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_12(self):
        #Miss semi
        input = """x,y,z : integer = 1,2,3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_13(self): #false
        #Miss SEMI
        input = """x:string """
        expect = "Error on line 1 col 9: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_14(self):
        #Miss semi
        input = """x,y,z : string = 1,2,3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
#----------------- [TEST FUNCTION DECLARATION] -----------------#
    def test_15(self):
        input = '''
            function mess: integer (n: integer){
                return n/50 * 2;
            }
        '''
        expect = "Error on line 2 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_16(self):
        input = '''
            function {

            }
        '''
        expect = "Error on line 2 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_17(self):
        input = '''
            {

            }
        '''
        expect = "Error on line 2 col 12: {"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_18(self):
        input = '''
            x: integer = 65;
            mess: function integer (n: integer){
                return n/50 * 2;
            }
            main: function void () {
                delta: integer = mess(7);
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_19(self):
        input = '''
            add: function integer (n: integer){
                sum: integer= 0;
                for (i = 0, i<=n, i+1){
                    sum = sum + i;
                }
                return sum;
            }
            main: function void () {
                delta: integer = add(10);
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_20(self):
        input = '''
            x: integer = 65;
            fact: function integer (n:integer){
                if (n == 0) return 1;
                else return n * fact(n-1);
            }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta: integer = fact(3);
                inc(x,delta);
                printInt(x);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_21(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i!=0){
                    i = i - 1;
                }
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_22(self):
        input = '''
            main: function void () {
                i: integer = 10;
                while (i>20){
                    i = i + 2;
                }
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_23(self):
        input = '''
            voidA: function integer (n: integer){
                return n%10;
            }
            voidB: function void (out n: integer, delta:integer){
                n = n + voidA(delta);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInt(x);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_24(self):
        input = '''
            main: function void () {
                delta: string = "Kien";
                printString(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_25(self):
        input = '''
            main: function void () {
                delta: float = 3.45;
                printFloat(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_26(self):
        input = '''
            main: function void () {
                delta: boolean = true;
                printBoolean(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_27(self):
        input = '''
            main: function void () {
                b: array [5] of integer;
                b[4] = 3;
                printInt(b[4]);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
# py run.py test ASTGenSuite
    def test_28(self):
        input = '''
            main: function void () {
                delta: integer = 3+34*30/5*16/4*2/2+19%4+2%2;
                printInt(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_29(self):
        input = '''
            main: function void () {
                i: integer = 10;
                do{
                    i = i - 1;
                }
                while (i!=0);
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_30(self):
        input = '''
            main: function void () {
                i: integer = -10;
                do{
                    i = i - 1;
                }
                while (i!=0);
                return  i;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_31(self):
        input = '''
            main: function void () {
                delta: float = 130.34e2;
                printFloat(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_32(self):
        input = '''
            main: function void () {
                delta: string = "true";
                printString(delta);
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test_33(self):
        input = '''
           test: function integer (out x:integer, data:string){
            c : integer;
           }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
#----------------- [TEST MIXED DECLARATION] -----------------#
    def test_34(self):
        input = '''
        integer x;
            test: function integer (out x:integer, data:string){
            c : integer;
           }
        '''
        expect = "Error on line 2 col 8: integer"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_35(self):
        input = '''
        z : string;
        x,y : boolean, float;
            test: function integer (out x:integer, data:string){
            c : integer;
           }
        '''
        expect = "Error on line 3 col 21: ,"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_36(self):
        input = '''
        z : string;
        out : x string;
        '''
        expect = "Error on line 3 col 8: out"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_37(self):
        input = '''
        z : string;
        out x: string;
        '''
        expect = "Error on line 3 col 8: out"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_38(self):
        input = '''
            test: function integer (out x:integer, data:string){
            a : integer;
            out b: string;
           }
        '''
        expect = "Error on line 4 col 12: out"
        self.assertTrue(TestParser.test(input, expect, 238))


    def test_39(self):
        # Check if body canbe empty?
        input = '''
            test: function integer (){
           }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_40(self):
        # Check SEMI after declaration function
        input = '''
            test: function integer (){
           };
        '''
        expect = "Error on line 3 col 12: ;"
        self.assertTrue(TestParser.test(input, expect, 240))
#----------------- [EXPRESSION TEST] -----------------#
    def test_41(self): #note
        input = """
            x: float = 10 % 2 + .2E-10 * 12 + 8.98;
            y: boolean =  (true||false)&&true||false;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_42(self): #note
        input = """
            x: float = 10 % 2 + .2E-10 * 12 + 8.98;
            y: boolean =  true||false&&true||false;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_43(self): #note
        input = """
            x: float = 10 % 2 + .2E-10 * 012 + 8.98;
            y: boolean =  (true||false)&&true||false;
        """
        expect = "Error on line 2 col 42: 12"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_44(self):
        input = """
                a:float = 1_000 % 2 + .2E-10  + 8.98;
                b:float = (1 - 1) * 2 / 2 / 2 + 8 % 3 + ---10 * !!!true&&false;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_45(self):
        input = """
                x: string = "Trung"::"Kien";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_46(self):
        input = """
                x: string = "Trung";
                y: string = "Kien";
                z: string = x::y;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

#----------------- [ARRAY TEST] -----------------#

    def test_47(self):
        input = """
                x: integer = 1/2*3 + 4;
                array_test : array [1,3] of integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_48(self):
        input = """
                x: integer = 1/2*3 + 4;
                array_test : array [x,3] of integer;
        """
        expect = "Error on line 3 col 36: x"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_49(self):
        input = """
                x: integer= 1/2*3 + 4;
                array_test : array [1+1,3] of integer;
        """
        expect = "Error on line 3 col 37: +"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_50(self):
        input = """
                x: integer = 1/2*3 + 4;
                array_test : array [1+1,3] of integer;
        """
        expect = "Error on line 3 col 37: +"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_51(self):
        input = """
                x: integer = 1/2*3 + 4;
                array_test : array [1,3] of integer;
                array_test [];
        """
        expect = "Error on line 4 col 27: ["
        self.assertTrue(TestParser.test(input,expect,251))

    def test_52(self): #note
        input = """
                x: integer = 1/2*3 + 4;
                array_test : array [1,3] of integer;
                array_test [1,2];
        """
        expect = "Error on line 4 col 27: ["
        self.assertTrue(TestParser.test(input,expect,252))

    def test_53(self): #note
        input = """
                x: integer = 1/2*3 + 4;
                array_test : array [1,3] of integer;
                array_test 1,2;
        """
        expect = "Error on line 4 col 27: 1"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_54(self): #note
        input = """
                x: integer= 1/2*3 + 4;
                array_test : array [1,3] of integer;
                y: float = array_test[1+1,x];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))


    def test_55(self):
        input = """
                x:integer = 1/2*3 + 4;
                array_test : array [1,3] of integer;
                y: float = array_test[1+1,x] + 1/100;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_56(self):
        input = """
                arr : array [2,3] of integer = {1,2,3,4,5,6};
                arr [0,1] = ;
                y: float = array_test[1+1,x] + 1/100;
        """
        expect = "Error on line 3 col 20: ["
        self.assertTrue(TestParser.test(input,expect,256))

    def test_57(self):
        input = """
                arr : array [2,3] of float;
                arr [0,1] = 1*2+1.2-1;
        """
        expect = "Error on line 3 col 20: ["
        self.assertTrue(TestParser.test(input,expect,257))

    def test_58(self):
        input = """
                x : integer;
                arr : array [2,3] of float;
                x = arr[0,1]
        """
        expect = "Error on line 4 col 18: ="
        self.assertTrue(TestParser.test(input,expect,258))

    def test_59(self):
        input = '''
            test: function integer (){
                arr : array [2,3] of float;
                x = arr [0,1];
           }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_60(self):
        # Array is parameter?
        input = '''
            arr : array [2,3] of float;
            test: function integer(out arr : array [2,3] of float){
                arr : array [2,3] of float;
                arr [0,1] = 1*2+1.2-1;
           }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_61(self):
        input = '''
            test: function integer(x:integer,){
                arr : array [2,3] of float;
                arr [0,1] = 1*2+1.2-1;
           }
        '''
        expect = "Error on line 2 col 45: )"
        self.assertTrue(TestParser.test(input, expect, 261))
#----------------- [STATEMENT TEST] -----------------#
    def test_62(self):
        input = '''
            return;
        '''
        expect = "Error on line 2 col 12: return"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_63(self):
        input = '''
            break;
        '''
        expect = "Error on line 2 col 12: break"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_64(self):
        input = '''
            continue;
        '''
        expect = "Error on line 2 col 12: continue"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_65(self):
        input = '''
            main : function void() {
                continue;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_66(self):
        input = '''
            x : integer ;
            main : function void() {
                x : integer ;
                if(x==3) y = 3;
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_67(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==3) {y :integer= 3;}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_68(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==3) {y : integer = 3}
            }

        '''
        expect = "Error on line 4 col 41: }"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_69(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==3) {y : integer = 3;};
            }
        '''
        expect = "Error on line 4 col 43: ;"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_70(self):
        input = '''
            x : integer ;
            main : function void() {
               if(x==3){break;}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_71(self):
        input = '''
            x : integer;
            main : function void() {
               if(x==3){continue;}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_72(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==3) {y : integer= 3;};
                else y : integer = 4;
            }
        '''
        expect = "Error on line 4 col 42: ;"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_73(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==3) {y :integer = 3;}
                else {y : integer = 34;}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_74(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==3) {y : integer = 3;};
                else {y : integer = 34};
            }
        '''
        expect = "Error on line 4 col 43: ;"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_75(self):
        input = '''
            x : integer ;
            main : function void() {
                if(x==3) {y :integer = 3;}
                else {y : integer = 34;}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_76(self):
        input = '''
            arr : array [1,2] of integer;
            x : integer ;
            main : function void() {
                if(x==3) {arr[0,1] = 3;}
                else {arr[0,1] = 4 ;}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_77(self):
        input = '''

            arr : array [1,2] of integer;
            main : function void() {
                if(x==3) {arr[0,1] = arr [0,2];}
                else {arr[0,1] = arr[1,2];}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_78(self):
        input = '''
            main : function void() {
                x : integer ;
                if(x==3){
                   y : integer ;
                    if(y==4) {z : integer = 4;}
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_79(self):
        input = '''
            main : function void() {
                x : integer ;
                if(x==3){
                    y : integer ;
                    if(y==4) {z : integer = 4;}
                    else {
                        z : integer = 5;
                    }
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_80(self):
        input = '''
            main : function void() {
                x :integer ;
                 if(x==3){
                    y : integer ;
                    if(y==4) {z : integer = 4;}
                    else {
                    z : integer = 5;
                    }
                } else { z : integer = 3;}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))


    def test_81(self):
        input = '''
            main : function void() {
                x : integer ;
                if(x==3){}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_82(self):
        input = '''
            main : function void() {
                x : integer ;
                if(x==3){} else z : integer = 3;
            }

        '''
        expect = "Error on line 4 col 34: :"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_83(self):
        input = '''
            main : function void() {
                x : integer ;
                if(x==3){} else {z : integer = 3;}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_84(self):
        input = '''
            main : function void() {
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_85(self):
        input = '''
            main : function void() {
                x : integer ;
                if(x==3){
                    for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    }
                } else {z : integer = 3;}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_86(self):
        input = '''
            main: function void() {
                for (i = 1, i < 10, i + 1) {
                writeInt(i);
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_87(self):
        input = '''
            main : function void() {
                x : integer ;
                {
                    for (i = 1, i < 10, i + 1) {
                        writeInt(i);
                        if(x==3){break;}
                    }
                }
            }

        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_88(self):
        input = '''
            main : function void() {
                x : integer ;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    if(x==3){break;}
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89(self):
        input = '''
            main : function void() {
                x : integer ;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    if(x==3){continue;}
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))


    def test_90(self):
        input = '''
            main : function void() {
                x : integer ;
                for (i = 1, i < 10, i + 1) {
                    if(i%2==0){writeInt(i);}
                    else foo(2*i);
                }
            }

        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_91(self):
        input = '''
            main : function void() {
                x : integer = 5;
                while (x > 0){
                    writeInt(x);
                    x = x - 1;
                }
            }

        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_92(self):
        input = '''
            main : function void() {
                x : integer = 5;
                while (x > 0){
                    if(x%2==0){writeInt(x);}
                    else break;
                    x = x - 1;
                }
            }

        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_93(self):
        input = '''
            main : function void() {
                x : integer = 5;
                while x > 0 {
                    x = x - 1;
                }
            }

        '''
        expect = "Error on line 4 col 22: x"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_94(self):
        input = '''
            main : function void() {
                x : integer = 5;
                while (){
                }
            }

        '''
        expect = "Error on line 4 col 23: )"
        self.assertTrue(TestParser.test(input, expect, 294))


    def test_95(self):
        input = '''
            main : function void() {
                x : integer = 5;
                while ( x > 0){
                }
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_96(self):
        input = '''
            main : function void() {
                x : integer = 5;
                while (x > 0)  x = x - 1;
            }

        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_97(self):
        input = '''
            main : function void() {
                x : integer = 5;
                do x = x - 1;
                while (x > 0);
            }

        '''
        expect = "Error on line 4 col 19: x"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_98(self):
        input = '''
            main : function void() {
                x : integer = 5;
                do {x = x - 1;}
                while (x > 0);
            }

        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_99(self):
        input = '''
            main : function void() {
                x : integer= 5;
                do {x = x - 1}
                while (x > 0);
            }

        '''
        expect = "Error on line 4 col 29: }"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_100(self):
        input = '''
            main : function void() {
                x : integer = 5;
                do {
                    if(x==3) writeInt(x);
                }
                while (x > 0);
            }

        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))

    def test_101(self):
        input = '''
            main : function void() {
            x : integer= 5;
                do {
                    if(x==3) break;
                    else writeInt(x);
                }
                while (x > 0);
            }

        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 301))

    def test_102(self):
        input = '''
            main : function void() {
                x : integer = 5;
                do {
                    if(x==3) continue;
                    else writeInt(x);
                }
                while (x > 0);
            }

        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 302))

    def test_103(self):
        input = '''
            main : function void() {
                x : integer;
                for (i = 1, i < 10, i + 1) {
                    if(x%2==0){writeInt(i)};
                }
            }
        '''
        expect = "Error on line 5 col 42: }"
        self.assertTrue(TestParser.test(input, expect, 303))

    def test_104(self):
        input = '''
        x : integer;
        x = count(1+1,1*2)
        '''
        expect = "Error on line 3 col 10: ="
        self.assertTrue(TestParser.test(input, expect, 304))

    def test_105(self):
        input = '''
            x : integer;
            main : function void () {count(1+1,1*2);} ;
        '''
        expect = "Error on line 3 col 54: ;"
        self.assertTrue(TestParser.test(input, expect, 305))

    def test_106(self):
        input = '''
            main : function void (x: function void()) {}
        '''
        expect = "Error on line 2 col 37: function"
        self.assertTrue(TestParser.test(input, expect, 306))

    def test_107(self):
        input = '''
            main : function void (x : auto) {}
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 307))
    def test_108(self):
        input = '''
          main : function void () {
             alse1 : integer = 1[2];
            a = ar[1,2];}
        '''
        expect = "Error on line 3 col 32: ["
        self.assertTrue(TestParser.test(input, expect, 308))
    def test_109(self):
        input = '''
        x : integer = 1__2;
        '''
        expect = "Error on line 2 col 23: __2"
        self.assertTrue(TestParser.test(input, expect, 309))

    def test_109(self):
        input = '''
        main : function void() {
                for( i[0] = 0 , i[0] < 1 , -1){}
            }
        '''
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 310))
