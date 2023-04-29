from Visitor import Visitor
from AST import AST
# Symbol: 
# Global: ArrayVar, , Function 
#######################GLOBAL VARIABLE ##############################

# class Type(ABC):
#     def __str__(self):
#         return self.__class__.__name__
# class AtomicType(Type): pass
# class IntegerType(AtomicType): pass
# class FloatType(AtomicType): pass
# class BooleanType(AtomicType): pass
# class AutoType(Type): pass
# class FunctionType(Type): pass
# class StringType(AtomicType): pass
# class VoidType(Type): pass
# class ArrayType(Type):
#     def __init__(self, dimensions: List[int], typ: AtomicType):
#         self.dimensions = dimensions
#         self.typ = typ

#     def __str__(self):
#         return "ArrayType([{}], {})".format(", ".join([str(dimen) for dimen in self.dimensions]), str(self.typ))

class Symbol(): 
    def __init__(self,name,typ):
        self.name = name
        self.typ = [typ] # define as list to seperate with Function
class FuncSymbol(Symbol): 
    def __init__(self,name,return_type,paramTypeOrder,inherit,env,body): 
        self.name = name
        self.typ = [return_type,FunctionType()]
        self.paramTypeOrder = paramTypeOrder 
        self.inherit = inherit # Parent's name is here ! 
        self.env = env # ParamDecl + VarDecl inside Function 
        self.body = body
class ParamSymbol(Symbol): 
    def __init__(self,name,typ,inherit,out):
        self.name = name
        self.typ = [typ]
        self.inherit = inherit
        self.out = self.out
class Utils(): 
    def infer(self,name,SymbolTable,typ): 
        for symbol_list in SymbolTable: 
            for symbol in symbol_list: 
                if symbol.name == name: 
                    if type(symbol) != FuncSymbol: symbol.typ = [typ]
                    else: symbol.typ[0] = typ # return type XDDD
# How we visit OutSide to Inside. 
# OutSide: 
isMainExist = False
funcDeclOrder = []
class GetEnv(Visitor): #visit vong ngoai truoc, tuc cac khai bao o tam vuc global.
    def visitProgram(self,ctx,o:object): 
        o = []
        for decl in ctx.decl:
            if type(decl) is FuncDecl: 
                o = self.visit(decl, o)
        return o 
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o: 
            return o
        return_typ = self.visit(ctx.typ,o)
        global isMainExist
        if ctx.name is 'main': 
            if type(return_typ) == VoidType and len(ctx.params) == 0: 
                isMainExist = True
        paramTypeOrder = []
        for decl in ctx.params: # to get typ order. 
            paramTypeOrder = self.visit(decl,paramTypeOrder)
        o = [FuncSymbol(ctx.name,return_typ,paramTypeOrder,ctx.inherit,[],ctx.body)] + o
        return o
    def visitParamDecl(self, ctx, o): # we need prototype at this pharse only ! 
        o += [self.visit(ctx.typ,o)]
        return o
    def visitIntegerType(self, ctx, o):
        return IntegerType()
    def visitFloatType(self, ctx, o):
        return FloatType()
    def visitBooleanType(self, ctx, o):
        return BooleanType()
    def visitStringType(self, ctx, o): 
        return StringType()
# dimensions: List[int], typ: AtomicType
    def visitArrayType(self, ctx, o):
        # Question: Nếu một hàm có kiểu là arraytype
        typ = self.visit(ctx.typ,o)
        return ArrayType(ctx.dimensions,typ)
    def visitAutoType(self, ctx, o): 
        return AutoType()
    def visitVoidType(self, ctx, o):
        return VoidType()
