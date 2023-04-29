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
    def __init__(self,name,typ,inherit = False,out = False):
        self.name = name
        self.typ = typ
        self.inherit = inherit
        self.out = out

class Utils(): 
    def infer(SymbolTable,name,typ):
        global funcDeclOrder
        global notDeclaredFunction
        if notDeclaredFunction == True: 
            for symbol in funcDeclOrder: 
                if symbol.name == name: 
                    symbol.return_type = typ
                    notDeclaredFunction = False
                    return typ
        for symbol_list in SymbolTable: 
            for symbol in symbol_list: 
                if symbol.name == name: 
                    if type(symbol) is FuncSymbol:
                        symbol.return_type = typ                       
                        return typ
                    else: 
                        symbol.typ = typ
                        return typ
isMainExist = False
funcDeclOrder = []
fatherExist = False
notDeclaredFunction = False

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
        o = [FuncSymbol(ast.name,return_type,paramTypeOrder,ast.inherit,paramTypeOrder,body)] + o
        return o
    def visitParamDecl(self, ast, o): # we need prototype at this pharse only 
        o = o + [ParamSymbol(ast.name,self.visit(ast.typ,o),ast.inherit,ast.out)] 
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
    def __del__(self):
        global funcDeclOrder
        global isMainExist
        global fatherExist
        global notDeclaredFunction
        isMainExist = False
        funcDeclOrder = []
        fatherExist = False
        notDeclaredFunction = False
    def visitProgram(self,ast,o:object): 
        global funcDeclOrder
        global isMainExist
        global fatherExist
        global notDeclaredFunction
        o = []
        round1 = GetEnv(ast,StaticChecker.preDefinedFunction)
        funcDeclOrder = round1.visit(ast, o)
        # o = [[]] + [o]
        
        o = [StaticChecker.preDefinedFunction]
        for decl in ast.decls:
            o = self.visit(decl, o)
        for decl in o[-1]: 
            if decl.name == "main":
                if type(decl.return_type) is VoidType and len(decl.paramTypeOrder) == 0: 
                    return
        isMainExist = False
        if isMainExist == False: 
            raise NoEntryPoint()
        o = [StaticChecker.preDefinedFunction]
    def visitFuncDecl(self,ast,o:object):
        global funcDeclOrder
        global fatherExist
        # global callOrder
        for x in o[0]:
            if ast.name == x.name:
                raise Redeclared(Function(),ast.name)
        return_type = self.visit(ast.return_type,o)
        env = [[]] + o
        paramTypeOrder = []
        body = []
        for decl in ast.params: # to check if redeclared happen in parameter
            env = self.visit(decl,env)
        for func in funcDeclOrder: # No error ? We inherit the order from round 1 ! 
            if func.name == ast.name: 
                env = [func.paramTypeOrder] + o
                body = func.body
                return_type = func.return_type
                break
        for param in env[0]: 
            paramTypeOrder += [param.typ]
        temp = func.body
        #Round 1: Check if parent exist, then check inherit parameter. 
        if ast.inherit is not None:
            for father in funcDeclOrder: 
                if father.name == ast.inherit: 
                    fatherExist = True
                    self.checkVaildParent(father.paramTypeOrder)
                    if len(body) != 0: 
                        if type(body[0]) is CallStmt: 
                            if body[0].name == "preventDefault": 
                                break
                        else: 
                            raise InvalidStatementInFunction(ast.name)
                    for param_father in father.paramTypeOrder: 
                                for x in env[0]: 
                                    if param_father.name == x.name:
                                        if param_father.inherit is not None: 
                                            raise Invalid(Parameter(),param_father.name)
                                        # else: raise Redeclared(Parameter(),param_father.name)
                                if param_father.inherit == True:
                                    env[0] = [param_father] + env[0]
                    for child in funcDeclOrder:
                        if child.name == ast.name:
                            if len(body) == 0:
                                child.body += [CallStmt("super",[])]
                            body = temp
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
                                    # vaildFirstStmt = False
                                if len(father.paramTypeOrder) != 0 and len(superCalledFromChild) != 0: 
                                    for i in range(len(superCalledFromChild)):
                                        if i == len(father.paramTypeOrder): 
                                            break
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
                                        if superfromChild_arg_type != type(father.paramTypeOrder[i].typ):
                                            if superfromChild_arg_type is IntegerType and type(father.paramTypeOrder[i].typ) is FloatType:
                                                continue
                                            else:
                                                raise TypeMismatchInExpression(child.body[0].args[i])
                                if len(superCalledFromChild) != len(father.paramTypeOrder):
                                    if len(superCalledFromChild) > len(father.paramTypeOrder):
                                            if len(father.paramTypeOrder) != 0: 
                                                raise TypeMismatchInExpression (child.body[0].args[len(father.paramTypeOrder)])
                                            else: raise TypeMismatchInExpression("")
                                    else: 
                                        if len(superCalledFromChild) != 0: 
                                            raise TypeMismatchInExpression("")
                            if child.body[0].name == "preventDefault": 
                                break
                    break
            if fatherExist == False: 
                raise Undeclared(Function(),ast.inherit)
        cntReturn = 0
        cntLoop = 0
        callList = ['FuncDecl']
        dive = [cntReturn,ast.name,env,callList,cntLoop]
        dive = self.visit(ast.body,dive)
        # raise Undeclared(Function(),ast.name)
        for x in funcDeclOrder: 
            if x.name == ast.name: 
                if type(ast.return_type) is AutoType: 
                    return_type = x.return_type
                    break
        o[0] = [FuncSymbol(ast.name,return_type,paramTypeOrder,ast.inherit,env,body)] + o[0]
        # callOrder = []
        fatherExist = False
        return o
    def getParamType(self, ast, o): # we need prototype at this pharse only ! 
        o = [self.visit(ast.typ,o)] + o
        return o

    def checkVaildParent(self,o):
        size = len(o)
        for i in range(1,size): 
            for j in range(0,i):
                if o[i].name == o[j].name: 
                    raise Redeclared(Parameter(),o[i].name)
    def visitParamDecl(self, ast, o):
        for x in o[0]: 
            if ast.name == x.name: 
                raise Redeclared(Parameter(),ast.name)
        o[0] = [ParamSymbol(ast.name,ast.typ,ast.inherit,ast.out)] + o[0]
        return o
    def inferVarDecl(self,ast,init,o):
        if type(init) is IntegerType: 
            o[0] = [Symbol(ast.name,IntegerType())] + o[0]
        if type(init) is StringType: 
            o[0] = [Symbol(ast.name,StringType())] + o[0]
        if type(init) is FloatType: 
            o[0] = [Symbol(ast.name,FloatType())] + o[0]
        if type(init) is BooleanType: 
            o[0] = [Symbol(ast.name,BooleanType())] + o[0]
        if type(init) is ArrayType:
            o[0] = [Symbol(ast.name,ArrayType(init.dimensions,init.typ))] + o[0]            
        return o
    def inferFuncDecl(self,ast,typ_,o): 
        global funcDeclOrder
        global notDeclaredFunction
        gblScope = len(o) - 1
        ret = None 
        for x in o[gblScope]: 
            if x.name == ast.name:
                if type(typ_) is IntegerType: 
                    ret = Utils.infer(o,ast.name,IntegerType())
                elif type(typ_) is StringType: 
                    ret = Utils.infer(o,ast.name,StringType())
                elif type(typ_) is FloatType: 
                    ret = Utils.infer(o,ast.name,FloatType())
                elif type(typ_) is BooleanType: 
                    ret = Utils.infer(o,ast.name,BooleanType())
                elif type(typ_) is ArrayType: pass
                return ret
        for x in funcDeclOrder: 
            if x.name == ast.name:
                notDeclaredFunction = True
                if type(typ_) is IntegerType: 
                    ret = Utils.infer(funcDeclOrder,ast.name,IntegerType())
                elif type(typ_) is StringType: 
                    ret = Utils.infer(funcDeclOrder,ast.name,StringType())
                elif type(typ_) is FloatType: 
                    ret = Utils.infer(funcDeclOrder,ast.name,FloatType())
                elif type(typ_) is BooleanType: 
                    ret = Utils.infer(funcDeclOrder,ast.name,BooleanType())
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
                        ret = Utils.infer(o,ast.name,IntegerType())
                    elif type(typ_) is StringType: 
                        ret = Utils.infer(o,ast.name, StringType())
                    elif type(typ_) is FloatType: 
                        ret = Utils.infer(o,ast.name, FloatType())
                    elif type(typ_) is BooleanType: 
                        ret = Utils.infer(o,ast.name,BooleanType())
                    elif type(typ_) is ArrayType: pass
                    return typ_
    def visitVarDecl(self, ast, o): 
        # Co suy dien kieu giua 2 phia nua nha ~ 
        # Case 1: lhs co kieu khac auto -> suy dien ben rhs 
        # Case 2 : rhs co kieu -> suy dien ben lhs 
        for x in o[0]:
            if ast.name == x.name:
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
                if type(init) is ArrayType and type(init.typ) is not AutoType: 
                    return self.inferVarDecl(ast,init,o)
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
                o[0] = [Symbol(ast.name,ArrayType(init.dimensions,init.typ))] + o[0]
                return o
            if type(init) is AutoType: #Function in Global or Function/Var inside function.     
                if type(typ) is AutoType: 
                    return o
                else: 
                    if type(ast.init) is FuncCall: 
                        init = self.inferFuncDecl(ast.init,typ,o)
                    else: 
                        if type(ast.init) is UnExpr:
                            init = self.inferID(ast.init.val,typ,o)
                        else: 
                            init = self.inferID(ast.name,typ,o)
            if type(typ) is FloatType and type(init) is IntegerType: 
                o[0] = [Symbol(ast.name,typ)] + o[0]
                return o
            if type(typ) != type(init):
                raise TypeMismatchInVarDecl(ast)
        o[0] = [Symbol(ast.name,typ)] + o[0]
        return o
    def visitId(self,ast,o:object):
        for symbol_list in o: 
            for symbol in symbol_list:
                if symbol.name == ast.name:
                    if type(symbol) is FuncSymbol: 
                        return symbol.return_type
                    return symbol.typ
        raise Undeclared(Identifier(),ast.name)
    
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
        rhs = self.visit(ast.right,o)
        lhs = self.visit(ast.left,o)
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
        if type(one) is AutoType: 
            return AutoType()
        if type(one) != IntegerType and type(one) != FloatType: 
            raise TypeMismatchInExpression(ast)
        return one
    def visitArrayCell(self, ast, o):
        for symbol_list in o: 
            for symbol in symbol_list: 
                if symbol.name == ast.name:
                    if type(symbol.typ) is not ArrayType:
                        raise Undeclared(Variable(),type(symbol.typ))
                    # Tim dimension size cua array (Co the la Function or variable)
                    cell = []
                    for expr in ast.cell: 
                        typ = self.visit(expr,o)
                        if type(typ) is not IntegerType: 
                            raise TypeMismatchInExpression(expr) # ele trong cell ko integer -> Mismatch
                        cell = cell + [expr]
                    # So sanh 2 dimension vs nhau, neu khac size -> TypeMismatch
                    expect_len = len(symbol.typ.dimensions)
                    got_len = len(cell)
                    if expect_len !=  got_len: 
                        if expect_len < got_len: 
                            raise TypeMismatchInExpression(ast)
                        else:
                            return ArrayType(symbol.typ.dimensions[(expect_len):],symbol.typ.typ)
                    return symbol.typ.typ
        raise Undeclared(Variable(),ast.name)
    def visitIntegerLit(self, ast, o):
        return IntegerType()
    def visitFloatLit(self, ast, o):
        return FloatType()
    def visitStringLit(self, ast, o):
        return StringType()
    def visitBooleanLit(self, ast, o):
        return BooleanType()
    def visitArrayLit(self, ast, o):
        # Dau tien lay type cua cac phan tu trong ds aray. 
        elm_type = [self.visit(exp,o) for exp in ast.explist]
        # Neu co bat ki phan tu nao la AutoType -> Di suy dien. 
        for x in elm_type: 
            if type(x) is AutoType: 
                pass
        # Lay phan tu dau tien de xet. 
        tmp_type = elm_type[0]
        sameType = True
        # Kiem tra xem cac phan tu co cung kieu khong. 
        for x in elm_type: 
            if type(x) is not type(tmp_type): 
                sameType = False
                break
        # Neu co -> ta di vao xet sau hon. 
        if sameType == True: 
            for x in elm_type: 
                # Truong hop dac biet: ArrayType
                if type(x) is ArrayType: 
                    # Goi De quy de lay Dimension. 
                    getInsideDim = self.visitArrayLit(ast.explist[0],o).dimensions
                    # Goi de quy de lay type o sau ben trong. 
                    getInsideType = self.visitArrayLit(ast.explist[0],o).typ

                    for x in ast.explist[1:]: 
                        # Goi de quy de lay dimension cua x thu 2
                        if getInsideDim != self.visitArrayLit(x,o).dimensions: 
                            raise IllegalArrayLiteral(ast)
                        # Lay kieu cua x thu 2, 3, ,4 
                        if getInsideType != self.visitArrayLit(x,o).typ: 
                            raise IllegalArrayLiteral(ast)
                    # Neu Ok ? Ta  tra ve dimen cua cai list trong cung roi de quy ra. 
                    return ArrayType([len(ast.explist)] + getInsideDim,getInsideType)
                # Khong co long (basecase) -> Tra ve nguyen mau thoi. 
                return ArrayType([len(ast.explist)],tmp_type)
        raise IllegalArrayLiteral(ast)
    def visitFuncCall(self, ast, o): 
 #args la id: No o dau ? Global or Function Scope.
        #args ko co type. Chi co Literal -> Type hoac Id -> Type.
        args = ast.args
        for symbol_list in o: 
            for x in symbol_list: # o[1] la global . Called in global. 
                if ast.name == x.name: 
                    if type(x) is not FuncSymbol: 
                        raise TypeMismatchInExpression(ast)
                    else:
                        if len(args) != len(x.paramTypeOrder):
                            raise TypeMismatchInExpression(ast)
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
                                    Utils.infer(x.env,x.env[0][i].name,IntegerType())
                                    x.paramTypeOrder[i] = IntegerType()
                                if type_of_args is BooleanType: 
                                    Utils.infer(x.env,x.env[0][i].name,BooleanType())
                                    x.paramTypeOrder[i] = BooleanType()
                                if type_of_args is FloatType: 
                                    Utils.infer(x.env,x.env[0][i].name,FloatType())
                                    x.paramTypeOrder[i] = FloatType()
                                if type_of_args is StringType: 
                                    Utils.infer(x.env,x.env[0][i].name,StringType())
                                    x.paramTypeOrder[i] = StringType()
                                if type_of_args is ArrayType: 
                                    type_of_param = Utils.infer(o,args[i].name,type_of_param)
                                    x.paramTypeOrder[i] = type_of_param                                        
                                type_of_param = x.paramTypeOrder[i]
                                                                
                            if type_of_args != type_of_param:
                                if type_of_args is IntegerType and type_of_param is FloatType:
                                    continue
                                raise TypeMismatchInExpression (ast)
                    if type(x.return_type) is VoidType: 
                        raise TypeMismatchInExpression(ast)
                    return x.return_type
        global notDeclaredFunction
        for x in funcDeclOrder:
            if x.name == ast.name:
                if len(args) != len(x.paramTypeOrder):
                        raise TypeMismatchInExpression(ast)
                for i in range(0,len(args)):
                    if i == len(x.paramTypeOrder): 
                        break
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
                            x.paramTypeOrder[i].typ = Utils.infer([x.env],x.env[i].name,IntegerType())
                        if type_of_args is BooleanType: 
                            x.paramTypeOrder[i].typ = Utils.infer([x.env],x.env[i].name,BooleanType())
                        if type_of_args is FloatType: 
                            x.paramTypeOrder[i].typ = Utils.infer([x.env],x.env[i].name,FloatType())
                        if type_of_args is StringType: 
                            x.paramTypeOrder[i].typ = Utils.infer([x.env],x.env[i].name,StringType())
                        if type_of_args is ArrayType: 
                            x.paramTypeOrder[i].typ = Utils.infer([x.env],x.env[i].name,type_of_param)
                        type_of_param = type(x.paramTypeOrder[i].typ)                                  
                     
                    if type_of_args != type_of_param:
                        if type_of_args is IntegerType and type_of_param is FloatType:
                            continue
                        raise TypeMismatchInExpression (ast)
                notDeclaredFunction = True
                if type(x.return_type) is VoidType: 
                    raise TypeMismatchInExpression(ast)
                return x.return_type
        raise Undeclared(Function(),ast.name)
