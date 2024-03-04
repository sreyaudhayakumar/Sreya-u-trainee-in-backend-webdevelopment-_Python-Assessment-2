"""9. Write a Python function that takes a list of integers as input and returns a
new list with only the numbers that are perfect squares"""

def is_perfect_square(num):
    return num >= 0 and int(num**0.5)**2 == num

def filter_perfect_squares(numbers):
    return [num for num in numbers if is_perfect_square(num)]

user_input = input("Enter numbers separated by spaces: ")
input_numbers = list(map(int, user_input.split()))

perfect_squares = filter_perfect_squares(input_numbers)

print("Perfect squares:", perfect_squares)
