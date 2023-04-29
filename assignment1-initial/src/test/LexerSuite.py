import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("+1", "+,1,<EOF>", 101))
    def test_higherCase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Abc1111", "Abc1111,<EOF>", 102))
    def test_underscore_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_Abc1111", "_Abc1111,<EOF>", 103))
    def test_number_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1abc", "Error Token 1", 104))
    def test_space_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a bc", "a,bc,<EOF>", 105))
    def test_two_unders_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("__", "__,<EOF>", 106))
    def test_number_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("69", "Error Token 6", 107))
    def test_number_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_234_567", "1234567,<EOF>", 108))
    def test_number2_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_72", "172,<EOF>", 109))
    def test_number3_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("172", "172,<EOF>", 110))
    def test_number_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1.234", "1.234,<EOF>", 111))
    def test_number2_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1.2e3", "1.2e3,<EOF>", 112))
    def test_number3_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("7E-10", "7E-10,<EOF>", 113))
    def test_number4_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_234.567", "1234.567,<EOF>", 114))
    def test_number5_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_23e4.567", "123e4,.,567,<EOF>", 115))
    def test_string1_identifier(self): 
        """test indentifiers"""
        self.assertTrue(TestLexer.test("abc\t", "abc,<EOF>", 116))
    def test_string2_identifier(self): 
        """test indentifiers"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """, "He asked me: \"Where is John?\",<EOF>", 117))
    def test_arrlit(self): 
        """test indentifiers"""
        self.assertTrue(TestLexer.test("55.", "55.,<EOF>", 118))
    def test_int_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1__72", "1,__72,<EOF>", 119))
    def test_unclosedString_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Where is the love\" ", "Where,is,the,love,Unclosed String:  ", 120))
    def test_unclosedString_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(" \"Where is the love", "Unclosed String: Where is the love", 121))
    def test_illegalEscape_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(" \"Where is the love", "Unclosed String: Where is the love", 122))
    def test_float2_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("__", "__,<EOF>", 123))
    def test_int1_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_7_2", "172,<EOF>", 124))
    def test_float5(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_7_2.33", "172.33,<EOF>", 125))
    def test_float6(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("1__72.33", "1,__72,Error Token .", 126))
    def test_float7111(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("1e7","1e7,<EOF>", 127))
    def test_int3(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("1_72_","1,__72,Error Token .", 128))
    def test_int4(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("1ee72","1,ee72,<EOF>", 129))
    def test_comment1(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("/* A C-style comment */","<EOF>", 130))
    def test_comment2(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("// A C++ style comment","<EOF>", 131))
    def test_comment3(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc // A C++ style comment","abc,<EOF>", 132))
    def test_comment4(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("123 // A C++ style comment","123,<EOF>", 133))
    def test_comment5(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc /* A C-style comment */","abc,<EOF>", 134))
    def test_comment6(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("123 /* A C-style comment */","123,<EOF>", 135))
    def test_comment7(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("// Bao thu? /* Bao thu? */","<EOF>", 136))
    def test_comment8(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("12_37 /* A C-style comment */","1237,<EOF>", 137))
    def test_comment9(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("true // A C-style comment ","true,<EOF>", 138))
    def test_comment10(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test(" \" Xin chao Viet Nam \" // A C-style comment ","\" Xin chao Viet Nam \",<EOF>", 139))
    def test_string2(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \t" """," \"This is a string containing tab\",<EOF>", 140))    
    def test_array1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("array [2, 3] of integer", "array [2, 3] of integer, <EOF>",141))
    def test_ilegalString1(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test(" \"This is a string containing tab \t", "Illegal Escape In String: This is a string containing tab \t",142))
    def test_ilegalString2(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test(" \"This is a string containing \" tab \" ", "Illegal Escape In String: This is a string containing \" tab",143))
    def test_ilegalString3(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test(" \"This is a string containing \n tab \" ", "Illegal Escape In String: This is a string containing \" tab",144))
    def test_float7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1ee72", "1,ee72, <EOF>",145))
    def test_bool(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("true", "true, <EOF>",146))
    def test_boolint(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("1true", "1,true, <EOF>",147))
    def test_boolbool(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("truefalse", "truefalse,<EOF>",148))
    def test_float8eee(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("172..47", "172.,Error Token .",149))
    def test_float8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "hello my fen \\t \\n"  ""","hello my fen \\t \\n,<EOF>",150))
    def test_float9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(""" "hello my fen \\" hi"  ""","""hello my fen \\" hi,<EOF>""",151))
    def test_float9(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \t"  ""","""This is a string containing tab \t,<EOF>""",152))
    def test_floatt10(self):
        self.assertTrue(TestLexer.test(""" "This is a \\\\string\'containing tab \'"  ""","""This is a \\\\string\'containing tab \',<EOF>""",153))
    def test_floa10(self):
       self.assertTrue(TestLexer.test(""" "This is a \" \\\\string\'containing tab \'"  ""","""This is a \" \\\\string\'containing tab \',<EOF>""",154))       
    def test_float11(self):
        self.assertTrue(TestLexer.test("""porter/*nuture*/robinson""","""porterrobinson,<EOF>""",155))
    def test_string5(self):
         self.assertTrue(TestLexer.test(""" "Hello, World\n" ""","""Hello, World,<EOF>""",156))
    def test_float12222(self): 
         self.assertTrue(TestLexer.test(".E-10","""Hello, World,<EOF>""",157))
    def test_float12(self): 
         self.assertTrue(TestLexer.test("delta: integer = 32;","delta: integer = 32;,<EOF>""",158))
    def test_integer12(self): 
         self.assertTrue(TestLexer.test("0","0,<EOF>",159)) 
    def test_float13(self): 
        self.assertTrue(TestLexer.test("1e-10","1e-10,<EOF>",160))
    def test_float14(self): 
        self.assertTrue(TestLexer.test(" \"a\"::\"b\"","\"a\"::\"b\",<EOF>",161))
    def test_float77(self): 
        self.assertTrue(TestLexer.test("." ,".<EOF>",162))
    def test_stringID(self): 
        self.assertTrue(TestLexer.test("abcd\"abcd\"" ,"abcd,\"abcd\",<EOF>",163))
    def test_stringint(self): 
        self.assertTrue(TestLexer.test("123\"abcd\"" ,"123,\"abcd\",<EOF>",164))
    def test_float78(self): 
        self.assertTrue(TestLexer.test("123_44.12_75" ,"12344.12,_75,<EOF>",165))
    def test_float15(self): 
        self.assertTrue(TestLexer.test("123_44.12.75" ,"12344.12,Error Token .",166))
    def test_int16(self): 
        self.assertTrue(TestLexer.test("123_44_77e" ,"1234477,e,<EOF>",167))
    def test_float17(self): 
        self.assertTrue(TestLexer.test("123_44_77e7" ,"1234477e7,<EOF>",168))
    def test_string20(self): 
        self.assertTrue(TestLexer.test("\"Hello World \\t\"" ,"1234477e7,<EOF>",169))
    def test_string21(self): 
        self.assertTrue(TestLexer.test("\"Hello World \\b\"" ,"1234477e7,<EOF>",170))
    def test_string22(self): 
        self.assertTrue(TestLexer.test("\"Hello World \\f\"" ,"1234477e7,<EOF>",171))
    def test_string23(self): 
        self.assertTrue(TestLexer.test("\"Hello World \\r\"" ,"1234477e7,<EOF>",172))
    def test_string24(self): 
        self.assertTrue(TestLexer.test("\"Hello World \\n\"" ,"1234477e7,<EOF>",173))
    def test_string25(self): 
        self.assertTrue(TestLexer.test("\"Hello World \\\\\"" ,"1234477e7,<EOF>",174))
    def test_string26(self): 
        self.assertTrue(TestLexer.test("\"Hello World \\\\\"" ,"1234477e7,<EOF>",175))
    def test_stringfloat(self): 
        self.assertTrue(TestLexer.test("12_34.99\"abc\"rebelneverdie" ,"1234.99,\"abc\",rebelneverdie,<EOF>",176))
    def test_mixedString1(self):
        input = """"x = -3"""
        expect = ",=,-,3,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 177))
    def test_mixedString2(self): 
        self.assertTrue(TestLexer.test("<identifer-list>: <type> [= <expression-list>]?;" ,"1234.99,\"abc\",rebelneverdie,<EOF>",178))
    def test_stringfloat3(self): 
        self.assertTrue(TestLexer.test("\"main : function void ( )\"" ,"1234.99,\"abc\",rebelneverdie,<EOF>",179))
    def test_stringfloat4(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",180))
    def test_stringfloat43(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",181))
    def test_stringfloat411(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",182))
    def test_stringfloat4111(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",183))
    def test_stringfloat41111(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",184))
    def test_stringfloat4121212(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",185))
    def test_stringfloat42212(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",186))
    def test_stringfloat4133(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",187))
    def test_stringfloat434(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",188))
    def test_stringfloat47(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",189))
    def test_stringfloat48(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",190))
    def test_stringfloat49(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",191))
    def test_stringfloat499(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",192))
    def test_stringfloat4999(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",193))
    def test_stringfloat49999(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",194))
    def test_stringfloat50(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",195))
    def test_stringfloat51(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",196))
    def test_stringfloat555(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",197))
    def test_stringfloat443343(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",198))
    def test_stringfloat44434(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",199))
    def test_stringfloat32334(self): 
        self.assertTrue(TestLexer.test("1722a.bc" ,"1234.99,\"abc\",rebelneverdie,<EOF>",200))
# py run.py test LexerSuite
# py run.py test ParserSuite
# py run.py gen