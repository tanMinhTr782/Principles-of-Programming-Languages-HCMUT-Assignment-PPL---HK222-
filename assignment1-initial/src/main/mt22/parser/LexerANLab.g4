//2012018
grammar MT22;

@lexer::header {
from lexererr import *
  
}
@members{  
    IDCount = 0; 
    LitCount = 0; 
}
options{
	language=Python3;        
}
// py run.py test ParserSuite
// py run.py gen
program: EOF;
/////////////////////// FRAGMENT
// OPERATORS    

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

// SEPERATORS	
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
 EQ: '='; 

// KEYWORDS

 fragment AUTO: 'auto';			
 FALSE: 'false'; 			
 OF: 'of';			
 INHERIT: 'inherit';
 fragment INTEGER: 'integer'; 	
 fragment VOID: 'void'; 				
 fragment FLOAT: 'float';		
 fragment BOOLEAN: 'boolean';		
 ARRAY: 'array';			
 FUNCTION: 'function';		
 STRING: 'string';
 BREAK: 'break';			
 RETURN: 'return';			
 OUT: 'out';
 FOR: 'for';				
 CONTINUE: 'continue';		
 DO: 'do';			
 WHILE: 'while';
 IF: 'if';				
 ELSE: 'else';				
 TRUE: 'true';
//////////////////////////
COMMENT: '//*' .*? '*//' -> skip
C_COMMENT: '///' .*? -> skip
ID: [_a-zA-Z][_a-zA-Z0-9]*; // key word not check now (ass1)
// LITERAL 
FLOATLIT: (INTLIT DECPART | INTLIT DECPART? EXPPART) {self.text = self.text.replace('_', '')};  
INTLIT: '0' | [+-]?[1-9][_0-9]*  {self.text = self.text.replace('_', '')};
BOOLLIT: TRUE | FALSE;
fragment EXPPART: [eE] [-+]? [0-9]+;
fragment DECPART: '.'[0-9]+;   
STRINGLIT: DOUBLEQ (StringChar*) DOUBLEQ
    {
        result = str(self.text)
        self.text = result[1:-1]
    };
fragment StringChar: ~[\b\f\r\n\t"\\] | ESC2; 
fragment ESC2: '\\' [bfrnt"\\];
fragment DOUBLEQ : '"';  
fragment ELE_LIST: ELEPRIME | ;
ELE : (INTLIT | FLOATLIT | STRINGLIT | BOOLEAN);
fragment ELEPRIME: ELE COMMA ELEPRIME | ELE;   
WS : [ \t\r\n]+ -> skip ;

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;

// py run.py test LexerSuite
// py run.py gen
// Q