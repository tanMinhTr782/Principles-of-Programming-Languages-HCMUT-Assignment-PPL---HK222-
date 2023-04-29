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
    def visitProgram(self,ast,o): 
        o = []
        for decl in ast.decl:
            if type(decl) is FuncDecl: 
                o = self.visit(decl, o)
        return o 
    def visitFuncDecl(self,ast:FuncDecl,o):
        if ast.name in o: 
            return o
        return_typ = self.visit(ast.typ,o)
        global isMainExist
        if ast.name is 'main': 
            if type(return_typ) == VoidType and len(ast.params) == 0: 
                isMainExist = True
        paramTypeOrder = []
        for decl in ast.params: # to get typ order. 
            paramTypeOrder = self.visit(decl,paramTypeOrder)
        o = [FuncSymbol(ast.name,return_typ,paramTypeOrder,ast.inherit,[],ast.body)] + o
        return o
    def visitParamDecl(self, ast, o): # we need prototype at this pharse only ! 
        o += [self.visit(ast.typ,o)]
        return o
    def visitIntegerType(self, ast, o):
        return IntegerType()
    def visitFloatType(self, ast, o):
        return FloatType()
    def visitBooleanType(self, ast, o):
        return BooleanType()
    def visitStringType(self, ast, o): 
        return StringType()
