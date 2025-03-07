#Bank Account Management System

class Bank:
    bname='SBI'
    def __init__(self,name,accno,ifsc,phno,balance):
        self.name=name
        self.accno=accno
        self.ifsc=ifsc
        self.phno=phno
        self.balance=balance

    def display(self):
        print(f'Account Holder : {self.name}')
        print(f'Account No : {self.accno}')
        print(f'ifsc : {self.ifsc}')
        print(f'Phone No : {self.phno}')
        print(f'Balance : {self.balance}')

    def deposit(self,amount):
        self.balance=self.add(self.balance,amount)
        print(f'{amount} credited your current balance is {self.balance}')

    def withdraw(self,amount):
        if amount>self.balance:
            print(f'Insufficient balance your current balance is {self.balance}')
        else:
            self.balance=self.sub(self.balance,amount)
            print(f'{amount} debited your balance is {self.balance}')

    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def sub(a,b):
        return a-b

obj=Bank('ram',13456789097531,'SBI24680',9876543210,5000)
obj.display()
obj.deposit(5000)
obj.withdraw(10000)
