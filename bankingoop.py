class Bank_account:
    
    def __init__(self):
        self.balance = 0
        print("Welcome to the withdrawal and Deposit machine")
    
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("deposited amount:", amount)
        
    def withdraw(self):
        amount = float(input("Enter amount to be withdraw: "))
        if self.balance >= amount:
            self.balance -= amount
            print("withdraw amount:", amount)
        else:
            print("insufficient balance")
        
        
    def display(self):
        print("Net available balance: ", self.balance)

s = Bank_account()

Bank_account.deposit(s)
Bank_account.withdraw(s)
Bank_account.display(s)
