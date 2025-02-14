#calculator mini
class add:
    @staticmethod
    def addition(a,b):
        return a+b
class sub:
    @staticmethod
    def subtraction(a,b):
        return a-b
class multi:
    @staticmethod
    def multiply(a,b):
        return a*b
class div:
    @staticmethod
    def division(a,b):
        return a/b
class floordiv:
    @staticmethod
    def floordivision(a,b):
        return a//b
class mod:
    @staticmethod
    def modulas(a,b):
        return a%b    
    
class calculator(add,sub,multi,div,floordiv,mod):
    def __init__(self):
        self.a=int(input('enter the first no:'))
        self.b=int(input('enter the second no:'))
        self.c=input('enter the operation:')
        if self.c=='+':
            print(self.addition(self.a,self.b))
        elif self.c=='-':
            print(self.subtraction(self.a,self.b))
        elif self.c=='*':
            print(self.multiply(self.a,self.b))
        elif self.c=='/':
            print(self.division(self.a,self.b))
        elif self.c=='//':
            print(self.floordivision(self.a,self.b))
        elif self.c=='%':
            print(self.modulas(self.a,self.b))
obj=calculator()




