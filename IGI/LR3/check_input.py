#Check input by defined criterion
def check_input(inp_type, checked_val):
    while True:
        try:
            temp = input()     
            if checked_val == "NO VALUE":
                return inp_type(temp) 
            elif checked_val != "NO VALUE" and temp != checked_val:
                return inp_type(temp)
            elif temp == checked_val:
                return "STOP"
            else:
                print("Incorrect value!")    
        except ValueError:
            print(f"Input of the {inp_type.__name__} type is expected. Try again.")