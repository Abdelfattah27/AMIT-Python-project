def get_number(message ) : 
    while True : 
        try :
            number = float(input(message))
            break
        except ValueError : 
            print("Invalid input, please enter a valid number")  
    return number