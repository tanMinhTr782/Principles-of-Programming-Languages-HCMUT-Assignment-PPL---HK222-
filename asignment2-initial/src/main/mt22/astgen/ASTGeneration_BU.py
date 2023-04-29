from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    #program: decllist EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))   
    
    def visitDecllist(self, ctx: MT22Parser.DecllistContext): 
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decllist())
    
    def visitDecl(self,ctx:MT22Parser.DeclContext):
        if ctx.var_decl(): 
            return self.visit(ctx.var_decl())
        return self.visit(ctx.func_decl())
    
    def visitVar_decl(self,ctx:MT22Parser.Var_declContext):
        if ctx.var_short():         
            return self.visit(ctx.var_short())
        else:
            return self.visit(ctx.var_full())
    
    def visitVar_short(self,ctx:MT22Parser.Var_shortContext): 
        idlist = self.visit(ctx.idlist())
        init = None
        typ = self.visit(ctx.typ())
        return list(map(lambda x: VarDecl(x,typ,init),idlist))
    def visitIdlist(self,ctx:MT22Parser.IdlistContext): 
        if ctx.getChildCount() == 1: 
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())
    def visitVar_full(self,ctx:MT22Parser.Var_fullContext): 
        idlist = self.visit(ctx.idlist())
        typ = self.visit(ctx.typ())
        expprime = self.visit(ctx.expprime())
        return list(map(lambda x,y:VarDecl(x,typ,y),idlist,expprime))
    def visitParamhead(self,ctx:MT22Parser.ParamheadContext):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.paramlist())
        return []
    def visitParamlist(self,ctx:MT22Parser.ParamlistContext): 
        if ctx.COMMA():
            return [self.visit(ctx.param())] + self.visit(ctx.paramlist())
        return [self.visit(ctx.param())]
    def visitParam(self,ctx:MT22Parser.ParamContext):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.parambase())
        dt = self.visit(ctx.parambase())
        head = self.visit(ctx.param_constraint())
        if head == "2":
            return ParamDecl(dt.name,dt.typ,True,True)
        elif head == "out": 
            return ParamDecl(dt.name,dt.typ,True,False)
        return ParamDecl(dt.name,dt.typ,False,True)
    def visitParambase(self,ctx:MT22Parser.ParambaseContext): 
        id = ctx.ID().getText()
        type = self.visit(ctx.typ())
        return ParamDecl(id,type,False,False)
    def visitParam_constraint(self,ctx:MT22Parser.Param_constraintContext):
        if (ctx.getChildCount() == 1): 
            return ctx.PARAM_CONST(0).getText()
        return "2"
    def visitParamType(self,ctx:MT22Parser.ParamTypeContext): 
        if ctx.AUTO(): 
            return AutoType()
        if ctx.atomictyp(): 
            return self.visit(ctx.atomictyp())
        return self.visit(ctx.arraytyp())
    def visitBase_func(self,ctx:MT22Parser.Base_funcContext):
        id = ctx.ID().getText()
        typ = self.visit(ctx.typ())
        params = self.visit(ctx.paramhead())
        return FuncDecl(id,typ,params,None,"")
    def visitFunc_decl(self,ctx:MT22Parser.Func_declContext):
        baseFunc = self.visit(ctx.base_func())
        body = self.visit(ctx.block_stmt())
        if ctx.PARAM_CONST(): 
            return [FuncDecl(baseFunc.name,baseFunc.return_type,baseFunc.params,ctx.ID().getText(),body)]
        return [FuncDecl(baseFunc.name,baseFunc.return_type,baseFunc.params,None,body)]
########################### EXPRESSION TIME ######################################
    def visitExprlist(self,ctx:MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 0: 
            return []
        return self.visit(ctx.expprime())
#expprime: expr COMMA expprime | expr;   
    def visitExpprime(self,ctx:MT22Parser.ExpprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.expprime())
# expr: expr1 CONCATENATE expr1 | expr1; 
    def visitExpr(self,ctx:MT22Parser.ExprContext): 
        if ctx.CONCATENATE():
            op = ctx.CONCATENATE().getText()
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            return BinExpr(op,left,right)
        return self.visit(ctx.exp1(0))
# exp1: exp2 RELATIONAL exp2 | exp2; 
    def visitExp1(self,ctx:MT22Parser.Exp1Context): 
        if ctx.RELATIONAL():
            op = ctx.RELATIONAL().getText()
            left = self.visit(ctx.exp2(0))
            right = self.visit(ctx.exp2(1))
            return BinExpr(op,left,right)
        return self.visit(ctx.exp2(0))
#exp2: exp2 ANDOR exp3 | exp3; 
    def visitExp2(self,ctx:MT22Parser.Exp2Context):
        if ctx.getChildCount() == 3:
            op = ""
            if ctx.AND(): op = ctx.AND().getText()
            else: op = ctx.OR().getText()
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            return BinExpr(op,left,right)
        return self.visit(ctx.exp3())
#exp3: exp3 ADDSUB exp4 | exp4;  
    def visitExp3(self,ctx:MT22Parser.Exp3Context): 
        if ctx.ADD():
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4()) 
            op = ctx.ADD().getText()
            return BinExpr(op,left,right)
        if ctx.SUB():
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4()) 
            op = ctx.SUB().getText()
            return BinExpr(op,left,right)
        return self.visit(ctx.exp4())
