from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC
class Symbol(): 
    def __init__(self,name,typ):
        self.name = name
        self.typ = typ # define as list to seperate with Function
    def __str__(self):
        return "Symbol({}, {})".format(str(self.name), str(self.typ))
class FuncSymbol(Symbol): 
    def __init__(self,name,return_type,paramTypeOrder,inherit,env,body): 
        self.name = name
        self.return_type = return_type
        self.paramTypeOrder = paramTypeOrder 
        self.inherit = inherit # Parent's name is here ! 
        self.env = env # ParamDecl + VarDecl inside Function 
        self.body = body
class ParamSymbol(Symbol): 
    def __init__(self,name,typ,inherit,out):
        self.name = name
        self.typ = typ
        self.inherit = inherit
        self.out = out

class Utils(): 
    def infer(SymbolTable,name,typ): 
        for symbol_list in SymbolTable: 
            for symbol in symbol_list: 
                if symbol.name == name: 
                    if type(symbol) is FuncSymbol: symbol.return_type = typ 
                    else: 
                        symbol.typ = typ
                    return typ
isMainExist = False
funcDeclOrder = []
fatherExist = False
callOrder = []
glbTemp = []
class GetEnv(Visitor): #visit vong ngoai truoc, tuc cac khai bao o tam vuc global.\
    def __init__(self, ast, preDefined):
        self.ast = ast
        self.preDefined = preDefined
    def check(self):
        return self.visitProgram(self.ast,self.preDefined)
    def visitProgram(self,ast,o:object): 
        for decl in ast.decls:
            if type(decl) is FuncDecl: 
                o = self.visit(decl, o)
        return o 
    def visitFuncDecl(self,ast,o):
        if ast.name in o: 
            return o
        return_type = ast.return_type
        global isMainExist
        if ast.name == 'main': 
            if type(return_type) == VoidType and len(ast.params) == 0: 
                isMainExist = True
        paramTypeOrder = []
        for decl in ast.params: # to get typ order. 
            paramTypeOrder = self.visit(decl,paramTypeOrder)
        body = self.visit(ast.body,o)
        o = [FuncSymbol(ast.name,return_type,paramTypeOrder,ast.inherit,[],body)] + o
        return o
    def visitParamDecl(self, ast, o): # we need prototype at this pharse only 
        o += [ParamSymbol(ast.name,self.visit(ast.typ,o),ast.inherit,ast.out)]
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
    def visitBlockStmt(self, ast, param):
        return ast.body