# dimensions: List[int], typ: AtomicType
    def visitArrayType(self, ast, o):
        # Question: Nếu một hàm có kiểu là arraytype
        typ = self.visit(ast.typ,o)
        return ArrayType(ast.dimensions,typ)
    def visitAutoType(self, ast, o): 
        return AutoType()
    def visitVoidType(self, ast, o):
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
    def visitProgram(self,ast,o): 
        global funcDeclOrder
        global isMainExist
        funcDeclOrder = GetEnv().visit(ast, o)
        o = [[]]
        for decl in ast.decl:
            o = self.visit(decl, o)
        if isMainExist == False: 
            raise NoEntryPoint()
    def visitFuncDecl(self,ast:FuncDecl,o):
        if ast.name in o[0]:
            raise Redeclared(Function(),ast.name)
        return_typ = self.visit(ast.typ,o)
        env = [[]] + o
        paramTypeOrder = []
        for decl in ast.params: # to get typ order.
            paramTypeOrder = self.getParamType(decl,paramTypeOrder)
            env = self.visit(decl,env)
        # We handle inheritance here xDDDDD
        # First we check if the function parent body is vaild (incase it also have parent). 
        # Second, we check if the param with keyword "inherit" 
        # is belong to this function 
        # body have 2 case: in a function or in some statement. 
        # inheritance will be the last to solve LOL. I need sleep 
        env = self.visit(ast.body,env)
        o[0] += [FuncSymbol(ast.name,return_typ,paramTypeOrder,ast.inherit,env,[])]
        return o
    def getParamType(self, ast, o): # we need prototype at this pharse only ! 
        o += [self.visit(ast.typ,o)]
        return o
    def visitBlockStmt(self, ast, o):
        for x in ast.body: 
            if type(x) is VarDecl: 
                o = self.visit(x,o)
            else: 
                self.visit(x,o)
        return o                 
    def checkVaildParent(self,ast,o): pass
    def getParentEnvironment(self,ast,o): pass
    def checkInheritParam(self,ast,o): pass
    def visitParamDecl(self, ast, o):
        if ast.name in o[0]: 
            raise Redeclared(Parameter(),ast.name)
        o[0] += [ParamSymbol(ast.name,ast.typ,ast.inherit,ast.out)]
        return o
    def inferVarDecl(self,ast,init,o):
        if type(init) is IntegerType: 
            o[0] += [Symbol(ast.name,IntegerType())]
        if type(init) is StringType: 
            o[0] += [Symbol(ast.name,StringType())]
        if type(init) is FloatType: 
            o[0] += [Symbol(ast.name,FloatType())]
        if type(init) is BooleanType: 
            o[0] += [Symbol(ast.name,BooleanType())]
        # if type(init) is AutoType or if type(init) is VoidType:
        #     raise TypeCannotBeInferred(ast)
        return o
    def inferArrayLit(self,ast,o): pass
    def inferArrayLitEle(self,typ_,exprs): pass
    def visitVarDecl(self, ast, o): 
        # Co suy dien kieu giua 2 phia nua nha ~ 
        # Case 1: lhs co kieu khac auto -> suy dien ben rhs 
        # Case 2 : rhs co kieu -> suy dien ben lhs 
        if ast.name in o[0]: #
            raise Redeclared(Variable(), ast.name)
        typ = self.visit(ast.typ,o) # Looking for its type 
        init = None
        if type(typ) is AutoType and ast.init is None: 
            raise Invaild(Variable(),ast.name)
        if ast.init != None:  
            init = self.visit(ast.init,o)
            if type(typ) is AutoType:
                if type(init) is not ArrayType: 
                    return self.inferVarDecl(ast,init,o)
                if type(init) is ArrayType:
                    return self.inferVarDecl(ast,init.typ,o)
        if type(init) is VoidType: 
            raise Invaild(Variable(),ast.name)
        if type(init) is ArrayType:
            if type(init.typ) is AutoType: # Arraylit with full ID auto type
                self.inferArrayLit(ast,o)
                #return o
            if type(init.typ) != type(typ): 
                raise TypeMismatchInVardecl(ast)
            if len(init.dimensions) != len(ast.dimensions): 
                raise TypeMismatchInVardecl(ast)
            for i in range(len(init.dimensions)): 
                if init.dimensions[i] != ast.dimensions[i]: 
                    raise TypeMismatchInVardecl(ast)
            o[0] += [Symbol(ast.name,typ)]
            return o
        
        if type(typ) is FloatType and type(init) is IntegerType: 
            o[0] += [Symbol(ast.name,typ)]
            return o
        if type(typ) != type(init): 
            raise TypeMismatchInVardecl(ast)
        o[0] += [Symbol(ast.name,typ)]
        return o
    def visitId(self,ast,o):
        for symbol_list in o: 
            for symbol in symbol_list: 
                if symbol.name == ast.name:
                    if type(symbol) is FuncSymbol: 
                        return symbol.typ[1]
                    return symbol.typ[0] 
        raise Undeclared(Identifier(),ast.name)
    def visitArrayLit(self, ast, o): # nho suy dien kieu o day nha :> 
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
        for i in ast.explist: 
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
                if count > 2: raise IllegalArrayLiteral(ast)
            if count == 2:
                for i in range(7):
                    if i != 4: 
                        if typehashmap[i] == len(ele) - typehashmap[4]:
                            if i == 6:  raise IllegalArrayLiteral(ast)
                            type2Infer = i
                            break
                            
            if type2Infer == 0: 
                for x in ast.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(IntegerType(),x)
            if type2Infer == 1: 
                for x in ast.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(FloatType(),x)
            if type2Infer == 2: 
                for x in ast.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(StringType(),x)
            if type2Infer == 3: 
                for x in ast.explist: 
                    kind = self.visit(x,o)
                    if type(kind) is AutoType:
                        self.inferArrayLitEle(BooleanType(),x)
            # if type2Infer == 5: 
            #     for x in ast.explist: 
            #         kind = self.visit(x,o)
            #         if type(kind) is AutoType:
            #             self.inferArrayLitEle(ArrayType(),x)
        if typehashmap[5] == len(ele):
            return ArrayType([len(ele)],ArrayType())
        if typehashmap[6] == len(ele): 
            raise IllegalArrayLiteral(ast)
        for i in range(len(ele)): 
            if type(ele[i]) != type(ele[i+1]): 
                raise IllegalArrayLiteral(ast)
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
    def visitIntegerType(self, ast, o):
        return IntegerType()
    def visitFloatType(self, ast, o):
        return FloatType()
    def visitBooleanType(self, ast, o):
        return BooleanType()
    def visitStringType(self, ast, o): 
        return StringType()
# dimensions: List[int], typ: AtomicType
    def visitArrayType(self, ast, o): 
        typ = self.visit(ast.typ,o)
        return ArrayType(ast.dimension,typ)
    def visitAutoType(self, ast, o): 
        return AutoType()
    def visitVoidType(self, ast, o):
        return VoidType()
