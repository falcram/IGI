from check_input import check_input
#Get string, count digits and print result
def task3():

    #Decorator function
    def count_digits_decorator(func):
        def wrapper(text):
            res = func(text)  # Call the function being checked
            print(f"Number of digits: {res}")
        return wrapper

    #Function that count digits in string and return integer result
    @count_digits_decorator
    def count_digits(count_string):
        """Function that count digits in string and return integer result"""
        count = 0
        for i in count_string:
            if i.isdigit():
                count+=1
        return count
    
    print("Enter string:")
    mystr = check_input(str, "NO VALUE")
    count_digits(mystr)

