class BankAccount:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        if self.balance == 'empty':
            raise ValueError
        else:
            return self.balance

    def open(self):
        self.balance = 0

    def deposit(self, amount):
        if self.balance == 'empty' or amount < 0:
            raise ValueError
        self.balance += amount 

    def withdraw(self, amount):
        if self.balance == 'empty' or amount > self.balance or amount < 0:
            raise ValueError
        self.balance -= amount 

    def display(self): 
        print("Net Available Balance =", self.balance) 

    def close(self):
        self.balance = 'empty'
    