class StaticChecker(Visitor):
    preDefinedFunction = [FuncSymbol("readInteger",IntegerType(),[],None,[],[]) 
                      , FuncSymbol("printInteger",IntegerType(),[IntegerType()],None,[],[]) 
                      , FuncSymbol("readFloat",FloatType(),[],None,[],[]) 
                      , FuncSymbol("writeFloat",FloatType(),[FloatType()],None,[],[]) 
                      , FuncSymbol("readBoolean",BooleanType(),[],None,[],[]) 
                      , FuncSymbol("printBoolean",BooleanType(),[BooleanType()],None,[],[])
                      , FuncSymbol("readString",StringType(),[],None,[],[])
                      , FuncSymbol("printString",StringType(),[StringType()],None,[],[])
                      ,FuncSymbol("super",StringType(),[StringType()],None,[],[])
                      , FuncSymbol("preventDefault",None,[],None,[],[])
                      ]
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast,StaticChecker.preDefinedFunction)
    def visitProgram(self,ast,o:object): 
        global funcDeclOrder
        global isMainExist
        round1 = GetEnv(ast,StaticChecker.preDefinedFunction)
        funcDeclOrder = round1.visit(ast, o)
        o = [[]] + [o]
        for decl in ast.decls:
            o = self.visit(decl, o)
        # global callOrder
        # callOrder = []
        if isMainExist == False: 
            raise NoEntryPoint()
        
    def visitFuncDecl(self,ast:FuncDecl,o:object):
        global funcDeclOrder
        global fatherExist
        # global callOrder
        if ast.name in o[0]:
            raise Redeclared(Function(),ast.name)
        return_type = self.visit(ast.return_type,o)
        env = [[]] + o
        paramTypeOrder = []
        body = []
        for decl in ast.params: # to check if redeclared happen in parameter
            env = self.visit(decl,env)
        for func in funcDeclOrder: # No error ? We inherit the order from round 1 ! 
            if func.name == ast.name: 
                env[0] = func.paramTypeOrder
                body = func.body
                return_type = func.return_type
                break
        for param in env[0]: 
            paramTypeOrder += [param.typ]
        #Round 1: Check if parent exist, then check inherit parameter. 
        if ast.inherit is not None:
            for father in funcDeclOrder: 
                if father.name == ast.inherit: 
                    fatherExist = True
                    if type(body[0]) is CallStmt: 
                        if body[0].name == "preventDefault": 
                            break
                    self.checkVaildParent(father.paramTypeOrder)
                    for param_father in father.paramTypeOrder: 
                            if param_father.inherit is not None:
                                for x in env[0]: 
                                    if param_father.name == x.name: 
                                        raise Invalid(Parameter(),param_father.name)
                                env[0] += [param_father]
                    for child in funcDeclOrder: 
                        if child.name == ast.name:
                            if len(child.body) == 0: 
                                raise InvalidStatementInFunction(ast)
                            if type(child.body[0]) is not CallStmt: 
                                # vaildFirstStmt = False
                                raise InvalidStatementInFunction(child.body[0])
                            if child.body[0].name != "super" and child.body[0].name != "preventDefault":
                                # vaildFirstStmt = False
                                raise InvalidStatementInFunction(child.body[0])
                            if child.body[0].name == "super":
                                superCalledFromChild = []
                                for arg in child.body[0].args: 
                                    superCalledFromChild += [self.visit(arg,env)]
                                if len(father.paramTypeOrder) != len(superCalledFromChild):
                                    if len(superCalledFromChild) != len(father.paramTypeOrder):
                                        if len(superCalledFromChild) > len(father.paramTypeOrder):
                                                if len(father.paramTypeOrder) != 0: 
                                                    raise TypeMismatchInExpression (child.body[0].args[len(x.paramTypeOrder) - 1])
                                                else: raise TypeMismatchInExpression("")
                                        else: 
                                            if len(superCalledFromChild) != 0: 
                                                raise TypeMismatchInExpression (child.body[0].args[len(x.superCalledFromChild) - 1])
                                            else: raise TypeMismatchInExpression("")
                                    # vaildFirstStmt = False
                                    # raise Undeclared(Function(),str(len(superCalledFromChild)))
                                if len(father.paramTypeOrder) != 0: 
                                    for i in range(len(superCalledFromChild)):
                                        superfromChild_arg_type = type(superCalledFromChild[i])
                                        if type(father.paramTypeOrder[i].typ) is AutoType: 
                                            if superfromChild_arg_type is BooleanType: 
                                                father.paramTypeOrder[i].typ = BooleanType()
                                            if superfromChild_arg_type is IntegerType: 
                                                father.paramTypeOrder[i].typ = IntegerType()
                                            if superfromChild_arg_type is FloatType: 
                                                father.paramTypeOrder[i].typ = FloatType()
                                            if superfromChild_arg_type is StringType: 
                                                father.paramTypeOrder[i].typ = StringType()
                                        
                                        if superfromChild_arg_type is AutoType: 
                                            if type(father.paramTypeOrder[i].typ) is BooleanType:
                                                superfromChild_arg_type = Utils.infer(env,child.body[0].args[i].name,BooleanType()) 
                                            if type(father.paramTypeOrder[i].typ) is IntegerType: 
                                                superfromChild_arg_type = Utils.infer(env,child.body[0].args[i].name,IntegerType())
                                            if type(father.paramTypeOrder[i].typ) is FloatType: 
                                                superfromChild_arg_type = Utils.infer(env,child.body[0].args[i].name,FloatType())
                                            if type(father.paramTypeOrder[i].typ) is StringType: 
                                                superfromChild_arg_type = Utils.infer(env,child.body[0].args[i].name,StringType())
                                            superfromChild_arg_type = type(superfromChild_arg_type)                           
                                        if superfromChild_arg_type != type(father.paramTypeOrder[i].typ): 
                                            if superfromChild_arg_type is IntegerType and type(father.paramTypeOrder[i].typ) is FloatType:
                                                break 
                                            else:
                                                raise TypeMismatchInStatement(child.body[0])
                            if child.body[0].name == "preventDefault": 
                                break
                    break
            if fatherExist == False: 
                raise Undeclared(Function(),ast.inherit)
        cntReturn = 0
        cntLoop = 0
        callList = [] + ['FuncDecl']
        dive = [cntReturn,ast.name,env,callList]
        for cmd in body: 
            if type(cmd) is VarDecl: 
                env = self.visit(cmd,env)
            elif type(cmd) is ReturnStmt: 
                getType = self.visit(cmd,dive)
                if getType != None: 
                    return_type = getType
            elif type(cmd) is ContinueStmt or type(cmd) is BreakStmt: 
                raise MustInLoop()
            else: self.visit(cmd,env)
   
        o[0] += [FuncSymbol(ast.name,return_type,paramTypeOrder,ast.inherit,env,body)]
        # callOrder = []
        return o
    def getParamType(self, ast, o): # we need prototype at this pharse only ! 
        o += [self.visit(ast.typ,o)]
        return o
    def visitBlockStmt(self, ast, o):
        return ast.body
        # env = [[]] + o
        # cnt_break_cont = 0
        # cnt_break_cont_return = 0
        # for x in ast.body: 
        #     if type(x) is VarDecl: 
        #         env = self.visit(x,env)
        #     # elif type(x) is BreakStmt or type(x) is ContinueStmt or type(x) is ReturnStmt: 
        #     #     # cnt_break_cont += 1
        #     #     # cnt_break_cont_return += 1
        #     #     # if cnt_break_cont > 1 or cnt_break_cont_return > 1: return 
        #     #     self.visit(x,env)
        #     else: self.visit(x,env)
        # return o                 
    def checkVaildParent(self,o):
        size = len(o)
        for i in range(1,size): 
            for j in range(0,i):
                if o[i].name == o[j].name: 
                    raise Redeclared(Parameter(),o[i].name)
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
    def inferFuncDecl(self,ast,typ_,o): 
        global funcDeclOrder
        gblScope = len(o) - 1
        ret = None 
        for x in o[gblScope]: 
            if x.name == ast.name:
                if type(typ_) is IntegerType: 
                    ret = Utils.infer(ast.name,o[gblScope],IntegerType())
                elif type(typ_) is StringType: 
                    ret = Utils.infer(ast.name,o[gblScope],StringType())
                elif type(typ_) is FloatType: 
                    ret = Utils.infer(ast.name,o[gblScope],FloatType())
                elif type(typ_) is BooleanType: 
                    ret = Utils.infer(ast.name,o[gblScope],BooleanType())
                elif type(typ_) is ArrayType: pass
                return ret
        for x in funcDeclOrder: 
            if x.name == ast.name:
                if type(typ_) is IntegerType: 
                    ret = Utils.infer(ast.name,funcDeclOrder,IntegerType())
                elif type(typ_) is StringType: 
                    ret = Utils.infer(ast.name,funcDeclOrder,StringType())
                elif type(typ_) is FloatType: 
                    ret = Utils.infer(ast.name,funcDeclOrder,FloatType())
                elif type(typ_) is BooleanType: 
                    ret = Utils.infer(ast.name,funcDeclOrder,BooleanType())
                elif type(typ_) is ArrayType: pass
                return ret
        raise Undeclared(Function(),ast.name)
    def inferArrayLit(self,ast,o): pass
    def inferArrayLitEle(self,typ_,exprs): pass
    def inferID(self,ast, typ_,o): 
        for symbol_list in o: 
            for symbol in symbol_list: 
                if symbol.name == ast.name: 
                    if type(typ_) is IntegerType: 
                        ret = Utils.infer(ast.name,symbol_list,IntegerType())
                    elif type(typ_) is StringType: 
                        ret = Utils.infer(ast.name,symbol_list,StringType())
                    elif type(typ_) is FloatType: 
                        ret = Utils.infer(ast.name,symbol_list,FloatType())
                    elif type(typ_) is BooleanType: 
                        ret = Utils.infer(ast.name,symbol_list,BooleanType())
                    elif type(typ_) is ArrayType: pass
                    return True
        return False
    def visitVarDecl(self, ast, o): 
        # Co suy dien kieu giua 2 phia nua nha ~ 
        # Case 1: lhs co kieu khac auto -> suy dien ben rhs 
        # Case 2 : rhs co kieu -> suy dien ben lhs 
        for x in o[0]:
            if ast.name == x.name: #
                raise Redeclared(Variable(), ast.name)
        typ = ast.typ # Looking for its type 
        init = None
        if type(typ) is AutoType and ast.init is None: 
            raise Invalid(Variable(),ast.name)
        if ast.init is not None:  
            init = self.visit(ast.init,o)
            if type(typ) is AutoType:
                if type(init) is not ArrayType: 
                    return self.inferVarDecl(ast,init,o)
                if type(init) is ArrayType:
                    return self.inferVarDecl(ast,init.typ,o)
            if type(init) is VoidType: 
                raise Invalid(Variable(),ast.name)
            if type(init) is ArrayType:
                if type(init.typ) is AutoType: # Arraylit with full ID auto type
                    self.inferArrayLit(ast,o)
                    #return o
                if type(typ) is ArrayType: 
                    if type(init.typ) != type(typ.typ) or len(init.dimensions) != len(typ.dimensions): 
                        raise TypeMismatchInVarDecl(ast)
                    for i in range(len(init.dimensions)): 
                        if init.dimensions[i] != typ.dimensions[i]: 
                            raise TypeMismatchInVarDecl(ast)
                o[0] += [Symbol(ast.name,typ)]
                return o
            if type(init) is AutoType: #Function in Global or Function/Var inside function.     
                if type(typ) is AutoType: 
                    return o
                else: 
                    if type(ast.init) is FuncCall: 
                        self.inferFuncDecl(ast.init,typ,o)
                    else: self.inferID(ast.init,typ,o)

            if type(typ) is FloatType and type(init) is IntegerType: 
                o[0] += [Symbol(ast.name,typ)]
                return o
            if type(typ) != type(init): 
                raise TypeMismatchInVarDecl(ast)
        o[0] += [Symbol(ast.name,typ)]
        return o
    def visitId(self,ast,o:object):
        for symbol_list in o: 
            for symbol in symbol_list: 
                if symbol.name == ast.name:
                    if type(symbol) is FuncSymbol: 
                        return symbol.return_type
                    return symbol.typ 
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
            ele += [self.visit(i,ele)]
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
        for i in range(len(ele) - 1): 
            if type(ele[i]) != type(ele[i+1]): 
                raise IllegalArrayLiteral(ast)
            # trong array co arraylit thi sao ? rofllmao , case nay bo nha ! 
            # tinh sau, met qua !
        if (type(ele[0])) is IntegerType: 
            return ArrayType([len(ele)],IntegerType())
        if (type(ele[0])) is BooleanType: 
            return ArrayType([len(ele)],BooleanType())
        if (type(ele[0])) is FloatType: 
            return ArrayType([len(ele)],FloatType())
        return ArrayType([len(ele)],StringType())       
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
            if ast.op =='%': 
                if type(lhs) is AutoType: 
                    lhs = Utils.infer(o, ast.left.name, IntegerType())
                if type(rhs) is AutoType:
                    rhs = Utils.infer(o, ast.right.name, IntegerType())             
                if type(rhs) == IntegerType and type(lhs) == IntegerType:
                    return IntegerType()
                raise TypeMismatchInExpression(ast)
            if type(lhs) is AutoType: 
                if type(rhs) is IntegerType: 
                    lhs = Utils.infer(o, ast.left.name, IntegerType())
                if type(rhs) is FloatType: 
                    lhs = Utils.infer(o, ast.left.name, FloatType())
            if type(rhs) is AutoType: 
                if type(lhs) is IntegerType: 
                    rhs = Utils.infer(o, ast.right.name, IntegerType())
                if type(lhs) is FloatType: 
                    rhs = Utils.infer(o, ast.right.name, FloatType())
            if type(rhs) is not FloatType and type(rhs) is not IntegerType: 
                raise TypeMismatchInExpression(ast)
            if type(lhs) is not FloatType and type(lhs) is not IntegerType: 
                raise TypeMismatchInExpression(ast)
     
            if type(rhs) == FloatType or type(lhs) == FloatType: 
                return FloatType()  # Implicit conversion
            return IntegerType()
        
        if ast.op in bool_op:
            if type(lhs) is AutoType: 
                lhs = Utils.infer(o, ast.left.name, BooleanType())
            if type(rhs) is AutoType:
                rhs = Utils.infer(o, ast.right.name, BooleanType())             
            if type(rhs) is not BooleanType or type(lhs) is not BooleanType: 
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        if ast.op in string_op:
            if type(lhs) is AutoType: 
                lhs = Utils.infer(o, ast.left.name, StringType())
            if type(rhs) is AutoType:
                rhs = Utils.infer(o, ast.right.name, StringType())  
            if type(rhs) is not StringType or type(lhs) is not StringType: 
                raise TypeMismatchInExpression(ast)
            return StringType()
