// Generated from d:\HCMUT_BaiTap\HK222\PPL\PPL-Assignment\asignment2-initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2

from lexererr import *
  

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MT22Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PARAM_KEYWORDS=1, BOOLLIT=2, FLOATLIT=3, INTLIT=4, STRINGLIT=5, INTEGER=6, 
		VOID=7, FLOAT=8, BOOLEAN=9, STRING=10, AUTO=11, OF=12, ARR=13, INHERIT=14, 
		FUNCTION=15, IF=16, ELSE=17, BREAK=18, RETURN=19, OUT=20, FOR=21, CONTINUE=22, 
		DO=23, WHILE=24, TRUE=25, FALSE=26, COMMENT=27, C_COMMENT=28, ID=29, LB=30, 
		RB=31, SQLB=32, SQRB=33, DOT=34, COMMA=35, SEMI=36, COLON=37, LCB=38, 
		RCB=39, ADDSUB=40, MULDIVMOD=41, ANDOR=42, COMPARE=43, ADD=44, MINUS=45, 
		MUL=46, DIV=47, PCENT=48, NOT=49, AND=50, OR=51, SAME=52, NOTSAME=53, 
		LOWER=54, HIGHER=55, LOWER_EQ=56, HIGHER_EQ=57, SCOPE=58, EQ=59, WS=60, 
		UNCLOSE_STRING=61, ILLEGAL_ESCAPE=62, ERROR_CHAR=63;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"EXPPART", "DECPART", "StringChar", "ESC2", "DOUBLEQ", "IllegalString", 
			"PARAM_KEYWORDS", "BOOLLIT", "FLOATLIT", "INTLIT", "STRINGLIT", "INTEGER", 
			"VOID", "FLOAT", "BOOLEAN", "STRING", "AUTO", "OF", "ARR", "INHERIT", 
			"FUNCTION", "IF", "ELSE", "BREAK", "RETURN", "OUT", "FOR", "CONTINUE", 
			"DO", "WHILE", "TRUE", "FALSE", "COMMENT", "C_COMMENT", "ID", "LB", "RB", 
			"SQLB", "SQRB", "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", "ADDSUB", 
			"MULDIVMOD", "ANDOR", "COMPARE", "ADD", "MINUS", "MUL", "DIV", "PCENT", 
			"NOT", "AND", "OR", "SAME", "NOTSAME", "LOWER", "HIGHER", "LOWER_EQ", 
			"HIGHER_EQ", "SCOPE", "EQ", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
			"ERROR_CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, "'integer'", "'void'", "'float'", 
			"'boolean'", "'string'", "'auto'", "'of'", "'array'", "'inherit'", "'function'", 
			"'if'", "'else'", "'break'", "'return'", "'out'", "'for'", "'continue'", 
			"'do'", "'while'", "'true'", "'false'", null, null, null, "'('", "')'", 
			"'['", "']'", "'.'", "','", "';'", "':'", "'{'", "'}'", null, null, null, 
			null, "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
			"'!='", "'<'", "'>'", "'<='", "'>='", "'::'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PARAM_KEYWORDS", "BOOLLIT", "FLOATLIT", "INTLIT", "STRINGLIT", 
			"INTEGER", "VOID", "FLOAT", "BOOLEAN", "STRING", "AUTO", "OF", "ARR", 
			"INHERIT", "FUNCTION", "IF", "ELSE", "BREAK", "RETURN", "OUT", "FOR", 
			"CONTINUE", "DO", "WHILE", "TRUE", "FALSE", "COMMENT", "C_COMMENT", "ID", 
			"LB", "RB", "SQLB", "SQRB", "DOT", "COMMA", "SEMI", "COLON", "LCB", "RCB", 
			"ADDSUB", "MULDIVMOD", "ANDOR", "COMPARE", "ADD", "MINUS", "MUL", "DIV", 
			"PCENT", "NOT", "AND", "OR", "SAME", "NOTSAME", "LOWER", "HIGHER", "LOWER_EQ", 
			"HIGHER_EQ", "SCOPE", "EQ", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
			"ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	  



	public MT22Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MT22.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 8:
			FLOATLIT_action((RuleContext)_localctx, actionIndex);
			break;
		case 9:
			INTLIT_action((RuleContext)_localctx, actionIndex);
			break;
		case 10:
			STRINGLIT_action((RuleContext)_localctx, actionIndex);
			break;
		case 66:
			UNCLOSE_STRING_action((RuleContext)_localctx, actionIndex);
			break;
		case 67:
			ILLEGAL_ESCAPE_action((RuleContext)_localctx, actionIndex);
			break;
		case 68:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void FLOATLIT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			self.text = self.text.replace('_', '')
			break;
		}
	}
	private void INTLIT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			self.text = self.text.replace('_', '')
			break;
		}
	}
	private void STRINGLIT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:

			        result = str(self.text)
			        self.text = result[1:-1]
			    
			break;
		}
	}
	private void UNCLOSE_STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:

			        unclose_str = str(self.text)
			        possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
			        if unclose_str[-1] in possible:
			            raise UncloseString(unclose_str[1:-1])
			        else:
			            raise UncloseString(unclose_str[1:])
			    
			break;
		}
	}
	private void ILLEGAL_ESCAPE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 4:

			        illegal_str = str(self.text)
			        raise IllegalEscape(illegal_str[1:])
			    
			break;
		}
	}
	private void ERROR_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 5:

			        raise ErrorToken(self.text)
			    
			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A\u01e7\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\3\2\3\2\5\2\u0090"+
		"\n\2\3\2\6\2\u0093\n\2\r\2\16\2\u0094\3\3\3\3\6\3\u0099\n\3\r\3\16\3\u009a"+
		"\3\4\3\4\5\4\u009f\n\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\5\7\u00a9\n\7\3"+
		"\b\3\b\5\b\u00ad\n\b\3\t\3\t\5\t\u00b1\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\5\n\u00bf\n\n\5\n\u00c1\n\n\3\n\3\n\3\13\3\13\3\13"+
		"\5\13\u00c8\n\13\3\13\7\13\u00cb\n\13\f\13\16\13\u00ce\13\13\3\13\5\13"+
		"\u00d1\n\13\3\f\3\f\7\f\u00d5\n\f\f\f\16\f\u00d8\13\f\3\f\3\f\3\f\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3"+
		"\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3"+
		"\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3"+
		"\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3"+
		"\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3"+
		"\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3"+
		"\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3"+
		" \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\7\"\u015c\n\"\f\"\16\"\u015f\13"+
		"\"\3\"\3\"\3#\3#\3#\3#\7#\u0167\n#\f#\16#\u016a\13#\3#\3#\3#\3#\3#\3$"+
		"\3$\7$\u0173\n$\f$\16$\u0176\13$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3"+
		"*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\5/\u018e\n/\3\60\3\60\3\60\5\60\u0193"+
		"\n\60\3\61\3\61\5\61\u0197\n\61\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u019f"+
		"\n\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3"+
		"9\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3"+
		"B\3B\3C\6C\u01c9\nC\rC\16C\u01ca\3C\3C\3D\3D\7D\u01d1\nD\fD\16D\u01d4"+
		"\13D\3D\5D\u01d7\nD\3D\3D\3E\3E\7E\u01dd\nE\fE\16E\u01e0\13E\3E\3E\3E"+
		"\3F\3F\3F\3\u0168\2G\3\2\5\2\7\2\t\2\13\2\r\2\17\3\21\4\23\5\25\6\27\7"+
		"\31\b\33\t\35\n\37\13!\f#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26"+
		"\67\279\30;\31=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e"+
		".g/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083=\u0085>\u0087"+
		"?\u0089@\u008bA\3\2\r\4\2GGgg\4\2--//\3\2\62;\6\2\n\f\16\17$$^^\t\2$$"+
		"^^ddhhppttvv\3\2\63;\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f"+
		"\17\17\"\"\6\3\n\f\16\17$$^^\2\u01fe\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3"+
		"\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2"+
		"\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2"+
		"\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2"+
		"\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2"+
		"\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2"+
		"O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3"+
		"\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2"+
		"\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2"+
		"u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2"+
		"\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089"+
		"\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u0096\3\2\2\2\7\u009e\3\2\2"+
		"\2\t\u00a0\3\2\2\2\13\u00a3\3\2\2\2\r\u00a8\3\2\2\2\17\u00ac\3\2\2\2\21"+
		"\u00b0\3\2\2\2\23\u00c0\3\2\2\2\25\u00d0\3\2\2\2\27\u00d2\3\2\2\2\31\u00dc"+
		"\3\2\2\2\33\u00e4\3\2\2\2\35\u00e9\3\2\2\2\37\u00ef\3\2\2\2!\u00f7\3\2"+
		"\2\2#\u00fe\3\2\2\2%\u0103\3\2\2\2\'\u0106\3\2\2\2)\u010c\3\2\2\2+\u0114"+
		"\3\2\2\2-\u011d\3\2\2\2/\u0120\3\2\2\2\61\u0125\3\2\2\2\63\u012b\3\2\2"+
		"\2\65\u0132\3\2\2\2\67\u0136\3\2\2\29\u013a\3\2\2\2;\u0143\3\2\2\2=\u0146"+
		"\3\2\2\2?\u014c\3\2\2\2A\u0151\3\2\2\2C\u0157\3\2\2\2E\u0162\3\2\2\2G"+
		"\u0170\3\2\2\2I\u0177\3\2\2\2K\u0179\3\2\2\2M\u017b\3\2\2\2O\u017d\3\2"+
		"\2\2Q\u017f\3\2\2\2S\u0181\3\2\2\2U\u0183\3\2\2\2W\u0185\3\2\2\2Y\u0187"+
		"\3\2\2\2[\u0189\3\2\2\2]\u018d\3\2\2\2_\u0192\3\2\2\2a\u0196\3\2\2\2c"+
		"\u019e\3\2\2\2e\u01a0\3\2\2\2g\u01a2\3\2\2\2i\u01a4\3\2\2\2k\u01a6\3\2"+
		"\2\2m\u01a8\3\2\2\2o\u01aa\3\2\2\2q\u01ac\3\2\2\2s\u01af\3\2\2\2u\u01b2"+
		"\3\2\2\2w\u01b5\3\2\2\2y\u01b8\3\2\2\2{\u01ba\3\2\2\2}\u01bc\3\2\2\2\177"+
		"\u01bf\3\2\2\2\u0081\u01c2\3\2\2\2\u0083\u01c5\3\2\2\2\u0085\u01c8\3\2"+
		"\2\2\u0087\u01ce\3\2\2\2\u0089\u01da\3\2\2\2\u008b\u01e4\3\2\2\2\u008d"+
		"\u008f\t\2\2\2\u008e\u0090\t\3\2\2\u008f\u008e\3\2\2\2\u008f\u0090\3\2"+
		"\2\2\u0090\u0092\3\2\2\2\u0091\u0093\t\4\2\2\u0092\u0091\3\2\2\2\u0093"+
		"\u0094\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\4\3\2\2\2"+
		"\u0096\u0098\7\60\2\2\u0097\u0099\t\4\2\2\u0098\u0097\3\2\2\2\u0099\u009a"+
		"\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\6\3\2\2\2\u009c"+
		"\u009f\n\5\2\2\u009d\u009f\5\t\5\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2"+
		"\2\2\u009f\b\3\2\2\2\u00a0\u00a1\7^\2\2\u00a1\u00a2\t\6\2\2\u00a2\n\3"+
		"\2\2\2\u00a3\u00a4\7$\2\2\u00a4\f\3\2\2\2\u00a5\u00a6\7^\2\2\u00a6\u00a9"+
		"\n\6\2\2\u00a7\u00a9\7^\2\2\u00a8\u00a5\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9"+
		"\16\3\2\2\2\u00aa\u00ad\5)\25\2\u00ab\u00ad\5\65\33\2\u00ac\u00aa\3\2"+
		"\2\2\u00ac\u00ab\3\2\2\2\u00ad\20\3\2\2\2\u00ae\u00b1\5? \2\u00af\u00b1"+
		"\5A!\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\22\3\2\2\2\u00b2"+
		"\u00b3\5\25\13\2\u00b3\u00b4\5\5\3\2\u00b4\u00c1\3\2\2\2\u00b5\u00b6\5"+
		"\25\13\2\u00b6\u00b7\5\5\3\2\u00b7\u00b8\5\3\2\2\u00b8\u00c1\3\2\2\2\u00b9"+
		"\u00ba\5\25\13\2\u00ba\u00bb\5\3\2\2\u00bb\u00c1\3\2\2\2\u00bc\u00be\5"+
		"\5\3\2\u00bd\u00bf\5\3\2\2\u00be\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf"+
		"\u00c1\3\2\2\2\u00c0\u00b2\3\2\2\2\u00c0\u00b5\3\2\2\2\u00c0\u00b9\3\2"+
		"\2\2\u00c0\u00bc\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\b\n\2\2\u00c3"+
		"\24\3\2\2\2\u00c4\u00d1\7\62\2\2\u00c5\u00cc\t\7\2\2\u00c6\u00c8\7a\2"+
		"\2\u00c7\u00c6\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb"+
		"\t\4\2\2\u00ca\u00c7\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc"+
		"\u00cd\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d1\b\13"+
		"\3\2\u00d0\u00c4\3\2\2\2\u00d0\u00c5\3\2\2\2\u00d1\26\3\2\2\2\u00d2\u00d6"+
		"\5\13\6\2\u00d3\u00d5\5\7\4\2\u00d4\u00d3\3\2\2\2\u00d5\u00d8\3\2\2\2"+
		"\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00d6"+
		"\3\2\2\2\u00d9\u00da\5\13\6\2\u00da\u00db\b\f\4\2\u00db\30\3\2\2\2\u00dc"+
		"\u00dd\7k\2\2\u00dd\u00de\7p\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7g\2\2"+
		"\u00e0\u00e1\7i\2\2\u00e1\u00e2\7g\2\2\u00e2\u00e3\7t\2\2\u00e3\32\3\2"+
		"\2\2\u00e4\u00e5\7x\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8"+
		"\7f\2\2\u00e8\34\3\2\2\2\u00e9\u00ea\7h\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec"+
		"\7q\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7v\2\2\u00ee\36\3\2\2\2\u00ef\u00f0"+
		"\7d\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7n\2\2\u00f3"+
		"\u00f4\7g\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7p\2\2\u00f6 \3\2\2\2\u00f7"+
		"\u00f8\7u\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7k\2\2"+
		"\u00fb\u00fc\7p\2\2\u00fc\u00fd\7i\2\2\u00fd\"\3\2\2\2\u00fe\u00ff\7c"+
		"\2\2\u00ff\u0100\7w\2\2\u0100\u0101\7v\2\2\u0101\u0102\7q\2\2\u0102$\3"+
		"\2\2\2\u0103\u0104\7q\2\2\u0104\u0105\7h\2\2\u0105&\3\2\2\2\u0106\u0107"+
		"\7c\2\2\u0107\u0108\7t\2\2\u0108\u0109\7t\2\2\u0109\u010a\7c\2\2\u010a"+
		"\u010b\7{\2\2\u010b(\3\2\2\2\u010c\u010d\7k\2\2\u010d\u010e\7p\2\2\u010e"+
		"\u010f\7j\2\2\u010f\u0110\7g\2\2\u0110\u0111\7t\2\2\u0111\u0112\7k\2\2"+
		"\u0112\u0113\7v\2\2\u0113*\3\2\2\2\u0114\u0115\7h\2\2\u0115\u0116\7w\2"+
		"\2\u0116\u0117\7p\2\2\u0117\u0118\7e\2\2\u0118\u0119\7v\2\2\u0119\u011a"+
		"\7k\2\2\u011a\u011b\7q\2\2\u011b\u011c\7p\2\2\u011c,\3\2\2\2\u011d\u011e"+
		"\7k\2\2\u011e\u011f\7h\2\2\u011f.\3\2\2\2\u0120\u0121\7g\2\2\u0121\u0122"+
		"\7n\2\2\u0122\u0123\7u\2\2\u0123\u0124\7g\2\2\u0124\60\3\2\2\2\u0125\u0126"+
		"\7d\2\2\u0126\u0127\7t\2\2\u0127\u0128\7g\2\2\u0128\u0129\7c\2\2\u0129"+
		"\u012a\7m\2\2\u012a\62\3\2\2\2\u012b\u012c\7t\2\2\u012c\u012d\7g\2\2\u012d"+
		"\u012e\7v\2\2\u012e\u012f\7w\2\2\u012f\u0130\7t\2\2\u0130\u0131\7p\2\2"+
		"\u0131\64\3\2\2\2\u0132\u0133\7q\2\2\u0133\u0134\7w\2\2\u0134\u0135\7"+
		"v\2\2\u0135\66\3\2\2\2\u0136\u0137\7h\2\2\u0137\u0138\7q\2\2\u0138\u0139"+
		"\7t\2\2\u01398\3\2\2\2\u013a\u013b\7e\2\2\u013b\u013c\7q\2\2\u013c\u013d"+
		"\7p\2\2\u013d\u013e\7v\2\2\u013e\u013f\7k\2\2\u013f\u0140\7p\2\2\u0140"+
		"\u0141\7w\2\2\u0141\u0142\7g\2\2\u0142:\3\2\2\2\u0143\u0144\7f\2\2\u0144"+
		"\u0145\7q\2\2\u0145<\3\2\2\2\u0146\u0147\7y\2\2\u0147\u0148\7j\2\2\u0148"+
		"\u0149\7k\2\2\u0149\u014a\7n\2\2\u014a\u014b\7g\2\2\u014b>\3\2\2\2\u014c"+
		"\u014d\7v\2\2\u014d\u014e\7t\2\2\u014e\u014f\7w\2\2\u014f\u0150\7g\2\2"+
		"\u0150@\3\2\2\2\u0151\u0152\7h\2\2\u0152\u0153\7c\2\2\u0153\u0154\7n\2"+
		"\2\u0154\u0155\7u\2\2\u0155\u0156\7g\2\2\u0156B\3\2\2\2\u0157\u0158\7"+
		"\61\2\2\u0158\u0159\7\61\2\2\u0159\u015d\3\2\2\2\u015a\u015c\n\b\2\2\u015b"+
		"\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2"+
		"\2\2\u015e\u0160\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\b\"\5\2\u0161"+
		"D\3\2\2\2\u0162\u0163\7\61\2\2\u0163\u0164\7,\2\2\u0164\u0168\3\2\2\2"+
		"\u0165\u0167\13\2\2\2\u0166\u0165\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0169"+
		"\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016b\3\2\2\2\u016a\u0168\3\2\2\2\u016b"+
		"\u016c\7,\2\2\u016c\u016d\7\61\2\2\u016d\u016e\3\2\2\2\u016e\u016f\b#"+
		"\5\2\u016fF\3\2\2\2\u0170\u0174\t\t\2\2\u0171\u0173\t\n\2\2\u0172\u0171"+
		"\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175"+
		"H\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\7*\2\2\u0178J\3\2\2\2\u0179"+
		"\u017a\7+\2\2\u017aL\3\2\2\2\u017b\u017c\7]\2\2\u017cN\3\2\2\2\u017d\u017e"+
		"\7_\2\2\u017eP\3\2\2\2\u017f\u0180\7\60\2\2\u0180R\3\2\2\2\u0181\u0182"+
		"\7.\2\2\u0182T\3\2\2\2\u0183\u0184\7=\2\2\u0184V\3\2\2\2\u0185\u0186\7"+
		"<\2\2\u0186X\3\2\2\2\u0187\u0188\7}\2\2\u0188Z\3\2\2\2\u0189\u018a\7\177"+
		"\2\2\u018a\\\3\2\2\2\u018b\u018e\5e\63\2\u018c\u018e\5g\64\2\u018d\u018b"+
		"\3\2\2\2\u018d\u018c\3\2\2\2\u018e^\3\2\2\2\u018f\u0193\5i\65\2\u0190"+
		"\u0193\5k\66\2\u0191\u0193\5m\67\2\u0192\u018f\3\2\2\2\u0192\u0190\3\2"+
		"\2\2\u0192\u0191\3\2\2\2\u0193`\3\2\2\2\u0194\u0197\5q9\2\u0195\u0197"+
		"\5s:\2\u0196\u0194\3\2\2\2\u0196\u0195\3\2\2\2\u0197b\3\2\2\2\u0198\u019f"+
		"\5u;\2\u0199\u019f\5w<\2\u019a\u019f\5{>\2\u019b\u019f\5\177@\2\u019c"+
		"\u019f\5y=\2\u019d\u019f\5}?\2\u019e\u0198\3\2\2\2\u019e\u0199\3\2\2\2"+
		"\u019e\u019a\3\2\2\2\u019e\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d"+
		"\3\2\2\2\u019fd\3\2\2\2\u01a0\u01a1\7-\2\2\u01a1f\3\2\2\2\u01a2\u01a3"+
		"\7/\2\2\u01a3h\3\2\2\2\u01a4\u01a5\7,\2\2\u01a5j\3\2\2\2\u01a6\u01a7\7"+
		"\61\2\2\u01a7l\3\2\2\2\u01a8\u01a9\7\'\2\2\u01a9n\3\2\2\2\u01aa\u01ab"+
		"\7#\2\2\u01abp\3\2\2\2\u01ac\u01ad\7(\2\2\u01ad\u01ae\7(\2\2\u01aer\3"+
		"\2\2\2\u01af\u01b0\7~\2\2\u01b0\u01b1\7~\2\2\u01b1t\3\2\2\2\u01b2\u01b3"+
		"\7?\2\2\u01b3\u01b4\7?\2\2\u01b4v\3\2\2\2\u01b5\u01b6\7#\2\2\u01b6\u01b7"+
		"\7?\2\2\u01b7x\3\2\2\2\u01b8\u01b9\7>\2\2\u01b9z\3\2\2\2\u01ba\u01bb\7"+
		"@\2\2\u01bb|\3\2\2\2\u01bc\u01bd\7>\2\2\u01bd\u01be\7?\2\2\u01be~\3\2"+
		"\2\2\u01bf\u01c0\7@\2\2\u01c0\u01c1\7?\2\2\u01c1\u0080\3\2\2\2\u01c2\u01c3"+
		"\7<\2\2\u01c3\u01c4\7<\2\2\u01c4\u0082\3\2\2\2\u01c5\u01c6\7?\2\2\u01c6"+
		"\u0084\3\2\2\2\u01c7\u01c9\t\13\2\2\u01c8\u01c7\3\2\2\2\u01c9\u01ca\3"+
		"\2\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc"+
		"\u01cd\bC\5\2\u01cd\u0086\3\2\2\2\u01ce\u01d2\5\13\6\2\u01cf\u01d1\5\7"+
		"\4\2\u01d0\u01cf\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2"+
		"\u01d3\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d7\t\f"+
		"\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\bD\6\2\u01d9"+
		"\u0088\3\2\2\2\u01da\u01de\5\13\6\2\u01db\u01dd\5\7\4\2\u01dc\u01db\3"+
		"\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df"+
		"\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2\u01e1\u01e2\5\r\7\2\u01e2\u01e3\bE"+
		"\7\2\u01e3\u008a\3\2\2\2\u01e4\u01e5\13\2\2\2\u01e5\u01e6\bF\b\2\u01e6"+
		"\u008c\3\2\2\2\33\2\u008f\u0094\u009a\u009e\u00a8\u00ac\u00b0\u00be\u00c0"+
		"\u00c7\u00cc\u00d0\u00d6\u015d\u0168\u0174\u018d\u0192\u0196\u019e\u01ca"+
		"\u01d2\u01d6\u01de\t\3\n\2\3\13\3\3\f\4\b\2\2\3D\5\3E\6\3F\7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}