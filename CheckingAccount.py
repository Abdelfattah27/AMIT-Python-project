from Account import Account 

class CheckingAccount (Account) : 
    def __init__(self , account_holder , balance , overdraft_limit) : 
        super().__init__(account_holder , balance)
        self.overdraft_limit = overdraft_limit 
    def get_overdraft_limit (self) :
        return self.overdraft_limit 
    def set_overdraft_limit(self , over_draft_limit) : 
        self.overdraft_limit = over_draft_limit 
    def withdraw(self , amount) : 
        if (self.balance + self.get_overdraft_limit) >= amount :
            self.balance -= amount 
        else : 
            print("Insufficient balance")
    def __str__(self) : 
        return f"Account Number: {self.account_number}\n Account Holder: {self.account_holder}\n OverDraftLimit: {self.overdraft_limit}"
    