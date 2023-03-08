import views_configration
from actions import *
import json

def main() : 
    while True : 
        menu_choice = show_menu()
        try : 
            if menu_choice == 1 : 
                display_tour()
            elif menu_choice == 2 : 
                create_account()
            elif menu_choice == 3 : 
                show_account_details()
            elif menu_choice == 4 : 
                show_account_balance()
            elif menu_choice == 5 : 
                modify_account()
            elif menu_choice == 6 :  
                delete_account()
            elif menu_choice == 7 : 
                print(list(bank.get_all_accounts()))  
            elif menu_choice == 8 : 
                with open(DATA_PATH , "w") as file : 
                    data = {"data" : list(bank.get_all_accounts())}
                    json.dump(data , fp=file)
                break 
            else : 
                print("Wrong input: Please enter number between 1 to 8 ")      
            
        except Exception as ex : 
            print(str(ex))
if __name__ == "__main__" : 
    main()