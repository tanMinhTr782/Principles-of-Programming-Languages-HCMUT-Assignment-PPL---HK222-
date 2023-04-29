from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    #program: decllist EOF
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))
    #decllist: decl decllist |     
    def visitDecllist(self, ctx: MT22Parser.DecllistContext): 
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decllist())
    # decl: vardecl | funcdecl
    def visitDecl(self,ctx:MT22Parser.DeclContext):
        if ctx.vardecl(): 
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())
    #vardecl: varnoinit | varinit | array
    def visitVardecl(self,ctx:MT22Parser.VardeclContext):
        if ctx.varnoinit():         
            return self.visit(ctx.varnoinit())
        if ctx.varassign(): 
            return self.visit(ctx.varassign())
        return self.visit(ctx.array())
    #varnoinit: idlist COLON vartype
    def visitVarnoinit(self,ctx:MT22Parser.VarnoinitContext): 
        idlist = self.visit(ctx.idlist())
        type = self.visit(ctx.vartype())
        init = None
        return list(map(lambda x: VarDecl(x,type,init),idlist))
    def visitVarassign(self,ctx:MT22Parser.VarassignContext): 
        ids = self.visit(ctx.idlist())
        type = self.visit(ctx.vartype())
        exprs = self.visit(ctx.expprime())
        return list(map(lambda x,y:VarDecl(x,type,y),ids,exprs))

    def visitVartype(self,ctx:MT22Parser.VardeclContext): 
        if ctx.INTEGER(): 
            return IntegerType()
        if ctx.FLOAT(): 
            return FloatType()
        if ctx.BOOLEAN(): 
            return BooleanType()
        if ctx.STRING(): 
            return StringType()
        return AutoType()
#
    def visitIdlist(self,ctx:MT22Parser.IdlistContext):
        if ctx.COMMA(): 
            return [ctx.ID().getText()] + self.visit(ctx.idlist())
        return [ctx.ID().getText()]
# array: arraydecl | arrayinit; 
    def visitArray(self,ctx:MT22Parser.ArrayContext):
        if ctx.arraydecl(): 
            return self.visit(ctx.arraydecl())
        return self.visit(ctx.arrayinit()) 
# arraydecl: idlist COLON arrayParam SEMI; # a,b : array [2,3] of integer; 
    def visitArraydecl(self,ctx:MT22Parser.ArraydeclContext):
        listID = self.visit(ctx.idlist())
        arrParam = self.visit(ctx.arrayParam())
        return list(map(lambda ID: VarDecl(ID,arrParam,None),listID))
# arrayinit: idlist COLON arrayParam EQ arraylit SEMI;
    def visitArrayinit(self,ctx:MT22Parser.ArrayinitContext): 
        listID = self.visit(ctx.idlist())
        arrParam = self.visit(ctx.arrayParam())
        arrLit = self.visit(ctx.exprlist())
        return list(map(lambda ID,lit: VarDecl(ID,arrParam,lit),listID,arrLit))
#arraylit: expprime | arrayVallist;
    # def visitArraylit(self,ctx:MT22Parser.ArraylitContext): 
    #     if ctx.expprime():
    #         return self.visit(ctx.expprime())
    #     return self.visit(ctx.arrayValList())
    # def visitArrayValList(self,ctx:MT22Parser.ArrayValListContext):
    #     if ctx.COMMA(): 
    #         return [ArrayLit(self.visit(ctx.arrayVal()))] + self.visit(ctx.arrayValList())
    #     return [ArrayLit(self.visit(ctx.arrayVal()))]
#arrayVal: LCB exprlist RCB;
    def visitArrayVal(self,ctx:MT22Parser.ArrayValContext): 
        return ArrayLit(self.visit(ctx.exprlist()))
#arrayParam: ARR SQLB dimension SQRB OF atomic_type; 
    def visitArrayParam(self,ctx:MT22Parser.ArrayParamContext):
        dimension = self.visit(ctx.dimension())
        atomic_type = self.visit(ctx.atomic_type())
        return ArrayType(dimension,atomic_type)
