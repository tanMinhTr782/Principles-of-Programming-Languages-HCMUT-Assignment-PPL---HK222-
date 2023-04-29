//2012018
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;

// KEYWORDS

AUTO: 'auto';			FALSE: 'false'; 			OF: 'of';			INHERIT: 'inherit';
INTEGER: 'integer'; 	VOID: 'void'; 				FLOAT: 'float';		BOOLEAN: 'boolean';		
ARRAY: 'array';			FUNCTION: 'function';		STRING: 'string';
BREAK: 'break';			RETURN: 'return';			OUT: 'out';
FOR: 'for';				CONTINUE: 'continue';		DO: 'do';			WHILE: 'while';
IF: 'if';				ELSE: 'else';				TRUE: 'true';

// OPERATORS

ADD: '+'; 		MINUS: '-'; 		MUL: '*';		DIV: '/'; 		PCENT: '%';
EXCLAM: '!'; 	AND: '&&'; 			OR: '||'; 		SAME: '=='; 	NOTSAME: '!=';
LOWER: '<';		HIGHER: '>';		LOWER_EQ: '<=';					HIGHER_EQ: '>='; 
SCOPE: '::';  

// SEPERATORS
LB :  '('; 		RB: ')';  	 SQLB: '['; 		SQRB: ']';  
DOT:  '.';  	COMMA: ',';  SEMI: ';';  		COLON: ':';
LCB: '{';  		RCB: '}';  	 EQ: '='; 

// ESCAPE SEQUENCE
BACKSPACE: '\b';			FORM_FEED: '\f'; 
CARRIAGE_RETURN: '\r'; 		NEWLINE: '\n'; 
HORIZONTAL_TAB: '\t'; 		SINGLE_QUOTE: ' \\' '; 
BACKSLASH: '\\'; 			DOUBLE_QUOTE: ' \' \' ';
DOUBLE_QUOTE_IN_STRING: ('\') DOUBLE_QUOTE;  

ESCAPE: BACKSPACE | FORM_FEED | CARRIAGE_RETURN | NEWLINE
		| HORIZONTAL_TAB | SINGLE_QUOTE | BACKSLASH; 

INTLIT: [1-9]('_')?[0-9]* | 0 {self.text = self.text.replace("_", "")};
FLOATLIT: INTLIT ('.'[0-9]* [eE]? [0-9]*) | ([eE]? [+-]? [0-9]*)?; 
BOOLLIT: 'true' | 'false'; 
STRINGLIT: DOUBLE_QUOTE []*ESCAPE? DOUBLE_QUOTE; 
ARRAY : LCB () RCB; 		
VOID: 'void'; 
AUTOTYPE: 'auto'; 
// 
ID: ['_'a-zA-Z]['_'a-zA-Z0-9]*; 

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
//////////////////////DECLARATIONS/////////////////////////////
program: decllist EOF;
decllist: decl decllist | decl;
decl: vardecl | funcdecl; 

vardecl: idlist COLON TYPE (EXPLIST)? SEMI; 
idlist: ID COMMA idlist | ID;
// not check the case when size ID = SIZE EXP. 
funcdecl: ID COLON TYPE LB paramlist RB (LCB INHERIT ID RCB)? body ;

paramlist: paramprime | ; 
paramprime: INHERIT? OUT? idlist COLON TYPE SEMI paramprime | param;
param: idlist COLON TYPE;  

body: LCB stmtlist RCB; 
stmtlist: stmt stmtlist |  ; 

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;