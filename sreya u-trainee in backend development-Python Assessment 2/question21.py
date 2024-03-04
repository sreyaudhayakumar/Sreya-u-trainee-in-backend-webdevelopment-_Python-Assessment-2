"""21.Write a Python program that executes an operation on a list and handles an
IndexError exception if the index is out of range"""

def perform_operation_on_list(my_list, index, operation):
    try:
        result = operation(my_list[index])
        print("Result:", result)
    except IndexError:
        print("Index is out of range. Please provide a valid index.")

def add_10(x):
    return x + 10

my_list = [1, 2, 3, 4, 5]

index = int(input("Enter the index to perform operation on: "))
perform_operation_on_list(my_list, index, add_10)
