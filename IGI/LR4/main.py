#from Task4 import pentagon 
from Task1 import Task1
from Task2 import Task2
from Task3 import Task3
from Task4 import Task4
from Task5 import Task5

#Show functions and allows to choose function to use
def main():
    """Show functions and allows to choose function to use"""
    print("Enter the number of the task you want to complete:")
    print("1 - Task 1")
    print("2 - Task 2")
    print("3 - Task 3")
    print("4 - Task 4")
    print("5 - Task 5")
    print("6 - Exit")
    task = input()
    exitTask=False
    while True:
            match task:
                case "1":
                    while exitTask==False:
                        try:
                            print("Task №1 selected")
                            Task1()
                            # Ask the user if they want to run the program again
                            run_again = input("Do you want to run task №1 again? (yes/no): ")
                            if run_again.lower() == 'yes':
                                print("Restarting the task")
                            if run_again.lower() == 'no':
                                print("Exiting task #1")
                                exitTask=True
                                main()
                            else:
                                while run_again.lower() != 'yes' and run_again.lower() != 'no':
                                    print("Input error! Repeat again:")
                                    run_again = input()
                        except ValueError:
                            print("An incorrect value has been entered. Please enter a numeric value.")
                        except Exception as e:
                            print(f"Error occurred: {e}")
                case "2":
                    while exitTask == False:
                        try:
                            print("Task №2 selected")
                            Task2()
                            # Ask the user if they want to run the program again
                            run_again = input("Do you want to run task №2 again? (yes/no): ")
                            if run_again.lower() == 'yes':
                                print("Restarting the task")
                            if run_again.lower() == 'no':
                                print("Exiting task №2")
                                exitTask = True
                                main()
                            else:
                                while run_again.lower() != 'yes' and run_again.lower() != 'no':
                                    print("Input error! Repeat again:")
                                    run_again = input()
                        except ValueError:
                            print("An incorrect value has been entered. Please enter a numeric value.")
                        except Exception as e:
                            print(f"Error occurred: {e}")
                case "3":
                    while exitTask == False:
                        try:
                            print("Task №3 selected")
                            Task3()
                            # Ask the user if they want to run the program again
                            run_again = input("Do you want to run task №1 again? (yes/no): ")
                            if run_again.lower() == 'yes':
                                print("Restarting the task")
                            if run_again.lower() == 'no':
                                print("Exiting task №3")
                                exitTask = True
                                main()
                            else:
                                while run_again.lower() != 'yes' and run_again.lower() != 'no':
                                    print("Input error! Repeat again:")
                                    run_again = input()
                        except ValueError:
                            print("An incorrect value has been entered. Please enter a numeric value.")
                        except Exception as e:
                            print(f"Error occurred: {e}")
                case "4":
                    while exitTask == False:
                        try:
                            print("Task №4 selected")
                            #obj = pentagon(4, "red")
                            #obj.draw()
                            Task4()
                            # Ask the user if they want to run the program again
                            run_again = input("Do you want to run task №1 again? (yes/no): ")
                            if run_again.lower() == 'yes':
                                print("Restarting the task")
                            if run_again.lower() == 'no':
                                print("Exiting task №4")
                                exitTask = True
                                main()
                            else:
                                while run_again.lower() != 'yes' and run_again.lower() != 'no':
                                    print("Input error! Repeat again:")
                                    run_again = input()
                        except ValueError:
                            print("An incorrect value has been entered. Please enter a numeric value.")
                        except Exception as e:
                            print(f"Error occurred: {e}")
                case "5":
                    while exitTask == False:
                        try:
                            print("Task №5 selected")
                            Task5()
                            # Ask the user if they want to run the program again
                            run_again = input("Do you want to run task №1 again? (yes/no): ")
                            if run_again.lower() == 'yes':
                                print("Restarting the task")
                            if run_again.lower() == 'no':
                                print("Exiting task №5  ")
                                exitTask = True
                                main()
                            else:
                                while run_again.lower() != 'yes' and run_again.lower() != 'no':
                                    print("Input error! Repeat again:")
                                    run_again = input()
                        except ValueError:
                            print("An incorrect value has been entered. Please enter a numeric value.")
                        except Exception as e:
                            print(f"Error occurred: {e}")
                case "6":
                    print("Program shutdown.")
                    exit()
                case _:
                    print("Invalid value entered, try again!")
                    main()

if __name__ == "__main__":
    main()
    