import helper
from config import DATA_PATH
from controllers.Bank import Bank
bank = Bank()

MENU_OPTIONS = {
    1: "Get a tour to the bank",
    2: "Create account",
    3: "Show account details",
    4: "Show balance",
    5: "Modify account",
    6: "Delete account",
    7: "Show all accounts",
    8: "Exit program"
}


def show_menu():
    print("***************** Welcome to your bank ***********") 
    while True:
        print("\nHow can I help you?\n")
        for option, description in MENU_OPTIONS.items():
            print(f"{option}. {description}")
        try:
            menu_choice = int(input("\nEnter your choice: "))
            if menu_choice in MENU_OPTIONS:
                return menu_choice
            else:
                print("Wrong input: Please enter a number between 1 to 8")
        except ValueError:
            print("Wrong input: Please enter a valid number")
            
def display_tour():
    print("""
This program allows you to control your account in the bank. 
You have the ability to create an account and choose the type you want, 
either Checking account or Saving account. 
You can read the data of your account and modify it as you want. 
You can also delete your account. 
    """)

def create_account():
    name = input("Please enter your name: ")
    balance = helper.get_number("Please enter your current balance: ")
    while True:
        account_type = helper.get_number("Please enter the type of the account - just enter the number\n1. Checking account\n2. Saving account")
        if account_type == 1:
            overdraft_limit = helper.get_number("Please enter your overdraft limit: ")
            account_type = "checking"
            interest_rate = None
            break
        elif account_type == 2:
            interest_rate = helper.get_number("Please enter your interest rate: ")
            account_type = "saving"
            overdraft_limit = None
            break
        else:
            print("Please enter 1 or 2")
    create_succession = bank.create_account(account_holder=name, balance=balance, account_type=account_type, overdraft_limit=overdraft_limit, interest_rate=interest_rate)
    if create_succession != -1:
        print("Account created successfully 😍")
    elif create_succession == 1:
        print("Something went wrong while creating this account")
        
def show_account_details():
    account_number = int(helper.get_number("Please enter your account number: "))
    account =bank.get_account_by_number(account_number=account_number)
    if account is not None : 
        print(account) 
    else  : 
        print("Account Not Found")  
def show_account_balance() : 
    account_number = int(helper.get_number("Please, enter your account number : "))
    account = bank.get_account_by_number(account_number)
    if account is not None :   
        balance = account.get_balance()
        print(f"your balance: {balance}")
    else  : 
        print("Account Not Found") 
def modify_account(): 
    account_number = int(helper.get_number("Please, enter your account number : "))
    balance = float(helper.get_number("Enter the modified balance : "))
    overdraft_limit = float(helper.get_number("if your account is checking account enter overdraft limit else enter -1 : "))
    interest_rate = float(helper.get_number("if your account is saving account enter interest rate else enter -1 : "))
    modify_succession = bank.modify_account(account_number=account_number ,balance = balance , overdraft_limit = overdraft_limit , interest_rate = interest_rate  )
    if modify_succession == 1 : 
        print("Modifies successfully")
    else : 
        print("Something wrong had happen")  
def delete_account() : 
    account_number = int(helper.get_number("Please, enter your account number : "))
    delete_succession = bank.delete_account(account_number=account_number)  
    if delete_succession == 1 : 
        print("deleted successfully")
    else : 
        print("Something wrong had happen")  