#dimension: INTLIT COMMA dimension | INTLIT;
    def visitDimension(self,ctx:MT22Parser.DimensionContext): 
        if ctx.COMMA(): 
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimension())
        return [int(ctx.INTLIT().getText())]
# funcdecl: funcdecl_no_inherit | funcdecl_inherit;
    def visitFuncdecl(self,ctx:MT22Parser.FuncdeclContext):
        baseEle = self.visit(ctx.base_funcdecl())
        body = self.visit(ctx.blockstmt())
        if ctx.PARAM_KEYWORDS(): 
            return [FuncDecl(baseEle.name,baseEle.return_type,baseEle.params,ctx.ID().getText(),body)]
        return [FuncDecl(baseEle.name,baseEle.return_type,baseEle.params,None,body)]
       # return self.visit(ctx.base_funcdecl)   
# base_funcdecl: ID COLON FUNCTION returntype LB paramlist RB body; 
    def visitBase_funcdecl(self,ctx:MT22Parser.Base_funcdeclContext): 
        name = ctx.ID().getText()
        type = self.visit(ctx.returntype())
        params = self.visit(ctx.paramlist())
        # inherit = None
        return FuncDecl(name,type,params,None,"")

    def visitReturntype(self,ctx:MT22Parser.ReturntypeContext):
        if ctx.VOID(): 
            return VoidType()
        if ctx.AUTO(): 
            return AutoType()
        if ctx.atomic_type(): 
            return self.visit(ctx.atomic_type())
        return self.visit(ctx.arrayParam())
#
    def visitParamlist(self,ctx:MT22Parser.ParamlistContext): 
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.paramprime())
        return []
#paramprime: param COMMA paramprime | param;
    def visitParamprime(self,ctx:MT22Parser.ParamprimeContext): 
        if ctx.COMMA(): 
            return [self.visit(ctx.param())] + self.visit(ctx.paramprime())
        return [self.visit(ctx.param())]
#param: param_nokey | param_with_one_keywords | param_with_two_keywords; 
    def visitParam(self,ctx:MT22Parser.ParamContext):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.parambase())
        data = self.visit(ctx.parambase())
        head = self.visit(ctx.paramHead())
        if (head == "2"): 
            return ParamDecl(data.name,data.typ,True,True)
        elif head == "inherit": 
            return ParamDecl(data.name,data.typ,False,True)
        return ParamDecl(data.name,data.typ,True,False)
    def visitParamHead(self,ctx:MT22Parser.ParamHeadContext):
        if (ctx.getChildCount() == 2): 
            return "2"
        return ctx.PARAM_KEYWORDS(0).getText()
    def visitParambase(self,ctx:MT22Parser.ParambaseContext): 
        name = ctx.ID().getText()
        type = self.visit(ctx.paramtype())
        return ParamDecl(name,type,False,False)

#paramtype: atomic_type | AUTO | arrayParam;
    def visitParamtype(self,ctx:MT22Parser.ParamtypeContext): 
        if ctx.AUTO(): 
            return AutoType()
        if ctx.atomic_type(): 
            return self.visit(ctx.atomic_type())
        return self.visit(ctx.arrayParam())
#atomic_type : INTEGER | FLOAT | BOOLEAN | STRING;
    def visitAtomic_type(self,ctx:MT22Parser.Atomic_typeContext): 
        if ctx.INTEGER(): 
            return IntegerType()
        if ctx.FLOAT(): 
            return FloatType()
        if ctx.BOOLEAN(): 
            return BooleanType()
        return StringType()