#exp4: exp4 MULDIVMOD exp5 | exp5;
    def visitExp4(self,ctx:MT22Parser.Exp4Context): 
        if ctx.getChildCount() == 3:
            op = ""
            if ctx.MUL(): op = ctx.MUL().getText()
            elif ctx.DIV(): op = ctx.DIV().getText()
            else: op = ctx.MOD().getText()
            left = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            return BinExpr(op,left,right)
        return self.visit(ctx.exp5())
#exp5: NOT exp5 | exp6;         
    def visitExp5(self,ctx:MT22Parser.Exp5Context):
        if ctx.NOT():
            op = ctx.NOT().getText()
            value = self.visit(ctx.exp5())
            return UnExpr(op,value)
        return self.visit(ctx.exp6())
#exp6: MINUS exp6 | exp7;
    def visitExp6(self,ctx:MT22Parser.Exp6Context):
        if ctx.SUB():
            op = ctx.SUB().getText()
            value = self.visit(ctx.exp6())
            return UnExpr(op,value)
        return self.visit(ctx.operand())
# expr7: BOOLLIT | INTLIT | STRINGLIT | FLOATLIT | ID | callexpr | subexpr | indexop; 
# return Id at this step. 
    def visitOperand(self,ctx:MT22Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.func_call_exp(): 
            return self.visit(ctx.func_call_exp())
        elif ctx.indexop(): 
            return self.visit(ctx.indexop())
        return self.visit(ctx.subexpr())

# subexpr: LB expr RB; 
    def visitSubexpr(self,ctx:MT22Parser.SubexprContext):
        if ctx.LP() and ctx.RP():
            return self.visit(ctx.expr())
#  indexop: ID SQLB exprlist SQRB;
    def visitIndexop(self,ctx:MT22Parser.IndexopContext): 
        if ctx.LSB() and ctx.RSB():
            name = ctx.ID().getText()
            exprs =self.visit(ctx.expprime())
            return ArrayCell(name,exprs) 
# callexpr: ID LB exprlist RB; 
    def visitFunc_call_exp(self,ctx:MT22Parser.Func_call_expContext): 
        if ctx.LP() and ctx.RP():
            name = ctx.ID().getText()
            exprs = self.visit(ctx.exprlist())
            return FuncCall(name,exprs)
    def visitStmt(self,ctx:MT22Parser.StmtContext): 
        if ctx.assign_stmt(): 
            return self.visit(ctx.assign_stmt())
        elif ctx.if_stmt(): 
            return self.visit(ctx.if_stmt())
        elif ctx.return_stmt(): 
            return self.visit(ctx.return_stmt())
        elif ctx.call_stmt(): 
            return self.visit(ctx.call_stmt())
        elif ctx.for_stmt(): 
            return self.visit(ctx.for_stmt())
        elif ctx.break_stmt(): 
            return self.visit(ctx.break_stmt())
        elif ctx.block_stmt(): 
            return self.visit(ctx.block_stmt())
        elif ctx.dowhile_stmt(): 
            return self.visit(ctx.dowhile_stmt())
        elif ctx.while_stmt(): 
            return self.visit(ctx.while_stmt())
        return self.visit(ctx.continue_stmt())
# blockstmt: LCB blocklist RCB;
    def visitBlock_stmt(self,ctx:MT22Parser.Block_stmtContext): 
        return BlockStmt(self.visit(ctx.inside_block_stmt_list()))
# dowhile_stmt: DO blockstmt WHILE LB expr RB SEMI; 
    def visitDowhile_stmt(self,ctx:MT22Parser.Dowhile_stmtContext): 
        return DoWhileStmt(self.visit(ctx.expr()),self.visit(ctx.block_stmt()))
# whilestmt: WHILE LB expr RB loopstmt;
    def visitWhile_stmt(self,ctx:MT22Parser.While_stmtContext):
        return WhileStmt(self.visit(ctx.expr()),self.visit(ctx.stmt()))
#forstmt: FOR LB scalar_variable EQ expr COMMA expr COMMA expr RB loopstmt;
    def visitFor_stmt(self,ctx:MT22Parser.For_stmtContext):
        s_var = self.visit(ctx.scala_var())
        init = self.visit(ctx.expr(0))
        cond = self.visit(ctx.expr(1))
        inc = self.visit(ctx.expr(2))
        st = self.visit(ctx.stmt())
        assStmtInit = AssignStmt(s_var,init)
        return ForStmt(assStmtInit,cond,inc,st)
#assignstmt: scalar_variable EQ expr SEMI;
    def visitAssign_stmt(self,ctx:MT22Parser.Assign_stmtContext):
        return AssignStmt(self.visit(ctx.scala_var()),self.visit(ctx.expr()))
    def visitScala_var(self,ctx:MT22Parser.Scala_varContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.indexop())
    def visitIf_stmt(self,ctx:MT22Parser.If_stmtContext):
        if ctx.ELSE():
            cond =  self.visit(ctx.expr())
            tstmt = self.visit(ctx.stmt(0))
            fstmt = self.visit(ctx.stmt(1))
            return IfStmt(cond,tstmt,fstmt)
        cond =  self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt(0))
        return IfStmt(cond,tstmt,None)
