from Visitor import Visitor
from StaticError import *
from AST import *
from abc import ABC
class Symbol(): 
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def __str__(self):
        return "Symbol({}, {})".format(str(self.name), str(self.type))
class Func_Symbol(Symbol): 
    def __init__(self,name,ret_type,param_typ_order,inherit,env,body): 
        self.name = name
        self.ret_type = ret_type
        self.param_typ_order = param_typ_order 
        self.inherit = inherit 
        self.env = env 
        self.body = body
class Param_Symbol(Symbol): 
    def __init__(self,name,type,inherit = False, out = False):
        self.name = name
        self.type = type
        self.inherit = inherit
        self.out = out

class Utils(): 
    def infer(SymbolTable,name,type):
        global OrderOfFuncDecl
        global fancyFunction
        if fancyFunction == True: 
            for symbol in OrderOfFuncDecl: 
                if symbol.name == name: 
                    symbol.ret_type = type
                    fancyFunction = False
                    return type
        for symlist in SymbolTable: 
            for symbol in symlist: 
                if symbol.name == name: 
                    if type(symbol) is Func_Symbol:
                        symbol.ret_type = type                       
                        return type
                    else: 
                        symbol.type = type
                        return type
OrderOfFuncDecl = []
checkMain = False
checkFather = False
fancyFunction = False

class GetEnv(Visitor):
    def __init__(self, ast, specialFunction):
        self.ast = ast
        self.specialFunction = specialFunction
    def check(self):
        return self.visitProgram(self.ast,self.specialFunction)
    def visitProgram(self,ast,o:object): 
        for decl in ast.decls:
            if type(decl) is FuncDecl: 
                o = self.visit(decl, o)
        return o 
    def visitFuncDecl(self,ast,o):
        if ast.name in o: 
            return o
        ret_type = ast.return_type
        global checkMain
        if ast.name == 'main': 
            if type(ret_type) == VoidType and len(ast.params) == 0: 
                checkMain = True

        param_typ_order = []
        for decl in ast.params:  
            param_typ_order = self.visit(decl,param_typ_order)

        body = self.visit(ast.body,o)

        o = [Func_Symbol(ast.name,ret_type,param_typ_order,ast.inherit,[],body)] + o
        return o
    def visitParamDecl(self, ast, o):

        o = o + [Param_Symbol(ast.name,self.visit(ast.type,o),ast.inherit,ast.out)] 
        return o
    
    def visitIntegerType(self, ast, o):
        return IntegerType()
    def visitFloatType(self, ast, o):
        return FloatType()
    def visitBooleanType(self, ast, o):
        return BooleanType()
    def visitStringType(self, ast, o): 
        return StringType()
    def visitArrayType(self, ast, o):
        type = self.visit(ast.type,o)
        return ArrayType(ast.dimensions,type)
    
    def visitAutoType(self, ast, o): 
        return AutoType()
    
    def visitVoidType(self, ast, o):
        return VoidType()
    
    def visitBlockStmt(self, ast, param):
        return ast.body
    
