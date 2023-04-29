# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u01a4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3r\n\3\3\4\3")
        buf.write("\4\5\4v\n\4\3\5\3\5\3\5\5\5{\n\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\5\n\u0091\n\n\3\13\3\13\5\13\u0095\n\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u00b2\n\20\3\21\3\21\3\21\3\21\5\21\u00b8\n")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u00c8\n\23\3\24\3\24\5\24\u00cc")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u00d3\n\25\3\26\3")
        buf.write("\26\5\26\u00d7\n\26\3\26\3\26\3\27\3\27\3\27\5\27\u00de")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\5\31\u00e7\n")
        buf.write("\31\3\32\3\32\3\32\3\32\5\32\u00ed\n\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u00f9\n\33\3")
        buf.write("\34\3\34\5\34\u00fd\n\34\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u010c\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\5\"\u012b\n\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\5\'\u0141\n\'\3(\3(\5(")
        buf.write("\u0145\n(\3)\3)\5)\u0149\n)\3*\3*\3*\3*\3*\5*\u0150\n")
        buf.write("*\3+\3+\3+\3+\3+\5+\u0157\n+\3,\3,\3,\3,\3,\5,\u015e\n")
        buf.write(",\3-\3-\3-\3-\3-\3-\7-\u0166\n-\f-\16-\u0169\13-\3.\3")
        buf.write(".\3.\3.\3.\3.\7.\u0171\n.\f.\16.\u0174\13.\3/\3/\3/\3")
        buf.write("/\3/\3/\7/\u017c\n/\f/\16/\u017f\13/\3\60\3\60\3\60\5")
        buf.write("\60\u0184\n\60\3\61\3\61\3\61\5\61\u0189\n\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u0194\n\62\3")
        buf.write("\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\2\5XZ\\\66\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfh\2\5\4\2\b\b\n\r\4\2\b\b\n\f\3\2,-\2\u01a0\2")
        buf.write("j\3\2\2\2\4q\3\2\2\2\6u\3\2\2\2\bz\3\2\2\2\n|\3\2\2\2")
        buf.write("\f\u0081\3\2\2\2\16\u0088\3\2\2\2\20\u008a\3\2\2\2\22")
        buf.write("\u0090\3\2\2\2\24\u0094\3\2\2\2\26\u0096\3\2\2\2\30\u009b")
        buf.write("\3\2\2\2\32\u00a2\3\2\2\2\34\u00a6\3\2\2\2\36\u00b1\3")
        buf.write("\2\2\2 \u00b3\3\2\2\2\"\u00bb\3\2\2\2$\u00c7\3\2\2\2&")
        buf.write("\u00cb\3\2\2\2(\u00d2\3\2\2\2*\u00d6\3\2\2\2,\u00da\3")
        buf.write("\2\2\2.\u00df\3\2\2\2\60\u00e6\3\2\2\2\62\u00ec\3\2\2")
        buf.write("\2\64\u00f8\3\2\2\2\66\u00fc\3\2\2\28\u00fe\3\2\2\2:\u0103")
        buf.write("\3\2\2\2<\u010d\3\2\2\2>\u0119\3\2\2\2@\u011f\3\2\2\2")
        buf.write("B\u0127\3\2\2\2D\u012e\3\2\2\2F\u0134\3\2\2\2H\u0137\3")
        buf.write("\2\2\2J\u013a\3\2\2\2L\u0140\3\2\2\2N\u0144\3\2\2\2P\u0148")
        buf.write("\3\2\2\2R\u014f\3\2\2\2T\u0156\3\2\2\2V\u015d\3\2\2\2")
        buf.write("X\u015f\3\2\2\2Z\u016a\3\2\2\2\\\u0175\3\2\2\2^\u0183")
        buf.write("\3\2\2\2`\u0188\3\2\2\2b\u0193\3\2\2\2d\u0195\3\2\2\2")
        buf.write("f\u019a\3\2\2\2h\u019e\3\2\2\2jk\5\4\3\2kl\7\2\2\3l\3")
        buf.write("\3\2\2\2mn\5\6\4\2no\5\4\3\2or\3\2\2\2pr\5\6\4\2qm\3\2")
        buf.write("\2\2qp\3\2\2\2r\5\3\2\2\2sv\5\b\5\2tv\5 \21\2us\3\2\2")
        buf.write("\2ut\3\2\2\2v\7\3\2\2\2w{\5\n\6\2x{\5\f\7\2y{\5\24\13")
        buf.write("\2zw\3\2\2\2zx\3\2\2\2zy\3\2\2\2{\t\3\2\2\2|}\5\22\n\2")
        buf.write("}~\7&\2\2~\177\5\16\b\2\177\u0080\7%\2\2\u0080\13\3\2")
        buf.write("\2\2\u0081\u0082\5\22\n\2\u0082\u0083\7&\2\2\u0083\u0084")
        buf.write("\5\16\b\2\u0084\u0085\7;\2\2\u0085\u0086\5R*\2\u0086\u0087")
        buf.write("\7%\2\2\u0087\r\3\2\2\2\u0088\u0089\t\2\2\2\u0089\17\3")
        buf.write("\2\2\2\u008a\u008b\t\3\2\2\u008b\21\3\2\2\2\u008c\u008d")
        buf.write("\7\37\2\2\u008d\u008e\7$\2\2\u008e\u0091\5\22\n\2\u008f")
        buf.write("\u0091\7\37\2\2\u0090\u008c\3\2\2\2\u0090\u008f\3\2\2")
        buf.write("\2\u0091\23\3\2\2\2\u0092\u0095\5\26\f\2\u0093\u0095\5")
        buf.write("\30\r\2\u0094\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095")
        buf.write("\25\3\2\2\2\u0096\u0097\5\22\n\2\u0097\u0098\7&\2\2\u0098")
        buf.write("\u0099\5\34\17\2\u0099\u009a\7%\2\2\u009a\27\3\2\2\2\u009b")
        buf.write("\u009c\5\22\n\2\u009c\u009d\7&\2\2\u009d\u009e\5\34\17")
        buf.write("\2\u009e\u009f\7;\2\2\u009f\u00a0\5P)\2\u00a0\u00a1\7")
        buf.write("%\2\2\u00a1\31\3\2\2\2\u00a2\u00a3\7\'\2\2\u00a3\u00a4")
        buf.write("\5P)\2\u00a4\u00a5\7(\2\2\u00a5\33\3\2\2\2\u00a6\u00a7")
        buf.write("\7\17\2\2\u00a7\u00a8\7\"\2\2\u00a8\u00a9\5\36\20\2\u00a9")
        buf.write("\u00aa\7#\2\2\u00aa\u00ab\7\16\2\2\u00ab\u00ac\5\20\t")
        buf.write("\2\u00ac\35\3\2\2\2\u00ad\u00ae\7\6\2\2\u00ae\u00af\7")
        buf.write("$\2\2\u00af\u00b2\5\36\20\2\u00b0\u00b2\7\6\2\2\u00b1")
        buf.write("\u00ad\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\37\3\2\2\2\u00b3")
        buf.write("\u00b7\5\"\22\2\u00b4\u00b5\7\3\2\2\u00b5\u00b8\7\37\2")
        buf.write("\2\u00b6\u00b8\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\5J&\2\u00ba!")
        buf.write("\3\2\2\2\u00bb\u00bc\7\37\2\2\u00bc\u00bd\7&\2\2\u00bd")
        buf.write("\u00be\7\21\2\2\u00be\u00bf\5$\23\2\u00bf\u00c0\7 \2\2")
        buf.write("\u00c0\u00c1\5&\24\2\u00c1\u00c2\7!\2\2\u00c2#\3\2\2\2")
        buf.write("\u00c3\u00c8\5\20\t\2\u00c4\u00c8\7\t\2\2\u00c5\u00c8")
        buf.write("\7\r\2\2\u00c6\u00c8\5\34\17\2\u00c7\u00c3\3\2\2\2\u00c7")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2")
        buf.write("\u00c8%\3\2\2\2\u00c9\u00cc\5(\25\2\u00ca\u00cc\3\2\2")
        buf.write("\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\'\3\2")
        buf.write("\2\2\u00cd\u00ce\5*\26\2\u00ce\u00cf\7$\2\2\u00cf\u00d0")
        buf.write("\5(\25\2\u00d0\u00d3\3\2\2\2\u00d1\u00d3\5*\26\2\u00d2")
        buf.write("\u00cd\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3)\3\2\2\2\u00d4")
        buf.write("\u00d7\5,\27\2\u00d5\u00d7\3\2\2\2\u00d6\u00d4\3\2\2\2")
        buf.write("\u00d6\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\5")
        buf.write(".\30\2\u00d9+\3\2\2\2\u00da\u00dd\7\3\2\2\u00db\u00de")
        buf.write("\7\3\2\2\u00dc\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00de-\3\2\2\2\u00df\u00e0\7\37\2\2\u00e0")
        buf.write("\u00e1\7&\2\2\u00e1\u00e2\5\60\31\2\u00e2/\3\2\2\2\u00e3")
        buf.write("\u00e7\5\20\t\2\u00e4\u00e7\7\r\2\2\u00e5\u00e7\5\34\17")
        buf.write("\2\u00e6\u00e3\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5")
        buf.write("\3\2\2\2\u00e7\61\3\2\2\2\u00e8\u00e9\5\66\34\2\u00e9")
        buf.write("\u00ea\5\62\32\2\u00ea\u00ed\3\2\2\2\u00eb\u00ed\3\2\2")
        buf.write("\2\u00ec\u00e8\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\63\3")
        buf.write("\2\2\2\u00ee\u00f9\58\35\2\u00ef\u00f9\5:\36\2\u00f0\u00f9")
        buf.write("\5B\"\2\u00f1\u00f9\5D#\2\u00f2\u00f9\5<\37\2\u00f3\u00f9")
        buf.write("\5> \2\u00f4\u00f9\5@!\2\u00f5\u00f9\5F$\2\u00f6\u00f9")
        buf.write("\5H%\2\u00f7\u00f9\5J&\2\u00f8\u00ee\3\2\2\2\u00f8\u00ef")
        buf.write("\3\2\2\2\u00f8\u00f0\3\2\2\2\u00f8\u00f1\3\2\2\2\u00f8")
        buf.write("\u00f2\3\2\2\2\u00f8\u00f3\3\2\2\2\u00f8\u00f4\3\2\2\2")
        buf.write("\u00f8\u00f5\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3")
        buf.write("\2\2\2\u00f9\65\3\2\2\2\u00fa\u00fd\5\64\33\2\u00fb\u00fd")
        buf.write("\5\b\5\2\u00fc\u00fa\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd")
        buf.write("\67\3\2\2\2\u00fe\u00ff\5N(\2\u00ff\u0100\7;\2\2\u0100")
        buf.write("\u0101\5T+\2\u0101\u0102\7%\2\2\u01029\3\2\2\2\u0103\u0104")
        buf.write("\7\22\2\2\u0104\u0105\7 \2\2\u0105\u0106\5T+\2\u0106\u0107")
        buf.write("\7!\2\2\u0107\u010b\5L\'\2\u0108\u0109\7\23\2\2\u0109")
        buf.write("\u010c\5L\'\2\u010a\u010c\3\2\2\2\u010b\u0108\3\2\2\2")
        buf.write("\u010b\u010a\3\2\2\2\u010c;\3\2\2\2\u010d\u010e\7\27\2")
        buf.write("\2\u010e\u010f\7 \2\2\u010f\u0110\5N(\2\u0110\u0111\7")
        buf.write(";\2\2\u0111\u0112\5T+\2\u0112\u0113\7$\2\2\u0113\u0114")
        buf.write("\5T+\2\u0114\u0115\7$\2\2\u0115\u0116\5T+\2\u0116\u0117")
        buf.write("\7!\2\2\u0117\u0118\5L\'\2\u0118=\3\2\2\2\u0119\u011a")
        buf.write("\7\32\2\2\u011a\u011b\7 \2\2\u011b\u011c\5T+\2\u011c\u011d")
        buf.write("\7!\2\2\u011d\u011e\5L\'\2\u011e?\3\2\2\2\u011f\u0120")
        buf.write("\7\31\2\2\u0120\u0121\5J&\2\u0121\u0122\7\32\2\2\u0122")
        buf.write("\u0123\7 \2\2\u0123\u0124\5T+\2\u0124\u0125\7!\2\2\u0125")
        buf.write("\u0126\7%\2\2\u0126A\3\2\2\2\u0127\u012a\7\25\2\2\u0128")
        buf.write("\u012b\5T+\2\u0129\u012b\3\2\2\2\u012a\u0128\3\2\2\2\u012a")
        buf.write("\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\7%\2\2")
        buf.write("\u012dC\3\2\2\2\u012e\u012f\7\37\2\2\u012f\u0130\7 \2")
        buf.write("\2\u0130\u0131\5P)\2\u0131\u0132\7!\2\2\u0132\u0133\7")
        buf.write("%\2\2\u0133E\3\2\2\2\u0134\u0135\7\30\2\2\u0135\u0136")
        buf.write("\7%\2\2\u0136G\3\2\2\2\u0137\u0138\7\24\2\2\u0138\u0139")
        buf.write("\7%\2\2\u0139I\3\2\2\2\u013a\u013b\7\'\2\2\u013b\u013c")
        buf.write("\5\62\32\2\u013c\u013d\7(\2\2\u013dK\3\2\2\2\u013e\u0141")
        buf.write("\5J&\2\u013f\u0141\5\64\33\2\u0140\u013e\3\2\2\2\u0140")
        buf.write("\u013f\3\2\2\2\u0141M\3\2\2\2\u0142\u0145\7\37\2\2\u0143")
        buf.write("\u0145\5h\65\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2\2\2")
        buf.write("\u0145O\3\2\2\2\u0146\u0149\5R*\2\u0147\u0149\3\2\2\2")
        buf.write("\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2\2\u0149Q\3\2\2")
        buf.write("\2\u014a\u014b\5T+\2\u014b\u014c\7$\2\2\u014c\u014d\5")
        buf.write("R*\2\u014d\u0150\3\2\2\2\u014e\u0150\5T+\2\u014f\u014a")
        buf.write("\3\2\2\2\u014f\u014e\3\2\2\2\u0150S\3\2\2\2\u0151\u0152")
        buf.write("\5V,\2\u0152\u0153\7:\2\2\u0153\u0154\5V,\2\u0154\u0157")
        buf.write("\3\2\2\2\u0155\u0157\5V,\2\u0156\u0151\3\2\2\2\u0156\u0155")
        buf.write("\3\2\2\2\u0157U\3\2\2\2\u0158\u0159\5X-\2\u0159\u015a")
        buf.write("\7+\2\2\u015a\u015b\5X-\2\u015b\u015e\3\2\2\2\u015c\u015e")
        buf.write("\5X-\2\u015d\u0158\3\2\2\2\u015d\u015c\3\2\2\2\u015eW")
        buf.write("\3\2\2\2\u015f\u0160\b-\1\2\u0160\u0161\5Z.\2\u0161\u0167")
        buf.write("\3\2\2\2\u0162\u0163\f\4\2\2\u0163\u0164\7*\2\2\u0164")
        buf.write("\u0166\5Z.\2\u0165\u0162\3\2\2\2\u0166\u0169\3\2\2\2\u0167")
        buf.write("\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168Y\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u016a\u016b\b.\1\2\u016b\u016c\5\\/\2\u016c")
        buf.write("\u0172\3\2\2\2\u016d\u016e\f\4\2\2\u016e\u016f\t\4\2\2")
        buf.write("\u016f\u0171\5\\/\2\u0170\u016d\3\2\2\2\u0171\u0174\3")
        buf.write("\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173[")
        buf.write("\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176\b/\1\2\u0176")
        buf.write("\u0177\5^\60\2\u0177\u017d\3\2\2\2\u0178\u0179\f\4\2\2")
        buf.write("\u0179\u017a\7)\2\2\u017a\u017c\5^\60\2\u017b\u0178\3")
        buf.write("\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e]\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181")
        buf.write("\7\61\2\2\u0181\u0184\5^\60\2\u0182\u0184\5`\61\2\u0183")
        buf.write("\u0180\3\2\2\2\u0183\u0182\3\2\2\2\u0184_\3\2\2\2\u0185")
        buf.write("\u0186\7-\2\2\u0186\u0189\5`\61\2\u0187\u0189\5b\62\2")
        buf.write("\u0188\u0185\3\2\2\2\u0188\u0187\3\2\2\2\u0189a\3\2\2")
        buf.write("\2\u018a\u0194\7\4\2\2\u018b\u0194\7\6\2\2\u018c\u0194")
        buf.write("\7\7\2\2\u018d\u0194\7\5\2\2\u018e\u0194\7\37\2\2\u018f")
        buf.write("\u0194\5d\63\2\u0190\u0194\5f\64\2\u0191\u0194\5h\65\2")
        buf.write("\u0192\u0194\5\32\16\2\u0193\u018a\3\2\2\2\u0193\u018b")
        buf.write("\3\2\2\2\u0193\u018c\3\2\2\2\u0193\u018d\3\2\2\2\u0193")
        buf.write("\u018e\3\2\2\2\u0193\u018f\3\2\2\2\u0193\u0190\3\2\2\2")
        buf.write("\u0193\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194c\3\2\2")
        buf.write("\2\u0195\u0196\7\37\2\2\u0196\u0197\7 \2\2\u0197\u0198")
        buf.write("\5P)\2\u0198\u0199\7!\2\2\u0199e\3\2\2\2\u019a\u019b\7")
        buf.write(" \2\2\u019b\u019c\5T+\2\u019c\u019d\7!\2\2\u019dg\3\2")
        buf.write("\2\2\u019e\u019f\7\37\2\2\u019f\u01a0\7\"\2\2\u01a0\u01a1")
        buf.write("\5R*\2\u01a1\u01a2\7#\2\2\u01a2i\3\2\2\2 quz\u0090\u0094")
        buf.write("\u00b1\u00b7\u00c7\u00cb\u00d2\u00d6\u00dd\u00e6\u00ec")
        buf.write("\u00f8\u00fc\u010b\u012a\u0140\u0144\u0148\u014f\u0156")
        buf.write("\u015d\u0167\u0172\u017d\u0183\u0188\u0193")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'integer'", "'void'", "'float'", 
                     "'boolean'", "'string'", "'auto'", "'of'", "'array'", 
                     "'inherit'", "'function'", "'if'", "'else'", "'break'", 
                     "'return'", "'out'", "'for'", "'continue'", "'do'", 
                     "'while'", "'true'", "'false'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'['", "']'", "','", "';'", 
                     "':'", "'{'", "'}'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'::'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "PARAM_KEYWORDS", "BOOLLIT", "FLOATLIT", 
                      "INTLIT", "STRINGLIT", "INTEGER", "VOID", "FLOAT", 
                      "BOOLEAN", "STRING", "AUTO", "OF", "ARR", "INHERIT", 
                      "FUNCTION", "IF", "ELSE", "BREAK", "RETURN", "OUT", 
                      "FOR", "CONTINUE", "DO", "WHILE", "TRUE", "FALSE", 
                      "COMMENT", "C_COMMENT", "ID", "LB", "RB", "SQLB", 
                      "SQRB", "COMMA", "SEMI", "COLON", "LCB", "RCB", "MULDIVMOD", 
                      "ANDOR", "COMPARE", "ADD", "MINUS", "MUL", "DIV", 
                      "PCENT", "NOT", "AND", "OR", "SAME", "NOTSAME", "LOWER", 
                      "HIGHER", "LOWER_EQ", "HIGHER_EQ", "SCOPE", "EQ", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_varnoinit = 4
    RULE_varassign = 5
    RULE_vartype = 6
    RULE_atomic_type = 7
    RULE_idlist = 8
    RULE_array = 9
    RULE_arraydecl = 10
    RULE_arrayinit = 11
    RULE_arrayVal = 12
    RULE_arrayParam = 13
    RULE_dimension = 14
    RULE_funcdecl = 15
    RULE_base_funcdecl = 16
    RULE_returntype = 17
    RULE_paramlist = 18
    RULE_paramprime = 19
    RULE_param = 20
    RULE_paramHead = 21
    RULE_parambase = 22
    RULE_paramtype = 23
    RULE_blocklist = 24
    RULE_stmt = 25
    RULE_allowed_blockstmt = 26
    RULE_assignstmt = 27
    RULE_ifstmt = 28
    RULE_forstmt = 29
    RULE_whilestmt = 30
    RULE_dowhile_stmt = 31
    RULE_returnstmt = 32
    RULE_callstmt = 33
    RULE_continuestmt = 34
    RULE_breakstmt = 35
    RULE_blockstmt = 36
    RULE_loopstmt = 37
    RULE_scalar_variable = 38
    RULE_exprlist = 39
    RULE_expprime = 40
    RULE_expr = 41
    RULE_expr1 = 42
    RULE_expr2 = 43
    RULE_expr3 = 44
    RULE_expr4 = 45
    RULE_expr5 = 46
    RULE_expr6 = 47
    RULE_expr7 = 48
    RULE_callexpr = 49
    RULE_subexpr = 50
    RULE_indexop = 51

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "varnoinit", 
                   "varassign", "vartype", "atomic_type", "idlist", "array", 
                   "arraydecl", "arrayinit", "arrayVal", "arrayParam", "dimension", 
                   "funcdecl", "base_funcdecl", "returntype", "paramlist", 
                   "paramprime", "param", "paramHead", "parambase", "paramtype", 
                   "blocklist", "stmt", "allowed_blockstmt", "assignstmt", 
                   "ifstmt", "forstmt", "whilestmt", "dowhile_stmt", "returnstmt", 
                   "callstmt", "continuestmt", "breakstmt", "blockstmt", 
                   "loopstmt", "scalar_variable", "exprlist", "expprime", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "callexpr", "subexpr", "indexop" ]

    EOF = Token.EOF
    PARAM_KEYWORDS=1
    BOOLLIT=2
    FLOATLIT=3
    INTLIT=4
    STRINGLIT=5
    INTEGER=6
    VOID=7
    FLOAT=8
    BOOLEAN=9
    STRING=10
    AUTO=11
    OF=12
    ARR=13
    INHERIT=14
    FUNCTION=15
    IF=16
    ELSE=17
    BREAK=18
    RETURN=19
    OUT=20
    FOR=21
    CONTINUE=22
    DO=23
    WHILE=24
    TRUE=25
    FALSE=26
    COMMENT=27
    C_COMMENT=28
    ID=29
    LB=30
    RB=31
    SQLB=32
    SQRB=33
    COMMA=34
    SEMI=35
    COLON=36
    LCB=37
    RCB=38
    MULDIVMOD=39
    ANDOR=40
    COMPARE=41
    ADD=42
    MINUS=43
    MUL=44
    DIV=45
    PCENT=46
    NOT=47
    AND=48
    OR=49
    SAME=50
    NOTSAME=51
    LOWER=52
    HIGHER=53
    LOWER_EQ=54
    HIGHER_EQ=55
    SCOPE=56
    EQ=57
    WS=58
    UNCLOSE_STRING=59
    ILLEGAL_ESCAPE=60
    ERROR_CHAR=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None


      




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.decllist()
            self.state = 105
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(MT22Parser.DecllistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




    def decllist(self):

        localctx = MT22Parser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.decl()
                self.state = 108
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varnoinit(self):
            return self.getTypedRuleContext(MT22Parser.VarnoinitContext,0)


        def varassign(self):
            return self.getTypedRuleContext(MT22Parser.VarassignContext,0)


        def array(self):
            return self.getTypedRuleContext(MT22Parser.ArrayContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.varnoinit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.varassign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarnoinitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_varnoinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarnoinit" ):
                return visitor.visitVarnoinit(self)
            else:
                return visitor.visitChildren(self)




    def varnoinit(self):

        localctx = MT22Parser.VarnoinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varnoinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.idlist()
            self.state = 123
            self.match(MT22Parser.COLON)
            self.state = 124
            self.vartype()
            self.state = 125
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def expprime(self):
            return self.getTypedRuleContext(MT22Parser.ExpprimeContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_varassign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarassign" ):
                return visitor.visitVarassign(self)
            else:
                return visitor.visitChildren(self)




    def varassign(self):

        localctx = MT22Parser.VarassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.idlist()
            self.state = 128
            self.match(MT22Parser.COLON)
            self.state = 129
            self.vartype()
            self.state = 130
            self.match(MT22Parser.EQ)
            self.state = 131
            self.expprime()
            self.state = 132
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = MT22Parser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.STRING) | (1 << MT22Parser.AUTO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomic_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_type" ):
                return visitor.visitAtomic_type(self)
            else:
                return visitor.visitChildren(self)




    def atomic_type(self):

        localctx = MT22Parser.Atomic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atomic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.INTEGER) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_idlist)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.match(MT22Parser.ID)
                self.state = 139
                self.match(MT22Parser.COMMA)
                self.state = 140
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraydecl(self):
            return self.getTypedRuleContext(MT22Parser.ArraydeclContext,0)


        def arrayinit(self):
            return self.getTypedRuleContext(MT22Parser.ArrayinitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MT22Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.arraydecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.arrayinit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def arrayParam(self):
            return self.getTypedRuleContext(MT22Parser.ArrayParamContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arraydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




    def arraydecl(self):

        localctx = MT22Parser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.idlist()
            self.state = 149
            self.match(MT22Parser.COLON)
            self.state = 150
            self.arrayParam()
            self.state = 151
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayinitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def arrayParam(self):
            return self.getTypedRuleContext(MT22Parser.ArrayParamContext,0)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayinit" ):
                return visitor.visitArrayinit(self)
            else:
                return visitor.visitChildren(self)




    def arrayinit(self):

        localctx = MT22Parser.ArrayinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arrayinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.idlist()
            self.state = 154
            self.match(MT22Parser.COLON)
            self.state = 155
            self.arrayParam()
            self.state = 156
            self.match(MT22Parser.EQ)
            self.state = 157
            self.exprlist()
            self.state = 158
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayVal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayVal" ):
                return visitor.visitArrayVal(self)
            else:
                return visitor.visitChildren(self)




    def arrayVal(self):

        localctx = MT22Parser.ArrayValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrayVal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MT22Parser.LCB)
            self.state = 161
            self.exprlist()
            self.state = 162
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARR(self):
            return self.getToken(MT22Parser.ARR, 0)

        def SQLB(self):
            return self.getToken(MT22Parser.SQLB, 0)

        def dimension(self):
            return self.getTypedRuleContext(MT22Parser.DimensionContext,0)


        def SQRB(self):
            return self.getToken(MT22Parser.SQRB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arrayParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayParam" ):
                return visitor.visitArrayParam(self)
            else:
                return visitor.visitChildren(self)




    def arrayParam(self):

        localctx = MT22Parser.ArrayParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_arrayParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MT22Parser.ARR)
            self.state = 165
            self.match(MT22Parser.SQLB)
            self.state = 166
            self.dimension()
            self.state = 167
            self.match(MT22Parser.SQRB)
            self.state = 168
            self.match(MT22Parser.OF)
            self.state = 169
            self.atomic_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def dimension(self):
            return self.getTypedRuleContext(MT22Parser.DimensionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = MT22Parser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dimension)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(MT22Parser.INTLIT)
                self.state = 172
                self.match(MT22Parser.COMMA)
                self.state = 173
                self.dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(MT22Parser.INTLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base_funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.Base_funcdeclContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def PARAM_KEYWORDS(self):
            return self.getToken(MT22Parser.PARAM_KEYWORDS, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.base_funcdecl()
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.PARAM_KEYWORDS]:
                self.state = 178
                self.match(MT22Parser.PARAM_KEYWORDS)
                self.state = 179
                self.match(MT22Parser.ID)
                pass
            elif token in [MT22Parser.LCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 183
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Base_funcdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def returntype(self):
            return self.getTypedRuleContext(MT22Parser.ReturntypeContext,0)


        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def paramlist(self):
            return self.getTypedRuleContext(MT22Parser.ParamlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_base_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBase_funcdecl" ):
                return visitor.visitBase_funcdecl(self)
            else:
                return visitor.visitChildren(self)




    def base_funcdecl(self):

        localctx = MT22Parser.Base_funcdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_base_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(MT22Parser.ID)
            self.state = 186
            self.match(MT22Parser.COLON)
            self.state = 187
            self.match(MT22Parser.FUNCTION)
            self.state = 188
            self.returntype()
            self.state = 189
            self.match(MT22Parser.LB)
            self.state = 190
            self.paramlist()
            self.state = 191
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturntypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def arrayParam(self):
            return self.getTypedRuleContext(MT22Parser.ArrayParamContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returntype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturntype" ):
                return visitor.visitReturntype(self)
            else:
                return visitor.visitChildren(self)




    def returntype(self):

        localctx = MT22Parser.ReturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returntype)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER, MT22Parser.FLOAT, MT22Parser.BOOLEAN, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.atomic_type()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.match(MT22Parser.AUTO)
                pass
            elif token in [MT22Parser.ARR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.arrayParam()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(MT22Parser.ParamprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MT22Parser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramlist)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.PARAM_KEYWORDS, MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.paramprime()
                pass
            elif token in [MT22Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(MT22Parser.ParamprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




    def paramprime(self):

        localctx = MT22Parser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_paramprime)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.param()
                self.state = 204
                self.match(MT22Parser.COMMA)
                self.state = 205
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parambase(self):
            return self.getTypedRuleContext(MT22Parser.ParambaseContext,0)


        def paramHead(self):
            return self.getTypedRuleContext(MT22Parser.ParamHeadContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.PARAM_KEYWORDS]:
                self.state = 210
                self.paramHead()
                pass
            elif token in [MT22Parser.ID]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 214
            self.parambase()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamHeadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAM_KEYWORDS(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.PARAM_KEYWORDS)
            else:
                return self.getToken(MT22Parser.PARAM_KEYWORDS, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_paramHead

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamHead" ):
                return visitor.visitParamHead(self)
            else:
                return visitor.visitChildren(self)




    def paramHead(self):

        localctx = MT22Parser.ParamHeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_paramHead)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MT22Parser.PARAM_KEYWORDS)
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.PARAM_KEYWORDS]:
                self.state = 217
                self.match(MT22Parser.PARAM_KEYWORDS)
                pass
            elif token in [MT22Parser.ID]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParambaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def paramtype(self):
            return self.getTypedRuleContext(MT22Parser.ParamtypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_parambase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParambase" ):
                return visitor.visitParambase(self)
            else:
                return visitor.visitChildren(self)




    def parambase(self):

        localctx = MT22Parser.ParambaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_parambase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(MT22Parser.ID)
            self.state = 222
            self.match(MT22Parser.COLON)
            self.state = 223
            self.paramtype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def arrayParam(self):
            return self.getTypedRuleContext(MT22Parser.ArrayParamContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_paramtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamtype" ):
                return visitor.visitParamtype(self)
            else:
                return visitor.visitChildren(self)




    def paramtype(self):

        localctx = MT22Parser.ParamtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_paramtype)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTEGER, MT22Parser.FLOAT, MT22Parser.BOOLEAN, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.atomic_type()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(MT22Parser.AUTO)
                pass
            elif token in [MT22Parser.ARR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.arrayParam()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocklistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def allowed_blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.Allowed_blockstmtContext,0)


        def blocklist(self):
            return self.getTypedRuleContext(MT22Parser.BlocklistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_blocklist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocklist" ):
                return visitor.visitBlocklist(self)
            else:
                return visitor.visitChildren(self)




    def blocklist(self):

        localctx = MT22Parser.BlocklistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_blocklist)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.IF, MT22Parser.BREAK, MT22Parser.RETURN, MT22Parser.FOR, MT22Parser.CONTINUE, MT22Parser.DO, MT22Parser.WHILE, MT22Parser.ID, MT22Parser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.allowed_blockstmt()
                self.state = 231
                self.blocklist()
                pass
            elif token in [MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MT22Parser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MT22Parser.IfstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MT22Parser.CallstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MT22Parser.ForstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(MT22Parser.WhilestmtContext,0)


        def dowhile_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Dowhile_stmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MT22Parser.BreakstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MT22Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.ifstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.returnstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 239
                self.callstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.forstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 241
                self.whilestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 242
                self.dowhile_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 243
                self.continuestmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 244
                self.breakstmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 245
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Allowed_blockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_allowed_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllowed_blockstmt" ):
                return visitor.visitAllowed_blockstmt(self)
            else:
                return visitor.visitChildren(self)




    def allowed_blockstmt(self):

        localctx = MT22Parser.Allowed_blockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_allowed_blockstmt)
        try:
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.vardecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_variable(self):
            return self.getTypedRuleContext(MT22Parser.Scalar_variableContext,0)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MT22Parser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.scalar_variable()
            self.state = 253
            self.match(MT22Parser.EQ)
            self.state = 254
            self.expr()
            self.state = 255
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def loopstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.LoopstmtContext)
            else:
                return self.getTypedRuleContext(MT22Parser.LoopstmtContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MT22Parser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(MT22Parser.IF)
            self.state = 258
            self.match(MT22Parser.LB)
            self.state = 259
            self.expr()
            self.state = 260
            self.match(MT22Parser.RB)
            self.state = 261
            self.loopstmt()
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 262
                self.match(MT22Parser.ELSE)
                self.state = 263
                self.loopstmt()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def scalar_variable(self):
            return self.getTypedRuleContext(MT22Parser.Scalar_variableContext,0)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def loopstmt(self):
            return self.getTypedRuleContext(MT22Parser.LoopstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MT22Parser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(MT22Parser.FOR)
            self.state = 268
            self.match(MT22Parser.LB)
            self.state = 269
            self.scalar_variable()
            self.state = 270
            self.match(MT22Parser.EQ)
            self.state = 271
            self.expr()
            self.state = 272
            self.match(MT22Parser.COMMA)
            self.state = 273
            self.expr()
            self.state = 274
            self.match(MT22Parser.COMMA)
            self.state = 275
            self.expr()
            self.state = 276
            self.match(MT22Parser.RB)
            self.state = 277
            self.loopstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def loopstmt(self):
            return self.getTypedRuleContext(MT22Parser.LoopstmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_whilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = MT22Parser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(MT22Parser.WHILE)
            self.state = 280
            self.match(MT22Parser.LB)
            self.state = 281
            self.expr()
            self.state = 282
            self.match(MT22Parser.RB)
            self.state = 283
            self.loopstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhile_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhile_stmt" ):
                return visitor.visitDowhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhile_stmt(self):

        localctx = MT22Parser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(MT22Parser.DO)
            self.state = 286
            self.blockstmt()
            self.state = 287
            self.match(MT22Parser.WHILE)
            self.state = 288
            self.match(MT22Parser.LB)
            self.state = 289
            self.expr()
            self.state = 290
            self.match(MT22Parser.RB)
            self.state = 291
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MT22Parser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(MT22Parser.RETURN)
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT, MT22Parser.ID, MT22Parser.LB, MT22Parser.LCB, MT22Parser.MINUS, MT22Parser.NOT]:
                self.state = 294
                self.expr()
                pass
            elif token in [MT22Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 298
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




    def callstmt(self):

        localctx = MT22Parser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(MT22Parser.ID)
            self.state = 301
            self.match(MT22Parser.LB)
            self.state = 302
            self.exprlist()
            self.state = 303
            self.match(MT22Parser.RB)
            self.state = 304
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MT22Parser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(MT22Parser.CONTINUE)
            self.state = 307
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MT22Parser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(MT22Parser.BREAK)
            self.state = 310
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def blocklist(self):
            return self.getTypedRuleContext(MT22Parser.BlocklistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = MT22Parser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(MT22Parser.LCB)
            self.state = 313
            self.blocklist()
            self.state = 314
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstmt(self):
            return self.getTypedRuleContext(MT22Parser.BlockstmtContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MT22Parser.StmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_loopstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopstmt" ):
                return visitor.visitLoopstmt(self)
            else:
                return visitor.visitChildren(self)




    def loopstmt(self):

        localctx = MT22Parser.LoopstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_loopstmt)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_scalar_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_variable" ):
                return visitor.visitScalar_variable(self)
            else:
                return visitor.visitChildren(self)




    def scalar_variable(self):

        localctx = MT22Parser.Scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_scalar_variable)
        try:
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(MT22Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.indexop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expprime(self):
            return self.getTypedRuleContext(MT22Parser.ExpprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MT22Parser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exprlist)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT, MT22Parser.ID, MT22Parser.LB, MT22Parser.LCB, MT22Parser.MINUS, MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.expprime()
                pass
            elif token in [MT22Parser.RB, MT22Parser.SEMI, MT22Parser.RCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def expprime(self):
            return self.getTypedRuleContext(MT22Parser.ExpprimeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpprime" ):
                return visitor.visitExpprime(self)
            else:
                return visitor.visitChildren(self)




    def expprime(self):

        localctx = MT22Parser.ExpprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expprime)
        try:
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.expr()
                self.state = 329
                self.match(MT22Parser.COMMA)
                self.state = 330
                self.expprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def SCOPE(self):
            return self.getToken(MT22Parser.SCOPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.expr1()
                self.state = 336
                self.match(MT22Parser.SCOPE)
                self.state = 337
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def COMPARE(self):
            return self.getToken(MT22Parser.COMPARE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr1)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.expr2(0)
                self.state = 343
                self.match(MT22Parser.COMPARE)
                self.state = 344
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def ANDOR(self):
            return self.getToken(MT22Parser.ANDOR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 352
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 353
                    self.match(MT22Parser.ANDOR)
                    self.state = 354
                    self.expr3(0) 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 363
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 364
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 365
                    self.expr4(0) 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def MULDIVMOD(self):
            return self.getToken(MT22Parser.MULDIVMOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    self.match(MT22Parser.MULDIVMOD)
                    self.state = 376
                    self.expr5() 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr5)
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(MT22Parser.NOT)
                self.state = 383
                self.expr5()
                pass
            elif token in [MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT, MT22Parser.ID, MT22Parser.LB, MT22Parser.LCB, MT22Parser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr6)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(MT22Parser.MINUS)
                self.state = 388
                self.expr6()
                pass
            elif token in [MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT, MT22Parser.ID, MT22Parser.LB, MT22Parser.LCB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLLIT(self):
            return self.getToken(MT22Parser.BOOLLIT, 0)

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def callexpr(self):
            return self.getTypedRuleContext(MT22Parser.CallexprContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(MT22Parser.SubexprContext,0)


        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def arrayVal(self):
            return self.getTypedRuleContext(MT22Parser.ArrayValContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MT22Parser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr7)
        try:
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(MT22Parser.BOOLLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 394
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 395
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 396
                self.match(MT22Parser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 397
                self.callexpr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 398
                self.subexpr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 399
                self.indexop()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 400
                self.arrayVal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(MT22Parser.ExprlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallexpr" ):
                return visitor.visitCallexpr(self)
            else:
                return visitor.visitChildren(self)




    def callexpr(self):

        localctx = MT22Parser.CallexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_callexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MT22Parser.ID)
            self.state = 404
            self.match(MT22Parser.LB)
            self.state = 405
            self.exprlist()
            self.state = 406
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_subexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




    def subexpr(self):

        localctx = MT22Parser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MT22Parser.LB)
            self.state = 409
            self.expr()
            self.state = 410
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def SQLB(self):
            return self.getToken(MT22Parser.SQLB, 0)

        def expprime(self):
            return self.getTypedRuleContext(MT22Parser.ExpprimeContext,0)


        def SQRB(self):
            return self.getToken(MT22Parser.SQRB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_indexop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexop" ):
                return visitor.visitIndexop(self)
            else:
                return visitor.visitChildren(self)




    def indexop(self):

        localctx = MT22Parser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(MT22Parser.ID)
            self.state = 413
            self.match(MT22Parser.SQLB)
            self.state = 414
            self.expprime()
            self.state = 415
            self.match(MT22Parser.SQRB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[43] = self.expr2_sempred
        self._predicates[44] = self.expr3_sempred
        self._predicates[45] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




