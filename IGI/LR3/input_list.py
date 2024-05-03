import random
from check_input import check_input

#Get user values and return list
def get_user_list_t2():
    numbers = []
    print("Enter integer numbers: ")
    while True:
    
        temp = check_input(int, "NO VALUE")
        if temp == 0:
            break
        numbers.append(temp)
    return numbers
#Generate random values and return list
def generate_random_list_t2():
    amount = int(input("Enter how much numbers should be in list:"))
    numbers = [random.randint(1, 100) for _ in range(amount)]
    print(numbers)
    #numbers.append(0)
    return numbers

#Get user values and return list
def get_user_list_t5():
    print("Enter your list:")
    inp_list = []
    while(True):
        temp = check_input(float, "stop")
        if temp == "STOP":
            break
        inp_list.append(temp)
    return inp_list

#Generate random values and return list
def generate_random_list_t5():
    amount = int(input("Enter how much numbers should be in list:"))
    numbers = [random.uniform(1, 100) for _ in range(amount)]
    print(numbers)
    #numbers.append(0)
    return numbers
