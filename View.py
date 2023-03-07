from Bank import Bank
MyBank = Bank()
import json
print("***************** Welcome to your bank ***********") 


while True : 
    print("""
How can i help you :

 
1. get a tour to the bank 
2. create account 
3. already have account and want to show it's details
4. show you balance
5. modify your account
6. delete your account
7. show all accounts
8. exit the program 
        """)
    try : 
        choice = int(input("Enter your choice : "))
        if choice == 1 : 
            print("""
this program allow you to control you account in the bank, 
while you have the ability to create account and choose the type you want 
either was Checking account or saving account
you can read the data of your account and modify it as you want  
you can also delete your account 
                """)
        elif choice == 2 : 
            name = input("Please enter your name : ")
            while True : 
                try :
                    balance = float(input("Please enter your current balance : "))
                    break
                except : 
                    print("Bad input Reenter again : ")  
            while True : 
                account_type = int(input("""
Please, Enter the type of the account - just enter the number
1. Checking account
2. Saving account
"""))
                
                if account_type == 1 : 
                    overdraft_limit  = float(input("Please enter your overdraft limit : "))
                    account_type = "checking"
                    interest_rate = None
                    break 
                elif account_type == 2 : 
                    interest_rate = float(input("Please enter your interest rate : "))
                    account_type = "saving"
                    overdraft_limit = None
                    break 
                else : 
                    print("Please enter a valid account type")
            MyBank.create_account(account_holder=name , balance=balance , account_type=account_type , overdraft_limit=overdraft_limit , interest_rate=interest_rate)
            print("Account Created successfully")
        elif choice == 3 : 
            while True: 
                account_number = int(input("Please, enter your account number : "))
                account = MyBank.get_account_by_number(account_number=account_number)
                if account is not None : 
                    print(account)
                    break 
                else  : 
                    print("Bad Input")  
        elif choice == 4 : 
            while True: 
                account_number = int(input("Please, enter your account number : "))
                account = MyBank.get_account_by_number(account_number)
                if account is not None :   
                    balance = account.get_balance()
                    print(f"your balance: {balance}")
                    break 
                else  : 
                    print("Bad Input") 
        elif choice == 5 : 
            while True : 
                try : 
                    account_number = int(input("Please, enter your account number : "))
                    balance = float(input("Enter the modified balance : "))
                    overdraft_limit = float(input("if your account is checking account enter overdraft limit else enter -1 : "))
                    interest_rate = float(input("if your account is saving account enter interest rate else enter -1 : "))
                    MyBank.modify_account(account_number=account_number ,balance = balance , overdraft_limit = overdraft_limit , interest_rate = interest_rate  )
                    break
                except Exception as ex : 
                    print(str(ex))
        elif choice == 6 : 
            while True :
                try :  
                    account_number = int(input("Please, enter your account number : "))
                    MyBank.delete_account(account_number=account_number)
                    break 
                except  : 
                    print("Bad Input")
        elif choice == 7 : 
            print(list(MyBank.get_all_accounts()))  
        elif choice == 8 : 
            with open("data.json" , "w") as file : 
                data = {"data" : list(MyBank.get_all_accounts())}
                json.dump(data , fp=file)
            break 
        else : 
            print("Wrong input: Please enter number between 1 to 8 ")      
        
    except Exception as ex : 
        print(str(ex))