# breakstmt: BREAK SEMI;
    def visitBreak_stmt(self,ctx:MT22Parser.Break_stmtContext): 
        return BreakStmt()
# continuestmt: CONTINUE SEMI;    
    def visitContinue_stmt(self,ctx:MT22Parser.Continue_stmtContext): 
        return ContinueStmt()
# callstmt: ID LB exprlist RB SEMI; 
    def visitCall_stmt(self,ctx:MT22Parser.Call_stmtContext):
        id = ctx.ID().getText()
        exprs = self.visit(ctx.exprlist())
        return CallStmt(id,exprs)
# returnstmt: RETURN expr SEMI; 
    def visitReturn_stmt(self,ctx:MT22Parser.Return_stmtContext):
        if ctx.getChildCount() == 2: 
            return ReturnStmt(None) 
        return ReturnStmt(self.visit(ctx.expr()))
# loopstmt: blockstmt | stmt; 
    def visitInside_block_stmt(self,ctx:MT22Parser.Inside_block_stmtContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())]
        return self.visit(ctx.var_decl())
    def visitInside_block_stmt_list(self,ctx:MT22Parser.Inside_block_stmt_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.inside_block_stmt()) + self.visit(ctx.inside_block_stmt_list())

# scalar_variable: ID |  indexop; # return Id at this parser rule 

    def visitLiteral(self,ctx:MT22Parser.LiteralContext): 
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.BOOLEANLIT():
            return BooleanLit(ctx.BOOLEANLIT().getText() == "true")
        elif ctx.FLOATLIT():
            st = ctx.FLOATLIT().getText()
            if st[0] == '.' and st[1] == 'e': 
                st = '0.0'
            return FloatLit(float(st))
        elif ctx.STRINGLIT():
            return StringLit(str(ctx.STRINGLIT().getText()))
        return self.visit(ctx.arraylit())
    def visitArraylit(self,ctx:MT22Parser.ArraylitContext): 
        return ArrayLit(self.visit(ctx.exprlist()))
    def visitTyp(self,ctx:MT22Parser.TypContext): 
        if ctx.AUTO(): 
            return AutoType()
        if ctx.VOID(): 
            return VoidType()
        if ctx.atomictyp(): 
            return self.visit(ctx.atomictyp())
        return self.visit(ctx.arraytyp())
    def visitAtomictyp(self,ctx:MT22Parser.AtomictypContext): 
        if ctx.INTEGER(): 
            return IntegerType()
        if ctx.FLOAT(): 
            return FloatType()
        if ctx.BOOLEAN(): 
            return BooleanType()
        if ctx.STRING(): 
            return StringType()
    def visitArraytyp(self,ctx:MT22Parser.AtomictypContext): 
        dimension = self.visit(ctx.intlist())
        atmt_typ = self.visit(ctx.atomictyp())
        return ArrayType(dimension,atmt_typ)
    def visitIntlist(self,ctx:MT22Parser.IntlistContext): 
        if ctx.getChildCount() == 1: 
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.intlist())
    
    



