# This is the main file of program written on python, that realise uses of task function of lab 3.
# Each task function defined in a separate file. 
# The user can choose which task to run, and the program will execute it and display the results.
# Lab №3 "Base syntacses of Python "
# Program Version: 1.0
# Developer: Dubovik Arseny
# Development Date: 04.04.2024
import os

# Import the module where the calculate_series function is defined
from Task1 import task1
from Task2 import task2
from Task3 import task3
from Task4 import task4
from Task5 import task5

#Show functions and allows to choose function to use
def main():
    """
    The main function of the program. It prompts the user for input,
    calls the calculate_series function, and prints the results.
    """
    print("Enter the number of the task you want to complete:")
    print("1 - Task 1")
    print("2 - Task 2")
    print("3 - Task 3")
    print("4 - Task 4")
    print("5 - Task 5")
    print("6 - Exit")
    task = input()
    exitTask=False
    exitLab=False
    while exitLab==False:
            match task:
                case "1":
                    while exitTask==False:
                        try:
                            print("Task №1 selected")
                            task1()
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
                            task2()
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
                            task3()
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
                            task4()
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
                            task5()
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
                    exitLab = True
                case _:
                    print("Invalid value entered, try again!")
                    main()

if __name__ == "__main__":
    main()