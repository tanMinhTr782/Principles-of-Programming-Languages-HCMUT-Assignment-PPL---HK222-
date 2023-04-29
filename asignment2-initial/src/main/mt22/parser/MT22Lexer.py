# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
  



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01e7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\5\2\u008e\n\2\3\2\6\2\u0091\n\2")
        buf.write("\r\2\16\2\u0092\3\3\3\3\3\4\3\4\6\4\u0099\n\4\r\4\16\4")
        buf.write("\u009a\3\5\3\5\5\5\u009f\n\5\3\6\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\b\5\b\u00a9\n\b\3\t\3\t\5\t\u00ad\n\t\3\n\3\n\5\n")
        buf.write("\u00b1\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u00bf\n\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00c7\n\13\3\13\3\13\3\f\3\f\3\f\5\f\u00ce")
        buf.write("\n\f\3\f\7\f\u00d1\n\f\f\f\16\f\u00d4\13\f\3\f\5\f\u00d7")
        buf.write("\n\f\3\r\3\r\7\r\u00db\n\r\f\r\16\r\u00de\13\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\7#\u0162\n#\f#\16#\u0165\13#\3#\3#\3$\3$\3$\3$\7$\u016d")
        buf.write("\n$\f$\16$\u0170\13$\3$\3$\3$\3$\3$\3%\3%\7%\u0179\n%")
        buf.write("\f%\16%\u017c\13%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3/\5/\u0193\n/\3\60\3\60\5\60")
        buf.write("\u0197\n\60\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u019f\n")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3")
        buf.write("=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3B\6B\u01c9\nB\r")
        buf.write("B\16B\u01ca\3B\3B\3C\3C\7C\u01d1\nC\fC\16C\u01d4\13C\3")
        buf.write("C\5C\u01d7\nC\3C\3C\3D\3D\7D\u01dd\nD\fD\16D\u01e0\13")
        buf.write("D\3D\3D\3D\3E\3E\3E\3\u016e\2F\3\2\5\2\7\2\t\2\13\2\r")
        buf.write("\2\17\2\21\3\23\4\25\5\27\6\31\7\33\b\35\t\37\n!\13#\f")
        buf.write("%\r\'\16)\17+\20-\21/\22\61\23\63\24\65\25\67\269\27;")
        buf.write("\30=\31?\32A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(])")
        buf.write("_*a+c,e-g.i/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177:")
        buf.write("\u0081;\u0083<\u0085=\u0087>\u0089?\3\2\r\4\2GGgg\4\2")
        buf.write("--//\3\2\62;\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\3\2\63")
        buf.write(";\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17")
        buf.write("\17\"\"\6\3\n\f\16\17$$^^\2\u01fe\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\3\u008b\3\2\2\2\5\u0094\3\2\2\2\7\u0096\3\2\2\2\t\u009e")
        buf.write("\3\2\2\2\13\u00a0\3\2\2\2\r\u00a3\3\2\2\2\17\u00a8\3\2")
        buf.write("\2\2\21\u00ac\3\2\2\2\23\u00b0\3\2\2\2\25\u00c6\3\2\2")
        buf.write("\2\27\u00d6\3\2\2\2\31\u00d8\3\2\2\2\33\u00e2\3\2\2\2")
        buf.write("\35\u00ea\3\2\2\2\37\u00ef\3\2\2\2!\u00f5\3\2\2\2#\u00fd")
        buf.write("\3\2\2\2%\u0104\3\2\2\2\'\u0109\3\2\2\2)\u010c\3\2\2\2")
        buf.write("+\u0112\3\2\2\2-\u011a\3\2\2\2/\u0123\3\2\2\2\61\u0126")
        buf.write("\3\2\2\2\63\u012b\3\2\2\2\65\u0131\3\2\2\2\67\u0138\3")
        buf.write("\2\2\29\u013c\3\2\2\2;\u0140\3\2\2\2=\u0149\3\2\2\2?\u014c")
        buf.write("\3\2\2\2A\u0152\3\2\2\2C\u0157\3\2\2\2E\u015d\3\2\2\2")
        buf.write("G\u0168\3\2\2\2I\u0176\3\2\2\2K\u017d\3\2\2\2M\u017f\3")
        buf.write("\2\2\2O\u0181\3\2\2\2Q\u0183\3\2\2\2S\u0185\3\2\2\2U\u0187")
        buf.write("\3\2\2\2W\u0189\3\2\2\2Y\u018b\3\2\2\2[\u018d\3\2\2\2")
        buf.write("]\u0192\3\2\2\2_\u0196\3\2\2\2a\u019e\3\2\2\2c\u01a0\3")
        buf.write("\2\2\2e\u01a2\3\2\2\2g\u01a4\3\2\2\2i\u01a6\3\2\2\2k\u01a8")
        buf.write("\3\2\2\2m\u01aa\3\2\2\2o\u01ac\3\2\2\2q\u01af\3\2\2\2")
        buf.write("s\u01b2\3\2\2\2u\u01b5\3\2\2\2w\u01b8\3\2\2\2y\u01ba\3")
        buf.write("\2\2\2{\u01bc\3\2\2\2}\u01bf\3\2\2\2\177\u01c2\3\2\2\2")
        buf.write("\u0081\u01c5\3\2\2\2\u0083\u01c8\3\2\2\2\u0085\u01ce\3")
        buf.write("\2\2\2\u0087\u01da\3\2\2\2\u0089\u01e4\3\2\2\2\u008b\u008d")
        buf.write("\t\2\2\2\u008c\u008e\t\3\2\2\u008d\u008c\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u0091\t\4\2\2")
        buf.write("\u0090\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0090\3")
        buf.write("\2\2\2\u0092\u0093\3\2\2\2\u0093\4\3\2\2\2\u0094\u0095")
        buf.write("\7\60\2\2\u0095\6\3\2\2\2\u0096\u0098\5\5\3\2\u0097\u0099")
        buf.write("\t\4\2\2\u0098\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\b\3\2\2\2\u009c")
        buf.write("\u009f\n\5\2\2\u009d\u009f\5\13\6\2\u009e\u009c\3\2\2")
        buf.write("\2\u009e\u009d\3\2\2\2\u009f\n\3\2\2\2\u00a0\u00a1\7^")
        buf.write("\2\2\u00a1\u00a2\t\6\2\2\u00a2\f\3\2\2\2\u00a3\u00a4\7")
        buf.write("$\2\2\u00a4\16\3\2\2\2\u00a5\u00a6\7^\2\2\u00a6\u00a9")
        buf.write("\n\6\2\2\u00a7\u00a9\7^\2\2\u00a8\u00a5\3\2\2\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a9\20\3\2\2\2\u00aa\u00ad\5+\26\2\u00ab")
        buf.write("\u00ad\5\67\34\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab\3\2\2")
        buf.write("\2\u00ad\22\3\2\2\2\u00ae\u00b1\5A!\2\u00af\u00b1\5C\"")
        buf.write("\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\24\3")
        buf.write("\2\2\2\u00b2\u00b3\5\27\f\2\u00b3\u00b4\5\7\4\2\u00b4")
        buf.write("\u00c7\3\2\2\2\u00b5\u00b6\5\27\f\2\u00b6\u00b7\5\7\4")
        buf.write("\2\u00b7\u00b8\5\3\2\2\u00b8\u00c7\3\2\2\2\u00b9\u00ba")
        buf.write("\5\27\f\2\u00ba\u00bb\5\3\2\2\u00bb\u00c7\3\2\2\2\u00bc")
        buf.write("\u00be\5\7\4\2\u00bd\u00bf\5\3\2\2\u00be\u00bd\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\u00c7\3\2\2\2\u00c0\u00c1\5")
        buf.write("\27\f\2\u00c1\u00c2\5\5\3\2\u00c2\u00c7\3\2\2\2\u00c3")
        buf.write("\u00c4\5\5\3\2\u00c4\u00c5\5\3\2\2\u00c5\u00c7\3\2\2\2")
        buf.write("\u00c6\u00b2\3\2\2\2\u00c6\u00b5\3\2\2\2\u00c6\u00b9\3")
        buf.write("\2\2\2\u00c6\u00bc\3\2\2\2\u00c6\u00c0\3\2\2\2\u00c6\u00c3")
        buf.write("\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\b\13\2\2\u00c9")
        buf.write("\26\3\2\2\2\u00ca\u00d7\7\62\2\2\u00cb\u00d2\t\7\2\2\u00cc")
        buf.write("\u00ce\7a\2\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\u00d1\t\4\2\2\u00d0\u00cd\3")
        buf.write("\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5")
        buf.write("\u00d7\b\f\3\2\u00d6\u00ca\3\2\2\2\u00d6\u00cb\3\2\2\2")
        buf.write("\u00d7\30\3\2\2\2\u00d8\u00dc\5\r\7\2\u00d9\u00db\5\t")
        buf.write("\5\2\u00da\u00d9\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00df\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00df\u00e0\5\r\7\2\u00e0\u00e1\b\r\4\2")
        buf.write("\u00e1\32\3\2\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7p\2")
        buf.write("\2\u00e4\u00e5\7v\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7")
        buf.write("i\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9\7t\2\2\u00e9\34\3")
        buf.write("\2\2\2\u00ea\u00eb\7x\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7k\2\2\u00ed\u00ee\7f\2\2\u00ee\36\3\2\2\2\u00ef\u00f0")
        buf.write("\7h\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3")
        buf.write("\7c\2\2\u00f3\u00f4\7v\2\2\u00f4 \3\2\2\2\u00f5\u00f6")
        buf.write("\7d\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9")
        buf.write("\7n\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7p\2\2\u00fc\"\3\2\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7k\2\2\u0101\u0102")
        buf.write("\7p\2\2\u0102\u0103\7i\2\2\u0103$\3\2\2\2\u0104\u0105")
        buf.write("\7c\2\2\u0105\u0106\7w\2\2\u0106\u0107\7v\2\2\u0107\u0108")
        buf.write("\7q\2\2\u0108&\3\2\2\2\u0109\u010a\7q\2\2\u010a\u010b")
        buf.write("\7h\2\2\u010b(\3\2\2\2\u010c\u010d\7c\2\2\u010d\u010e")
        buf.write("\7t\2\2\u010e\u010f\7t\2\2\u010f\u0110\7c\2\2\u0110\u0111")
        buf.write("\7{\2\2\u0111*\3\2\2\2\u0112\u0113\7k\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\u0115\7j\2\2\u0115\u0116\7g\2\2\u0116\u0117")
        buf.write("\7t\2\2\u0117\u0118\7k\2\2\u0118\u0119\7v\2\2\u0119,\3")
        buf.write("\2\2\2\u011a\u011b\7h\2\2\u011b\u011c\7w\2\2\u011c\u011d")
        buf.write("\7p\2\2\u011d\u011e\7e\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7k\2\2\u0120\u0121\7q\2\2\u0121\u0122\7p\2\2\u0122.\3")
        buf.write("\2\2\2\u0123\u0124\7k\2\2\u0124\u0125\7h\2\2\u0125\60")
        buf.write("\3\2\2\2\u0126\u0127\7g\2\2\u0127\u0128\7n\2\2\u0128\u0129")
        buf.write("\7u\2\2\u0129\u012a\7g\2\2\u012a\62\3\2\2\2\u012b\u012c")
        buf.write("\7d\2\2\u012c\u012d\7t\2\2\u012d\u012e\7g\2\2\u012e\u012f")
        buf.write("\7c\2\2\u012f\u0130\7m\2\2\u0130\64\3\2\2\2\u0131\u0132")
        buf.write("\7t\2\2\u0132\u0133\7g\2\2\u0133\u0134\7v\2\2\u0134\u0135")
        buf.write("\7w\2\2\u0135\u0136\7t\2\2\u0136\u0137\7p\2\2\u0137\66")
        buf.write("\3\2\2\2\u0138\u0139\7q\2\2\u0139\u013a\7w\2\2\u013a\u013b")
        buf.write("\7v\2\2\u013b8\3\2\2\2\u013c\u013d\7h\2\2\u013d\u013e")
        buf.write("\7q\2\2\u013e\u013f\7t\2\2\u013f:\3\2\2\2\u0140\u0141")
        buf.write("\7e\2\2\u0141\u0142\7q\2\2\u0142\u0143\7p\2\2\u0143\u0144")
        buf.write("\7v\2\2\u0144\u0145\7k\2\2\u0145\u0146\7p\2\2\u0146\u0147")
        buf.write("\7w\2\2\u0147\u0148\7g\2\2\u0148<\3\2\2\2\u0149\u014a")
        buf.write("\7f\2\2\u014a\u014b\7q\2\2\u014b>\3\2\2\2\u014c\u014d")
        buf.write("\7y\2\2\u014d\u014e\7j\2\2\u014e\u014f\7k\2\2\u014f\u0150")
        buf.write("\7n\2\2\u0150\u0151\7g\2\2\u0151@\3\2\2\2\u0152\u0153")
        buf.write("\7v\2\2\u0153\u0154\7t\2\2\u0154\u0155\7w\2\2\u0155\u0156")
        buf.write("\7g\2\2\u0156B\3\2\2\2\u0157\u0158\7h\2\2\u0158\u0159")
        buf.write("\7c\2\2\u0159\u015a\7n\2\2\u015a\u015b\7u\2\2\u015b\u015c")
        buf.write("\7g\2\2\u015cD\3\2\2\2\u015d\u015e\7\61\2\2\u015e\u015f")
        buf.write("\7\61\2\2\u015f\u0163\3\2\2\2\u0160\u0162\n\b\2\2\u0161")
        buf.write("\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u0163\3")
        buf.write("\2\2\2\u0166\u0167\b#\5\2\u0167F\3\2\2\2\u0168\u0169\7")
        buf.write("\61\2\2\u0169\u016a\7,\2\2\u016a\u016e\3\2\2\2\u016b\u016d")
        buf.write("\13\2\2\2\u016c\u016b\3\2\2\2\u016d\u0170\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0171\3\2\2\2")
        buf.write("\u0170\u016e\3\2\2\2\u0171\u0172\7,\2\2\u0172\u0173\7")
        buf.write("\61\2\2\u0173\u0174\3\2\2\2\u0174\u0175\b$\5\2\u0175H")
        buf.write("\3\2\2\2\u0176\u017a\t\t\2\2\u0177\u0179\t\n\2\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017bJ\3\2\2\2\u017c\u017a\3\2\2")
        buf.write("\2\u017d\u017e\7*\2\2\u017eL\3\2\2\2\u017f\u0180\7+\2")
        buf.write("\2\u0180N\3\2\2\2\u0181\u0182\7]\2\2\u0182P\3\2\2\2\u0183")
        buf.write("\u0184\7_\2\2\u0184R\3\2\2\2\u0185\u0186\7.\2\2\u0186")
        buf.write("T\3\2\2\2\u0187\u0188\7=\2\2\u0188V\3\2\2\2\u0189\u018a")
        buf.write("\7<\2\2\u018aX\3\2\2\2\u018b\u018c\7}\2\2\u018cZ\3\2\2")
        buf.write("\2\u018d\u018e\7\177\2\2\u018e\\\3\2\2\2\u018f\u0193\5")
        buf.write("g\64\2\u0190\u0193\5i\65\2\u0191\u0193\5k\66\2\u0192\u018f")
        buf.write("\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("^\3\2\2\2\u0194\u0197\5o8\2\u0195\u0197\5q9\2\u0196\u0194")
        buf.write("\3\2\2\2\u0196\u0195\3\2\2\2\u0197`\3\2\2\2\u0198\u019f")
        buf.write("\5s:\2\u0199\u019f\5u;\2\u019a\u019f\5y=\2\u019b\u019f")
        buf.write("\5}?\2\u019c\u019f\5w<\2\u019d\u019f\5{>\2\u019e\u0198")
        buf.write("\3\2\2\2\u019e\u0199\3\2\2\2\u019e\u019a\3\2\2\2\u019e")
        buf.write("\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d\3\2\2\2")
        buf.write("\u019fb\3\2\2\2\u01a0\u01a1\7-\2\2\u01a1d\3\2\2\2\u01a2")
        buf.write("\u01a3\7/\2\2\u01a3f\3\2\2\2\u01a4\u01a5\7,\2\2\u01a5")
        buf.write("h\3\2\2\2\u01a6\u01a7\7\61\2\2\u01a7j\3\2\2\2\u01a8\u01a9")
        buf.write("\7\'\2\2\u01a9l\3\2\2\2\u01aa\u01ab\7#\2\2\u01abn\3\2")
        buf.write("\2\2\u01ac\u01ad\7(\2\2\u01ad\u01ae\7(\2\2\u01aep\3\2")
        buf.write("\2\2\u01af\u01b0\7~\2\2\u01b0\u01b1\7~\2\2\u01b1r\3\2")
        buf.write("\2\2\u01b2\u01b3\7?\2\2\u01b3\u01b4\7?\2\2\u01b4t\3\2")
        buf.write("\2\2\u01b5\u01b6\7#\2\2\u01b6\u01b7\7?\2\2\u01b7v\3\2")
        buf.write("\2\2\u01b8\u01b9\7>\2\2\u01b9x\3\2\2\2\u01ba\u01bb\7@")
        buf.write("\2\2\u01bbz\3\2\2\2\u01bc\u01bd\7>\2\2\u01bd\u01be\7?")
        buf.write("\2\2\u01be|\3\2\2\2\u01bf\u01c0\7@\2\2\u01c0\u01c1\7?")
        buf.write("\2\2\u01c1~\3\2\2\2\u01c2\u01c3\7<\2\2\u01c3\u01c4\7<")
        buf.write("\2\2\u01c4\u0080\3\2\2\2\u01c5\u01c6\7?\2\2\u01c6\u0082")
        buf.write("\3\2\2\2\u01c7\u01c9\t\13\2\2\u01c8\u01c7\3\2\2\2\u01c9")
        buf.write("\u01ca\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01cc\u01cd\bB\5\2\u01cd\u0084\3")
        buf.write("\2\2\2\u01ce\u01d2\5\r\7\2\u01cf\u01d1\5\t\5\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d3\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d5\u01d7\t\f\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01d8\3")
        buf.write("\2\2\2\u01d8\u01d9\bC\6\2\u01d9\u0086\3\2\2\2\u01da\u01de")
        buf.write("\5\r\7\2\u01db\u01dd\5\t\5\2\u01dc\u01db\3\2\2\2\u01dd")
        buf.write("\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2")
        buf.write("\u01df\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e2\5")
        buf.write("\17\b\2\u01e2\u01e3\bD\7\2\u01e3\u0088\3\2\2\2\u01e4\u01e5")
        buf.write("\13\2\2\2\u01e5\u01e6\bE\b\2\u01e6\u008a\3\2\2\2\32\2")
        buf.write("\u008d\u0092\u009a\u009e\u00a8\u00ac\u00b0\u00be\u00c6")
        buf.write("\u00cd\u00d2\u00d6\u00dc\u0163\u016e\u017a\u0192\u0196")
        buf.write("\u019e\u01ca\u01d2\u01d6\u01de\t\3\13\2\3\f\3\3\r\4\b")
        buf.write("\2\2\3C\5\3D\6\3E\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PARAM_KEYWORDS = 1
    BOOLLIT = 2
    FLOATLIT = 3
    INTLIT = 4
    STRINGLIT = 5
    INTEGER = 6
    VOID = 7
    FLOAT = 8
    BOOLEAN = 9
    STRING = 10
    AUTO = 11
    OF = 12
    ARR = 13
    INHERIT = 14
    FUNCTION = 15
    IF = 16
    ELSE = 17
    BREAK = 18
    RETURN = 19
    OUT = 20
    FOR = 21
    CONTINUE = 22
    DO = 23
    WHILE = 24
    TRUE = 25
    FALSE = 26
    COMMENT = 27
    C_COMMENT = 28
    ID = 29
    LB = 30
    RB = 31
    SQLB = 32
    SQRB = 33
    COMMA = 34
    SEMI = 35
    COLON = 36
    LCB = 37
    RCB = 38
    MULDIVMOD = 39
    ANDOR = 40
    COMPARE = 41
    ADD = 42
    MINUS = 43
    MUL = 44
    DIV = 45
    PCENT = 46
    NOT = 47
    AND = 48
    OR = 49
    SAME = 50
    NOTSAME = 51
    LOWER = 52
    HIGHER = 53
    LOWER_EQ = 54
    HIGHER_EQ = 55
    SCOPE = 56
    EQ = 57
    WS = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'integer'", "'void'", "'float'", "'boolean'", "'string'", "'auto'", 
            "'of'", "'array'", "'inherit'", "'function'", "'if'", "'else'", 
            "'break'", "'return'", "'out'", "'for'", "'continue'", "'do'", 
            "'while'", "'true'", "'false'", "'('", "')'", "'['", "']'", 
            "','", "';'", "':'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'::'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "PARAM_KEYWORDS", "BOOLLIT", "FLOATLIT", "INTLIT", "STRINGLIT", 
            "INTEGER", "VOID", "FLOAT", "BOOLEAN", "STRING", "AUTO", "OF", 
            "ARR", "INHERIT", "FUNCTION", "IF", "ELSE", "BREAK", "RETURN", 
            "OUT", "FOR", "CONTINUE", "DO", "WHILE", "TRUE", "FALSE", "COMMENT", 
            "C_COMMENT", "ID", "LB", "RB", "SQLB", "SQRB", "COMMA", "SEMI", 
            "COLON", "LCB", "RCB", "MULDIVMOD", "ANDOR", "COMPARE", "ADD", 
            "MINUS", "MUL", "DIV", "PCENT", "NOT", "AND", "OR", "SAME", 
            "NOTSAME", "LOWER", "HIGHER", "LOWER_EQ", "HIGHER_EQ", "SCOPE", 
            "EQ", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "EXPPART", "DOT", "DECPART", "StringChar", "ESC2", "DOUBLEQ", 
                  "IllegalString", "PARAM_KEYWORDS", "BOOLLIT", "FLOATLIT", 
                  "INTLIT", "STRINGLIT", "INTEGER", "VOID", "FLOAT", "BOOLEAN", 
                  "STRING", "AUTO", "OF", "ARR", "INHERIT", "FUNCTION", 
                  "IF", "ELSE", "BREAK", "RETURN", "OUT", "FOR", "CONTINUE", 
                  "DO", "WHILE", "TRUE", "FALSE", "COMMENT", "C_COMMENT", 
                  "ID", "LB", "RB", "SQLB", "SQRB", "COMMA", "SEMI", "COLON", 
                  "LCB", "RCB", "MULDIVMOD", "ANDOR", "COMPARE", "ADD", 
                  "MINUS", "MUL", "DIV", "PCENT", "NOT", "AND", "OR", "SAME", 
                  "NOTSAME", "LOWER", "HIGHER", "LOWER_EQ", "HIGHER_EQ", 
                  "SCOPE", "EQ", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

      



    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[9] = self.FLOATLIT_action 
            actions[10] = self.INTLIT_action 
            actions[11] = self.STRINGLIT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    result = str(self.text)
                    self.text = result[1:-1]
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    unclose_str = str(self.text)
                    possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
                    if unclose_str[-1] in possible:
                        raise UncloseString(unclose_str[1:-1])
                    else:
                        raise UncloseString(unclose_str[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    illegal_str = str(self.text)
                    raise IllegalEscape(illegal_str[1:])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                    raise ErrorToken(self.text)
                
     


