from Account import Account

class SavingAccount(Account) : 
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__( account_holder, balance)
        self.interest_rate = interest_rate
    def get_interest_rate(self):
        return self.__interest_rate

    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

    def add_interest(self):
        self.__balance += self.__balance * (self.__interest_rate / 100)

    def __str__(self):
        return f"Account Number: {self.get_account_number()}\nAccount Holder: {self.get_account_holder()}\nInterest Rate: {self.__interest_rate}%"
    
    
