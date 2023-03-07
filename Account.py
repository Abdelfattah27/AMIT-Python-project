class Account : 
    counter = 0 
    def __init__(self , account_holder , balance) : 
        self.account_holder = account_holder 
        self.balance = balance 
        Account.counter+=1
        self.account_number = Account.counter
    def get_account_number(self) : 
        return self.account_number 
    def get_account_holder (self) : 
        return self.account_holder()
    def get_balance(self) : 
        return self.balance 
    def deposite(self , amount) : 
        self.balance += amount 
    def withdraw(self , amount) : 
        if self.balance >= amount :
            self.balance -= amount 
        else : 
            print("Insufficient balance")
    def __str__(self) : 
        return f"Account number: {self.account_number} && Account Holder: {self.account_holder}"
    def __add__(self , other) :
        return self.balance + other.balance
    def __sub__(self , other) :
        return self.balance - other.balance
    
     
        
    
    
        