# op: str, left: Expr, right: Expr
    def visitBinExpr(self, ast, o):
        lhs = self.visit(ast.left,o)
        rhs = self.visit(ast.right,o)
        arithmetic_op = ['-','+','*','/','%']
        bool_op = ['!','&&','||']
        string_op = ['::']
        relation_op = ['==','!=','>','<','>=','<=']
        # index_op -> Type
        # funcCall -> Type 
        if ast.op in arithmetic_op:
            if ast.op is '%': 
                if type(lhs) is AutoType: 
                    lhs = Utils.infer(o, ast.left.name, IntegerType())
                if type(rhs) is AutoType:
                    rhs = Utils.infer(o, ast.right.name, IntegerType())             
                if type(rhs) == IntegerType and type(lhs) == IntegerType:
                    return IntegerType
                raise TypeMismatchInExpression(ast)
            if type(lhs) is AutoType and type(rhs) is IntegerType: 
                lhs = Utils.infer(o, ast.left.name, IntegerType())
            if type(lhs) is AutoType and type(rhs) is FloatType: 
                lhs = Utils.infer(o, ast.left.name, FloatType())
            if type(rhs) is AutoType and type(lhs) is IntegerType: 
                rhs = Utils.infer(o, ast.right.name, IntegerType())
            if type(rhs) is AutoType and type(lhs) is FloatType: 
                rhs = Utils.infer(o, ast.right.name, FloatType())
            if type(rhs) is not FloatType or IntegerType: 
                raise TypeMisMatchInExpression(ast)
            if type(lhs) is not FloatType or IntegerType: 
                raise TypeMisMatchInExpression(ast)
            
            if type(rhs) == FloatType or type(lhs) == FloatType: 
                return FloatType()  # Implicit conversion
            return IntegerType()
        
        if ast.op in bool_op:
            if type(lhs) is AutoType: 
                lhs = Utils.infer(o, ast.left.name, BooleanType())
            if type(rhs) is AutoType:
                rhs = Utils.infer(o, ast.right.name, BooleanType())             
            if type(rhs) != BooleanType or type(lhs) != BooleanType: 
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        if ast.op in string_op:
            if type(lhs) is AutoType: 
                lhs = Utils.infer(o, ast.left.name, StringType())
            if type(rhs) is AutoType:
                rhs = Utils.infer(o, ast.right.name, StringType())  
            if type(rhs) != StringType or type(lhs) != StringType: 
                raise TypeMismatchInExpression(ast)
            return StringType()
# Case 1: Start       
        if ast.op in relation_op: 
            if ast.op in ['==','!=']:
                
                if type(lhs) is AutoType and type(rhs) is IntegerType: 
                    lhs = Utils.infer(o, ast.left.name, IntegerType())
                if type(lhs) is AutoType and type(rhs) is BooleanType: 
                    lhs = Utils.infer(o, ast.left.name, BooleanType())
                if type(rhs) is AutoType and type(lhs) is IntegerType: 
                    rhs = Utils.infer(o, ast.right.name, IntegerType())
                if type(rhs) is AutoType and type(lhs) is BooleanType: 
                    rhs = Utils.infer(o, ast.right.name, BooleanType())

                if type(rhs) is not BooleanType or IntegerType: 
                    raise TypeMisMatchInExpression(ast)
                if type(lhs) is not BooleanType or IntegerType: 
                    raise TypeMisMatchInExpression(ast)
                return BooleanType()
# Case 1: End

#Case 2: Start 
                
            if type(lhs) is AutoType and type(rhs) is IntegerType: 
                lhs = Utils.infer(o, ast.left.name, IntegerType())
            if type(lhs) is AutoType and type(rhs) is FloatType: 
                lhs = Utils.infer(o, ast.left.name, FloatType())
            if type(rhs) is AutoType and type(lhs) is IntegerType: 
                rhs = Utils.infer(o, ast.right.name, IntegerType())
            if type(rhs) is AutoType and type(lhs) is FloatType: 
                rhs = Utils.infer(o, ast.right.name, FloatType())

            if type(rhs) is not FloatType or IntegerType: 
                raise TypeMisMatchInExpression(ast)
            if type(lhs) is not FloatType or IntegerType: 
                raise TypeMisMatchInExpression(ast)
            return BooleanType()
#Case 2: End. 
    def visitUnExpr(self, ast, o):
        one = self.visit(ast.val,o)

        if ast.op in ['!']: 
            if type(one) is AutoType: 
                one = Utils.infer(o, ast.val.name, BooleanType())
            if type(one) != BooleanType: 
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        # -expr case
        if type(one) != IntegerType or type(one) != FloatType: 
            raise TypeMismatchInExpression(ast)
        return type(one)
    def visitArrayCell(self, ast, o):
        for symbol_list in o: 
            for symbol in o: 
                if type(symbol) is not FuncSymbol: 
                    # Tim dimension size cua array (Co the la Function or variable)
                    cell = []
                    for expr in ast.cell: 
                        typ = self.visit(expr,o)
                        if type(typ) is not IntegerType: 
                            raise TypeMismatchInExpression(ast) # ele trong cell ko integer -> Mismatch
                        cell = cell + [expr]
                    # So sanh 2 dimension vs nhau, neu khac size -> TypeMismatch
                    return symbol.typ[0]
                else: raise TypeMismatchInExpression(ast) 
        raise Undeclared(ast.name)
    def visitIntegerLit(self, ast, o):
        return IntegerType()
    def visitFloatLit(self, ast, o):
        return FloatType()
    def visitStringLit(self, ast, o):
        return StringType()
    def visitBooleanLit(self, ast, o):
        return BooleanType()
   
    def visitFuncCall(self, ast, o): pass
