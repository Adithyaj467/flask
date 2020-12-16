class Account:
    def __init__(self,owner,balance):
        print('hello and welcome to dummie bank account')
        self.owner=owner
        self.balance=balance

    def deposit(self,amt):
        print('hello you are making a deposit')
        self.balance=self.balance+amt
        print(f"new balance is {self.balance}")

    def withdraw(self,amt):
        print('hello you are making a withdraw')
        if self.balance>amt:
            self.balance=self.balance-amt
        else:
            print(f"amount is greater than balance of {self.balance}")

acct=Account('jose',100)
print(acct)
acct.owner
acct.balance
acct.deposit(50)
acct.withdraw(75)
acct.withdraw(500)          
