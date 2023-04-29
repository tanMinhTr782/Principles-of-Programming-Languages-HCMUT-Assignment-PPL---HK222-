//2012018
grammar MT22;

@lexer::header {
from lexererr import *
  
}
@members{  

}
options{
	language=Python3;        
}
// py run.py test ParserSuite
// py run.py test LexerSuite
// py run.py gen
program: decllist EOF;

decllist: decl decllist | decl;

decl: vardecl | funcdecl;


vardecl: varnoinit | varassign | array; 


varnoinit: idlist COLON vartype SEMI; 

varassign: helper SEMI; 
basecase: ID COLON vartype EQ expr;
helper: ID COMMA helper COMMA expr | basecase; 

vartype: INTEGER | FLOAT | BOOLEAN | STRING | AUTO; 


atomic_type : INTEGER | FLOAT | BOOLEAN | STRING;

idlist: ID COMMA idlist | ID ;

/* Array Declaration */ 
array: arraydecl | arrayinit; 
arraydecl: idlist COLON arrayParam SEMI;
arrayinit: idlist COLON arrayParam EQ arraylit SEMI;

// arrayAccess: arrayAssign | arrayIndex; 
// arrayAssign: ID SQLB dimension SQRB EQ expr SEMI;
// arrayIndex: ID SQLB dimension SQRB SEMI; 

arraylit: ID | arrayVal; 
arrayVal: LCB exprlist RCB;
arrayParam: ARR SQLB dimension SQRB OF atomic_type; 
dimension: INTLIT COMMA dimension | INTLIT;
    
/* Array Declaration */

funcdecl: ID COLON FUNCTION (atomic_type | VOID | AUTO | arrayParam) LB paramlist RB inherit_part body ;
inherit_part: INHERIT ID; 
body: LCB blocklist RCB;

paramlist: paramprime | ; 
paramprime: param COMMA paramprime | param;
param: INHERIT? OUT? ID COLON (atomic_type | AUTO | arrayParam);  

stmtlist: stmt stmtlist |   ;
blocklist: allowed_blockstmt blocklist | ;  
/* Statement */
stmt: assignstmt | ifstmt| returnstmt | callstmt | forstmt| whilestmt | dowhile_stmt | continuestmt |breakstmt | blockstmt; 
allowed_blockstmt: stmt | vardecl; 
assignstmt: scalar_variable EQ expr SEMI;
ifstmt: IF LB exprlist RB loopstmt (ELSE loopstmt | ); 
/* loop statement */
forstmt: FOR LB scalar_variable EQ expr COMMA expr COMMA expr RB loopstmt;
whilestmt: WHILE LB expr RB loopstmt;
dowhile_stmt: DO blockstmt WHILE LB expr RB SEMI; 
/* loop statement */
returnstmt: RETURN expr SEMI; 
callstmt: ID LB exprlist RB SEMI; 
continuestmt: CONTINUE SEMI;
breakstmt: BREAK SEMI;
blockstmt: LCB blocklist RCB;
loopstmt: blockstmt | stmt; 
/* Statement */

scalar_variable: ID |  indexop; 


/* expression list */
exprlist: expprime | ;
expprime: expr COMMA expprime | expr;
expr: expr1 SCOPE expr1 | expr1; 
expr1: expr2 (SAME | NOTSAME | HIGHER | HIGHER_EQ | LOWER | LOWER_EQ ) expr2 | expr2;
expr2: expr2 (AND| OR) expr3 | expr3; 
expr3: expr3 (ADD | MINUS) expr4 | expr4;  
expr4: expr4 (MUL | DIV | PCENT) expr5 | expr5;
expr5: NOT expr5 | expr6; 
expr6: MINUS expr6 | expr7;
expr7: BOOLLIT | INTLIT | STRINGLIT | FLOATLIT | ID | callexpr | subexpr | indexop; 
callexpr: ID LB exprlist RB; 
subexpr: LB expr RB; 
indexop: ID SQLB expprime SQRB;
/* expression list */
/**************************************************** FRAGMENTS **********************************************/

fragment EXPPART: [eE] [-+]? [0-9]+;
fragment DECPART: '.'[0-9]+;   
fragment StringChar: ~[\b\f\r\n\t"\\] | ESC2; 
fragment ESC2: '\\' [bfrnt"\\];
fragment DOUBLEQ : '"';
fragment IllegalString
    : '\\' ~[bfrnt"\\]
    | '\\'
    ;

/***************************************************** Lexer *************************************************/
BOOLLIT: TRUE | FALSE;

FLOATLIT: (INTLIT DECPART | INTLIT DECPART EXPPART | INTLIT EXPPART | DECPART EXPPART?) {self.text = self.text.replace('_', '')};
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
 DOT:  '.';  	
 COMMA: ',';  
 SEMI: ';';  		
 COLON: ':';
 LCB: '{';  		
 RCB: '}';  	  
/* SEPERATORS */ 	

/*OPERATORS */     

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