# self, lhs: LHS, rhs: Expr
    def visitSingleStmt(self,ast,o): 
        global fatherExist
        # o = dive = [cntReturn,ast.name,env,callList,cntLoop]
        if type(ast) is VarDecl:
            o[2] = self.visit(ast,o[2])
        elif type(ast) is ReturnStmt:
            self.visit(ast,o)
            return o
        elif type(ast) is ContinueStmt or type(ast) is BreakStmt: 
            self.visit(ast,o)
        elif type(ast) is AssignStmt or type(ast) is CallStmt:
            if type(ast) is CallStmt: 
                if ast.name is "super" or ast.name is "preventDefault":
                    raise InvalidStatementInFunction(ast) 
            self.visit(ast,o[2])
        else:    
            self.visit(ast,o)
        return o
    def visitBlockStmt(self, ast, o):
        global fatherExist
        # o = dive = [cntReturn,ast.name,env,callList,cntLoop]
        for i in range(0,len(ast.body)):

            if type(ast.body[i]) is VarDecl:
                o[2] = self.visit(ast.body[i],o[2])
            elif type(ast.body[i]) is ReturnStmt:
                self.visit(ast.body[i],o)
            elif type(ast.body[i]) is ContinueStmt or type(ast.body[i]) is BreakStmt: 
                self.visit(ast.body[i],o)
            
            elif type(ast.body[i]) is BlockStmt: 
                o[2] = [[]] + o[2]
                self.visit(ast.body[i],o)
            elif type(ast.body[i]) is AssignStmt or type(ast.body[i]) is CallStmt:
                if type(ast.body[i]) is CallStmt: 
                    if ast.body[i].name is "super" or ast.body[i].name is "preventDefault":
                        if i == 0: continue
                        else: raise InvalidStatementInFunction(ast.body[i]) 
                self.visit(ast.body[i],o[2])
            elif type(ast.body[i]) is ForStmt or type(ast.body[i]) is WhileStmt or type(ast.body[i]) is DoWhileStmt:
                self.visit(ast.body[i],o)
            else:
                self.visit(ast.body[i],o)
                        

        if len(o[2]) > 2:
            o[2].pop(0)
        return o
    def visitAssignStmt(self, ast, o):
        #
        rhs = self.visit(ast.rhs,o)
        lhs = self.visit(ast.lhs,o)
        if type(lhs) is VoidType or type(rhs) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(lhs) is ArrayType or type(rhs) is ArrayType: 
            # raise Undeclared(Function(),type(rhs))
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
            if type(ast.rhs) is UnExpr:  
                if type(lhs) is AutoType:
                    return # raise TypeCannotBeInferred(ast)
                if type(lhs) is BooleanType: 
                    rhs = Utils.infer(o,ast.rhs.val.name,BooleanType())
                if type(lhs) is IntegerType: 
                    rhs = Utils.infer(o,ast.rhs.val.name,IntegerType())
                if type(lhs) is FloatType: 
                    rhs = Utils.infer(o,ast.rhs.val.name,FloatType())
                if type(lhs) is StringType: 
                    rhs = Utils.infer(o,ast.rhs.val.name,StringType())
            else:
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
    # o = dive = [cntReturn,ast.name,env,callList,cntLoop]   
        type_cond = self.visit(ast.cond,o[2])
        
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        o[3] = o[3] + ["IfStmt"] 

        if type(ast.tstmt) is BlockStmt:
            o[2] = [[]] + o[2]
            self.visit(ast.tstmt,o)
            o[0] = 0
        else: self.visitSingleStmt(ast.tstmt,o)
        
        if ast.fstmt is not None:
            if type(ast.fstmt) is BlockStmt:
                o[2] = [[]] + o[2]
                self.visit(ast.fstmt,o)
                o[0] = 0
            else: self.visitSingleStmt(ast.fstmt,o)
        
        o[3].pop()
