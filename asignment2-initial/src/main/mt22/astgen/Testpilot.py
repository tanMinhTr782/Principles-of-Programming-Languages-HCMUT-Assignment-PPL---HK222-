def compose(f,g): 
    def h(x): 
        return f(g(x))
    return h 
def square(x): return x*x
def increase(x): return x + 1
def double(x): return x*2
m = compose(double,increase)
print(m(5))

# class Num: 
#     def __init__(self,x): 
#         self.x = x
# class Add: 
#     def __add__(self,other): 
#         return self.x + other.x
# class Mul: 
#     def __mul__(self,other): 
#         return self.x * other.x
# class Num1(Num, Add): pass 
# class Num2(Num, Mul): pass
# x = Num1(4)
# y = Num2(5)
# print(x*y)