// 2012018
grammar MT22;

@lexer::header {
from lexererr import *
  
}
@members{  

}
options{
	language=Python3;        
}

program: decllist EOF;

decllist: decl decllist | decl;

decl: vardecl | funcdecl;
/**************************************************** VARIABLE/ARRAY DECLARE **********************************************/
vardecl: varnoinit | varassign | array; 

varnoinit: idlist COLON vartype SEMI; 

varassign: idlist COLON vartype EQ expprime SEMI; 
// basecase: ID COLON vartype EQ expr;
// helper: ID COMMA helper COMMA expr | basecase; 
// py run.py test ASTGenSuite
vartype: INTEGER | FLOAT | BOOLEAN | STRING | AUTO; 


atomic_type : INTEGER | FLOAT | BOOLEAN | STRING;

idlist: ID COMMA idlist | ID ;

/* Array Declaration */ 
array: arraydecl | arrayinit; 
arraydecl: idlist COLON arrayParam SEMI;
arrayinit: idlist COLON arrayParam EQ exprlist SEMI;


//arraylit: expprime | arrayValList;
//arrayValList: arrayVal COMMA arrayValList | arrayVal;  
arrayVal: LCB exprlist RCB;
arrayParam: ARR SQLB dimension SQRB OF atomic_type; 
dimension: INTLIT COMMA dimension | INTLIT;
/**************************************************** FUNCTION DECLARE **********************************************/
/* Array Declaration */
funcdecl: base_funcdecl (PARAM_KEYWORDS ID| ) blockstmt;
base_funcdecl: ID COLON FUNCTION returntype LB paramlist RB;
returntype: atomic_type | VOID | AUTO | arrayParam; 
paramlist: paramprime | ; 
paramprime: param COMMA paramprime | param;
param: (paramHead | ) parambase;
paramHead: PARAM_KEYWORDS (PARAM_KEYWORDS|);
parambase: ID COLON paramtype; 
paramtype: atomic_type | AUTO | arrayParam;
// stmtlist: stmt stmtlist |   ;
blocklist: allowed_blockstmt blocklist | ;  
/**************************************************** STATEMENT **********************************************/
stmt: assignstmt | ifstmt| returnstmt | callstmt | forstmt| whilestmt | dowhile_stmt | continuestmt |breakstmt | blockstmt; 
allowed_blockstmt: stmt | vardecl; 
assignstmt: scalar_variable EQ expr SEMI;

ifstmt: IF LB expr RB loopstmt (ELSE loopstmt | ); 


/* loop statement */
forstmt: FOR LB scalar_variable EQ expr COMMA expr COMMA expr RB loopstmt;
whilestmt: WHILE LB expr RB loopstmt;
dowhile_stmt: DO blockstmt WHILE LB expr RB SEMI; 
/* loop statement */
returnstmt: RETURN (expr | ) SEMI; 
callstmt: ID LB exprlist RB SEMI; 
continuestmt: CONTINUE SEMI;
breakstmt: BREAK SEMI;
blockstmt: LCB blocklist RCB;  
loopstmt: blockstmt | stmt; // (STMT | VARDECL | )
/* Statement */

scalar_variable: ID |  indexop; 


/**************************************************** EXPRESSION LIST **********************************************/
exprlist: expprime | ;
expprime: expr COMMA expprime | expr;
expr: expr1 SCOPE expr1 | expr1; 
expr1: expr2 COMPARE expr2 | expr2;
expr2: expr2 ANDOR expr3 | expr3; 
expr3: expr3 (ADD | MINUS) expr4 | expr4;  
expr4: expr4 MULDIVMOD expr5 | expr5;
expr5: NOT expr5 | expr6; 
expr6: MINUS expr6 | expr7;
expr7: BOOLLIT | INTLIT | STRINGLIT | FLOATLIT | ID | callexpr | subexpr | indexop| arrayVal; 
callexpr: ID LB exprlist RB; 
subexpr: LB expr RB; 
indexop: ID SQLB expprime SQRB;
/* expression list */
/**************************************************** FRAGMENTS **********************************************/

