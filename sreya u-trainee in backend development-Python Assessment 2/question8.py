"""8. Write a Python program that takes a list of integers as input and returns a
new list with only the numbers that are prime."""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime_numbers(numbers):
    return [num for num in numbers if is_prime(num)]

user_input = input("Enter numbers separated by spaces: ")
input_numbers = list(map(int, user_input.split()))

prime_numbers = filter_prime_numbers(input_numbers)

print("Prime numbers:", prime_numbers)
