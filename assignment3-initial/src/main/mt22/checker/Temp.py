class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast, [])
class Symbol(): 
    def __init__(self,name,typ):
        self.name = name
        self.typ =typ # define as list to seperate with Function
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
        self.out = self.out
class Utils(): 
    def infer(self,name,SymbolTable,typ): 
        for symbol_list in SymbolTable: 
            for symbol in symbol_list: 
                if symbol.name == name: 
                    if type(symbol) != FuncSymbol: symbol.typ = [typ]
                    else: symbol.typ[0] = typ # return type XDDD


class GetEnv(Visitor): #visit vong ngoai truoc, tuc cac khai bao o tam vuc global.\
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast, [])
    def visitProgram(self,ast,o:object): 
        o = []
        for decl in ast.decls:
            if type(decl) is FuncDecl: 
                o = self.visit(decl, o)
        return o 
    def visitFuncDecl(self,ast:FuncDecl,o:object):
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
        o = [FuncSymbol(ast.name,return_type,paramTypeOrder,ast.inherit,[],ast.body)] + o
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