fragment EXPPART: [eE] [-+]? [0-9]+;
fragment DOT: '.'; 
fragment DECPART: DOT [0-9]+;   
fragment StringChar: ~[\b\f\r\n\t"\\] | ESC2; 
fragment ESC2: '\\' [bfrnt"\\];
fragment DOUBLEQ : '"';
fragment IllegalString
    : '\\' ~[bfrnt"\\]
    | '\\'
    ;

/***************************************************** Lexer *************************************************/
PARAM_KEYWORDS: INHERIT | OUT;  
BOOLLIT: TRUE | FALSE;

FLOATLIT: (INTLIT DECPART | INTLIT DECPART EXPPART | INTLIT EXPPART | DECPART EXPPART? | INTLIT DOT | DOT EXPPART) {self.text = self.text.replace('_', '')};
/* 1. ; .e ;  */
INTLIT: '0' | [1-9] ('_'?[0-9])* {self.text = self.text.replace('_', '')};

STRINGLIT: DOUBLEQ (StringChar*) DOUBLEQ
    {
        result = str(self.text)
        self.text = result[1:-1]
    };

 /* TYPE */
  INTEGER: 'integer'; 	
 VOID: 'void'; 				
  FLOAT: 'float';		
  BOOLEAN: 'boolean';
  STRING: 'string';		
 /* TYPE */

 /* KEYWORD */
AUTO: 'auto';			
OF: 'of';
ARR : 'array';			
INHERIT: 'inherit';
FUNCTION: 'function';
 IF: 'if';				
 ELSE: 'else';		
 BREAK: 'break';		
 RETURN: 'return';			
 OUT: 'out';
 FOR: 'for';				
 CONTINUE: 'continue';		
 DO: 'do';			
 WHILE: 'while';
 TRUE: 'true';
 FALSE: 'false'; 			

/* KEYWORDS */
// .e12 , 12. , .111, .1e2 

/* COMMENT */
COMMENT: '//' ~[\r\n]* -> skip;
C_COMMENT: '/*' .*? '*/' -> skip;
/* COMMENT */

ID: [_a-zA-Z][_a-zA-Z0-9]*; // key word not check now (ass1)

/* SEPERATORS */ 	
 LB :  '('; 		
 RB: ')';  	 
 SQLB: '['; 		
 SQRB: ']';  
 COMMA: ',';  
 SEMI: ';';  		
 COLON: ':';
 LCB: '{';  		
 RCB: '}';  	  
/* SEPERATORS */ 	

/*OPERATORS */     
// ADDSUB: ADD | MINUS; 
MULDIVMOD: MUL | DIV | PCENT; 
ANDOR: AND | OR; 
COMPARE: SAME | NOTSAME | HIGHER | HIGHER_EQ | LOWER | LOWER_EQ;
ADD: '+';	
 MINUS: '-'; 		
 MUL: '*';		
 DIV: '/'; 		
 PCENT: '%';
 NOT: '!'; 	
 AND: '&&'; 			
 OR: '||'; 		
 SAME: '=='; 	
 NOTSAME: '!=';
 LOWER: '<';		
 HIGHER: '>';		
 LOWER_EQ: '<=';					
 HIGHER_EQ: '>='; 
 SCOPE: '::';  
  EQ: '=';
/*OPERATORS */ 


WS : [ \t\r\n]+ -> skip ;

/* ERROR HANDLING */
//UNDERTERMINATED_COMMENT: '/*' .* (~[/*] | EOF) {raise UnterminatedComment(self.text[2:])};
UNCLOSE_STRING: DOUBLEQ StringChar* ([\b\t\f\n\r"\\] | EOF)
    {
        unclose_str = str(self.text)
        possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
        if unclose_str[-1] in possible:
            raise UncloseString(unclose_str[1:-1])
        else:
            raise UncloseString(unclose_str[1:])
    }
    ;
ILLEGAL_ESCAPE:DOUBLEQ StringChar* IllegalString
    {
        illegal_str = str(self.text)
        raise IllegalEscape(illegal_str[1:])
    }
    ;   
ERROR_CHAR: .
    {
        raise ErrorToken(self.text)
    }
    ;
/* ERROR HANDLING */

// py run.py test LexerSuite
// py run.py gen