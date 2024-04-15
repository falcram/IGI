from check_input import check_input
def task2():
    def my_integer_sum(nums):
        sum = 0
        for i in range(len(nums)):
            if i%2!=0:
                sum+=nums[i]
        return sum

    numbers = []
    print("Enter integer")
    while True:
    
        temp = check_input(int, "NO VALUE")
        if temp == 0:
            break
        numbers.append(temp)

    res = my_integer_sum(numbers)
    print(f"Sum of every second: {res}")