# The exception Invalid(Parameter(), <parameter-name>) 
# is released when a parameter is declared in a function with no parent.
# We visit first round to collect function declareation order. Second round will be on decl. The funcOder is used on callstmt and 
# Funccall
# Van de: Lo cai ham do co error thi sao ? 
#Giai quyet: Neu ham do dc goi -> di check Vaild. 
# Ta se luu thong tin cua no (inherit ; paramdecl ; body de sau check)
# param -> redeclared..
class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast, [])
    def visitProgram(self,ctx,o:object): 
        global funcDeclOrder
        global isMainExist
        funcDeclOrder = GetEnv().visit(ctx, o)
        o = [[]]
        for decl in ctx.decl:
            o = self.visit(decl, o)
        if isMainExist == False: 
            raise NoEntryPoint()
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o[0]:
            raise Redeclared(Function(),ctx.name)
        return_typ = self.visit(ctx.typ,o)
        env = [[]] + o
        paramTypeOrder = []
        for decl in ctx.params: # to get typ order.
            paramTypeOrder = self.getParamType(decl,paramTypeOrder)
            env = self.visit(decl,env)
        # We handle inheritance here xDDDDD
        # First we check if the function parent body is vaild (incase it also have parent). 
        # Second, we check if the param with keyword "inherit" 
        # is belong to this function 
        # body have 2 case: in a function or in some statement. 
        # inheritance will be the last to solve LOL. I need sleep 
        env = self.visit(ctx.body,env)
        o[0] += [FuncSymbol(ctx.name,return_typ,paramTypeOrder,ctx.inherit,env,[])]
        return o
    def getParamType(self, ctx, o): # we need prototype at this pharse only ! 
        o += [self.visit(ctx.typ,o)]
        return o
    def visitBlockStmt(self, ctx, o):
        for x in ctx.body: 
            if type(x) is VarDecl: 
                o = self.visit(x,o)
            else: 
                self.visit(x,o)
        return o                 
    def checkVaildParent(self,ctx,o): pass
    def getParentEnvironment(self,ctx,o): pass
    def checkInheritParam(self,ctx,o): pass
    def visitParamDecl(self, ctx, o):
        if ctx.name in o[0]: 
            raise Redeclared(Parameter(),ctx.name)
        o[0] += [ParamSymbol(ctx.name,ctx.typ,ctx.inherit,ctx.out)]
        return o
    def inferVarDecl(self,ctx,init,o):
        if type(init) is IntegerType: 
            o[0] += [Symbol(ctx.name,IntegerType())]
        if type(init) is StringType: 
            o[0] += [Symbol(ctx.name,StringType())]
        if type(init) is FloatType: 
            o[0] += [Symbol(ctx.name,FloatType())]
        if type(init) is BooleanType: 
            o[0] += [Symbol(ctx.name,BooleanType())]
        # if type(init) is AutoType or if type(init) is VoidType:
        #     raise TypeCannotBeInferred(ctx)
        return o
    def inferArrayLit(self,ctx,o): pass
    def inferArrayLitEle(self,typ_,exprs): pass
    def visitVarDecl(self, ctx, o): 
        # Co suy dien kieu giua 2 phia nua nha ~ 
        # Case 1: lhs co kieu khac auto -> suy dien ben rhs 
        # Case 2 : rhs co kieu -> suy dien ben lhs 
        if ctx.name in o[0]: #
            raise Redeclared(Variable(), ctx.name)
        typ = self.visit(ctx.typ,o) # Looking for its type 
        init = None
        if type(typ) is AutoType and ctx.init is None: 
            raise Invaild(Variable(),ctx.name)
        if ctx.init != None:  
            init = self.visit(ctx.init,o)
            if type(typ) is AutoType:
                if type(init) is not ArrayType: 
                    return self.inferVarDecl(ctx,init,o)
                if type(init) is ArrayType:
                    return self.inferVarDecl(ctx,init.typ,o)
        if type(init) is VoidType: 
            raise Invaild(Variable(),ctx.name)
        if type(init) is ArrayType:
            if type(init.typ) is AutoType: # Arraylit with full ID auto type
                self.inferArrayLit(ctx,o)
                #return o
            if type(init.typ) != type(typ): 
                raise TypeMismatchInVardecl(ctx)
            if len(init.dimensions) != len(ctx.dimensions): 
                raise TypeMismatchInVardecl(ctx)
            for i in range(len(init.dimensions)): 
                if init.dimensions[i] != ctx.dimensions[i]: 
                    raise TypeMismatchInVardecl(ctx)
            o[0] += [Symbol(ctx.name,typ)]
            return o
        
        if type(typ) is FloatType and type(init) is IntegerType: 
            o[0] += [Symbol(ctx.name,typ)]
            return o
        if type(typ) != type(init): 
            raise TypeMismatchInVardecl(ctx)
        o[0] += [Symbol(ctx.name,typ)]
        return o
    def visitId(self,ctx,o:object):
        for symbol_list in o: 
            for symbol in symbol_list: 
                if symbol.name == ctx.name:
                    if type(symbol) is FuncSymbol: 
                        return symbol.typ[1]
                    return symbol.typ[0] 
        raise Undeclared(Identifier(),ctx.name)
    def visitArrayLit(self, ctx, o): # nho suy dien kieu o day nha :> 
        ele = []
        # typehashmap = {
        #     "IntegerType": 0, 
        #     "FloatType": 0,
        #     "StringType": 0,
        #     "BooleanType":0,
        #     "AutoType": 0,
        #     "ArrayType": 0
        #     "VoidType": 0
        # }
        typehashmap = [0,0,0,0,0,0,0]
        for i in ctx.explist: 
            ele = self.visit(i,ele)
        for i in range(0, len(ele) - 1):
            if type(ele[i]) is IntegerType: 
                typehashmap[0] += 1
            elif type(ele[i]) is FloatType: 
                typehashmap[1] += 1
            elif type(ele[i]) is StringType: 
                typehashmap[2] += 1
            elif type(ele[i]) is BooleanType: 
                typehashmap[3] += 1
            elif type(ele[i]) is AutoType:
                typehashmap[4] += 1
            elif type(ele[i]) is ArrayType:
                typehashmap[5] += 1
            else: typehashmap[6] += 1
        if typehashmap[4] == len(ele): 
            return ArrayType([len(ele)],AutoType())
        else:
            count = 0
            type2Infer = -1
            for i in range(7): 
                if typehashmap[i] > 0: count = count + 1
                if count > 2: raise IllegalArrayLiteral(ctx)
            if count == 2:
                for i in range(7):
                    if i != 4: 
                        if typehashmap[i] == len(ele) - typehashmap[4]:
                            if i == 6:  raise IllegalArrayLiteral(ctx)
                            type2Infer = i
                            break
                            
            if type2Infer == 0: 
                for x in ctx.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(IntegerType(),x)
            if type2Infer == 1: 
                for x in ctx.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(FloatType(),x)
            if type2Infer == 2: 
                for x in ctx.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(StringType(),x)
            if type2Infer == 3: 
                for x in ctx.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(BooleanType(),x)
            # if type2Infer == 5: 
            #     for x in ctx.explist: 
            #         kind = self.visit(x,o)
            #         if type(kind) is AutoType:
            #             self.inferArrayLitEle(ArrayType(),x)
        if typehashmap[5] == len(ele):
            return ArrayType([len(ele)],ArrayType())
        if typehashmap[6] == len(ele): 
            raise IllegalArrayLiteral(ctx)
        for i in range(len(ele)): 
            if type(ele[i]) != type(ele[i+1]): 
                raise IllegalArrayLiteral(ctx)
            # trong array co arraylit thi sao ? rofllmao , case nay bo nha ! 
            # tinh sau, met qua !
        if (type(ele[0])) is IntegerType: 
            return ArrayType([len[ele]],IntegerType())
        if (type(ele[0])) is BooleanType: 
            return ArrayType([len[ele]],BooleanType())
        if (type(ele[0])) is FloatType: 
            return ArrayType([len[ele]],FloatType())
        return ArrayType([len[ele]],StringType())       
    # decls: List[Decl]
    def visitIntegerType(self, ctx, o):
        return IntegerType()
    def visitFloatType(self, ctx, o):
        return FloatType()
    def visitBooleanType(self, ctx, o):
        return BooleanType()
    def visitStringType(self, ctx, o): 
        return StringType()
