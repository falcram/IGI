from check_input import check_input
from input_list import get_user_list_t2
from input_list import generate_random_list_t2
# Get list of integer values and sum every second of them and print result
def task2():
    #Sum every second number and return integer sum
    def my_integer_sum(nums):
        sum = 0
        for i in range(len(nums)):
            if i%2!=0:
                sum+=nums[i]
        return sum

    numbers = []
    print("1 - input in list by yourself\n2 - input in list random values")
    while True:
        choice = check_input(int, "NO VALUE")
        if choice == 1:
            numbers = get_user_list_t2()
            break
        elif choice == 2:
            numbers = generate_random_list_t2()
            break
        else:
            print("Incorrect value! Try again.")
    
    res = my_integer_sum(numbers)
    print(f"Sum of every second: {res}")

