"""10. Write a Python function that takes a list of numbers as input and returns
the sum of all the numbers divisible by 3 or 5."""

def sum_of_num(numbers):
    total_sum = 0
    for num in numbers:
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num
    return total_sum

user_input = input("Enter numbers separated by spaces: ")
input_numbers = list(map(int, user_input.split()))

result = sum_of_num(input_numbers)
print("Sum of numbers divisible by 3 or 5:", result)