# dimensions: List[int], typ: AtomicType
    def visitArrayType(self, ctx, o): 
        typ = self.visit(ctx.typ,o)
        return ArrayType(ctx.dimension,typ)
    def visitAutoType(self, ctx, o): 
        return AutoType()
    def visitVoidType(self, ctx, o):
        return VoidType()
# op: str, left: Expr, right: Expr
    def visitBinExpr(self, ctx, o):
        lhs = self.visit(ctx.left,o)
        rhs = self.visit(ctx.right,o)
        arithmetic_op = ['-','+','*','/','%']
        bool_op = ['!','&&','||']
        string_op = ['::']
        relation_op = ['==','!=','>','<','>=','<=']
        # index_op -> Type
        # funcCall -> Type 
        if ctx.op in arithmetic_op:
            if ctx.op is '%': 
                if type(lhs) is AutoType: 
                    lhs = Utils.infer(o, ctx.left.name, IntegerType())
                if type(rhs) is AutoType:
                    rhs = Utils.infer(o, ctx.right.name, IntegerType())             
                if type(rhs) == IntegerType and type(lhs) == IntegerType:
                    return IntegerType
                raise TypeMismatchInExpression(ctx)
            if type(lhs) is AutoType and type(rhs) is IntegerType: 
                lhs = Utils.infer(o, ctx.left.name, IntegerType())
            if type(lhs) is AutoType and type(rhs) is FloatType: 
                lhs = Utils.infer(o, ctx.left.name, FloatType())
            if type(rhs) is AutoType and type(lhs) is IntegerType: 
                rhs = Utils.infer(o, ctx.right.name, IntegerType())
            if type(rhs) is AutoType and type(lhs) is FloatType: 
                rhs = Utils.infer(o, ctx.right.name, FloatType())
            if type(rhs) is not FloatType or IntegerType: 
                raise TypeMisMatchInExpression(ctx)
            if type(lhs) is not FloatType or IntegerType: 
                raise TypeMisMatchInExpression(ctx)
            
            if type(rhs) == FloatType or type(lhs) == FloatType: 
                return FloatType()  # Implicit conversion
            return IntegerType()
        
        if ctx.op in bool_op:
            if type(lhs) is AutoType: 
                lhs = Utils.infer(o, ctx.left.name, BooleanType())
            if type(rhs) is AutoType:
                rhs = Utils.infer(o, ctx.right.name, BooleanType())             
            if type(rhs) != BooleanType or type(lhs) != BooleanType: 
                raise TypeMismatchInExpression(ctx)
            return BooleanType()
        if ctx.op in string_op:
            if type(lhs) is AutoType: 
                lhs = Utils.infer(o, ctx.left.name, StringType())
            if type(rhs) is AutoType:
                rhs = Utils.infer(o, ctx.right.name, StringType())  
            if type(rhs) != StringType or type(lhs) != StringType: 
                raise TypeMismatchInExpression(ctx)
            return StringType()
