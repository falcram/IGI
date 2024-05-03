from check_input import check_input
from input_list import get_user_list_t5
from input_list import generate_random_list_t5
def task5():
    #Finde in list last element that the same as check value 
    def list_rindex(lst, item):
        i = len(lst) - 1
        while i >= 0:
            if lst[i] == item:
                return i
            i -= 1
        return -1
    #Sum numbers after last defined element and count alements that greater than zero and even 
    def task_func(input_list):
        target = 0
        place = list_rindex(input_list, target)
        if place == -1:
            return 0, 0
        print(f"Place: {place}")
        sum = 0
        amount = 0
        #for i in input_list[input_list.index(place+1):]:
        for i, num in enumerate(input_list):
            if i <= place:
                continue
            #print(num)
            sum+=num
            if num > 0 and num%2==0:
                amount+=1
        return sum, amount

    inp_list = []
    print("1 - input in list by yourself\n2 - input in list random values")
    while True:
        choice = check_input(int, "NO VALUE")
        if choice == 1:
            inp_list = get_user_list_t5()
            break
        elif choice == 2:
            inp_list = generate_random_list_t5()
            break
        else:
            print("Incorrect value! Try again.")

    sum, amount = task_func(inp_list)
    print(f"Sum: {sum}, Amount: {amount}")  
    for i in inp_list:
        print(i, end=", ")
    
#task5()