# Case 1: Start       
        if ast.op in relation_op: 
            if ast.op in ['==','!=']:
                
                if type(lhs) is AutoType: 
                    if type(rhs) is IntegerType: 
                        lhs = Utils.infer(o, ast.left.name, IntegerType())
                    if type(rhs) is BooleanType: 
                        lhs = Utils.infer(o, ast.left.name, BooleanType())
                if type(rhs) is AutoType:
                    if type(lhs) is IntegerType: 
                        rhs = Utils.infer(o, ast.right.name, IntegerType())
                    if type(lhs) is BooleanType: 
                        rhs = Utils.infer(o, ast.right.name, BooleanType())

                if type(rhs) is not BooleanType and type(rhs) is not IntegerType: 
                    raise TypeMismatchInExpression(ast)
                if type(lhs) is not BooleanType and type(lhs) is not IntegerType: 
                    raise TypeMismatchInExpression(ast)
                return BooleanType()
# Case 1: End

#Case 2: Start 
                
            if type(lhs) is AutoType:
                if type(rhs) is IntegerType: 
                    lhs = Utils.infer(o, ast.left.name, IntegerType())
                if type(rhs) is FloatType: 
                    lhs = Utils.infer(o, ast.left.name, FloatType())
            if type(rhs) is AutoType:
                if type(lhs) is IntegerType: 
                    rhs = Utils.infer(o, ast.right.name, IntegerType())
                if type(lhs) is FloatType: 
                    rhs = Utils.infer(o, ast.right.name, FloatType())

            if type(rhs) is not FloatType and type(rhs) is not IntegerType: 
                raise TypeMismatchInExpression(ast)
            if type(lhs) is not FloatType and type(lhs) is not IntegerType: 
                raise TypeMismatchInExpression(ast)
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
        if type(one) != IntegerType and type(one) != FloatType: 
            raise TypeMismatchInExpression(ast)
        return one
    def visitArrayCell(self, ast, o):
        for symbol_list in o: 
            for symbol in symbol_list: 
                if type(symbol) is not FuncSymbol: 
                    # Tim dimension size cua array (Co the la Function or variable)
                    cell = []
                    for expr in ast.cell: 
                        typ = self.visit(expr,o)
                        if type(typ) is not IntegerType: 
                            raise TypeMismatchInExpression(ast) # ele trong cell ko integer -> Mismatch
                        cell = cell + [expr]
                    # So sanh 2 dimension vs nhau, neu khac size -> TypeMismatch
                    return symbol.typ
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
   
    def visitFuncCall(self, ast, o): 
 #args la id: No o dau ? Global or Function Scope.
        #args ko co type. Chi co Literal -> Type hoac Id -> Type.
        args = ast.args
        scopesize = len(o)
        return_type = None
        # raise UndeclaredIdentifier(str(type(o[0]))) 
        for x in o[scopesize - 1]: # o[1] la global . Called in global. 
            if ast.name == x.name: 
                if type(x) is not FuncSymbol: 
                    raise Undeclared(Function(),ast.name)
                else:
                    if len(args) != len(x.paramTypeOrder):
                        if len(args) > len(x.paramTypeOrder):
                            if len(x.paramTypeOrder) != 0: 
                                raise TypeMismatchInExpression (args[len(x.paramTypeOrder) - 1])
                            else: raise TypeMismatchInStatement(ast)
                        else: 
                            if len(args) != 0: 
                                raise TypeMismatchInStatement(ast)
                    for i in range(0,len(args)):
                # x.typ[1] is Function Enviroment 
                # o is global environment, which contains Function
                # up
                        type_of_args = type(self.visit(args[i],o))
                        type_of_param = type(x.paramTypeOrder[i])

                        if type_of_args is AutoType and type_of_param is AutoType:
                            # raise TypeCannotBeInferred (ast)
                            return
                        if type_of_args is AutoType:
                            if type_of_param is IntegerType: 
                                type_of_args = Utils.infer(o,args[i].name,IntegerType())
                            if type_of_param is BooleanType: 
                                type_of_args = Utils.infer(o,args[i].name,BooleanType())
                            if type_of_param is FloatType: 
                                type_of_args = Utils.infer(o,args[i].name,FloatType())
                            if type_of_param is StringType: 
                                type_of_args = Utils.infer(o,args[i].name,StringType())
                            if type_of_param is ArrayType: 
                                type_of_args = Utils.infer(o,args[i].name,type_of_param)
                            type_of_args = type(type_of_args)
                        if type_of_param is AutoType:
                            if type_of_args is IntegerType: 
                                Utils.infer(x.env,x.env[i].name,IntegerType())
                                x.paramTypeOrder[i] = IntegerType()
                            if type_of_args is BooleanType: 
                                Utils.infer(x.env,x.env[i].name,BooleanType())
                                x.paramTypeOrder[i] = BooleanType()
                            if type_of_args is FloatType: 
                                Utils.infer(x.env,x.env[i].name,FloatType())
                                x.paramTypeOrder[i] = FloatType()
                            if type_of_args is StringType: 
                                Utils.infer(x.env,x.env[i].name,StringType())
                                x.paramTypeOrder[i] = StringType()
                            if type_of_args is ArrayType: 
                                type_of_param = Utils.infer(o,args[i].name,type_of_param)
                                x.paramTypeOrder[i] = type_of_param                                        
                            type_of_param = x.paramTypeOrder[i]
                                                            
                        if type_of_args != type_of_param:
                            raise TypeMismatchInExpression (args[i])
                    return x.return_type
        for x in funcDeclOrder:
            if x.name == ast.name:
                if len(args) != len(x.paramTypeOrder):
                    if len(args) > len(x.paramTypeOrder):
                        if len(x.paramTypeOrder) != 0: 
                            raise TypeMismatchInExpression (args[len(x.paramTypeOrder) - 1])
                        else: raise TypeMismatchInStatement(ast)
                    else: 
                        if len(args) != 0: 
                            raise TypeMismatchInStatement(ast)
                for i in range(0,len(args)):
                    type_of_args = type(self.visit(args[i],o))
                    type_of_param = type(x.paramTypeOrder[i].typ)

                    if type_of_args is AutoType and type_of_param is AutoType:
                        # raise TypeCannotBeInferred (ast)
                        return
                    if type_of_args is AutoType:           
                        if type_of_param is IntegerType: 
                            type_of_args = Utils.infer(o,args[i].name,IntegerType())
                        if type_of_param is BooleanType: 
                            type_of_args = Utils.infer(o,args[i].name,BooleanType())
                        if type_of_param is FloatType: 
                            type_of_args = Utils.infer(o,args[i].name,FloatType())
                        if type_of_param is StringType: 
                            type_of_args = Utils.infer(o,args[i].name,StringType())
                        if type_of_param is ArrayType: 
                            type_of_args = Utils.infer(o,args[i].name,type_of_param)
                        type_of_args = type(type_of_args)
                    if type_of_param is AutoType: 
                        if type_of_args is IntegerType: 
                            x.paramTypeOrder[i].typ = Utils.infer(x.env,x.env[i].name,IntegerType())
                        if type_of_args is BooleanType: 
                            x.paramTypeOrder[i].typ = Utils.infer(x.env,x.env[i].name,BooleanType())
                        if type_of_args is FloatType: 
                            x.paramTypeOrder[i].typ = Utils.infer(x.env,x.env[i].name,FloatType())
                        if type_of_args is StringType: 
                            x.paramTypeOrder[i].typ =Utils.infer(x.env,x.env[i].name,StringType())
                        if type_of_args is ArrayType: 
                            x.paramTypeOrder[i].typ = Utils.infer(x.env,x.env[i].name,type_of_param)
                        type_of_param = type(x.paramTypeOrder[i].typ)                                  
                     
                    if type_of_args != type_of_param:
                        raise TypeMismatchInExpression (args[i])
                return x.return_type
        raise Undeclared(Function(),ast.name)
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
                lhs = Utils.infer(o,ast.lhs.name,BooleanType())
            if type(rhs) is IntegerType: 
                lhs = Utils.infer(o,ast.lhs.name,IntegerType())
            if type(rhs) is FloatType: 
                lhs = Utils.infer(o,ast.lhs.name,FloatType())
            if type(rhs) is StringType: 
                lhs = Utils.infer(o,ast.lhs.name,StringType())
        if type(rhs) is AutoType: 
            if type(lhs) is AutoType:
                return # raise TypeCannotBeInferred(ast)
            if type(lhs) is BooleanType: 
                rhs = Utils.infer(o,ast.rhs.name,BooleanType())
            if type(lhs) is IntegerType: 
                rhs = Utils.infer(o,ast.rhs.name,IntegerType())
            if type(lhs) is FloatType: 
                rhs = Utils.infer(o,ast.rhs.name,FloatType())
            if type(lhs) is StringType: 
                rhs = Utils.infer(o,ast.rhs.name,StringType())
        if type(lhs) != type(rhs): 
            if type(lhs) == IntegerType and type(rhs) == FloatType: 
                raise TypeMismatchInStatement(ast)
            if type(lhs) == FloatType and type(rhs) == IntegerType:
                return FloatType()
            raise TypeMismatchInStatement(ast) 
        return lhs