#        return o 
    def visitForStmt(self, ast, o):
        type_init = self.visit(ast.init,o[2])
        if type(type_init) is not IntegerType: 
            raise TypeMismatchInStatement(ast) 
              
        type_cond = self.visit(ast.cond,o[2])
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        
        type_update = self.visit(ast.upd,o[2])
        if type(type_update) is not IntegerType: 
            raise TypeMismatchInStatement(ast)
        o[3] += ["ForStmt"]
        
        if type(ast.stmt) is BlockStmt: 
            o[2] = [[]] + o[2]
            self.visit(ast.stmt,o)
            o[0] = 0
        else: self.visitSingleStmt(ast.stmt,o)

        o[3].pop()
        
        # raise Undeclared(Function(),callOrder)
        # return o
    def visitWhileStmt(self, ast, o):
        type_cond = self.visit(ast.cond,o[2])
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        o[3] += ["WhileStmt"]
        o[0] = 0
        if type(ast.stmt) is BlockStmt: 
            o[2] = [[]] + o[2]
            self.visit(ast.stmt,o)
            o[0] = 0
        else: self.visitSingleStmt(ast.stmt,o)
        
        o[3].pop()

    def visitDoWhileStmt(self, ast, o):

        type_cond = self.visit(ast.cond,o[2])
        if type(type_cond) is not BooleanType: 
            raise TypeMismatchInStatement(ast)
        # env = [[]] + o
        o[3] += ["DoWhileStmt"]
        o[2] = [[]] + o[2]
        self.visit(ast.stmt,o)
        o[3].pop()
        o[0] = 0
    def visitBreakStmt(self, ast, o):
        o[4] = o[4] + 1
        # if o[4] > 1: return
        # size = len(o[3])
        for x in reversed(o[3]): 
            if x == "ForStmt" or x == "WhileStmt" or x == "DoWhileStmt": 
                return
        raise MustInLoop(ast)
    def visitContinueStmt(self, ast, o): 
        o[4] = o[4] + 1
        # if o[4] > 1: return
        for x in reversed(o[3]): 
            if x == "ForStmt" or x == "WhileStmt" or x == "DoWhileStmt": 
                return
        raise MustInLoop(ast)
    def visitReturnStmt(self, ast, o):
        # 0: so luong ham returnstmt trong Block
        # 1: TenHam / -1
        # 2: GlobalScope
        o[0] = o[0] + 1
        # Chua Suy dien~ Kieu.
        typ = None
        if o[0] == 1: 
            for x in funcDeclOrder:
                if x.name == o[1]: 
                    if ast.expr is None: 
                        typ = VoidType()
                    else: typ = self.visit(ast.expr,o[2])
                    if type(x.return_type) is AutoType: 
                        x.return_type = typ
                    if type(x.return_type) is FloatType and type(typ) is IntegerType:
                        return x.return_type
                    if type(x.return_type) != type(typ): 
                        raise TypeMismatchInStatement(ast)
                    return typ
    # o[0] > 1
        for x in funcDeclOrder: 
            if x.name == o[1]: 
                if ast.expr is None:
                    typ = VoidType()
                else: typ = self.visit(ast.expr,o[2])
                if type(x.return_type) != type(typ): 
                    raise TypeMismatchInStatement(ast)      
        return typ
    def visitCallStmt(self, ast, o):
 #args la id: No o dau ? Global or Function Scope.
        #args ko co type. Chi co Literal -> Type hoac Id -> Type.
        global funcDeclOrder
        if ast.name == "super" or ast.name == "preventDefault": 
            return VoidType()
        args = ast.args
        # raise UndeclaredIdentifier(str(type(o[0])))
        for symbol_list in o: 
            for x in symbol_list: # o[1] la global . Called in global. 
                if ast.name == x.name: 
                    if type(x) is not FuncSymbol: 
                        raise TypeMismatchInStatement(ast)
                    else:
                        if len(args) != len(x.paramTypeOrder):
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
                                    Utils.infer(x.env, x.env[0][i].name,IntegerType())
                                    x.paramTypeOrder[i] = IntegerType()
                                if type_of_args is BooleanType: 
                                    Utils.infer(x.env,x.env[0][i].name,BooleanType())
                                    x.paramTypeOrder[i] = BooleanType()
                                if type_of_args is FloatType: 
                                    Utils.infer(x.env,x.env[0][i].name,FloatType())
                                    x.paramTypeOrder[i] = FloatType()
                                if type_of_args is StringType: 
                                    Utils.infer(x.env,x.env[0][i].name,StringType())
                                    x.paramTypeOrder[i] = StringType()
                                if type_of_args is ArrayType: 
                                    type_of_param = Utils.infer(o,args[i].name,type_of_param)
                                    x.paramTypeOrder[i] = type_of_param                                        
                                type_of_param = x.paramTypeOrder[i]
                                                                
                            if type_of_args != type_of_param:
                                if type_of_args is IntegerType and type_of_param is FloatType:
                                    continue
                                raise TypeMismatchInStatement (ast)
                        # if type(x.return_type) is AutoType: 
                        #     x.return_type = VoidType()
                        return VoidType()
        for x in funcDeclOrder:
            if x.name == ast.name: 
                if len(args) != len(x.paramTypeOrder):
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
                            x.paramTypeOrder[i].typ = Utils.infer([x.env],x.env[i].name,IntegerType())
                        if type_of_args is BooleanType: 
                            x.paramTypeOrder[i].typ = Utils.infer([x.env],x.env[i].name,BooleanType())
                        if type_of_args is FloatType: 
                            x.paramTypeOrder[i].typ = Utils.infer([x.env],x.env[i].name,FloatType())
                        if type_of_args is StringType: 
                            x.paramTypeOrder[i].typ =Utils.infer([x.env],x.env[i].name,StringType())
                        if type_of_args is ArrayType: 
                            x.paramTypeOrder[i].typ = Utils.infer([x.env],x.env[i].name,type_of_param)
                        type_of_param = type(x.paramTypeOrder[i].typ)                                  
                     
                    if type_of_args != type_of_param:
                        if type_of_args is IntegerType and type_of_param is FloatType:
                            continue
                        raise TypeMismatchInStatement (ast)
                # if type(x.return_type) is AutoType: 
                #     x.return_type = VoidType()
                return VoidType()
        raise Undeclared(Function(),ast.name)