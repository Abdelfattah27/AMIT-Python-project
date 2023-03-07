from SavingAccount import SavingAccount 
from CheckingAccount import CheckingAccount 
from Account import Account
import json
class Bank : 
    def __init__(self) :
        self.accounts = []
        with open("data.json" , "r") as file : 
            accounts = json.load(file)
        for i in accounts["data"] : 
            if(i["type"] == "checking") : 
                new_account = CheckingAccount(account_holder=i["account_holder"] , balance=i["balance"] , overdraft_limit= i["overdraft_limit"] )
            elif(i["type"] == "checking") : 
                new_account = SavingAccount(account_holder=i["account_holder"] , balance=i["balance"] ,interest_rate= i["interest_rate"] )
            self.accounts.append(new_account)
    def get_all_accounts(self) : 
        for i in self.accounts : 
            if isinstance( i , CheckingAccount) :
                i.type = "checking"
            else : 
                i.type = "saving" 
            yield i.__dict__
        #return self.accounts
    def create_account(self , account_holder: str, balance: float, account_type: str, overdraft_limit=None, interest_rate=None) :
        """
        Create a new bank account with the specified details, and add it to the list of accounts.

        Parameters:
        - account_number (str): the account number
        - account_holder (str): the name of the account holder
        - balance (float): the initial balance of the account
        - account_type (str): the type of the account (e.g., "checking", "savings")
        - overdraft_limit (float, optional): the overdraft limit for a checking account (default=None)
        - interest_rate (float, optional): the interest rate for a savings account (default=None)
        """
        if account_type == "checking" :
            new_account = CheckingAccount(account_holder , balance , overdraft_limit)
            self.accounts.append(new_account)
        elif account_type == "saving" : 
            new_account = SavingAccount(account_holder , balance , interest_rate) 
            self.accounts.append(new_account)
            
        else : 
            raise ValueError(f"Invalid account type {account_type}")
        
    def get_account_by_number(self, account_number: str) -> Account:
        """
        Search for a bank account with the specified account number, and return it.

        Parameters:
        - account_number (str): the account number to search for

        Returns:
        - Account: the account object with the specified account number, or None if not found
        """
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None
    
    def get_accounts_by_holder(self, account_holder: str) -> list[Account]:
        """
        Search for all bank accounts owned by the specified account holder, and return them.

        Parameters:
        - account_holder (str): the name of the account holder to search for

        Returns:
        - List[Account]: a list of account objects owned by the specified account holder
        """
        matching_accounts = []
        for account in self.accounts:
            if account.get_account_holder() == account_holder:
                matching_accounts.append(account)
        return matching_accounts
    def delete_account(self , account_number)  :
        """
        delete the specified bank account with the specified account number.

        Parameters:
        - account_number (str): the account number of the account to delete
        
        """
        account = self.get_account_by_number(account_number)
        if account is not None:
            self.accounts.remove(account)
        else : 
            return -1
        
        
    def modify_account(self, account_number: str, *args, **kwargs):
        print(kwargs)
        """
        Modify the specified attribute of a bank account with the specified account number.

        Parameters:
        - account_number (str): the account number of the account to modify
        - attribute (str): the name of the attribute to modify (e.g., "balance", "overdraft_limit", "interest_rate")
        - value (float): the new value to set for the attribute
        """
        account = self.get_account_by_number(account_number)
        for attribute , value in kwargs.items() :
            if account is not None:
                if int(value) != -1 and attribute == "balance":
                    account.deposite(value)
                elif int(value) != -1 and attribute == "overdraft_limit":
                    if isinstance(account, CheckingAccount) :
                        account.set_overdraft_limit(value)
                    else:
                        raise ValueError(f"Account {account_number} is not a checking account")
                elif int(value) != -1 and attribute == "interest_rate":
                    if isinstance(account, SavingAccount):
                        account.set_interest_rate(value)
                    else:
                        raise ValueError(f"Account {account_number} is not a savings account")
            else:
                raise ValueError(f"Account {account_number} not found" )
        
        
    
    