# Case 1: Start       
        if ctx.op in relation_op: 
            if ctx.op in ['==','!=']:
                
                if type(lhs) is AutoType and type(rhs) is IntegerType: 
                    lhs = Utils.infer(o, ctx.left.name, IntegerType())
                if type(lhs) is AutoType and type(rhs) is BooleanType: 
                    lhs = Utils.infer(o, ctx.left.name, BooleanType())
                if type(rhs) is AutoType and type(lhs) is IntegerType: 
                    rhs = Utils.infer(o, ctx.right.name, IntegerType())
                if type(rhs) is AutoType and type(lhs) is BooleanType: 
                    rhs = Utils.infer(o, ctx.right.name, BooleanType())

                if type(rhs) is not BooleanType or IntegerType: 
                    raise TypeMisMatchInExpression(ctx)
                if type(lhs) is not BooleanType or IntegerType: 
                    raise TypeMisMatchInExpression(ctx)
                return BooleanType()
# Case 1: End

#Case 2: Start 
                
            if type(lhs) is AutoType and type(rhs) is IntegerType: 
                lhs = Utils.infer(o, ctx.left.name, IntegerType())
            if type(lhs) is AutoType and type(rhs) is FloatType: 
                lhs = Utils.infer(o, ctx.left.name, FloatType())
            if type(rhs) is AutoType and type(lhs) is IntegerType: 
                rhs = Utils.infer(o, ctx.right.name, IntegerType())
            if type(rhs) is AutoType and type(lhs) is FloatType: 
                rhs = Utils.infer(o, ctx.right.name, FloatType())

            if type(rhs) is not FloatType or IntegerType: 
                raise TypeMisMatchInExpression(ctx)
            if type(lhs) is not FloatType or IntegerType: 
                raise TypeMisMatchInExpression(ctx)
            return BooleanType()
