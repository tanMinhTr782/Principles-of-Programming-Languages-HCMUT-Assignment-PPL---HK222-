// Generated from MT22.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MT22Parser extends Parser {
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
	public static final int
		RULE_program = 0, RULE_decllist = 1, RULE_decl = 2, RULE_vardecl = 3, 
		RULE_varnoinit = 4, RULE_varassign = 5, RULE_vartype = 6, RULE_atomic_type = 7, 
		RULE_idlist = 8, RULE_array = 9, RULE_arraydecl = 10, RULE_arrayinit = 11, 
		RULE_arraylit = 12, RULE_arrayVal = 13, RULE_arrayParam = 14, RULE_dimension = 15, 
		RULE_funcdecl = 16, RULE_base_funcdecl = 17, RULE_returntype = 18, RULE_body = 19, 
		RULE_paramlist = 20, RULE_paramprime = 21, RULE_param = 22, RULE_paramHead = 23, 
		RULE_parambase = 24, RULE_paramtype = 25, RULE_blocklist = 26, RULE_stmt = 27, 
		RULE_allowed_blockstmt = 28, RULE_assignstmt = 29, RULE_ifstmt = 30, RULE_if_noelsestmt = 31, 
		RULE_ifelsestmt = 32, RULE_forstmt = 33, RULE_whilestmt = 34, RULE_dowhile_stmt = 35, 
		RULE_returnstmt = 36, RULE_callstmt = 37, RULE_continuestmt = 38, RULE_breakstmt = 39, 
		RULE_blockstmt = 40, RULE_loopstmt = 41, RULE_scalar_variable = 42, RULE_exprlist = 43, 
		RULE_expprime = 44, RULE_expr = 45, RULE_expr1 = 46, RULE_expr2 = 47, 
		RULE_expr3 = 48, RULE_expr4 = 49, RULE_expr5 = 50, RULE_expr6 = 51, RULE_expr7 = 52, 
		RULE_callexpr = 53, RULE_subexpr = 54, RULE_indexop = 55;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "decllist", "decl", "vardecl", "varnoinit", "varassign", "vartype", 
			"atomic_type", "idlist", "array", "arraydecl", "arrayinit", "arraylit", 
			"arrayVal", "arrayParam", "dimension", "funcdecl", "base_funcdecl", "returntype", 
			"body", "paramlist", "paramprime", "param", "paramHead", "parambase", 
			"paramtype", "blocklist", "stmt", "allowed_blockstmt", "assignstmt", 
			"ifstmt", "if_noelsestmt", "ifelsestmt", "forstmt", "whilestmt", "dowhile_stmt", 
			"returnstmt", "callstmt", "continuestmt", "breakstmt", "blockstmt", "loopstmt", 
			"scalar_variable", "exprlist", "expprime", "expr", "expr1", "expr2", 
			"expr3", "expr4", "expr5", "expr6", "expr7", "callexpr", "subexpr", "indexop"
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

	@Override
	public String getGrammarFileName() { return "MT22.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	  


	public MT22Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public DecllistContext decllist() {
			return getRuleContext(DecllistContext.class,0);
		}
		public TerminalNode EOF() { return getToken(MT22Parser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			decllist();
			setState(113);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DecllistContext extends ParserRuleContext {
		public DeclContext decl() {
			return getRuleContext(DeclContext.class,0);
		}
		public DecllistContext decllist() {
			return getRuleContext(DecllistContext.class,0);
		}
		public DecllistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decllist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterDecllist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitDecllist(this);
		}
	}

	public final DecllistContext decllist() throws RecognitionException {
		DecllistContext _localctx = new DecllistContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_decllist);
		try {
			setState(119);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(115);
				decl();
				setState(116);
				decllist();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(118);
				decl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclContext extends ParserRuleContext {
		public VardeclContext vardecl() {
			return getRuleContext(VardeclContext.class,0);
		}
		public FuncdeclContext funcdecl() {
			return getRuleContext(FuncdeclContext.class,0);
		}
		public DeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterDecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitDecl(this);
		}
	}

	public final DeclContext decl() throws RecognitionException {
		DeclContext _localctx = new DeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_decl);
		try {
			setState(123);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(121);
				vardecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(122);
				funcdecl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardeclContext extends ParserRuleContext {
		public VarnoinitContext varnoinit() {
			return getRuleContext(VarnoinitContext.class,0);
		}
		public VarassignContext varassign() {
			return getRuleContext(VarassignContext.class,0);
		}
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public VardeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterVardecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitVardecl(this);
		}
	}

	public final VardeclContext vardecl() throws RecognitionException {
		VardeclContext _localctx = new VardeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_vardecl);
		try {
			setState(128);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(125);
				varnoinit();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(126);
				varassign();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(127);
				array();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarnoinitContext extends ParserRuleContext {
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public TerminalNode COLON() { return getToken(MT22Parser.COLON, 0); }
		public VartypeContext vartype() {
			return getRuleContext(VartypeContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MT22Parser.SEMI, 0); }
		public VarnoinitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varnoinit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterVarnoinit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitVarnoinit(this);
		}
	}

	public final VarnoinitContext varnoinit() throws RecognitionException {
		VarnoinitContext _localctx = new VarnoinitContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_varnoinit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			idlist();
			setState(131);
			match(COLON);
			setState(132);
			vartype();
			setState(133);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarassignContext extends ParserRuleContext {
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public TerminalNode COLON() { return getToken(MT22Parser.COLON, 0); }
		public VartypeContext vartype() {
			return getRuleContext(VartypeContext.class,0);
		}
		public TerminalNode EQ() { return getToken(MT22Parser.EQ, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MT22Parser.SEMI, 0); }
		public VarassignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varassign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterVarassign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitVarassign(this);
		}
	}

	public final VarassignContext varassign() throws RecognitionException {
		VarassignContext _localctx = new VarassignContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_varassign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			idlist();
			setState(136);
			match(COLON);
			setState(137);
			vartype();
			setState(138);
			match(EQ);
			setState(139);
			exprlist();
			setState(140);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VartypeContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(MT22Parser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(MT22Parser.FLOAT, 0); }
		public TerminalNode BOOLEAN() { return getToken(MT22Parser.BOOLEAN, 0); }
		public TerminalNode STRING() { return getToken(MT22Parser.STRING, 0); }
		public TerminalNode AUTO() { return getToken(MT22Parser.AUTO, 0); }
		public VartypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vartype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterVartype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitVartype(this);
		}
	}

	public final VartypeContext vartype() throws RecognitionException {
		VartypeContext _localctx = new VartypeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_vartype);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEGER) | (1L << FLOAT) | (1L << BOOLEAN) | (1L << STRING) | (1L << AUTO))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Atomic_typeContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(MT22Parser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(MT22Parser.FLOAT, 0); }
		public TerminalNode BOOLEAN() { return getToken(MT22Parser.BOOLEAN, 0); }
		public TerminalNode STRING() { return getToken(MT22Parser.STRING, 0); }
		public Atomic_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atomic_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterAtomic_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitAtomic_type(this);
		}
	}

	public final Atomic_typeContext atomic_type() throws RecognitionException {
		Atomic_typeContext _localctx = new Atomic_typeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_atomic_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEGER) | (1L << FLOAT) | (1L << BOOLEAN) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdlistContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MT22Parser.ID, 0); }
		public TerminalNode COMMA() { return getToken(MT22Parser.COMMA, 0); }
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public IdlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterIdlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitIdlist(this);
		}
	}

	public final IdlistContext idlist() throws RecognitionException {
		IdlistContext _localctx = new IdlistContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_idlist);
		try {
			setState(150);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(146);
				match(ID);
				setState(147);
				match(COMMA);
				setState(148);
				idlist();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(149);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayContext extends ParserRuleContext {
		public ArraydeclContext arraydecl() {
			return getRuleContext(ArraydeclContext.class,0);
		}
		public ArrayinitContext arrayinit() {
			return getRuleContext(ArrayinitContext.class,0);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterArray(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitArray(this);
		}
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_array);
		try {
			setState(154);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(152);
				arraydecl();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(153);
				arrayinit();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArraydeclContext extends ParserRuleContext {
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public TerminalNode COLON() { return getToken(MT22Parser.COLON, 0); }
		public ArrayParamContext arrayParam() {
			return getRuleContext(ArrayParamContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MT22Parser.SEMI, 0); }
		public ArraydeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arraydecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterArraydecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitArraydecl(this);
		}
	}

	public final ArraydeclContext arraydecl() throws RecognitionException {
		ArraydeclContext _localctx = new ArraydeclContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_arraydecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			idlist();
			setState(157);
			match(COLON);
			setState(158);
			arrayParam();
			setState(159);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayinitContext extends ParserRuleContext {
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public TerminalNode COLON() { return getToken(MT22Parser.COLON, 0); }
		public ArrayParamContext arrayParam() {
			return getRuleContext(ArrayParamContext.class,0);
		}
		public TerminalNode EQ() { return getToken(MT22Parser.EQ, 0); }
		public ArraylitContext arraylit() {
			return getRuleContext(ArraylitContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MT22Parser.SEMI, 0); }
		public ArrayinitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayinit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterArrayinit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitArrayinit(this);
		}
	}

	public final ArrayinitContext arrayinit() throws RecognitionException {
		ArrayinitContext _localctx = new ArrayinitContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_arrayinit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			idlist();
			setState(162);
			match(COLON);
			setState(163);
			arrayParam();
			setState(164);
			match(EQ);
			setState(165);
			arraylit();
			setState(166);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArraylitContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MT22Parser.ID, 0); }
		public ArrayValContext arrayVal() {
			return getRuleContext(ArrayValContext.class,0);
		}
		public ArraylitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arraylit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterArraylit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitArraylit(this);
		}
	}

	public final ArraylitContext arraylit() throws RecognitionException {
		ArraylitContext _localctx = new ArraylitContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_arraylit);
		try {
			setState(170);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(168);
				match(ID);
				}
				break;
			case LCB:
				enterOuterAlt(_localctx, 2);
				{
				setState(169);
				arrayVal();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayValContext extends ParserRuleContext {
		public TerminalNode LCB() { return getToken(MT22Parser.LCB, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public TerminalNode RCB() { return getToken(MT22Parser.RCB, 0); }
		public ArrayValContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayVal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterArrayVal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitArrayVal(this);
		}
	}

	public final ArrayValContext arrayVal() throws RecognitionException {
		ArrayValContext _localctx = new ArrayValContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_arrayVal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(LCB);
			setState(173);
			exprlist();
			setState(174);
			match(RCB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArrayParamContext extends ParserRuleContext {
		public TerminalNode ARR() { return getToken(MT22Parser.ARR, 0); }
		public TerminalNode SQLB() { return getToken(MT22Parser.SQLB, 0); }
		public DimensionContext dimension() {
			return getRuleContext(DimensionContext.class,0);
		}
		public TerminalNode SQRB() { return getToken(MT22Parser.SQRB, 0); }
		public TerminalNode OF() { return getToken(MT22Parser.OF, 0); }
		public Atomic_typeContext atomic_type() {
			return getRuleContext(Atomic_typeContext.class,0);
		}
		public ArrayParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayParam; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterArrayParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitArrayParam(this);
		}
	}

	public final ArrayParamContext arrayParam() throws RecognitionException {
		ArrayParamContext _localctx = new ArrayParamContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_arrayParam);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(ARR);
			setState(177);
			match(SQLB);
			setState(178);
			dimension();
			setState(179);
			match(SQRB);
			setState(180);
			match(OF);
			setState(181);
			atomic_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DimensionContext extends ParserRuleContext {
		public TerminalNode INTLIT() { return getToken(MT22Parser.INTLIT, 0); }
		public TerminalNode COMMA() { return getToken(MT22Parser.COMMA, 0); }
		public DimensionContext dimension() {
			return getRuleContext(DimensionContext.class,0);
		}
		public DimensionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dimension; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterDimension(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitDimension(this);
		}
	}

	public final DimensionContext dimension() throws RecognitionException {
		DimensionContext _localctx = new DimensionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_dimension);
		try {
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(183);
				match(INTLIT);
				setState(184);
				match(COMMA);
				setState(185);
				dimension();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(186);
				match(INTLIT);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncdeclContext extends ParserRuleContext {
		public Base_funcdeclContext base_funcdecl() {
			return getRuleContext(Base_funcdeclContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode PARAM_KEYWORDS() { return getToken(MT22Parser.PARAM_KEYWORDS, 0); }
		public TerminalNode ID() { return getToken(MT22Parser.ID, 0); }
		public FuncdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterFuncdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitFuncdecl(this);
		}
	}

	public final FuncdeclContext funcdecl() throws RecognitionException {
		FuncdeclContext _localctx = new FuncdeclContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_funcdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			base_funcdecl();
			setState(193);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PARAM_KEYWORDS:
				{
				setState(190);
				match(PARAM_KEYWORDS);
				setState(191);
				match(ID);
				}
				break;
			case LCB:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(195);
			body();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Base_funcdeclContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MT22Parser.ID, 0); }
		public TerminalNode COLON() { return getToken(MT22Parser.COLON, 0); }
		public TerminalNode FUNCTION() { return getToken(MT22Parser.FUNCTION, 0); }
		public ReturntypeContext returntype() {
			return getRuleContext(ReturntypeContext.class,0);
		}
		public TerminalNode LB() { return getToken(MT22Parser.LB, 0); }
		public ParamlistContext paramlist() {
			return getRuleContext(ParamlistContext.class,0);
		}
		public TerminalNode RB() { return getToken(MT22Parser.RB, 0); }
		public Base_funcdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_base_funcdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterBase_funcdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitBase_funcdecl(this);
		}
	}

	public final Base_funcdeclContext base_funcdecl() throws RecognitionException {
		Base_funcdeclContext _localctx = new Base_funcdeclContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_base_funcdecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			match(ID);
			setState(198);
			match(COLON);
			setState(199);
			match(FUNCTION);
			setState(200);
			returntype();
			setState(201);
			match(LB);
			setState(202);
			paramlist();
			setState(203);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturntypeContext extends ParserRuleContext {
		public Atomic_typeContext atomic_type() {
			return getRuleContext(Atomic_typeContext.class,0);
		}
		public TerminalNode VOID() { return getToken(MT22Parser.VOID, 0); }
		public TerminalNode AUTO() { return getToken(MT22Parser.AUTO, 0); }
		public ArrayParamContext arrayParam() {
			return getRuleContext(ArrayParamContext.class,0);
		}
		public ReturntypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returntype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterReturntype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitReturntype(this);
		}
	}

	public final ReturntypeContext returntype() throws RecognitionException {
		ReturntypeContext _localctx = new ReturntypeContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_returntype);
		try {
			setState(209);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
			case FLOAT:
			case BOOLEAN:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				atomic_type();
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				match(VOID);
				}
				break;
			case AUTO:
				enterOuterAlt(_localctx, 3);
				{
				setState(207);
				match(AUTO);
				}
				break;
			case ARR:
				enterOuterAlt(_localctx, 4);
				{
				setState(208);
				arrayParam();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BodyContext extends ParserRuleContext {
		public TerminalNode LCB() { return getToken(MT22Parser.LCB, 0); }
		public BlocklistContext blocklist() {
			return getRuleContext(BlocklistContext.class,0);
		}
		public TerminalNode RCB() { return getToken(MT22Parser.RCB, 0); }
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitBody(this);
		}
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			match(LCB);
			setState(212);
			blocklist();
			setState(213);
			match(RCB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamlistContext extends ParserRuleContext {
		public ParamprimeContext paramprime() {
			return getRuleContext(ParamprimeContext.class,0);
		}
		public ParamlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterParamlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitParamlist(this);
		}
	}

	public final ParamlistContext paramlist() throws RecognitionException {
		ParamlistContext _localctx = new ParamlistContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_paramlist);
		try {
			setState(217);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PARAM_KEYWORDS:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(215);
				paramprime();
				}
				break;
			case RB:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamprimeContext extends ParserRuleContext {
		public ParamContext param() {
			return getRuleContext(ParamContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(MT22Parser.COMMA, 0); }
		public ParamprimeContext paramprime() {
			return getRuleContext(ParamprimeContext.class,0);
		}
		public ParamprimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramprime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterParamprime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitParamprime(this);
		}
	}

	public final ParamprimeContext paramprime() throws RecognitionException {
		ParamprimeContext _localctx = new ParamprimeContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_paramprime);
		try {
			setState(224);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(219);
				param();
				setState(220);
				match(COMMA);
				setState(221);
				paramprime();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(223);
				param();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public ParambaseContext parambase() {
			return getRuleContext(ParambaseContext.class,0);
		}
		public ParamHeadContext paramHead() {
			return getRuleContext(ParamHeadContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitParam(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PARAM_KEYWORDS:
				{
				setState(226);
				paramHead();
				}
				break;
			case ID:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(230);
			parambase();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamHeadContext extends ParserRuleContext {
		public List<TerminalNode> PARAM_KEYWORDS() { return getTokens(MT22Parser.PARAM_KEYWORDS); }
		public TerminalNode PARAM_KEYWORDS(int i) {
			return getToken(MT22Parser.PARAM_KEYWORDS, i);
		}
		public ParamHeadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramHead; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterParamHead(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitParamHead(this);
		}
	}

	public final ParamHeadContext paramHead() throws RecognitionException {
		ParamHeadContext _localctx = new ParamHeadContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_paramHead);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(PARAM_KEYWORDS);
			setState(235);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PARAM_KEYWORDS:
				{
				setState(233);
				match(PARAM_KEYWORDS);
				}
				break;
			case ID:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParambaseContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MT22Parser.ID, 0); }
		public TerminalNode COLON() { return getToken(MT22Parser.COLON, 0); }
		public ParamtypeContext paramtype() {
			return getRuleContext(ParamtypeContext.class,0);
		}
		public ParambaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parambase; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterParambase(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitParambase(this);
		}
	}

	public final ParambaseContext parambase() throws RecognitionException {
		ParambaseContext _localctx = new ParambaseContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_parambase);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			match(ID);
			setState(238);
			match(COLON);
			setState(239);
			paramtype();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamtypeContext extends ParserRuleContext {
		public Atomic_typeContext atomic_type() {
			return getRuleContext(Atomic_typeContext.class,0);
		}
		public TerminalNode AUTO() { return getToken(MT22Parser.AUTO, 0); }
		public ArrayParamContext arrayParam() {
			return getRuleContext(ArrayParamContext.class,0);
		}
		public ParamtypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramtype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterParamtype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitParamtype(this);
		}
	}

	public final ParamtypeContext paramtype() throws RecognitionException {
		ParamtypeContext _localctx = new ParamtypeContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_paramtype);
		try {
			setState(244);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
			case FLOAT:
			case BOOLEAN:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(241);
				atomic_type();
				}
				break;
			case AUTO:
				enterOuterAlt(_localctx, 2);
				{
				setState(242);
				match(AUTO);
				}
				break;
			case ARR:
				enterOuterAlt(_localctx, 3);
				{
				setState(243);
				arrayParam();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlocklistContext extends ParserRuleContext {
		public Allowed_blockstmtContext allowed_blockstmt() {
			return getRuleContext(Allowed_blockstmtContext.class,0);
		}
		public BlocklistContext blocklist() {
			return getRuleContext(BlocklistContext.class,0);
		}
		public BlocklistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blocklist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterBlocklist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitBlocklist(this);
		}
	}

	public final BlocklistContext blocklist() throws RecognitionException {
		BlocklistContext _localctx = new BlocklistContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_blocklist);
		try {
			setState(250);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
			case BREAK:
			case RETURN:
			case FOR:
			case CONTINUE:
			case DO:
			case WHILE:
			case ID:
			case LCB:
				enterOuterAlt(_localctx, 1);
				{
				setState(246);
				allowed_blockstmt();
				setState(247);
				blocklist();
				}
				break;
			case RCB:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public AssignstmtContext assignstmt() {
			return getRuleContext(AssignstmtContext.class,0);
		}
		public IfstmtContext ifstmt() {
			return getRuleContext(IfstmtContext.class,0);
		}
		public ReturnstmtContext returnstmt() {
			return getRuleContext(ReturnstmtContext.class,0);
		}
		public CallstmtContext callstmt() {
			return getRuleContext(CallstmtContext.class,0);
		}
		public ForstmtContext forstmt() {
			return getRuleContext(ForstmtContext.class,0);
		}
		public WhilestmtContext whilestmt() {
			return getRuleContext(WhilestmtContext.class,0);
		}
		public Dowhile_stmtContext dowhile_stmt() {
			return getRuleContext(Dowhile_stmtContext.class,0);
		}
		public ContinuestmtContext continuestmt() {
			return getRuleContext(ContinuestmtContext.class,0);
		}
		public BreakstmtContext breakstmt() {
			return getRuleContext(BreakstmtContext.class,0);
		}
		public BlockstmtContext blockstmt() {
			return getRuleContext(BlockstmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitStmt(this);
		}
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_stmt);
		try {
			setState(262);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(252);
				assignstmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(253);
				ifstmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(254);
				returnstmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(255);
				callstmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(256);
				forstmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(257);
				whilestmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(258);
				dowhile_stmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(259);
				continuestmt();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(260);
				breakstmt();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(261);
				blockstmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Allowed_blockstmtContext extends ParserRuleContext {
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public VardeclContext vardecl() {
			return getRuleContext(VardeclContext.class,0);
		}
		public Allowed_blockstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_allowed_blockstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterAllowed_blockstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitAllowed_blockstmt(this);
		}
	}

	public final Allowed_blockstmtContext allowed_blockstmt() throws RecognitionException {
		Allowed_blockstmtContext _localctx = new Allowed_blockstmtContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_allowed_blockstmt);
		try {
			setState(266);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(264);
				stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(265);
				vardecl();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignstmtContext extends ParserRuleContext {
		public Scalar_variableContext scalar_variable() {
			return getRuleContext(Scalar_variableContext.class,0);
		}
		public TerminalNode EQ() { return getToken(MT22Parser.EQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MT22Parser.SEMI, 0); }
		public AssignstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterAssignstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitAssignstmt(this);
		}
	}

	public final AssignstmtContext assignstmt() throws RecognitionException {
		AssignstmtContext _localctx = new AssignstmtContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_assignstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			scalar_variable();
			setState(269);
			match(EQ);
			setState(270);
			expr();
			setState(271);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfstmtContext extends ParserRuleContext {
		public IfelsestmtContext ifelsestmt() {
			return getRuleContext(IfelsestmtContext.class,0);
		}
		public If_noelsestmtContext if_noelsestmt() {
			return getRuleContext(If_noelsestmtContext.class,0);
		}
		public IfstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterIfstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitIfstmt(this);
		}
	}

	public final IfstmtContext ifstmt() throws RecognitionException {
		IfstmtContext _localctx = new IfstmtContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_ifstmt);
		try {
			setState(275);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(273);
				ifelsestmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(274);
				if_noelsestmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_noelsestmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(MT22Parser.IF, 0); }
		public TerminalNode LB() { return getToken(MT22Parser.LB, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public TerminalNode RB() { return getToken(MT22Parser.RB, 0); }
		public LoopstmtContext loopstmt() {
			return getRuleContext(LoopstmtContext.class,0);
		}
		public If_noelsestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_noelsestmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterIf_noelsestmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitIf_noelsestmt(this);
		}
	}

	public final If_noelsestmtContext if_noelsestmt() throws RecognitionException {
		If_noelsestmtContext _localctx = new If_noelsestmtContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_if_noelsestmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			match(IF);
			setState(278);
			match(LB);
			setState(279);
			exprlist();
			setState(280);
			match(RB);
			setState(281);
			loopstmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfelsestmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(MT22Parser.IF, 0); }
		public TerminalNode LB() { return getToken(MT22Parser.LB, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public TerminalNode RB() { return getToken(MT22Parser.RB, 0); }
		public List<LoopstmtContext> loopstmt() {
			return getRuleContexts(LoopstmtContext.class);
		}
		public LoopstmtContext loopstmt(int i) {
			return getRuleContext(LoopstmtContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(MT22Parser.ELSE, 0); }
		public IfelsestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifelsestmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterIfelsestmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitIfelsestmt(this);
		}
	}

	public final IfelsestmtContext ifelsestmt() throws RecognitionException {
		IfelsestmtContext _localctx = new IfelsestmtContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_ifelsestmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			match(IF);
			setState(284);
			match(LB);
			setState(285);
			exprlist();
			setState(286);
			match(RB);
			setState(287);
			loopstmt();
			setState(288);
			match(ELSE);
			setState(289);
			loopstmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ForstmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(MT22Parser.FOR, 0); }
		public TerminalNode LB() { return getToken(MT22Parser.LB, 0); }
		public Scalar_variableContext scalar_variable() {
			return getRuleContext(Scalar_variableContext.class,0);
		}
		public TerminalNode EQ() { return getToken(MT22Parser.EQ, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MT22Parser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MT22Parser.COMMA, i);
		}
		public TerminalNode RB() { return getToken(MT22Parser.RB, 0); }
		public LoopstmtContext loopstmt() {
			return getRuleContext(LoopstmtContext.class,0);
		}
		public ForstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterForstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitForstmt(this);
		}
	}

	public final ForstmtContext forstmt() throws RecognitionException {
		ForstmtContext _localctx = new ForstmtContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_forstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(291);
			match(FOR);
			setState(292);
			match(LB);
			setState(293);
			scalar_variable();
			setState(294);
			match(EQ);
			setState(295);
			expr();
			setState(296);
			match(COMMA);
			setState(297);
			expr();
			setState(298);
			match(COMMA);
			setState(299);
			expr();
			setState(300);
			match(RB);
			setState(301);
			loopstmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhilestmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(MT22Parser.WHILE, 0); }
		public TerminalNode LB() { return getToken(MT22Parser.LB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RB() { return getToken(MT22Parser.RB, 0); }
		public LoopstmtContext loopstmt() {
			return getRuleContext(LoopstmtContext.class,0);
		}
		public WhilestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whilestmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterWhilestmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitWhilestmt(this);
		}
	}

	public final WhilestmtContext whilestmt() throws RecognitionException {
		WhilestmtContext _localctx = new WhilestmtContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_whilestmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			match(WHILE);
			setState(304);
			match(LB);
			setState(305);
			expr();
			setState(306);
			match(RB);
			setState(307);
			loopstmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Dowhile_stmtContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(MT22Parser.DO, 0); }
		public BlockstmtContext blockstmt() {
			return getRuleContext(BlockstmtContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(MT22Parser.WHILE, 0); }
		public TerminalNode LB() { return getToken(MT22Parser.LB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RB() { return getToken(MT22Parser.RB, 0); }
		public TerminalNode SEMI() { return getToken(MT22Parser.SEMI, 0); }
		public Dowhile_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dowhile_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterDowhile_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitDowhile_stmt(this);
		}
	}

	public final Dowhile_stmtContext dowhile_stmt() throws RecognitionException {
		Dowhile_stmtContext _localctx = new Dowhile_stmtContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_dowhile_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(309);
			match(DO);
			setState(310);
			blockstmt();
			setState(311);
			match(WHILE);
			setState(312);
			match(LB);
			setState(313);
			expr();
			setState(314);
			match(RB);
			setState(315);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturnstmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(MT22Parser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MT22Parser.SEMI, 0); }
		public ReturnstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterReturnstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitReturnstmt(this);
		}
	}

	public final ReturnstmtContext returnstmt() throws RecognitionException {
		ReturnstmtContext _localctx = new ReturnstmtContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_returnstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(317);
			match(RETURN);
			setState(318);
			expr();
			setState(319);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallstmtContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MT22Parser.ID, 0); }
		public TerminalNode LB() { return getToken(MT22Parser.LB, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public TerminalNode RB() { return getToken(MT22Parser.RB, 0); }
		public TerminalNode SEMI() { return getToken(MT22Parser.SEMI, 0); }
		public CallstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterCallstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitCallstmt(this);
		}
	}

	public final CallstmtContext callstmt() throws RecognitionException {
		CallstmtContext _localctx = new CallstmtContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_callstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(321);
			match(ID);
			setState(322);
			match(LB);
			setState(323);
			exprlist();
			setState(324);
			match(RB);
			setState(325);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ContinuestmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(MT22Parser.CONTINUE, 0); }
		public TerminalNode SEMI() { return getToken(MT22Parser.SEMI, 0); }
		public ContinuestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continuestmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterContinuestmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitContinuestmt(this);
		}
	}

	public final ContinuestmtContext continuestmt() throws RecognitionException {
		ContinuestmtContext _localctx = new ContinuestmtContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_continuestmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(327);
			match(CONTINUE);
			setState(328);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BreakstmtContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(MT22Parser.BREAK, 0); }
		public TerminalNode SEMI() { return getToken(MT22Parser.SEMI, 0); }
		public BreakstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterBreakstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitBreakstmt(this);
		}
	}

	public final BreakstmtContext breakstmt() throws RecognitionException {
		BreakstmtContext _localctx = new BreakstmtContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_breakstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(330);
			match(BREAK);
			setState(331);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockstmtContext extends ParserRuleContext {
		public TerminalNode LCB() { return getToken(MT22Parser.LCB, 0); }
		public BlocklistContext blocklist() {
			return getRuleContext(BlocklistContext.class,0);
		}
		public TerminalNode RCB() { return getToken(MT22Parser.RCB, 0); }
		public BlockstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_blockstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterBlockstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitBlockstmt(this);
		}
	}

	public final BlockstmtContext blockstmt() throws RecognitionException {
		BlockstmtContext _localctx = new BlockstmtContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_blockstmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(333);
			match(LCB);
			setState(334);
			blocklist();
			setState(335);
			match(RCB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LoopstmtContext extends ParserRuleContext {
		public BlockstmtContext blockstmt() {
			return getRuleContext(BlockstmtContext.class,0);
		}
		public StmtContext stmt() {
			return getRuleContext(StmtContext.class,0);
		}
		public LoopstmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loopstmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterLoopstmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitLoopstmt(this);
		}
	}

	public final LoopstmtContext loopstmt() throws RecognitionException {
		LoopstmtContext _localctx = new LoopstmtContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_loopstmt);
		try {
			setState(339);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(337);
				blockstmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(338);
				stmt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Scalar_variableContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MT22Parser.ID, 0); }
		public IndexopContext indexop() {
			return getRuleContext(IndexopContext.class,0);
		}
		public Scalar_variableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scalar_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterScalar_variable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitScalar_variable(this);
		}
	}

	public final Scalar_variableContext scalar_variable() throws RecognitionException {
		Scalar_variableContext _localctx = new Scalar_variableContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_scalar_variable);
		try {
			setState(343);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(341);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(342);
				indexop();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprlistContext extends ParserRuleContext {
		public ExpprimeContext expprime() {
			return getRuleContext(ExpprimeContext.class,0);
		}
		public ExprlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterExprlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitExprlist(this);
		}
	}

	public final ExprlistContext exprlist() throws RecognitionException {
		ExprlistContext _localctx = new ExprlistContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_exprlist);
		try {
			setState(347);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BOOLLIT:
			case FLOATLIT:
			case INTLIT:
			case STRINGLIT:
			case ID:
			case LB:
			case MINUS:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(345);
				expprime();
				}
				break;
			case RB:
			case SEMI:
			case RCB:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpprimeContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(MT22Parser.COMMA, 0); }
		public ExpprimeContext expprime() {
			return getRuleContext(ExpprimeContext.class,0);
		}
		public ExpprimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expprime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterExpprime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitExpprime(this);
		}
	}

	public final ExpprimeContext expprime() throws RecognitionException {
		ExpprimeContext _localctx = new ExpprimeContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_expprime);
		try {
			setState(354);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(349);
				expr();
				setState(350);
				match(COMMA);
				setState(351);
				expprime();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(353);
				expr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public List<Expr1Context> expr1() {
			return getRuleContexts(Expr1Context.class);
		}
		public Expr1Context expr1(int i) {
			return getRuleContext(Expr1Context.class,i);
		}
		public TerminalNode SCOPE() { return getToken(MT22Parser.SCOPE, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_expr);
		try {
			setState(361);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(356);
				expr1();
				setState(357);
				match(SCOPE);
				setState(358);
				expr1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(360);
				expr1();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr1Context extends ParserRuleContext {
		public List<Expr2Context> expr2() {
			return getRuleContexts(Expr2Context.class);
		}
		public Expr2Context expr2(int i) {
			return getRuleContext(Expr2Context.class,i);
		}
		public TerminalNode COMPARE() { return getToken(MT22Parser.COMPARE, 0); }
		public Expr1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterExpr1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitExpr1(this);
		}
	}

	public final Expr1Context expr1() throws RecognitionException {
		Expr1Context _localctx = new Expr1Context(_ctx, getState());
		enterRule(_localctx, 92, RULE_expr1);
		try {
			setState(368);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(363);
				expr2(0);
				setState(364);
				match(COMPARE);
				setState(365);
				expr2(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(367);
				expr2(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr2Context extends ParserRuleContext {
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public TerminalNode ANDOR() { return getToken(MT22Parser.ANDOR, 0); }
		public Expr2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterExpr2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitExpr2(this);
		}
	}

	public final Expr2Context expr2() throws RecognitionException {
		return expr2(0);
	}

	private Expr2Context expr2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr2Context _localctx = new Expr2Context(_ctx, _parentState);
		Expr2Context _prevctx = _localctx;
		int _startState = 94;
		enterRecursionRule(_localctx, 94, RULE_expr2, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(371);
			expr3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(378);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr2);
					setState(373);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(374);
					match(ANDOR);
					setState(375);
					expr3(0);
					}
					} 
				}
				setState(380);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expr3Context extends ParserRuleContext {
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public TerminalNode ADDSUB() { return getToken(MT22Parser.ADDSUB, 0); }
		public Expr3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr3; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterExpr3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitExpr3(this);
		}
	}

	public final Expr3Context expr3() throws RecognitionException {
		return expr3(0);
	}

	private Expr3Context expr3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr3Context _localctx = new Expr3Context(_ctx, _parentState);
		Expr3Context _prevctx = _localctx;
		int _startState = 96;
		enterRecursionRule(_localctx, 96, RULE_expr3, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(382);
			expr4(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(389);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr3);
					setState(384);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(385);
					match(ADDSUB);
					setState(386);
					expr4(0);
					}
					} 
				}
				setState(391);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expr4Context extends ParserRuleContext {
		public Expr5Context expr5() {
			return getRuleContext(Expr5Context.class,0);
		}
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public TerminalNode MULDIVMOD() { return getToken(MT22Parser.MULDIVMOD, 0); }
		public Expr4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr4; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterExpr4(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitExpr4(this);
		}
	}

	public final Expr4Context expr4() throws RecognitionException {
		return expr4(0);
	}

	private Expr4Context expr4(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr4Context _localctx = new Expr4Context(_ctx, _parentState);
		Expr4Context _prevctx = _localctx;
		int _startState = 98;
		enterRecursionRule(_localctx, 98, RULE_expr4, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(393);
			expr5();
			}
			_ctx.stop = _input.LT(-1);
			setState(400);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr4Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr4);
					setState(395);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(396);
					match(MULDIVMOD);
					setState(397);
					expr5();
					}
					} 
				}
				setState(402);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Expr5Context extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(MT22Parser.NOT, 0); }
		public Expr5Context expr5() {
			return getRuleContext(Expr5Context.class,0);
		}
		public Expr6Context expr6() {
			return getRuleContext(Expr6Context.class,0);
		}
		public Expr5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr5; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterExpr5(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitExpr5(this);
		}
	}

	public final Expr5Context expr5() throws RecognitionException {
		Expr5Context _localctx = new Expr5Context(_ctx, getState());
		enterRule(_localctx, 100, RULE_expr5);
		try {
			setState(406);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(403);
				match(NOT);
				setState(404);
				expr5();
				}
				break;
			case BOOLLIT:
			case FLOATLIT:
			case INTLIT:
			case STRINGLIT:
			case ID:
			case LB:
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(405);
				expr6();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr6Context extends ParserRuleContext {
		public TerminalNode MINUS() { return getToken(MT22Parser.MINUS, 0); }
		public Expr6Context expr6() {
			return getRuleContext(Expr6Context.class,0);
		}
		public Expr7Context expr7() {
			return getRuleContext(Expr7Context.class,0);
		}
		public Expr6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr6; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterExpr6(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitExpr6(this);
		}
	}

	public final Expr6Context expr6() throws RecognitionException {
		Expr6Context _localctx = new Expr6Context(_ctx, getState());
		enterRule(_localctx, 102, RULE_expr6);
		try {
			setState(411);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(408);
				match(MINUS);
				setState(409);
				expr6();
				}
				break;
			case BOOLLIT:
			case FLOATLIT:
			case INTLIT:
			case STRINGLIT:
			case ID:
			case LB:
				enterOuterAlt(_localctx, 2);
				{
				setState(410);
				expr7();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr7Context extends ParserRuleContext {
		public TerminalNode BOOLLIT() { return getToken(MT22Parser.BOOLLIT, 0); }
		public TerminalNode INTLIT() { return getToken(MT22Parser.INTLIT, 0); }
		public TerminalNode STRINGLIT() { return getToken(MT22Parser.STRINGLIT, 0); }
		public TerminalNode FLOATLIT() { return getToken(MT22Parser.FLOATLIT, 0); }
		public TerminalNode ID() { return getToken(MT22Parser.ID, 0); }
		public CallexprContext callexpr() {
			return getRuleContext(CallexprContext.class,0);
		}
		public SubexprContext subexpr() {
			return getRuleContext(SubexprContext.class,0);
		}
		public IndexopContext indexop() {
			return getRuleContext(IndexopContext.class,0);
		}
		public Expr7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr7; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterExpr7(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitExpr7(this);
		}
	}

	public final Expr7Context expr7() throws RecognitionException {
		Expr7Context _localctx = new Expr7Context(_ctx, getState());
		enterRule(_localctx, 104, RULE_expr7);
		try {
			setState(421);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(413);
				match(BOOLLIT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(414);
				match(INTLIT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(415);
				match(STRINGLIT);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(416);
				match(FLOATLIT);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(417);
				match(ID);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(418);
				callexpr();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(419);
				subexpr();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(420);
				indexop();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallexprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MT22Parser.ID, 0); }
		public TerminalNode LB() { return getToken(MT22Parser.LB, 0); }
		public ExprlistContext exprlist() {
			return getRuleContext(ExprlistContext.class,0);
		}
		public TerminalNode RB() { return getToken(MT22Parser.RB, 0); }
		public CallexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_callexpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterCallexpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitCallexpr(this);
		}
	}

	public final CallexprContext callexpr() throws RecognitionException {
		CallexprContext _localctx = new CallexprContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_callexpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(423);
			match(ID);
			setState(424);
			match(LB);
			setState(425);
			exprlist();
			setState(426);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubexprContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(MT22Parser.LB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RB() { return getToken(MT22Parser.RB, 0); }
		public SubexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subexpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterSubexpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitSubexpr(this);
		}
	}

	public final SubexprContext subexpr() throws RecognitionException {
		SubexprContext _localctx = new SubexprContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_subexpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(428);
			match(LB);
			setState(429);
			expr();
			setState(430);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IndexopContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MT22Parser.ID, 0); }
		public TerminalNode SQLB() { return getToken(MT22Parser.SQLB, 0); }
		public ExpprimeContext expprime() {
			return getRuleContext(ExpprimeContext.class,0);
		}
		public TerminalNode SQRB() { return getToken(MT22Parser.SQRB, 0); }
		public IndexopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_indexop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).enterIndexop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MT22Listener ) ((MT22Listener)listener).exitIndexop(this);
		}
	}

	public final IndexopContext indexop() throws RecognitionException {
		IndexopContext _localctx = new IndexopContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_indexop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(432);
			match(ID);
			setState(433);
			match(SQLB);
			setState(434);
			expprime();
			setState(435);
			match(SQRB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 47:
			return expr2_sempred((Expr2Context)_localctx, predIndex);
		case 48:
			return expr3_sempred((Expr3Context)_localctx, predIndex);
		case 49:
			return expr4_sempred((Expr4Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr2_sempred(Expr2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr3_sempred(Expr3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr4_sempred(Expr4Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A\u01b8\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\3\2\3\3\3\3\3\3"+
		"\3\3\5\3z\n\3\3\4\3\4\5\4~\n\4\3\5\3\5\3\5\5\5\u0083\n\5\3\6\3\6\3\6\3"+
		"\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\5\n"+
		"\u0099\n\n\3\13\3\13\5\13\u009d\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\r\3\16\3\16\5\16\u00ad\n\16\3\17\3\17\3\17\3\17\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00be\n\21\3\22\3\22"+
		"\3\22\3\22\5\22\u00c4\n\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\24\3\24\3\24\3\24\5\24\u00d4\n\24\3\25\3\25\3\25\3\25\3\26\3\26"+
		"\5\26\u00dc\n\26\3\27\3\27\3\27\3\27\3\27\5\27\u00e3\n\27\3\30\3\30\5"+
		"\30\u00e7\n\30\3\30\3\30\3\31\3\31\3\31\5\31\u00ee\n\31\3\32\3\32\3\32"+
		"\3\32\3\33\3\33\3\33\5\33\u00f7\n\33\3\34\3\34\3\34\3\34\5\34\u00fd\n"+
		"\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0109\n\35"+
		"\3\36\3\36\5\36\u010d\n\36\3\37\3\37\3\37\3\37\3\37\3 \3 \5 \u0116\n "+
		"\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3"+
		"#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3"+
		"&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3+\3+\5+\u0156"+
		"\n+\3,\3,\5,\u015a\n,\3-\3-\5-\u015e\n-\3.\3.\3.\3.\3.\5.\u0165\n.\3/"+
		"\3/\3/\3/\3/\5/\u016c\n/\3\60\3\60\3\60\3\60\3\60\5\60\u0173\n\60\3\61"+
		"\3\61\3\61\3\61\3\61\3\61\7\61\u017b\n\61\f\61\16\61\u017e\13\61\3\62"+
		"\3\62\3\62\3\62\3\62\3\62\7\62\u0186\n\62\f\62\16\62\u0189\13\62\3\63"+
		"\3\63\3\63\3\63\3\63\3\63\7\63\u0191\n\63\f\63\16\63\u0194\13\63\3\64"+
		"\3\64\3\64\5\64\u0199\n\64\3\65\3\65\3\65\5\65\u019e\n\65\3\66\3\66\3"+
		"\66\3\66\3\66\3\66\3\66\3\66\5\66\u01a8\n\66\3\67\3\67\3\67\3\67\3\67"+
		"\38\38\38\38\39\39\39\39\39\39\2\5`bd:\2\4\6\b\n\f\16\20\22\24\26\30\32"+
		"\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\4\4\2\b\b"+
		"\n\r\4\2\b\b\n\f\2\u01af\2r\3\2\2\2\4y\3\2\2\2\6}\3\2\2\2\b\u0082\3\2"+
		"\2\2\n\u0084\3\2\2\2\f\u0089\3\2\2\2\16\u0090\3\2\2\2\20\u0092\3\2\2\2"+
		"\22\u0098\3\2\2\2\24\u009c\3\2\2\2\26\u009e\3\2\2\2\30\u00a3\3\2\2\2\32"+
		"\u00ac\3\2\2\2\34\u00ae\3\2\2\2\36\u00b2\3\2\2\2 \u00bd\3\2\2\2\"\u00bf"+
		"\3\2\2\2$\u00c7\3\2\2\2&\u00d3\3\2\2\2(\u00d5\3\2\2\2*\u00db\3\2\2\2,"+
		"\u00e2\3\2\2\2.\u00e6\3\2\2\2\60\u00ea\3\2\2\2\62\u00ef\3\2\2\2\64\u00f6"+
		"\3\2\2\2\66\u00fc\3\2\2\28\u0108\3\2\2\2:\u010c\3\2\2\2<\u010e\3\2\2\2"+
		">\u0115\3\2\2\2@\u0117\3\2\2\2B\u011d\3\2\2\2D\u0125\3\2\2\2F\u0131\3"+
		"\2\2\2H\u0137\3\2\2\2J\u013f\3\2\2\2L\u0143\3\2\2\2N\u0149\3\2\2\2P\u014c"+
		"\3\2\2\2R\u014f\3\2\2\2T\u0155\3\2\2\2V\u0159\3\2\2\2X\u015d\3\2\2\2Z"+
		"\u0164\3\2\2\2\\\u016b\3\2\2\2^\u0172\3\2\2\2`\u0174\3\2\2\2b\u017f\3"+
		"\2\2\2d\u018a\3\2\2\2f\u0198\3\2\2\2h\u019d\3\2\2\2j\u01a7\3\2\2\2l\u01a9"+
		"\3\2\2\2n\u01ae\3\2\2\2p\u01b2\3\2\2\2rs\5\4\3\2st\7\2\2\3t\3\3\2\2\2"+
		"uv\5\6\4\2vw\5\4\3\2wz\3\2\2\2xz\5\6\4\2yu\3\2\2\2yx\3\2\2\2z\5\3\2\2"+
		"\2{~\5\b\5\2|~\5\"\22\2}{\3\2\2\2}|\3\2\2\2~\7\3\2\2\2\177\u0083\5\n\6"+
		"\2\u0080\u0083\5\f\7\2\u0081\u0083\5\24\13\2\u0082\177\3\2\2\2\u0082\u0080"+
		"\3\2\2\2\u0082\u0081\3\2\2\2\u0083\t\3\2\2\2\u0084\u0085\5\22\n\2\u0085"+
		"\u0086\7\'\2\2\u0086\u0087\5\16\b\2\u0087\u0088\7&\2\2\u0088\13\3\2\2"+
		"\2\u0089\u008a\5\22\n\2\u008a\u008b\7\'\2\2\u008b\u008c\5\16\b\2\u008c"+
		"\u008d\7=\2\2\u008d\u008e\5X-\2\u008e\u008f\7&\2\2\u008f\r\3\2\2\2\u0090"+
		"\u0091\t\2\2\2\u0091\17\3\2\2\2\u0092\u0093\t\3\2\2\u0093\21\3\2\2\2\u0094"+
		"\u0095\7\37\2\2\u0095\u0096\7%\2\2\u0096\u0099\5\22\n\2\u0097\u0099\7"+
		"\37\2\2\u0098\u0094\3\2\2\2\u0098\u0097\3\2\2\2\u0099\23\3\2\2\2\u009a"+
		"\u009d\5\26\f\2\u009b\u009d\5\30\r\2\u009c\u009a\3\2\2\2\u009c\u009b\3"+
		"\2\2\2\u009d\25\3\2\2\2\u009e\u009f\5\22\n\2\u009f\u00a0\7\'\2\2\u00a0"+
		"\u00a1\5\36\20\2\u00a1\u00a2\7&\2\2\u00a2\27\3\2\2\2\u00a3\u00a4\5\22"+
		"\n\2\u00a4\u00a5\7\'\2\2\u00a5\u00a6\5\36\20\2\u00a6\u00a7\7=\2\2\u00a7"+
		"\u00a8\5\32\16\2\u00a8\u00a9\7&\2\2\u00a9\31\3\2\2\2\u00aa\u00ad\7\37"+
		"\2\2\u00ab\u00ad\5\34\17\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad"+
		"\33\3\2\2\2\u00ae\u00af\7(\2\2\u00af\u00b0\5X-\2\u00b0\u00b1\7)\2\2\u00b1"+
		"\35\3\2\2\2\u00b2\u00b3\7\17\2\2\u00b3\u00b4\7\"\2\2\u00b4\u00b5\5 \21"+
		"\2\u00b5\u00b6\7#\2\2\u00b6\u00b7\7\16\2\2\u00b7\u00b8\5\20\t\2\u00b8"+
		"\37\3\2\2\2\u00b9\u00ba\7\6\2\2\u00ba\u00bb\7%\2\2\u00bb\u00be\5 \21\2"+
		"\u00bc\u00be\7\6\2\2\u00bd\u00b9\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be!\3"+
		"\2\2\2\u00bf\u00c3\5$\23\2\u00c0\u00c1\7\3\2\2\u00c1\u00c4\7\37\2\2\u00c2"+
		"\u00c4\3\2\2\2\u00c3\u00c0\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3\2"+
		"\2\2\u00c5\u00c6\5(\25\2\u00c6#\3\2\2\2\u00c7\u00c8\7\37\2\2\u00c8\u00c9"+
		"\7\'\2\2\u00c9\u00ca\7\21\2\2\u00ca\u00cb\5&\24\2\u00cb\u00cc\7 \2\2\u00cc"+
		"\u00cd\5*\26\2\u00cd\u00ce\7!\2\2\u00ce%\3\2\2\2\u00cf\u00d4\5\20\t\2"+
		"\u00d0\u00d4\7\t\2\2\u00d1\u00d4\7\r\2\2\u00d2\u00d4\5\36\20\2\u00d3\u00cf"+
		"\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4"+
		"\'\3\2\2\2\u00d5\u00d6\7(\2\2\u00d6\u00d7\5\66\34\2\u00d7\u00d8\7)\2\2"+
		"\u00d8)\3\2\2\2\u00d9\u00dc\5,\27\2\u00da\u00dc\3\2\2\2\u00db\u00d9\3"+
		"\2\2\2\u00db\u00da\3\2\2\2\u00dc+\3\2\2\2\u00dd\u00de\5.\30\2\u00de\u00df"+
		"\7%\2\2\u00df\u00e0\5,\27\2\u00e0\u00e3\3\2\2\2\u00e1\u00e3\5.\30\2\u00e2"+
		"\u00dd\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3-\3\2\2\2\u00e4\u00e7\5\60\31"+
		"\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8"+
		"\3\2\2\2\u00e8\u00e9\5\62\32\2\u00e9/\3\2\2\2\u00ea\u00ed\7\3\2\2\u00eb"+
		"\u00ee\7\3\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ec\3\2"+
		"\2\2\u00ee\61\3\2\2\2\u00ef\u00f0\7\37\2\2\u00f0\u00f1\7\'\2\2\u00f1\u00f2"+
		"\5\64\33\2\u00f2\63\3\2\2\2\u00f3\u00f7\5\20\t\2\u00f4\u00f7\7\r\2\2\u00f5"+
		"\u00f7\5\36\20\2\u00f6\u00f3\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3"+
		"\2\2\2\u00f7\65\3\2\2\2\u00f8\u00f9\5:\36\2\u00f9\u00fa\5\66\34\2\u00fa"+
		"\u00fd\3\2\2\2\u00fb\u00fd\3\2\2\2\u00fc\u00f8\3\2\2\2\u00fc\u00fb\3\2"+
		"\2\2\u00fd\67\3\2\2\2\u00fe\u0109\5<\37\2\u00ff\u0109\5> \2\u0100\u0109"+
		"\5J&\2\u0101\u0109\5L\'\2\u0102\u0109\5D#\2\u0103\u0109\5F$\2\u0104\u0109"+
		"\5H%\2\u0105\u0109\5N(\2\u0106\u0109\5P)\2\u0107\u0109\5R*\2\u0108\u00fe"+
		"\3\2\2\2\u0108\u00ff\3\2\2\2\u0108\u0100\3\2\2\2\u0108\u0101\3\2\2\2\u0108"+
		"\u0102\3\2\2\2\u0108\u0103\3\2\2\2\u0108\u0104\3\2\2\2\u0108\u0105\3\2"+
		"\2\2\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u01099\3\2\2\2\u010a\u010d"+
		"\58\35\2\u010b\u010d\5\b\5\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2\2\2\u010d"+
		";\3\2\2\2\u010e\u010f\5V,\2\u010f\u0110\7=\2\2\u0110\u0111\5\\/\2\u0111"+
		"\u0112\7&\2\2\u0112=\3\2\2\2\u0113\u0116\5B\"\2\u0114\u0116\5@!\2\u0115"+
		"\u0113\3\2\2\2\u0115\u0114\3\2\2\2\u0116?\3\2\2\2\u0117\u0118\7\22\2\2"+
		"\u0118\u0119\7 \2\2\u0119\u011a\5X-\2\u011a\u011b\7!\2\2\u011b\u011c\5"+
		"T+\2\u011cA\3\2\2\2\u011d\u011e\7\22\2\2\u011e\u011f\7 \2\2\u011f\u0120"+
		"\5X-\2\u0120\u0121\7!\2\2\u0121\u0122\5T+\2\u0122\u0123\7\23\2\2\u0123"+
		"\u0124\5T+\2\u0124C\3\2\2\2\u0125\u0126\7\27\2\2\u0126\u0127\7 \2\2\u0127"+
		"\u0128\5V,\2\u0128\u0129\7=\2\2\u0129\u012a\5\\/\2\u012a\u012b\7%\2\2"+
		"\u012b\u012c\5\\/\2\u012c\u012d\7%\2\2\u012d\u012e\5\\/\2\u012e\u012f"+
		"\7!\2\2\u012f\u0130\5T+\2\u0130E\3\2\2\2\u0131\u0132\7\32\2\2\u0132\u0133"+
		"\7 \2\2\u0133\u0134\5\\/\2\u0134\u0135\7!\2\2\u0135\u0136\5T+\2\u0136"+
		"G\3\2\2\2\u0137\u0138\7\31\2\2\u0138\u0139\5R*\2\u0139\u013a\7\32\2\2"+
		"\u013a\u013b\7 \2\2\u013b\u013c\5\\/\2\u013c\u013d\7!\2\2\u013d\u013e"+
		"\7&\2\2\u013eI\3\2\2\2\u013f\u0140\7\25\2\2\u0140\u0141\5\\/\2\u0141\u0142"+
		"\7&\2\2\u0142K\3\2\2\2\u0143\u0144\7\37\2\2\u0144\u0145\7 \2\2\u0145\u0146"+
		"\5X-\2\u0146\u0147\7!\2\2\u0147\u0148\7&\2\2\u0148M\3\2\2\2\u0149\u014a"+
		"\7\30\2\2\u014a\u014b\7&\2\2\u014bO\3\2\2\2\u014c\u014d\7\24\2\2\u014d"+
		"\u014e\7&\2\2\u014eQ\3\2\2\2\u014f\u0150\7(\2\2\u0150\u0151\5\66\34\2"+
		"\u0151\u0152\7)\2\2\u0152S\3\2\2\2\u0153\u0156\5R*\2\u0154\u0156\58\35"+
		"\2\u0155\u0153\3\2\2\2\u0155\u0154\3\2\2\2\u0156U\3\2\2\2\u0157\u015a"+
		"\7\37\2\2\u0158\u015a\5p9\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015a"+
		"W\3\2\2\2\u015b\u015e\5Z.\2\u015c\u015e\3\2\2\2\u015d\u015b\3\2\2\2\u015d"+
		"\u015c\3\2\2\2\u015eY\3\2\2\2\u015f\u0160\5\\/\2\u0160\u0161\7%\2\2\u0161"+
		"\u0162\5Z.\2\u0162\u0165\3\2\2\2\u0163\u0165\5\\/\2\u0164\u015f\3\2\2"+
		"\2\u0164\u0163\3\2\2\2\u0165[\3\2\2\2\u0166\u0167\5^\60\2\u0167\u0168"+
		"\7<\2\2\u0168\u0169\5^\60\2\u0169\u016c\3\2\2\2\u016a\u016c\5^\60\2\u016b"+
		"\u0166\3\2\2\2\u016b\u016a\3\2\2\2\u016c]\3\2\2\2\u016d\u016e\5`\61\2"+
		"\u016e\u016f\7-\2\2\u016f\u0170\5`\61\2\u0170\u0173\3\2\2\2\u0171\u0173"+
		"\5`\61\2\u0172\u016d\3\2\2\2\u0172\u0171\3\2\2\2\u0173_\3\2\2\2\u0174"+
		"\u0175\b\61\1\2\u0175\u0176\5b\62\2\u0176\u017c\3\2\2\2\u0177\u0178\f"+
		"\4\2\2\u0178\u0179\7,\2\2\u0179\u017b\5b\62\2\u017a\u0177\3\2\2\2\u017b"+
		"\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017da\3\2\2\2"+
		"\u017e\u017c\3\2\2\2\u017f\u0180\b\62\1\2\u0180\u0181\5d\63\2\u0181\u0187"+
		"\3\2\2\2\u0182\u0183\f\4\2\2\u0183\u0184\7*\2\2\u0184\u0186\5d\63\2\u0185"+
		"\u0182\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2"+
		"\2\2\u0188c\3\2\2\2\u0189\u0187\3\2\2\2\u018a\u018b\b\63\1\2\u018b\u018c"+
		"\5f\64\2\u018c\u0192\3\2\2\2\u018d\u018e\f\4\2\2\u018e\u018f\7+\2\2\u018f"+
		"\u0191\5f\64\2\u0190\u018d\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2"+
		"\2\2\u0192\u0193\3\2\2\2\u0193e\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0196"+
		"\7\63\2\2\u0196\u0199\5f\64\2\u0197\u0199\5h\65\2\u0198\u0195\3\2\2\2"+
		"\u0198\u0197\3\2\2\2\u0199g\3\2\2\2\u019a\u019b\7/\2\2\u019b\u019e\5h"+
		"\65\2\u019c\u019e\5j\66\2\u019d\u019a\3\2\2\2\u019d\u019c\3\2\2\2\u019e"+
		"i\3\2\2\2\u019f\u01a8\7\4\2\2\u01a0\u01a8\7\6\2\2\u01a1\u01a8\7\7\2\2"+
		"\u01a2\u01a8\7\5\2\2\u01a3\u01a8\7\37\2\2\u01a4\u01a8\5l\67\2\u01a5\u01a8"+
		"\5n8\2\u01a6\u01a8\5p9\2\u01a7\u019f\3\2\2\2\u01a7\u01a0\3\2\2\2\u01a7"+
		"\u01a1\3\2\2\2\u01a7\u01a2\3\2\2\2\u01a7\u01a3\3\2\2\2\u01a7\u01a4\3\2"+
		"\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8k\3\2\2\2\u01a9\u01aa"+
		"\7\37\2\2\u01aa\u01ab\7 \2\2\u01ab\u01ac\5X-\2\u01ac\u01ad\7!\2\2\u01ad"+
		"m\3\2\2\2\u01ae\u01af\7 \2\2\u01af\u01b0\5\\/\2\u01b0\u01b1\7!\2\2\u01b1"+
		"o\3\2\2\2\u01b2\u01b3\7\37\2\2\u01b3\u01b4\7\"\2\2\u01b4\u01b5\5Z.\2\u01b5"+
		"\u01b6\7#\2\2\u01b6q\3\2\2\2 y}\u0082\u0098\u009c\u00ac\u00bd\u00c3\u00d3"+
		"\u00db\u00e2\u00e6\u00ed\u00f6\u00fc\u0108\u010c\u0115\u0155\u0159\u015d"+
		"\u0164\u016b\u0172\u017c\u0187\u0192\u0198\u019d\u01a7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}