###################### STATEMENT ######################
# stmt: assignstmt | ifstmt| returnstmt | callstmt | forstmt| whilestmt | dowhile_stmt | continuestmt |breakstmt | blockstmt; 
    def visitStmt(self,ctx:MT22Parser.StmtContext): 
        if ctx.assignstmt(): 
            return self.visit(ctx.assignstmt())
        elif ctx.ifstmt(): 
            return self.visit(ctx.ifstmt())
        elif ctx.returnstmt(): 
            return self.visit(ctx.returnstmt())
        elif ctx.callstmt(): 
            return self.visit(ctx.callstmt())
        elif ctx.forstmt(): 
            return self.visit(ctx.forstmt())
        elif ctx.breakstmt(): 
            return self.visit(ctx.breakstmt())
        elif ctx.blockstmt(): 
            return self.visit(ctx.blockstmt())
        elif ctx.dowhile_stmt(): 
            return self.visit(ctx.dowhile_stmt())
        elif ctx.whilestmt(): 
            return self.visit(ctx.whilestmt())
        return self.visit(ctx.continuestmt())
# blockstmt: LCB blocklist RCB;
    def visitBlockstmt(self,ctx:MT22Parser.BlockstmtContext): 
        return BlockStmt(self.visit(ctx.blocklist()))
# blocklist: allowed_blockstmt blocklist | ;
    def visitBlocklist(self,ctx:MT22Parser.BlocklistContext): 
        if (ctx.getChildCount() == 2): 
            return self.visit(ctx.allowed_blockstmt())+ self.visit(ctx.blocklist())
        return []
# allowed_blockstmt: stmt | vardecl; 
    def visitAllowed_blockstmt(self,ctx:MT22Parser.Allowed_blockstmtContext): 
        if ctx.stmt(): 
            return [self.visit(ctx.stmt())]
        return self.visit(ctx.vardecl())
# dowhile_stmt: DO blockstmt WHILE LB expr RB SEMI; 
    def visitDowhile_stmt(self,ctx:MT22Parser.Dowhile_stmtContext): 
        return DoWhileStmt(self.visit(ctx.expr()),self.visit(ctx.blockstmt()))
# whilestmt: WHILE LB expr RB loopstmt;
    def visitWhilestmt(self,ctx:MT22Parser.WhilestmtContext):
        return WhileStmt(self.visit(ctx.expr()),self.visit(ctx.loopstmt()))
#forstmt: FOR LB scalar_variable EQ expr COMMA expr COMMA expr RB loopstmt;
    def visitForstmt(self,ctx:MT22Parser.ForstmtContext):
        s_var = self.visit(ctx.scalar_variable())
        init = self.visit(ctx.expr(0))
        cond = self.visit(ctx.expr(1))
        inc = self.visit(ctx.expr(2))
        st = self.visit(ctx.loopstmt())
        assInit = AssignStmt(s_var,init)
        return ForStmt(assInit,cond,inc,st)
#assignstmt: scalar_variable EQ expr SEMI;
    def visitAssignstmt(self,ctx:MT22Parser.AssignstmtContext):
        return AssignStmt(self.visit(ctx.scalar_variable()),self.visit(ctx.expr()))
# ifstmt: IF LB expr RB loopstmt (ELSE loopstmt | ); 
    def visitIfstmt(self,ctx:MT22Parser.IfstmtContext):
        if ctx.ELSE():
            cond =  self.visit(ctx.expr())
            tstmt = self.visit(ctx.loopstmt(0))
            fstmt = self.visit(ctx.loopstmt(1))
            return IfStmt(cond,tstmt,fstmt)
        cond =  self.visit(ctx.expr())
        tstmt = self.visit(ctx.loopstmt(0))
        return IfStmt(cond,tstmt,None)
# breakstmt: BREAK SEMI;
    def visitBreakstmt(self,ctx:MT22Parser.BreakstmtContext): 
        return BreakStmt()
# continuestmt: CONTINUE SEMI;    
    def visitContinuestmt(self,ctx:MT22Parser.ContinuestmtContext): 
        return ContinueStmt()
# callstmt: ID LB exprlist RB SEMI; 
    def visitCallstmt(self,ctx:MT22Parser.CallstmtContext):
        return CallStmt(ctx.ID().getText(),self.visit(ctx.exprlist()))
