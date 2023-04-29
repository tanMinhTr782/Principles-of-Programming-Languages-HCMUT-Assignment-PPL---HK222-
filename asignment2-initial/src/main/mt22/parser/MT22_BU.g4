//2012397
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
/*********************PARSER**********************/
program: decllist EOF ;
decllist: decl decllist | decl;
decl: var_decl | func_decl;

/*********************FUNC & VAR DECL**********************/
var_decl: var_short | var_full ;
var_short: idlist  COLON typ SEMI;
idlist: ID COMMA idlist | ID;
var_full: idlist COLON typ ASSIGN expprime SEMI;
// var_helper: COLON typ ASSIGN | COMMA ID var_helper expr COMMA;

//parameters & funcdecl
func_decl:  base_func (PARAM_CONST ID | ) block_stmt;
base_func: ID COLON FUNCTION typ LP paramhead RP; 
paramhead: paramlist | ; 
paramlist: param COMMA paramlist | param;
param: (param_constraint | ) parambase;
parambase: ID COLON typ; 
param_constraint: PARAM_CONST (PARAM_CONST | );
paramType: atomictyp | AUTO | arraytyp; 
/*********************EXPRESSIONS**********************/
expr: exp1 CONCATENATE exp1 | exp1;
exp1: exp2 RELATIONAL exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | operand ;
operand: literal| ID | func_call_exp| indexop | subexpr;
indexop: ID LSB expprime RSB;
subexpr: LP expr RP;
func_call_exp: ID LP exprlist RP;
exprlist: expprime | ;
expprime: expr COMMA expprime | expr;
/*------------------------------- STATEMENTS --------------------------------*/
stmt:  assign_stmt | if_stmt | for_stmt | while_stmt | dowhile_stmt | break_stmt | continue_stmt | return_stmt | call_stmt | block_stmt ;
assign_stmt: scala_var ASSIGN expr SEMI;
scala_var: ID | indexop ;

if_stmt: IF LP expr RP stmt (ELSE stmt)?;
for_stmt:FOR LP scala_var ASSIGN expr COMMA expr COMMA expr RP stmt;
while_stmt: WHILE LP expr RP stmt;
dowhile_stmt: DO block_stmt WHILE LP expr RP SEMI;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN expr? SEMI;

call_stmt: ID LP exprlist RP SEMI;
inside_block_stmt: stmt | var_decl;
inside_block_stmt_list: inside_block_stmt inside_block_stmt_list | ;
block_stmt: LCB inside_block_stmt_list RCB;
/****** COMMENT *****/
LINE_CMT: '//' ~[\r\n]* -> skip;
BLOCK_CMT: '/*' .*? '*/' -> skip;


/********************* FRAGMENTS **********************/
fragment DOT: '.';
fragment Digit: [0-9];
fragment NonZeroDigit: [1-9];
fragment EXP: [Ee][+-]?[0-9]+ ;
fragment DECPA: DOT Digit+;


/********************* LITERALS ***********************/
// Integer literal
literal: INTLIT |FLOATLIT| BOOLEANLIT | STRINGLIT | arraylit;
PARAM_CONST: INHERIT | OUT; 

INTLIT: NonZeroDigit Digit* ('_'Digit+)* {self.text = self.text.replace("_", "")} | '0';
// Float literal 
FLOATLIT: (INTLIT DECPA | INTLIT DECPA? EXP| INTLIT? DECPA EXP| DOT EXP | DECPA| INTLIT DOT) {self.text = self.text.replace("_", "")} ;
// Boolean literal
BOOLEANLIT: TRUE | FALSE ;
//String literal
STRINGLIT: '"' STRING_CHAR* '"'
{
    y = str(self.text)
    self.text = y[1:-1]
};
fragment STRING_CHAR        :  ~[\b\f\r\n\t"\\] | ESC2; 
fragment ESC2: '\\' [bfrnt"\\];
fragment ESCAPE             : '\\' [bfntr'"\\] ;
fragment ESCERROR           : '\\' ~[bfrnt'"\\] ;
fragment SINGLEQUOTE        : '\\\'' ;
fragment DOUBLEQUOTE        : '\\"' ;

//Arrayr literal
arraylit: LCB exprlist RCB;
/******************** TYPE SYSTEM AND VALUES **********************/
typ: atomictyp | arraytyp | VOID | AUTO;
atomictyp: BOOLEAN | INTEGER | FLOAT | STRING;
arraytyp: ARRAY LSB intlist RSB OF atomictyp;
intlist: INTLIT COMMA intlist | INTLIT;
/******************** SEPARATORS **********************/
LP: '(' ;
RP: ')' ;
LSB: '[';
RSB: ']';
COMMA: ',';
SEMI: ';' ;
COLON: ':';
LCB: '{';
RCB: '}';

/********************* OPERATORS **********************/
//+ - * / %
//! && || ==
//!= < <= > >=
//::
RELATIONAL: EQUAL | NOT_EQUAL | LT | GT | LE | GE;
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
CONCATENATE: '::';
ASSIGN: '=';
/********************* KEY WORDS **********************/
//auto break boolean do else
//false float for function if
//integer return string true while
//void out continue of inherit
//array

AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

/******************** IDENTIFIERS *********************/
ID:[A-Za-z_][A-Za-z0-9_]*;
/*********************** SKIP *************************/
WS : [ \t\r\n\f\b]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' STRING_CHAR* ([\b\t\f\n\r"\\] | EOF)
    {
        unclose_str = str(self.text)
        possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
        if unclose_str[-1] in possible:
            raise UncloseString(unclose_str[1:-1])
        else:
            raise UncloseString(unclose_str[1:])
    }
    ;
ILLEGAL_ESCAPE: '"' STRING_CHAR* ESCERROR {
	illegal_str = str(self.text)
	raise IllegalEscape(illegal_str[1:])
};

ERROR_CHAR: .{raise ErrorToken(self.text)};
