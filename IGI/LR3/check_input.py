def check_input(inp_type, checked_val):
    while True:
        try:
            temp = inp_type(input())     
            if checked_val == "NO VALUE":
                return temp 
            elif checked_val != "NO VALUE" and temp == checked_val:
                return temp
            else:
                print("Incorrect value!")    
        except ValueError:
            print(f"Input of the {inp_type.__name__} type is expected. Try again.")