# returnstmt: RETURN expr SEMI; 
    def visitReturnstmt(self,ctx:MT22Parser.ReturnstmtContext):
        if ctx.getChildCount() == 2: 
            return ReturnStmt(None) 
        return ReturnStmt(self.visit(ctx.expr()))
# loopstmt: blockstmt | stmt; 
    def visitLoopStmt(self,ctx:MT22Parser.LoopstmtContext):
        if ctx.stmt():
            return self.visit(ctx.stmt())
        return self.visit(ctx.blockstmt())
# scalar_variable: ID |  indexop; # return Id at this parser rule 
    def visitScalar_variable(self,ctx:MT22Parser.Scalar_variableContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.indexop())

###################### STATEMENT ######################

###################### EXPRESSION ######################
# exprlist: expprime | ;
    def visitExprlist(self,ctx:MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 0: 
            return []
        return self.visit(ctx.expprime())
#expprime: expr COMMA expprime | expr;   
    def visitExpprime(self,ctx:MT22Parser.ExpprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.expprime())
# expr: expr1 SCOPE expr1 | expr1; 
    def visitExpr(self,ctx:MT22Parser.ExprContext): 
        if ctx.SCOPE():
            op = ctx.SCOPE().getText()
            left = self.visit(ctx.expr1(0))
            right = self.visit(ctx.expr1(1))
            return BinExpr(op,left,right)
        return self.visit(ctx.expr1(0))
# expr1: expr2 COMPARE expr2 | expr2; 
    def visitExpr1(self,ctx:MT22Parser.Expr1Context): 
        if ctx.COMPARE():
            op = ctx.COMPARE().getText()
            left = self.visit(ctx.expr2(0))
            right = self.visit(ctx.expr2(1))
            return BinExpr(op,left,right)
        return self.visit(ctx.expr2(0))
#expr2: expr2 ANDOR expr3 | expr3; 
    def visitExpr2(self,ctx:MT22Parser.Expr2Context): 
        if ctx.ANDOR():
            op = ctx.ANDOR().getText()
            left = self.visit(ctx.expr2())
            right = self.visit(ctx.expr3())
            return BinExpr(op,left,right)
        return self.visit(ctx.expr3())
#expr3: expr3 ADDSUB expr4 | expr4;  
    def visitExpr3(self,ctx:MT22Parser.Expr3Context): 
        if ctx.ADD():
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4()) 
            op = ctx.ADD().getText()
            return BinExpr(op,left,right)
        if ctx.MINUS():
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4()) 
            op = ctx.MINUS().getText()
            return BinExpr(op,left,right)
        return self.visit(ctx.expr4())
#expr4: expr4 MULDIVMOD expr5 | expr5;
    def visitExpr4(self,ctx:MT22Parser.Expr4Context): 
        if ctx.MULDIVMOD():
            op = ctx.MULDIVMOD().getText()
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinExpr(op,left,right)
        return self.visit(ctx.expr5())
#expr5: NOT expr5 | expr6;         
    def visitExpr5(self,ctx:MT22Parser.Expr5Context):
        if ctx.NOT():
            op = ctx.NOT().getText()
            value = self.visit(ctx.expr5())
            return UnExpr(op,value)
        return self.visit(ctx.expr6())
#expr6: MINUS expr6 | expr7;
    def visitExpr6(self,ctx:MT22Parser.Expr6Context):
        if ctx.MINUS():
            op = ctx.MINUS().getText()
            value = self.visit(ctx.expr6())
            return UnExpr(op,value)
        return self.visit(ctx.expr7())
