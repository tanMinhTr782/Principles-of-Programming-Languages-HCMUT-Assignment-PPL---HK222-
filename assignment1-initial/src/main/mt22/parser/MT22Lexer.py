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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<")
        buf.write("\u01c4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\5\2")
        buf.write("\u0086\n\2\3\2\6\2\u0089\n\2\r\2\16\2\u008a\3\3\3\3\6")
        buf.write("\3\u008f\n\3\r\3\16\3\u0090\3\4\3\4\5\4\u0095\n\4\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\7\5\7\u009f\n\7\3\b\3\b\5\b")
        buf.write("\u00a3\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u00b1\n\t\5\t\u00b3\n\t\3\t\3\t\3\n\3\n\3\n\5")
        buf.write("\n\u00ba\n\n\3\n\7\n\u00bd\n\n\f\n\16\n\u00c0\13\n\3\n")
        buf.write("\5\n\u00c3\n\n\3\13\3\13\7\13\u00c7\n\13\f\13\16\13\u00ca")
        buf.write("\13\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\7!\u014e\n!\f!\16!\u0151\13!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\7\"\u0159\n\"\f\"\16\"\u015c\13\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3#\3#\7#\u0165\n#\f#\16#\u0168\13")
        buf.write("#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3")
        buf.write("<\3=\3=\3>\6>\u01a6\n>\r>\16>\u01a7\3>\3>\3?\3?\7?\u01ae")
        buf.write("\n?\f?\16?\u01b1\13?\3?\5?\u01b4\n?\3?\3?\3@\3@\7@\u01ba")
        buf.write("\n@\f@\16@\u01bd\13@\3@\3@\3@\3A\3A\3A\3\u015a\2B\3\2")
        buf.write("\5\2\7\2\t\2\13\2\r\2\17\3\21\4\23\5\25\6\27\7\31\b\33")
        buf.write("\t\35\n\37\13!\f#\r%\16\'\17)\20+\21-\22/\23\61\24\63")
        buf.write("\25\65\26\67\279\30;\31=\32?\33A\34C\35E\36G\37I K!M\"")
        buf.write("O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61m\62o\63q\64s\65u\66")
        buf.write("w\67y8{9}:\177;\u0081<\3\2\r\4\2GGgg\4\2--//\3\2\62;\6")
        buf.write("\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\3\2\63;\4\2\f\f\17")
        buf.write("\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\6\3\n")
        buf.write("\f\16\17$$^^\2\u01d1\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
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
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083")
        buf.write("\3\2\2\2\5\u008c\3\2\2\2\7\u0094\3\2\2\2\t\u0096\3\2\2")
        buf.write("\2\13\u0099\3\2\2\2\r\u009e\3\2\2\2\17\u00a2\3\2\2\2\21")
        buf.write("\u00b2\3\2\2\2\23\u00c2\3\2\2\2\25\u00c4\3\2\2\2\27\u00ce")
        buf.write("\3\2\2\2\31\u00d6\3\2\2\2\33\u00db\3\2\2\2\35\u00e1\3")
        buf.write("\2\2\2\37\u00e9\3\2\2\2!\u00f0\3\2\2\2#\u00f5\3\2\2\2")
        buf.write("%\u00f8\3\2\2\2\'\u00fe\3\2\2\2)\u0106\3\2\2\2+\u010f")
        buf.write("\3\2\2\2-\u0112\3\2\2\2/\u0117\3\2\2\2\61\u011d\3\2\2")
        buf.write("\2\63\u0124\3\2\2\2\65\u0128\3\2\2\2\67\u012c\3\2\2\2")
        buf.write("9\u0135\3\2\2\2;\u0138\3\2\2\2=\u013e\3\2\2\2?\u0143\3")
        buf.write("\2\2\2A\u0149\3\2\2\2C\u0154\3\2\2\2E\u0162\3\2\2\2G\u0169")
        buf.write("\3\2\2\2I\u016b\3\2\2\2K\u016d\3\2\2\2M\u016f\3\2\2\2")
        buf.write("O\u0171\3\2\2\2Q\u0173\3\2\2\2S\u0175\3\2\2\2U\u0177\3")
        buf.write("\2\2\2W\u0179\3\2\2\2Y\u017b\3\2\2\2[\u017d\3\2\2\2]\u017f")
        buf.write("\3\2\2\2_\u0181\3\2\2\2a\u0183\3\2\2\2c\u0185\3\2\2\2")
        buf.write("e\u0187\3\2\2\2g\u0189\3\2\2\2i\u018c\3\2\2\2k\u018f\3")
        buf.write("\2\2\2m\u0192\3\2\2\2o\u0195\3\2\2\2q\u0197\3\2\2\2s\u0199")
        buf.write("\3\2\2\2u\u019c\3\2\2\2w\u019f\3\2\2\2y\u01a2\3\2\2\2")
        buf.write("{\u01a5\3\2\2\2}\u01ab\3\2\2\2\177\u01b7\3\2\2\2\u0081")
        buf.write("\u01c1\3\2\2\2\u0083\u0085\t\2\2\2\u0084\u0086\t\3\2\2")
        buf.write("\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0088\3")
        buf.write("\2\2\2\u0087\u0089\t\4\2\2\u0088\u0087\3\2\2\2\u0089\u008a")
        buf.write("\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\4\3\2\2\2\u008c\u008e\7\60\2\2\u008d\u008f\t\4\2\2\u008e")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u008e\3\2\2\2")
        buf.write("\u0090\u0091\3\2\2\2\u0091\6\3\2\2\2\u0092\u0095\n\5\2")
        buf.write("\2\u0093\u0095\5\t\5\2\u0094\u0092\3\2\2\2\u0094\u0093")
        buf.write("\3\2\2\2\u0095\b\3\2\2\2\u0096\u0097\7^\2\2\u0097\u0098")
        buf.write("\t\6\2\2\u0098\n\3\2\2\2\u0099\u009a\7$\2\2\u009a\f\3")
        buf.write("\2\2\2\u009b\u009c\7^\2\2\u009c\u009f\n\6\2\2\u009d\u009f")
        buf.write("\7^\2\2\u009e\u009b\3\2\2\2\u009e\u009d\3\2\2\2\u009f")
        buf.write("\16\3\2\2\2\u00a0\u00a3\5=\37\2\u00a1\u00a3\5? \2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\20\3\2\2\2\u00a4")
        buf.write("\u00a5\5\23\n\2\u00a5\u00a6\5\5\3\2\u00a6\u00b3\3\2\2")
        buf.write("\2\u00a7\u00a8\5\23\n\2\u00a8\u00a9\5\5\3\2\u00a9\u00aa")
        buf.write("\5\3\2\2\u00aa\u00b3\3\2\2\2\u00ab\u00ac\5\23\n\2\u00ac")
        buf.write("\u00ad\5\3\2\2\u00ad\u00b3\3\2\2\2\u00ae\u00b0\5\5\3\2")
        buf.write("\u00af\u00b1\5\3\2\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3")
        buf.write("\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00a4\3\2\2\2\u00b2\u00a7")
        buf.write("\3\2\2\2\u00b2\u00ab\3\2\2\2\u00b2\u00ae\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00b5\b\t\2\2\u00b5\22\3\2\2\2\u00b6")
        buf.write("\u00c3\7\62\2\2\u00b7\u00be\t\7\2\2\u00b8\u00ba\7a\2\2")
        buf.write("\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3")
        buf.write("\2\2\2\u00bb\u00bd\t\4\2\2\u00bc\u00b9\3\2\2\2\u00bd\u00c0")
        buf.write("\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("\u00c1\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c3\b\n\3\2")
        buf.write("\u00c2\u00b6\3\2\2\2\u00c2\u00b7\3\2\2\2\u00c3\24\3\2")
        buf.write("\2\2\u00c4\u00c8\5\13\6\2\u00c5\u00c7\5\7\4\2\u00c6\u00c5")
        buf.write("\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write("\u00cb\u00cc\5\13\6\2\u00cc\u00cd\b\13\4\2\u00cd\26\3")
        buf.write("\2\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7i\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7t\2\2\u00d5\30\3\2\2\2\u00d6\u00d7")
        buf.write("\7x\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9\7k\2\2\u00d9\u00da")
        buf.write("\7f\2\2\u00da\32\3\2\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd")
        buf.write("\7n\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7c\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0\34\3\2\2\2\u00e1\u00e2\7d\2\2\u00e2\u00e3")
        buf.write("\7q\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6")
        buf.write("\7g\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8\7p\2\2\u00e8\36")
        buf.write("\3\2\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7i\2\2\u00ef \3\2\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2")
        buf.write("\7w\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4\7q\2\2\u00f4\"")
        buf.write("\3\2\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7h\2\2\u00f7$")
        buf.write("\3\2\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7t\2\2\u00fb\u00fc\7c\2\2\u00fc\u00fd\7{\2\2\u00fd&\3")
        buf.write("\2\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101")
        buf.write("\7j\2\2\u0101\u0102\7g\2\2\u0102\u0103\7t\2\2\u0103\u0104")
        buf.write("\7k\2\2\u0104\u0105\7v\2\2\u0105(\3\2\2\2\u0106\u0107")
        buf.write("\7h\2\2\u0107\u0108\7w\2\2\u0108\u0109\7p\2\2\u0109\u010a")
        buf.write("\7e\2\2\u010a\u010b\7v\2\2\u010b\u010c\7k\2\2\u010c\u010d")
        buf.write("\7q\2\2\u010d\u010e\7p\2\2\u010e*\3\2\2\2\u010f\u0110")
        buf.write("\7k\2\2\u0110\u0111\7h\2\2\u0111,\3\2\2\2\u0112\u0113")
        buf.write("\7g\2\2\u0113\u0114\7n\2\2\u0114\u0115\7u\2\2\u0115\u0116")
        buf.write("\7g\2\2\u0116.\3\2\2\2\u0117\u0118\7d\2\2\u0118\u0119")
        buf.write("\7t\2\2\u0119\u011a\7g\2\2\u011a\u011b\7c\2\2\u011b\u011c")
        buf.write("\7m\2\2\u011c\60\3\2\2\2\u011d\u011e\7t\2\2\u011e\u011f")
        buf.write("\7g\2\2\u011f\u0120\7v\2\2\u0120\u0121\7w\2\2\u0121\u0122")
        buf.write("\7t\2\2\u0122\u0123\7p\2\2\u0123\62\3\2\2\2\u0124\u0125")
        buf.write("\7q\2\2\u0125\u0126\7w\2\2\u0126\u0127\7v\2\2\u0127\64")
        buf.write("\3\2\2\2\u0128\u0129\7h\2\2\u0129\u012a\7q\2\2\u012a\u012b")
        buf.write("\7t\2\2\u012b\66\3\2\2\2\u012c\u012d\7e\2\2\u012d\u012e")
        buf.write("\7q\2\2\u012e\u012f\7p\2\2\u012f\u0130\7v\2\2\u0130\u0131")
        buf.write("\7k\2\2\u0131\u0132\7p\2\2\u0132\u0133\7w\2\2\u0133\u0134")
        buf.write("\7g\2\2\u01348\3\2\2\2\u0135\u0136\7f\2\2\u0136\u0137")
        buf.write("\7q\2\2\u0137:\3\2\2\2\u0138\u0139\7y\2\2\u0139\u013a")
        buf.write("\7j\2\2\u013a\u013b\7k\2\2\u013b\u013c\7n\2\2\u013c\u013d")
        buf.write("\7g\2\2\u013d<\3\2\2\2\u013e\u013f\7v\2\2\u013f\u0140")
        buf.write("\7t\2\2\u0140\u0141\7w\2\2\u0141\u0142\7g\2\2\u0142>\3")
        buf.write("\2\2\2\u0143\u0144\7h\2\2\u0144\u0145\7c\2\2\u0145\u0146")
        buf.write("\7n\2\2\u0146\u0147\7u\2\2\u0147\u0148\7g\2\2\u0148@\3")
        buf.write("\2\2\2\u0149\u014a\7\61\2\2\u014a\u014b\7\61\2\2\u014b")
        buf.write("\u014f\3\2\2\2\u014c\u014e\n\b\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153")
        buf.write("\b!\5\2\u0153B\3\2\2\2\u0154\u0155\7\61\2\2\u0155\u0156")
        buf.write("\7,\2\2\u0156\u015a\3\2\2\2\u0157\u0159\13\2\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u015a\3")
        buf.write("\2\2\2\u015d\u015e\7,\2\2\u015e\u015f\7\61\2\2\u015f\u0160")
        buf.write("\3\2\2\2\u0160\u0161\b\"\5\2\u0161D\3\2\2\2\u0162\u0166")
        buf.write("\t\t\2\2\u0163\u0165\t\n\2\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write("\u0167F\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016a\7*\2\2")
        buf.write("\u016aH\3\2\2\2\u016b\u016c\7+\2\2\u016cJ\3\2\2\2\u016d")
        buf.write("\u016e\7]\2\2\u016eL\3\2\2\2\u016f\u0170\7_\2\2\u0170")
        buf.write("N\3\2\2\2\u0171\u0172\7\60\2\2\u0172P\3\2\2\2\u0173\u0174")
        buf.write("\7.\2\2\u0174R\3\2\2\2\u0175\u0176\7=\2\2\u0176T\3\2\2")
        buf.write("\2\u0177\u0178\7<\2\2\u0178V\3\2\2\2\u0179\u017a\7}\2")
        buf.write("\2\u017aX\3\2\2\2\u017b\u017c\7\177\2\2\u017cZ\3\2\2\2")
        buf.write("\u017d\u017e\7-\2\2\u017e\\\3\2\2\2\u017f\u0180\7/\2\2")
        buf.write("\u0180^\3\2\2\2\u0181\u0182\7,\2\2\u0182`\3\2\2\2\u0183")
        buf.write("\u0184\7\61\2\2\u0184b\3\2\2\2\u0185\u0186\7\'\2\2\u0186")
        buf.write("d\3\2\2\2\u0187\u0188\7#\2\2\u0188f\3\2\2\2\u0189\u018a")
        buf.write("\7(\2\2\u018a\u018b\7(\2\2\u018bh\3\2\2\2\u018c\u018d")
        buf.write("\7~\2\2\u018d\u018e\7~\2\2\u018ej\3\2\2\2\u018f\u0190")
        buf.write("\7?\2\2\u0190\u0191\7?\2\2\u0191l\3\2\2\2\u0192\u0193")
        buf.write("\7#\2\2\u0193\u0194\7?\2\2\u0194n\3\2\2\2\u0195\u0196")
        buf.write("\7>\2\2\u0196p\3\2\2\2\u0197\u0198\7@\2\2\u0198r\3\2\2")
        buf.write("\2\u0199\u019a\7>\2\2\u019a\u019b\7?\2\2\u019bt\3\2\2")
        buf.write("\2\u019c\u019d\7@\2\2\u019d\u019e\7?\2\2\u019ev\3\2\2")
        buf.write("\2\u019f\u01a0\7<\2\2\u01a0\u01a1\7<\2\2\u01a1x\3\2\2")
        buf.write("\2\u01a2\u01a3\7?\2\2\u01a3z\3\2\2\2\u01a4\u01a6\t\13")
        buf.write("\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01aa\b>\5\2\u01aa|\3\2\2\2\u01ab\u01af\5\13\6\2\u01ac")
        buf.write("\u01ae\5\7\4\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2")
        buf.write("\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b3\3")
        buf.write("\2\2\2\u01b1\u01af\3\2\2\2\u01b2\u01b4\t\f\2\2\u01b3\u01b2")
        buf.write("\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\b?\6\2\u01b6")
        buf.write("~\3\2\2\2\u01b7\u01bb\5\13\6\2\u01b8\u01ba\5\7\4\2\u01b9")
        buf.write("\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2")
        buf.write("\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3")
        buf.write("\2\2\2\u01be\u01bf\5\r\7\2\u01bf\u01c0\b@\7\2\u01c0\u0080")
        buf.write("\3\2\2\2\u01c1\u01c2\13\2\2\2\u01c2\u01c3\bA\b\2\u01c3")
        buf.write("\u0082\3\2\2\2\26\2\u0085\u008a\u0090\u0094\u009e\u00a2")
        buf.write("\u00b0\u00b2\u00b9\u00be\u00c2\u00c8\u014f\u015a\u0166")
        buf.write("\u01a7\u01af\u01b3\u01bb\t\3\t\2\3\n\3\3\13\4\b\2\2\3")
        buf.write("?\5\3@\6\3A\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLLIT = 1
    FLOATLIT = 2
    INTLIT = 3
    STRINGLIT = 4
    INTEGER = 5
    VOID = 6
    FLOAT = 7
    BOOLEAN = 8
    STRING = 9
    AUTO = 10
    OF = 11
    ARR = 12
    INHERIT = 13
    FUNCTION = 14
    IF = 15
    ELSE = 16
    BREAK = 17
    RETURN = 18
    OUT = 19
    FOR = 20
    CONTINUE = 21
    DO = 22
    WHILE = 23
    TRUE = 24
    FALSE = 25
    COMMENT = 26
    C_COMMENT = 27
    ID = 28
    LB = 29
    RB = 30
    SQLB = 31
    SQRB = 32
    DOT = 33
    COMMA = 34
    SEMI = 35
    COLON = 36
    LCB = 37
    RCB = 38
    ADD = 39
    MINUS = 40
    MUL = 41
    DIV = 42
    PCENT = 43
    NOT = 44
    AND = 45
    OR = 46
    SAME = 47
    NOTSAME = 48
    LOWER = 49
    HIGHER = 50
    LOWER_EQ = 51
    HIGHER_EQ = 52
    SCOPE = 53
    EQ = 54
    WS = 55
    UNCLOSE_STRING = 56
    ILLEGAL_ESCAPE = 57
    ERROR_CHAR = 58

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'integer'", "'void'", "'float'", "'boolean'", "'string'", "'auto'", 
            "'of'", "'array'", "'inherit'", "'function'", "'if'", "'else'", 
            "'break'", "'return'", "'out'", "'for'", "'continue'", "'do'", 
            "'while'", "'true'", "'false'", "'('", "')'", "'['", "']'", 
            "'.'", "','", "';'", "':'", "'{'", "'}'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
            "'>'", "'<='", "'>='", "'::'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "FLOATLIT", "INTLIT", "STRINGLIT", "INTEGER", "VOID", 
            "FLOAT", "BOOLEAN", "STRING", "AUTO", "OF", "ARR", "INHERIT", 
            "FUNCTION", "IF", "ELSE", "BREAK", "RETURN", "OUT", "FOR", "CONTINUE", 
            "DO", "WHILE", "TRUE", "FALSE", "COMMENT", "C_COMMENT", "ID", 
            "LB", "RB", "SQLB", "SQRB", "DOT", "COMMA", "SEMI", "COLON", 
            "LCB", "RCB", "ADD", "MINUS", "MUL", "DIV", "PCENT", "NOT", 
            "AND", "OR", "SAME", "NOTSAME", "LOWER", "HIGHER", "LOWER_EQ", 
            "HIGHER_EQ", "SCOPE", "EQ", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "EXPPART", "DECPART", "StringChar", "ESC2", "DOUBLEQ", 
                  "IllegalString", "BOOLLIT", "FLOATLIT", "INTLIT", "STRINGLIT", 
                  "INTEGER", "VOID", "FLOAT", "BOOLEAN", "STRING", "AUTO", 
                  "OF", "ARR", "INHERIT", "FUNCTION", "IF", "ELSE", "BREAK", 
                  "RETURN", "OUT", "FOR", "CONTINUE", "DO", "WHILE", "TRUE", 
                  "FALSE", "COMMENT", "C_COMMENT", "ID", "LB", "RB", "SQLB", 
                  "SQRB", "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", 
                  "ADD", "MINUS", "MUL", "DIV", "PCENT", "NOT", "AND", "OR", 
                  "SAME", "NOTSAME", "LOWER", "HIGHER", "LOWER_EQ", "HIGHER_EQ", 
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
            actions[7] = self.FLOATLIT_action 
            actions[8] = self.INTLIT_action 
            actions[9] = self.STRINGLIT_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_CHAR_action 
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
                
     