class StaticChecker(Visitor):
    specialFunction = [Func_Symbol("readInteger",IntegerType(),[],None,[],[]) 
                      , Func_Symbol("printInteger",IntegerType(),[IntegerType()],None,[],[]) 
                      , Func_Symbol("readFloat",FloatType(),[],None,[],[]) 
                      , Func_Symbol("writeFloat",FloatType(),[FloatType()],None,[],[]) 
                      , Func_Symbol("readBoolean",BooleanType(),[],None,[],[]) 
                      , Func_Symbol("printBoolean",BooleanType(),[BooleanType()],None,[],[])
                      , Func_Symbol("readString",StringType(),[],None,[],[])
                      , Func_Symbol("printString",StringType(),[StringType()],None,[],[])
                      ,Func_Symbol("super",StringType(),[StringType()],None,[],[])
                      , Func_Symbol("preventDefault",None,[],None,[],[])
                      ]
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast,StaticChecker.specialFunction)
    
    def __del__(self):
        global OrderOfFuncDecl
        global checkMain
        global checkFather
        global fancyFunction
        checkMain = False
        OrderOfFuncDecl = []
        checkFather = False
        fancyFunction = False

    def visitProgram(self,ast,o:object): 
        global OrderOfFuncDecl
        global checkMain
        global checkFather
        global fancyFunction
        o = []

        r1 = GetEnv(ast,StaticChecker.specialFunction)
        OrderOfFuncDecl = r1.visit(ast, o)
        
        o = [StaticChecker.specialFunction]

        for decl in ast.decls:
            o = self.visit(decl, o)

        for decl in o[-1]: 
            if decl.name == "main":
                if type(decl.ret_type) is VoidType and len(decl.param_typ_order) == 0: 
                    return
                
        checkMain = False
        if checkMain == False: 
            raise NoEntryPoint()
        o = [StaticChecker.specialFunction]
        
    def visitFuncDecl(self,ast,o:object):
        global OrderOfFuncDecl
        global checkFather
        
        for i in o[0]:
            if ast.name == i.name:
                raise Redeclared(Function(),ast.name)
            
        ret_type = self.visit(ast.return_type,o)
        env = [[]] + o
        param_typ_order = []
        body = []
        for decl in ast.params:
            env = self.visit(decl,env)

        for func in OrderOfFuncDecl: 
            if func.name == ast.name: 
                env = [func.param_typ_order] + o
                body = func.body
                ret_type = func.ret_type
                break

        for param in env[0]: 
            param_typ_order += [param.type]
        t = func.body

        if ast.inherit is not None:
            for father in OrderOfFuncDecl: 
                if father.name == ast.inherit: 
                    checkFather = True

                    if len(body) != 0: 

                        if type(body[0]) is CallStmt: 
                            if body[0].name == "preventDefault": 
                                break
                            if body[0].name != "super": 

                                raise InvalidStatementInFunction(body[0].name)
                        else: 
                            raise InvalidStatementInFunction(ast.name)
                        
                    self.checkParent(father.param_typ_order)

                    for param_father in father.param_typ_order: 
                                for i in env[0]: 
                                    if param_father.name == i.name:
                                        if param_father.inherit is not None: 
                                            raise Invalid(Parameter(),param_father.name)
                                if param_father.inherit == True:
                                    env[0] = [param_father] + env[0]

                    for child in OrderOfFuncDecl:
                        if child.name == ast.name:
                            if len(body) == 0:
                                child.body += [CallStmt("super",[])]
                            body = t
                            if type(child.body[0]) is not CallStmt: 
                                raise InvalidStatementInFunction(child.body[0])
                            
                            if child.body[0].name != "super" and child.body[0].name != "preventDefault":
                                raise InvalidStatementInFunction(child.body[0])
                            if child.body[0].name == "super":
                                SCallFromChild = []
                                for arg in child.body[0].args: 
                                    SCallFromChild += [self.visit(arg,env)]

                                if len(father.param_typ_order) != 0 and len(SCallFromChild) != 0: 
                                    for i in range(len(SCallFromChild)):
                                        if i == len(father.param_typ_order): 
                                            break
                                        superfromChild_arg_type = type(SCallFromChild[i])

                                        if type(father.param_typ_order[i].type) is AutoType: 

                                            if superfromChild_arg_type is BooleanType: 
                                                father.param_typ_order[i].type = BooleanType()

                                            if superfromChild_arg_type is IntegerType: 
                                                father.param_typ_order[i].type = IntegerType()

                                            if superfromChild_arg_type is FloatType: 
                                                father.param_typ_order[i].type = FloatType()

                                            if superfromChild_arg_type is StringType: 
                                                father.param_typ_order[i].type = StringType()
                                        
                                        if superfromChild_arg_type is AutoType: 

                                            if type(father.param_typ_order[i].type) is BooleanType:
                                                superfromChild_arg_type = Utils.infer(env,child.body[0].args[i].name,BooleanType()) 

                                            if type(father.param_typ_order[i].type) is IntegerType: 
                                                superfromChild_arg_type = Utils.infer(env,child.body[0].args[i].name,IntegerType())

                                            if type(father.param_typ_order[i].type) is FloatType: 
                                                superfromChild_arg_type = Utils.infer(env,child.body[0].args[i].name,FloatType())

                                            if type(father.param_typ_order[i].type) is StringType: 
                                                superfromChild_arg_type = Utils.infer(env,child.body[0].args[i].name,StringType())

                                        if superfromChild_arg_type != type(father.param_typ_order[i].type):
                                            if superfromChild_arg_type is IntegerType and type(father.param_typ_order[i].type) is FloatType:
                                                continue
                                            else:
                                                raise TypeMismatchInExpression(child.body[0].args[i])
                                            
                                if len(SCallFromChild) != len(father.param_typ_order):

                                    if len(SCallFromChild) > len(father.param_typ_order):
                                            
                                            if len(father.param_typ_order) != 0: 

                                                raise TypeMismatchInExpression (child.body[0].args[len(father.param_typ_order)])
                                            
                                            else: raise TypeMismatchInExpression("")
                                    else: 

                                        if len(SCallFromChild) != 0: 
                                            raise TypeMismatchInExpression("")
                                        
                            if child.body[0].name == "preventDefault": 
                                break
                    break
            if checkFather == False: 
                raise Undeclared(Function(),ast.inherit)
            
        call_list = ['FuncDecl']

        cnt_ret = 0
        cnt_loop = 0

        dive = [cnt_ret,ast.name,env,call_list,cnt_loop]
        dive = self.visit(ast.body,dive)

        for i in OrderOfFuncDecl: 
            if i.name == ast.name: 
                if type(ast.return_type) is AutoType: 
                    ret_type = i.ret_type
                    break

        o[0] = [Func_Symbol(ast.name,ret_type,param_typ_order,ast.inherit,env,body)] + o[0]
        checkFather = False
        return o
    
    def getParamType(self, ast, o): 
        o = [self.visit(ast.type,o)] + o
        return o

    def checkParent(self,o):
        size = len(o)
        for i in range(1,size): 
            for j in range(0,i):
                if o[i].name == o[j].name: 
                    raise Redeclared(Parameter(),o[i].name)
                
    def visitParamDecl(self, ast, o):
        for i in o[0]: 
            if ast.name == i.name: 
                raise Redeclared(Parameter(),ast.name)
        o[0] = [Param_Symbol(ast.name,ast.type,ast.inherit,ast.out)] + o[0]
        return o
    
    def inferVarDecl(self,ast,first,o):
        if type(first) is IntegerType: 
            o[0] = [Symbol(ast.name,IntegerType())] + o[0]
        if type(first) is FloatType: 
            o[0] = [Symbol(ast.name,FloatType())] + o[0]

        if type(first) is StringType: 
            o[0] = [Symbol(ast.name,StringType())] + o[0]

        if type(first) is BooleanType: 
            o[0] = [Symbol(ast.name,BooleanType())] + o[0]

        if type(first) is ArrayType:
            o[0] = [Symbol(ast.name,ArrayType(first.dimensions,first.type))] + o[0]            
        return o
    def inferFuncDecl(self,ast,typ_,o): 
        global OrderOfFuncDecl
        global fancyFunction
        globalScope = len(o) - 1
        ret = None 
        for i in o[globalScope]: 
            if i.name == ast.name:
                if type(typ_) is IntegerType: 
                    ret = Utils.infer(ast.name,o,IntegerType())
                elif type(typ_) is FloatType: 
                    ret = Utils.infer(ast.name,o,FloatType())

                elif type(typ_) is StringType: 
                    ret = Utils.infer(ast.name,o,StringType())
                
                elif type(typ_) is BooleanType: 
                    ret = Utils.infer(ast.name,o,BooleanType())
                elif type(typ_) is ArrayType: pass
                return ret
        for i in OrderOfFuncDecl: 
            if i.name == ast.name:
                fancyFunction = True
                if type(typ_) is IntegerType: 
                    ret = Utils.infer(OrderOfFuncDecl,ast.name,IntegerType())

                elif type(typ_) is FloatType: 
                    ret = Utils.infer(OrderOfFuncDecl,ast.name,FloatType())

                elif type(typ_) is StringType: 
                    ret = Utils.infer(OrderOfFuncDecl,ast.name,StringType())
                elif type(typ_) is BooleanType: 
                    ret = Utils.infer(OrderOfFuncDecl,ast.name,BooleanType())
                elif type(typ_) is ArrayType: pass
                return ret
        raise Undeclared(Function(),ast.name)
    
    def inferArrayLit(self,ast,o): pass
    def inferArrayLitEle(self,typ_,exprs): pass
    def inferID(self,ast, typ_,o): 
        for symlist in o: 
            for symbol in symlist: 
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

        for i in o[0]:
            if ast.name == i.name:
                raise Redeclared(Variable(), ast.name)
        type = ast.type
        first = None

        if type(type) is AutoType and ast.first is None: 
            raise Invalid(Variable(),ast.name)
        if ast.first is not None:
            first = self.visit(ast.first,o)
            if type(type) is AutoType:
                if type(first) is not ArrayType: 
                    return self.inferVarDecl(ast,first,o)
                
                if type(first) is ArrayType and type(first.type) is not AutoType: 
                    return self.inferVarDecl(ast,first,o)
                
            if type(first) is ArrayType:
                if type(first.type) is AutoType:
                    self.inferArrayLit(ast,o)


                if type(type) is ArrayType: 
                    if type(first.type) != type(type.type) or len(first.dimensions) != len(type.dimensions): 
                        raise TypeMismatchInVarDecl(ast)
                    
                    for i in range(len(first.dimensions)): 
                        if first.dimensions[i] != type.dimensions[i]: 
                            raise TypeMismatchInVarDecl(ast)
                o[0] = [Symbol(ast.name,ArrayType(first.dimensions,first.type))] + o[0]
                return o
            
            if type(first) is AutoType:    
                if type(type) is AutoType: 
                    return o
                else: 
                    if type(ast.first) is FuncCall: 
                        first = self.inferFuncDecl(ast.first,type,o)
                    else: 
                        if type(ast.first) is UnExpr:
                            first = self.inferID(ast.first.val,type,o)
                        else: 
                            first = self.inferID(ast.name,type,o)

            if type(type) is FloatType and type(first) is IntegerType: 
                o[0] = [Symbol(ast.name,type)] + o[0]
                return o
            if type(type) != type(first):
                raise TypeMismatchInVarDecl(ast)
        o[0] = [Symbol(ast.name,type)] + o[0]
        return o
    
    def visitId(self,ast,o:object):
        for symlist in o: 
            for symbol in symlist:
                if symbol.name == ast.name:
                    if type(symbol) is Func_Symbol: 
                        return symbol.ret_type
                    return symbol.type
        raise Undeclared(Identifier(),ast.name)
    
    def visitIntegerType(self, ast, o):
        return IntegerType()
    def visitFloatType(self, ast, o):
        return FloatType()
    def visitBooleanType(self, ast, o):
        return BooleanType()
    def visitStringType(self, ast, o): 
        return StringType()

    def visitArrayType(self, ast, o): 
        type = self.visit(ast.type,o)
        return ArrayType(ast.dimension,type)
    def visitAutoType(self, ast, o): 
        return AutoType()
    def visitVoidType(self, ast, o):
        return VoidType()

    def visitBinExpr(self, ast, o):
        rhs = self.visit(ast.right,o)
        lhs = self.visit(ast.left,o)
        arithmetic_operator = ['-','+','*','/','%']
        bool_operator = ['!','&&','||']
        string_operator = ['::']
        relation_operator = ['==','!=','>','<','>=','<=']

        if ast.op in arithmetic_operator:
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
                return FloatType()  
            return IntegerType()
        
        if ast.op in bool_operator:
            if type(lhs) is AutoType: 
                lhs = Utils.infer(o, ast.left.name, BooleanType())

            if type(rhs) is AutoType:
                rhs = Utils.infer(o, ast.right.name, BooleanType())             
            if type(rhs) is not BooleanType or type(lhs) is not BooleanType: 

                raise TypeMismatchInExpression(ast)
            return BooleanType()
        
        if ast.op in string_operator:
            if type(lhs) is AutoType: 
                lhs = Utils.infer(o, ast.left.name, StringType())
            if type(rhs) is AutoType:
                rhs = Utils.infer(o, ast.right.name, StringType())  
            if type(rhs) is not StringType or type(lhs) is not StringType: 
                raise TypeMismatchInExpression(ast)
            return StringType()

        if ast.op in relation_operator: 
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

    def visitUnExpr(self, ast, o):
        i = self.visit(ast.val,o)

        if ast.op in ['!']: 
            if type(i) is AutoType: 
                i = Utils.infer(o, ast.val.name, BooleanType())
            if type(i) != BooleanType: 
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        if type(i) is AutoType: 
            return AutoType()
        if type(i) != IntegerType and type(i) != FloatType: 
            raise TypeMismatchInExpression(ast)
        return i
    
    def visitArrayCell(self, ast, o):
        for symlist in o: 
            for symbol in symlist: 
                if symbol.name == ast.name:
                    if type(symbol.type) is not ArrayType:
                        raise Undeclared(Variable(),type(symbol.type))
                    cell = []

                    for expr in ast.cell: 
                        type = self.visit(expr,o)
                        if type(type) is not IntegerType: 
                            raise TypeMismatchInExpression(expr)
                        cell = cell + [expr]

                    expected_len = len(symbol.type.dimensions)
                    real_len = len(cell)
                    if expected_len !=  real_len: 
                        if expected_len < real_len: 
                            raise TypeMismatchInExpression(ast)
                        else:
                            return ArrayType(symbol.type.dimensions[(expected_len):],symbol.type.type)
                    return symbol.type.type
                
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

        elementType = [self.visit(exp,o) for exp in ast.explist]

        for i in elementType: 
            if type(x) is AutoType: 
                pass

        temp_type = elementType[0]
        sameType = True

        for i in elementType: 
            if type(i) is not type(temp_type): 
                sameType = False
                break

        if sameType == True: 
            for i in elementType: 
                if type(i) is ArrayType: 
                    retInsideDimension = self.visitArrayLit(ast.explist[0],o).dimensions
                    retInsideType = self.visitArrayLit(ast.explist[0],o).type

                    for i in ast.explist[1:]: 
                        if retInsideDimension != self.visitArrayLit(i,o).dimensions: 
                            raise IllegalArrayLiteral(ast)

                        if retInsideType != self.visitArrayLit(i,o).type: 
                            raise IllegalArrayLiteral(ast)

                    return ArrayType([len(ast.explist)] + retInsideDimension,retInsideType)
                return ArrayType([len(ast.explist)],temp_type)
        raise IllegalArrayLiteral(ast)
    
    def visitFuncCall(self, ast, o): 
        args = ast.args
        for symlist in o: 
            for i in symlist:
                if ast.name == i.name: 
                    if type(i) is not Func_Symbol: 
                        raise TypeMismatchInExpression()
                    else:
                        if len(args) != len(i.param_typ_order):
                            raise TypeMismatchInExpression(ast)
                        for i in range(0,len(args)):

                            type_of_args = type(self.visit(args[i],o))
                            type_of_param = type(i.param_typ_order[i])

                            if type_of_args is AutoType and type_of_param is AutoType:
                                return
                            if type_of_args is AutoType:
                                if type_of_param is IntegerType: 
                                    type_of_args = Utils.infer(o,args[i].name,IntegerType())
                                if type_of_param is FloatType: 
                                    type_of_args = Utils.infer(o,args[i].name,FloatType())

                                if type_of_param is BooleanType: 
                                    type_of_args = Utils.infer(o,args[i].name,BooleanType())

                                if type_of_param is StringType: 
                                    type_of_args = Utils.infer(o,args[i].name,StringType())

                                if type_of_param is ArrayType: 
                                    type_of_args = Utils.infer(o,args[i].name,type_of_param)
                                type_of_args = type(type_of_args)

                            if type_of_param is AutoType:
                                if type_of_args is IntegerType: 
                                    Utils.infer(i.env,i.env[i].name,IntegerType())
                                    i.param_typ_order[i] = IntegerType()
                                if type_of_args is BooleanType: 
                                    Utils.infer(i.env,i.env[i].name,BooleanType())
                                    i.param_typ_order[i] = BooleanType()
                                if type_of_args is FloatType: 
                                    Utils.infer(i.env,i.env[i].name,FloatType())
                                    i.param_typ_order[i] = FloatType()
                                if type_of_args is StringType: 
                                    Utils.infer(i.env,i.env[i].name,StringType())
                                    i.param_typ_order[i] = StringType()
                                if type_of_args is ArrayType: 
                                    type_of_param = Utils.infer(o,args[i].name,type_of_param)
                                    i.param_typ_order[i] = type_of_param                                        
                                type_of_param = i.param_typ_order[i]
                                                                
                            if type_of_args != type_of_param:
                                if type_of_args is IntegerType and type_of_param is FloatType:
                                    continue
                                raise TypeMismatchInExpression (ast)
                            
                    if type(i.ret_type) is VoidType: 
                        raise TypeMismatchInExpression(ast)
                    return i.ret_type
            
        global fancyFunction
        for i in OrderOfFuncDecl:
            if i.name == ast.name:
                if len(args) != len(i.param_typ_order):
                        raise TypeMismatchInExpression(ast)
                for i in range(0,len(args)):
                    type_of_args = type(self.visit(args[i],o))
                    type_of_param = type(i.param_typ_order[i].type)

                    if type_of_args is AutoType and type_of_param is AutoType:
                        return
                    
                    if type_of_args is AutoType:           
                        if type_of_param is IntegerType: 
                            type_of_args = Utils.infer(o,args[i].name,IntegerType())

                        if type_of_param is FloatType: 
                            type_of_args = Utils.infer(o,args[i].name,FloatType())

                        if type_of_param is BooleanType: 
                            type_of_args = Utils.infer(o,args[i].name,BooleanType())
                        
                        if type_of_param is StringType: 
                            type_of_args = Utils.infer(o,args[i].name,StringType())

                        if type_of_param is ArrayType: 
                            type_of_args = Utils.infer(o,args[i].name,type_of_param)
                        type_of_args = type(type_of_args)

                    if type_of_param is AutoType: 
                        if type_of_args is IntegerType: 
                            i.param_typ_order[i].type = Utils.infer(i.env,i.env[i].name,IntegerType())

                        if type_of_args is FloatType: 
                            i.param_typ_order[i].type = Utils.infer(i.env,i.env[i].name,FloatType())
                            
                        if type_of_args is BooleanType: 
                            i.param_typ_order[i].type = Utils.infer(i.env,i.env[i].name,BooleanType())
                        
                        if type_of_args is StringType: 
                            i.param_typ_order[i].type =Utils.infer(i.env,i.env[i].name,StringType())
                        if type_of_args is ArrayType: 
                            i.param_typ_order[i].type = Utils.infer(i.env,i.env[i].name,type_of_param)
                        type_of_param = type(i.param_typ_order[i].type)                                  
                     
                    if type_of_args != type_of_param:
                        if type_of_args is IntegerType and type_of_param is FloatType:
                            continue
                        raise TypeMismatchInExpression (ast)
                fancyFunction = True
                if type(i.ret_type) is VoidType: 
                    raise TypeMismatchInExpression(ast)
                return i.ret_type
        raise Undeclared(Function(),ast.name)

    def visitSingleStmt(self,ast,o): 
        global checkFather

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
        global checkFather

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

        rhs = self.visit(ast.rhs,o)
        lhs = self.visit(ast.lhs,o)
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
                return
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

    def visitIfStmt(self, ast, o):

        type_condition = self.visit(ast.cond,o[2])
        
        if type(type_condition) is not BooleanType: 
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

    def visitForStmt(self, ast, o):
        init_type = self.visit(ast.first,o[2])
        if type(init_type) is not IntegerType: 
            raise TypeMismatchInStatement(ast) 
              
        type_condition = self.visit(ast.cond,o[2])
        if type(type_condition) is not BooleanType: 
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
        

    def visitWhileStmt(self, ast, o):
        type_condition = self.visit(ast.cond,o[2])
        if type(type_condition) is not BooleanType: 
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

        type_condition = self.visit(ast.cond,o[2])
        if type(type_condition) is not BooleanType: 
            raise TypeMismatchInStatement(ast)

        o[3] += ["DoWhileStmt"]
        o[2] = [[]] + o[2]
        self.visit(ast.stmt,o)
        o[3].pop()
        o[0] = 0

    def visitBreakStmt(self, ast, o):
        o[4] = o[4] + 1

        for i in reversed(o[3]): 
            if i == "ForStmt" or i == "WhileStmt" or i == "DoWhileStmt": 
                return
        raise MustInLoop(ast)
    
    def visitContinueStmt(self, ast, o): 
        o[4] = o[4] + 1
        # if o[4] > 1: return
        for i in reversed(o[3]): 
            if i == "ForStmt" or i  == "WhileStmt" or i == "DoWhileStmt": 
                return
        raise MustInLoop(ast)
    
    def visitReturnStmt(self, ast, o):
        o[0] = o[0] + 1
        type = None
        if o[0] == 1: 
            for i in OrderOfFuncDecl:
                if i.name == o[1]: 
                    if ast.expr is None: 
                        type = VoidType()
                    else: type = self.visit(ast.expr,o[2])

                    if type(i.ret_type) is AutoType: 
                        i.ret_type = type

                    if type(i.ret_type) is FloatType and type(type) is IntegerType:
                        return i.ret_type
                    
                    if type(i.ret_type) != type(type): 

                        raise TypeMismatchInStatement(ast)
                    return type

        for i in OrderOfFuncDecl: 
            if i.name == o[1]: 
                if ast.expr is None:
                    type = VoidType()
                else: type = self.visit(ast.expr,o[2])
                if type(i.ret_type) != type(type): 
                    raise TypeMismatchInStatement(ast)      
        return type
    def visitCallStmt(self, ast, o):

        global OrderOfFuncDecl
        if ast.name == "super" or ast.name == "preventDefault": 
            return VoidType()
        args = ast.args

        for symlist in o: 
            for i in symlist: 
                if ast.name == i.name: 
                    if type(i) is not Func_Symbol: 
                        raise TypeMismatchInStatement(ast)
                    else:
                        if len(args) != len(i.param_typ_order):
                            raise TypeMismatchInStatement(ast)
                        for i in range(0,len(args)):

                            type_of_args = type(self.visit(args[i],o))
                            type_of_param = type(i.param_typ_order[i])

                            if type_of_args is AutoType and type_of_param is AutoType:
                                return
                            if type_of_args is AutoType:
                                if type_of_param is IntegerType: 
                                    type_of_args = Utils.infer(o,args[i].name,IntegerType())

                                if type_of_param is FloatType: 
                                    type_of_args = Utils.infer(o,args[i].name,FloatType())

                                if type_of_param is BooleanType: 
                                    type_of_args = Utils.infer(o,args[i].name,BooleanType())
                                
                                if type_of_param is StringType: 
                                    type_of_args = Utils.infer(o,args[i].name,StringType())
                                if type_of_param is ArrayType: 
                                    type_of_args = Utils.infer(o,args[i].name,type_of_param)

                                type_of_args = type(type_of_args)
                            if type_of_param is AutoType:
                                if type_of_args is IntegerType: 
                                    Utils.infer(i.env,i.env[i].name,IntegerType())
                                    i.param_typ_order[i] = IntegerType()

                                if type_of_args is FloatType: 
                                    Utils.infer(i.env,i.env[i].name,FloatType())
                                    i.param_typ_order[i] = FloatType()

                                if type_of_args is BooleanType: 
                                    Utils.infer(i.env,i.env[i].name,BooleanType())
                                    i.param_typ_order[i] = BooleanType()
                                if type_of_args is StringType: 
                                    Utils.infer(i.env,i.env[i].name,StringType())
                                    i.param_typ_order[i] = StringType()
                                if type_of_args is ArrayType: 
                                    type_of_param = Utils.infer(o,args[i].name,type_of_param)
                                    i.param_typ_order[i] = type_of_param                                        
                                type_of_param = i.param_typ_order[i]
                                                                
                            if type_of_args != type_of_param:
                                if type_of_args is IntegerType and type_of_param is FloatType:
                                    continue
                                raise TypeMismatchInStatement (ast)

                        return VoidType()
        for i in OrderOfFuncDecl:
            if i.name == ast.name: 
                if len(args) != len(i.param_typ_order):
                    raise TypeMismatchInStatement(ast)
                for i in range(0,len(args)):
                    type_of_args = type(self.visit(args[i],o))
                    type_of_param = type(i.param_typ_order[i].type)

                    if type_of_args is AutoType and type_of_param is AutoType:

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
                            i.param_typ_order[i].type = Utils.infer(i.env,i.env[i].name,IntegerType())
                        if type_of_args is BooleanType: 
                            i.param_typ_order[i].type = Utils.infer(i.env,i.env[i].name,BooleanType())
                        if type_of_args is FloatType: 
                            i.param_typ_order[i].type = Utils.infer(i.env,i.env[i].name,FloatType())
                        if type_of_args is StringType: 
                            i.param_typ_order[i].type =Utils.infer(i.env,i.env[i].name,StringType())
                        if type_of_args is ArrayType: 
                            i.param_typ_order[i].type = Utils.infer(i.env,i.env[i].name,type_of_param)
                        type_of_param = type(i.param_typ_order[i].type)                                  
                     
                    if type_of_args != type_of_param:
                        if type_of_args is IntegerType and type_of_param is FloatType:
                            continue
                        raise TypeMismatchInStatement (ast)

                return VoidType()
        raise Undeclared(Function(),ast.name)