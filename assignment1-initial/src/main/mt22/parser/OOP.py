# class Employee: 
#     'test'
#     empCount = 0 #static field
#     def __init__(self, name, salary):
#         self.name = name  #instance field
#         self.salary = salary #instance field
#         Employee.empCount += 1
#     def displayEmployee(self): 
#         print("Name : ", self.name, 
#         " Salary : ", self.salary)
#     @classmethod #to define class method
#     def create(cls,n, s): #first param for class
#         print (cls, s.empCount) #access to static field
#         return cls (n,s) # 
#     @staticmethod
#     def isHighSal(s): #define static method
#         if s > 8:  #no param for class
#             print("High salary\n") #unable to access any fiel 
# obj = Employee.create("Nam", 30)

# print(obj.isHighSal(obj.salary))
# def lstSquare(n): 
#     return [i*i for i in range(1,n+1)]
def lstSquare(n): 
    lst = []; 
    for i in range(1,n+1): 
        lst.append(i*i)
    return lst
print(lstSquare(3))
a,b = 3,4
print(a)
class Eval: 
    def visit(self,ctx: Exp): 
        if type(ctx) is IntLit: 
            return ctx.value
        elif type(ctx) is FloatLit: 
            return ctx.value
        elif type(ctx) is BinExp: 
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            if ctx.op == "+": return left + right
            elif ctx.op == "-": return left - right
            elif ctx.op == "*": return left * right
            elif ctx.op == "/": return left / right
        elif type(ctx) is UnExp: 
            value = self.visit(ctx.operand)
            return -value if ctx.op == "-" else value
class PrintPreFix:
    def visit(self,ctx: Exp): 
        self.visit(ctx.left)
        
        left = self.visit(ctx.right)
""" void prefix(Node* root): 
    if (root != null){
    prefix(root->left);
    

    }
""" 
class Visitor: 
    def visit(self.ctx): 
        return ctx.accept(self) #vo nha``
class Eval(Visitor):
    def visitIntLit(self,ctx): # go cua
        return ctx.value
    def visitFloatLit(self,ctx):
        return ctx.value
    def visitBinExp(self,ctx): 
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if (ctx.op == "+") return left + right
    
