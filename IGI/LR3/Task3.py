from check_input import check_input
def task3():
    def count_digits(count_string):
        count = 0
        for i in range(len(count_string)):
            if count_string[i].isdigit():
                count+=1
        return count
    
    print("Enter string")
    mystr = check_input(str, "NO VALUE")
    res = count_digits(mystr)
    print(f"Number of digits: {res}")

task3()