# For an assignment statement, the left-hand side can be in 
# any type except void type and
# array type. The right-hand side (RHS) is either in 
# the same type as that of the LHS or
# in the type that can coerce to the LHS type.
    def visitIfStmt(self, ast, o):
        # global callOrder
        # temp = callOrder      
        # callOrder += ['IfStmt'] 

        type_cond = self.visit(ast.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        env = [[]] + o
        count_continue_break = 0
        body = []
        if type(ast.tstmt) is BlockStmt: 
            body = self.visit(ast.tstmt,o)
            for stmt in body: 
                if type(stmt) is VarDecl: 
                    env = self.visit(stmt,env)
                else: self.visit(stmt,env)
        else: 
            if type(ast.tstmt) is ContinueStmt or type(ast.tstmt) is BreakStmt: 
                self.visit(ast.tstmt,[count_continue_break])
            else: 
                self.visit(ast.tstmt,env)
        # reset env 
        if ast.fstmt is not None:
            env = [[]] + o 
            count_continue_break = 0
            if type(ast.fstmt) is BlockStmt: 
                body = self.visit(ast.fstmt,o)
            for stmt in body: 
                if type(stmt) is VarDecl: 
                    env = self.visit(stmt,env)
                else: self.visit(stmt,env)
            else: 
                if type(ast.fstmt) is ContinueStmt or type(ast.fstmt) is BreakStmt: 
                    self.visit(ast.fstmt,[count_continue_break])
                else: 
                    self.visit(ast.fstmt,env)

        # callOrder = temp
        
        return o 
    def visitForStmt(self, ast, o):
        # global callOrder
        # temp = callOrder
        # callOrder += ['ForStmt']

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

        count_continue_break = 0
        if type(ast.stmt) is BlockStmt: 
            body = self.visit(ast.stmt,o)
            for stmt in body: 
                if type(stmt) is VarDecl: 
                    env = self.visit(stmt,env)
                else: self.visit(stmt,env)
        else: 
            if type(ast.stmt) is ContinueStmt or type(ast.stmt) is BreakStmt: 
                self.visit(ast.stmt,[count_continue_break])
            else: 
                self.visit(ast.stmt,env)
        # raise Undeclared(Function(),callOrder)
        return o
    def visitWhileStmt(self, ast, o):
        # global callOrder
        # temp = callOrder
        # callOrder += ['WhileStmt']  

        type_cond = self.visit(ast.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        env = [[]] + o
        
        count_continue_break = 0
        if type(ast.stmt) is BlockStmt: 
            body = self.visit(ast.stmt,o)
            for stmt in body: 
                if type(stmt) is VarDecl: 
                    env = self.visit(stmt,env)
                else: self.visit(stmt,env)
        else: 
            if type(ast.stmt) is ContinueStmt or type(ast.stmt) is BreakStmt: 
                self.visit(ast.stmt,[count_continue_break])
            else: 
                self.visit(ast.stmt,env)

        # callOrder = temp

        return o
    def visitDoWhileStmt(self, ast, o):
        # global callOrder
        # temp = callOrder
        # callOrder += ['DoWhileStmt'] 
        
        type_cond = self.visit(ast.cond,o)
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        env = [[]] + o

        body = self.visit(ast.stmt,o)
        for stmt in body: 
            if type(stmt) is VarDecl: 
                env = self.visit(stmt,env)
            else: self.visit(stmt,env)

        # callOrder = temp

        return o      
    def visitBreakStmt(self, ast, o):
        o[0] = o[0] + 1
        if o[0] >= 1: return
        global callOrder
        for x in callOrder: 
            if x == "ForStmt" or x == "WhileStmt" or x == "DoWhileStmt": 
                # inLoop = True
                return
        raise MustInLoop(ast)
    
    def visitContinueStmt(self, ast, o): 
        o[0] = o[0] + 1
        if o[0] > 1: return

        global callOrder
        for x in callOrder: 
            if x == "ForStmt" or x == "WhileStmt" or x == "DoWhileStmt": 
                # inLoop = True
                return
        raise MustInLoop(ast)
    def visitReturnStmt(self, ast, o):
        # 0: so luong ham returnstmt trong Block
        # 1: TenHam / -1
        # 2: GlobalScope
        o[0] = o[0] + 1
        if o[0] > 1: return 1
        # Chua Suy dien~ Kieu.
        typ = None
        for x in funcDeclOrder:
            if x.name == o[1]: 
                if type(ast.expr) is None: 
                    typ = VoidType()
                else: typ = self.visit(ast.expr,o[2])
                if type(x.return_type) is AutoType: 
                    x.return_typ = typ
                return typ
        return typ
    def visitCallStmt(self, ast, o):
 #args la id: No o dau ? Global or Function Scope.
        #args ko co type. Chi co Literal -> Type hoac Id -> Type.
        global funcDeclOrder
        if ast.name == "super" or ast.name == "preventDefault": 
            return VoidType()
        args = ast.args
        scopesize = len(o)
        # raise UndeclaredIdentifier(str(type(o[0]))) 
        for x in o[scopesize - 1]: # o[1] la global . Called in global. 
            if ast.name == x.name: 
                if type(x) is not FuncSymbol: 
                    raise Undeclared(Function(),ast.name)
                else:
                    if len(args) != len(x.paramTypeOrder):
                        if len(args) > len(x.paramTypeOrder):
                            if len(x.paramTypeOrder) != 0: 
                                raise TypeMismatchInExpression (args[len(x.paramTypeOrder) - 1])
                            else: raise TypeMismatchInStatement(ast)
                        else: 
                            if len(args) != 0: 
                                raise TypeMismatchInStatement(ast)
                    for i in range(0,len(args)):
                # x.typ[1] is Function Enviroment 
                # o is global environment, which contains Function
                # up
                        type_of_args = type(self.visit(args[i],o))
                        type_of_param = type(x.paramTypeOrder[i])

                        if type_of_args is AutoType and type_of_param is AutoType:
                            # raise TypeCannotBeInferred (ast)
                            return
                        if type_of_args is AutoType:
                            if type_of_param is IntegerType: 
                                type_of_args = Utils.infer(o,args[i].name,IntegerType())
                            if type_of_param is BooleanType: 
                                type_of_args = Utils.infer(o,args[i].name,BooleanType())
                            if type_of_param is FloatType: 
                                type_of_args = Utils.infer(o,args[i].name,FloatType())
                            if type_of_param is StringType: 
                                type_of_args = Utils.infer(o,args[i].name,StringType())
                            if type_of_param is ArrayType: 
                                type_of_args = Utils.infer(o,args[i].name,type_of_param)
                            type_of_args = type(type_of_args)
                        if type_of_param is AutoType:
                            if type_of_args is IntegerType: 
                                Utils.infer(x.env,x.env[i].name,IntegerType())
                                x.paramTypeOrder[i] = IntegerType()
                            if type_of_args is BooleanType: 
                                Utils.infer(x.env,x.env[i].name,BooleanType())
                                x.paramTypeOrder[i] = BooleanType()
                            if type_of_args is FloatType: 
                                Utils.infer(x.env,x.env[i].name,FloatType())
                                x.paramTypeOrder[i] = FloatType()
                            if type_of_args is StringType: 
                                Utils.infer(x.env,x.env[i].name,StringType())
                                x.paramTypeOrder[i] = StringType()
                            if type_of_args is ArrayType: 
                                type_of_param = Utils.infer(o,args[i].name,type_of_param)
                                x.paramTypeOrder[i] = type_of_param                                        
                            type_of_param = x.paramTypeOrder[i]
                                                            
                        if type_of_args != type_of_param:
                            raise TypeMismatchInExpression (args[i])
                    return VoidType()
        for x in funcDeclOrder:
            if x.name == ast.name: 
                if len(args) != len(x.paramTypeOrder):
                    if len(args) > len(x.paramTypeOrder):
                        if len(x.paramTypeOrder) != 0: 
                            raise TypeMismatchInExpression (args[len(x.paramTypeOrder) - 1])
                        else: raise TypeMismatchInStatement(ast)
                    else: 
                        if len(args) != 0: 
                            raise TypeMismatchInStatement(ast)
                for i in range(0,len(args)):
                    type_of_args = type(self.visit(args[i],o))
                    type_of_param = type(x.paramTypeOrder[i].typ)

                    if type_of_args is AutoType and type_of_param is AutoType:
                        # raise TypeCannotBeInferred (ast)
                        return
                    if type_of_args is AutoType:           
                        if type_of_param is IntegerType: 
                            type_of_args = Utils.infer(o,args[i].name,IntegerType())
                        if type_of_param is BooleanType: 
                            type_of_args = Utils.infer(o,args[i].name,BooleanType())
                        if type_of_param is FloatType: 
                            type_of_args = Utils.infer(o,args[i].name,FloatType())
                        if type_of_param is StringType: 
                            type_of_args = Utils.infer(o,args[i].name,StringType())
                        if type_of_param is ArrayType: 
                            type_of_args = Utils.infer(o,args[i].name,type_of_param)
                        type_of_args = type(type_of_args)
                    if type_of_param is AutoType: 
                        if type_of_args is IntegerType: 
                            x.paramTypeOrder[i].typ = Utils.infer(x.env,x.env[i].name,IntegerType())
                        if type_of_args is BooleanType: 
                            x.paramTypeOrder[i].typ = Utils.infer(x.env,x.env[i].name,BooleanType())
                        if type_of_args is FloatType: 
                            x.paramTypeOrder[i].typ = Utils.infer(x.env,x.env[i].name,FloatType())
                        if type_of_args is StringType: 
                            x.paramTypeOrder[i].typ =Utils.infer(x.env,x.env[i].name,StringType())
                        if type_of_args is ArrayType: 
                            x.paramTypeOrder[i].typ = Utils.infer(x.env,x.env[i].name,type_of_param)
                        type_of_param = type(x.paramTypeOrder[i].typ)                                  
                     
                    if type_of_args != type_of_param:
                        raise TypeMismatchInExpression (args[i])
                return VoidType()
        raise Undeclared(Function(),ast.name)