#Case 2: End. 
    def visitUnExpr(self, ctx, o):
        one = self.visit(ctx.val,o)

        if ctx.op in ['!']: 
            if type(one) is AutoType: 
                one = Utils.infer(o, ctx.val.name, BooleanType())
            if type(one) != BooleanType: 
                raise TypeMismatchInExpression(ctx)
            return BooleanType()
        # -expr case
        if type(one) != IntegerType or type(one) != FloatType: 
            raise TypeMismatchInExpression(ctx)
        return type(one)
    def visitArrayCell(self, ctx, o):
        for symbol_list in o: 
            for symbol in o: 
                if type(symbol) is not FuncSymbol: 
                    # Tim dimension size cua array (Co the la Function or variable)
                    cell = []
                    for expr in ctx.cell: 
                        typ = self.visit(expr,o)
                        if type(typ) is not IntegerType: 
                            raise TypeMismatchInExpression(ctx) # ele trong cell ko integer -> Mismatch
                        cell = cell + [expr]
                    # So sanh 2 dimension vs nhau, neu khac size -> TypeMismatch
                    return symbol.typ[0]
                else: raise TypeMismatchInExpression(ctx) 
        raise Undeclared(ctx.name)
    def visitIntegerLit(self, ctx, o):
        return IntegerType()
    def visitFloatLit(self, ctx, o):
        return FloatType()
    def visitStringLit(self, ctx, o):
        return StringType()
    def visitBooleanLit(self, ctx, o):
        return BooleanType()
   
    def visitFuncCall(self, ctx, o): pass
# self, lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ctx, o):
        lhs = self.visit(ctx.lhs,o)
        rhs = self.visit(ctx.rhs,o)
        if type(lhs) is VoidType or type(rhs) is VoidType: 
            raise TypeMismatchInStatement(ctx)
        if type(lhs) is ArrayType or type(rhs) is ArrayType: 
            raise TypeMismatchInStatement(ctx)
        if type(lhs) is AutoType: 
            if type(rhs) is AutoType: 
                return # raise TypeCannotBeInferred(ctx)
            if type(rhs) is BooleanType: 
                lhs = Utils.infer(ctx.lhs.name,o,BooleanType())
            if type(rhs) is IntegerType: 
                lhs = Utils.infer(ctx.lhs.name,o,IntegerType())
            if type(rhs) is FloatType: 
                lhs = Utils.infer(ctx.lhs.name,o,FloatType())
            if type(rhs) is StringType: 
                lhs = Utils.infer(ctx.lhs.name,o,StringType())
        if type(rhs) is AutoType: 
            if type(lhs) is AutoType:
                return # raise TypeCannotBeInferred(ctx)
            if type(lhs) is BooleanType: 
                rhs = Utils.infer(ctx.rhs.name,o,BooleanType())
            if type(lhs) is IntegerType: 
                rhs = Utils.infer(ctx.rhs.name,o,IntegerType())
            if type(lhs) is FloatType: 
                rhs = Utils.infer(ctx.rhs.name,o,FloatType())
            if type(lhs) is StringType: 
                rhs = Utils.infer(ctx.rhs.name,o,StringType())
        if type(lhs) != type(rhs): 
            if type(lhs) == IntegerType and type(rhs) == FloatType: 
                raise TypeMismatchInStatement(ctx)
            if type(lhs) == FloatType and type(rhs) == IntegerType:
                return
            raise TypeMismatchInStatement(ctx) 
        return