# expr7: BOOLLIT | INTLIT | STRINGLIT | FLOATLIT | ID | callexpr | subexpr | indexop; 
# return Id at this step. 
    def visitExpr7(self,ctx:MT22Parser.Expr7Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLit(ctx.BOOLLIT().getText() == "true")
        elif ctx.FLOATLIT():
            st = ctx.FLOATLIT().getText()
            if st[0] == '.' and st[1] == 'e': 
                st = '0.0'
            return FloatLit(float(st))
        elif ctx.STRINGLIT():
            return StringLit(str(ctx.STRINGLIT().getText()))
        elif ctx.callexpr(): 
            return self.visit(ctx.callexpr())
        elif ctx.subexpr(): 
            return self.visit(ctx.subexpr())
        elif ctx.indexop(): 
            return self.visit(ctx.indexop())
        return self.visit(ctx.arrayVal())
# subexpr: LB expr RB; 
    def visitSubexpr(self,ctx:MT22Parser.SubexprContext):
        if ctx.LB() and ctx.RB():
            return self.visit(ctx.expr())
#  indexop: ID SQLB exprlist SQRB;
    def visitIndexop(self,ctx:MT22Parser.IndexopContext): 
        if ctx.SQLB() and ctx.SQRB():
            name = ctx.ID().getText()
            exprs =self.visit(ctx.expprime())
            return ArrayCell(name,exprs) 
# callexpr: ID LB exprlist RB; 
    def visitCallexpr(self,ctx:MT22Parser.CallexprContext): 
        if ctx.LB() and ctx.RB():
            name = ctx.ID().getText()
            exprs = self.visit(ctx.exprlist())
            return FuncCall(name,exprs)

###################### EXPRESSION ###################### 


        # return ParamDecl(name,type,False,False)
        # if ctx.getChildCount == 4: 
        #     isOut = ctx.PARAM_KEYWORDS().getText() == "out"
        #     isInherit = ctx.PARAM_KEYWORDS().getText() == "inherit"
        #     return ParamDecl(name,type,isOut,isInherit)

        # return ParamDecl(name,type,True,True)
# # param_nokey: ID COLON paramtype; 
#     def visitParam_nokey(self,ctx:MT22Parser.Param_nokeyContext):
#         name = (ctx.ID().getText())
#         type = self.visit(ctx.paramtype())
#         return ParamDecl(name,type,False,False)
# # param_with_one_keywords: PARAM_KEYWORDS ID COLON paramtype;
#     def visitParam_with_one_key(self,ctx:MT22Parser.Param_with_one_keyContext):
#         name = (ctx.ID().getText())
#         type = self.visit(ctx.paramtype())
#         isOut = ctx.PARAM_KEYWORDS().getText() == "out"
#         isInherit = ctx.PARAM_KEYWORDS().getText() == "inherit"
#         return ParamDecl(name,type,isOut,isInherit)
# # param_with_two_keywords: INHERIT OUT ID COLON paramtype; 
#     def visitParam_with_two_key(self,ctx:MT22Parser.Param_with_two_keyContext):
#         name = (ctx.ID().getText())
#         type = self.visit(ctx.paramtype())
#         return ParamDecl(name,type,True,True)

    # def visitBasecase(self,ctx:MT22Parser.BasecaseContext): 
    #     id = Id(ctx.ID().getText())
    #     type = self.visit(ctx.vartype())
    #     init = self.visit(ctx.expr())
    #     return [VarDecl(id,type,init)]
# helper: ID COMMA helper COMMA expr | basecase; 
    # def visitHelper(self,ctx:MT22Parser.HelperContext):
    #     if ctx.getChildCount() == 1: 
    #         return [self.visit(ctx.basecase())]
            
    # def visitInherit_id(self,ctx:MT22Parser.Inherit_idContext): 
    #     return ctx.ID().getText()
# #funcdecl_inherit: ID COLON FUNCTION returntype LB paramlist RB INHERIT ID body;
#     def visitFuncdecl_inherit(self,ctx:MT22Parser.Funcdecl_inheritContext): 
#         name = ctx.ID().getText()
#         type = self.visit(ctx.returntype())
#         params = self.visit(ctx.paramlist())
#         inherit = ctx.ID().getText()
#         body = self.visit(ctx.body())
#         return [FuncDecl(name,type,params,inherit,body)]
#