# self, lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast, o):
        lhs = self.visit(ast.lhs,o)
        rhs = self.visit(ast.rhs,o)
        if type(lhs) is VoidType or type(rhs) is VoidType: 
            raise TypeMismatchInStatement(ast)
        if type(lhs) is ArrayType or type(rhs) is ArrayType: 
            raise TypeMismatchInStatement(ast)
        if type(lhs) is AutoType: 
            if type(rhs) is AutoType: 
                return # raise TypeCannotBeInferred(ast)
            if type(rhs) is BooleanType: 
                lhs = Utils.infer(ast.lhs.name,o,BooleanType())
            if type(rhs) is IntegerType: 
                lhs = Utils.infer(ast.lhs.name,o,IntegerType())
            if type(rhs) is FloatType: 
                lhs = Utils.infer(ast.lhs.name,o,FloatType())
            if type(rhs) is StringType: 
                lhs = Utils.infer(ast.lhs.name,o,StringType())
        if type(rhs) is AutoType: 
            if type(lhs) is AutoType:
                return # raise TypeCannotBeInferred(ast)
            if type(lhs) is BooleanType: 
                rhs = Utils.infer(ast.rhs.name,o,BooleanType())
            if type(lhs) is IntegerType: 
                rhs = Utils.infer(ast.rhs.name,o,IntegerType())
            if type(lhs) is FloatType: 
                rhs = Utils.infer(ast.rhs.name,o,FloatType())
            if type(lhs) is StringType: 
                rhs = Utils.infer(ast.rhs.name,o,StringType())
        if type(lhs) != type(rhs): 
            if type(lhs) == IntegerType and type(rhs) == FloatType: 
                raise TypeMismatchInStatement(ast)
            if type(lhs) == FloatType and type(rhs) == IntegerType:
                return
            raise TypeMismatchInStatement(ast) 
        return
# For an assignment statement, the left-hand side can be in 
# any type except void type and
# array type. The right-hand side (RHS) is either in 
# the same type as that of the LHS or
# in the type that can coerce to the LHS type.
    def visitIfStmt(self, ast, o):
        type_cond = self.visit(ast.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        env = [[]] + o
        env = self.visit(ast.tstmt,env)
        # reset env 
        if ast.fstmt is not None:
            env = [[]] + o 
            env = self.visit(ast.fstmt,env)
        return env
    def visitForStmt(self, ast, o):
        type_init = self.visit(ast.init,o)
        if type(type_init) is not IntegerType: 
            raise TypeMismatchInStatement(ast) 
              
        type_cond = self.visit(ast.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        
        type_update = self.visit(ast.upd,o)
        if type(type_update) is not IntegerType: 
            raise TypeMismatchInStatement(ast)
        env = [[]] + o
        env = self.visit(ast.stmt,env)
        return env
    def visitWhileStmt(self, ast, o):
        type_cond = self.visit(ast.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        env = [[]] + o
        env = self.visit(ast.stmt,env)
        return env
    def visitDoWhileStmt(self, ast, o):
        type_cond = self.visit(ast.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        env = [[]] + o
        env = self.visit(ast.stmt,env)
        return env      
    def visitBreakStmt(self, ast, o): pass
    def visitContinueStmt(self, ast, o): pass
    def visitReturnStmt(self, ast, o):
        if ast.expr is None: 
            return None
        return self.visit(ast.expr,o)
    def visitCallStmt(self, ast, o):
 #args la id: No o dau ? Global or Function Scope.
        #args ko co type. Chi co Literal -> Type hoac Id -> Type.
        args = ast.args
        # raise UndeclaredIdentifier(str(type(o[0])))
        for list_block in o: 
            for x in list_block: # o[1] la global . Called in global. 
                if ast.name == x.name: 
                    if type(x.typ[0]) is not FunctionType: 
                        raise UndeclaredIdentifier (ast.name)
                    else:
                        if len(args) != len(x.typ[1]): 
                            raise TypeMismatchInStatement (ast)
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
                                raise TypeCannotBeInferred (ast)
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
                                raise TypeMismatchInStatement (ast)
                            # if len(args) == 2: 
                            #     raise UndeclaredIdentifier (str(type_of_args) + " " + str(type_of_param))
                        return
        raise UndeclaredIdentifier(ast.name)