# For an assignment statement, the left-hand side can be in 
# any type except void type and
# array type. The right-hand side (RHS) is either in 
# the same type as that of the LHS or
# in the type that can coerce to the LHS type.
    def visitIfStmt(self, ctx, o):
        type_cond = self.visit(ctx.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ctx)
        env = [[]] + o
        env = self.visit(ctx.tstmt,env)
        # reset env 
        if ctx.fstmt is not None:
            env = [[]] + o 
            env = self.visit(ctx.fstmt,env)
        return env
    def visitForStmt(self, ctx, o):
        type_init = self.visit(ctx.init,o)
        if type(type_init) is not IntegerType: 
            raise TypeMismatchInStatement(ctx) 
              
        type_cond = self.visit(ctx.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ctx)
        
        type_update = self.visit(ctx.upd,o)
        if type(type_update) is not IntegerType: 
            raise TypeMismatchInStatement(ctx)
        env = [[]] + o
        env = self.visit(ctx.stmt,env)
        return env
    def visitWhileStmt(self, ctx, o):
        type_cond = self.visit(ctx.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ctx)
        env = [[]] + o
        env = self.visit(ctx.stmt,env)
        return env
    def visitDoWhileStmt(self, ctx, o):
        type_cond = self.visit(ctx.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ctx)
        env = [[]] + o
        env = self.visit(ctx.stmt,env)
        return env      
    def visitBreakStmt(self, ctx, o): pass
    def visitContinueStmt(self, ctx, o): pass
    def visitReturnStmt(self, ctx, o):
        if ctx.expr is None: 
            return None
        return self.visit(ctx.expr,o)
    def visitCallStmt(self, ctx, o):
 #args la id: No o dau ? Global or Function Scope.
        #args ko co type. Chi co Literal -> Type hoac Id -> Type.
        args = ctx.args
        # raise UndeclaredIdentifier(str(type(o[0])))
        for list_block in o: 
            for x in list_block: # o[1] la global . Called in global. 
                if ctx.name == x.name: 
                    if type(x.typ[0]) is not FunctionType: 
                        raise UndeclaredIdentifier (ctx.name)
                    else:
                        if len(args) != len(x.typ[1]): 
                            raise TypeMismatchInStatement (ctx)
                        for i in range(0,len(args)):
                    # x.typ[1] is Function Enviroment 
                    # o is global environment, which contains Function
                    # up
                            type_of_args = type(self.visit(args[i],o))
                            type_of_param = type(x.typ[1][i].typ[0])
                            # if len(args) == 2:
                                # if type(args[i]) == Id:
                                #     if args[i].name == 'x': 
                                #         raise UndeclaredIdentifier("index = " + str(i) + " val =  " + str(args[i].name) + " type = " + str(type_of_args) +" " + str(x.typ[1][i].name) + str(type_of_param))
                        # raise UndeclaredIdentifier (str(type_of_args))
                            if type_of_args is NoType and type_of_param is NoType:
                                raise TypeCannotBeInferred (ctx)
                            if type_of_args is NoType and type_of_param is not NoType:
                                
                                if type_of_param is IntType: 
                                    Utils.infer(o,args[i].name,IntType())
                                if type_of_param is BoolType: 
                                    Utils.infer(o,args[i].name,BoolType())
                                if type_of_param is FloatType: 
                                    Utils.infer(o,args[i].name,FloatType())
                                type_of_args = type(self.visit(args[i],o))
                                
                            if type_of_args is not NoType and type_of_param is NoType:
                                if type_of_args is IntType: 
                                    Utils.infer([x.typ[1]],x.typ[1][i].name,IntType())
                                if type_of_args is BoolType: 
                                    Utils.infer([x.typ[1]],x.typ[1][i].name,BoolType())
                                if type_of_args is FloatType: 
                                    Utils.infer([x.typ[1]],x.typ[1][i].name,FloatType())
                                type_of_param = type(x.typ[1][i].typ[0])
                                
                                # raise UndeclaredIdentifier (str(type_of_args) + " " + str(test))
                                
                            if type_of_args != type_of_param:
                                raise TypeMismatchInStatement (ctx)
                            # if len(args) == 2: 
                            #     raise UndeclaredIdentifier (str(type_of_args) + " " + str(type_of_param))
                        return
        raise UndeclaredIdentifier(ctx.name)



