"""7. Write a function that takes a list of numbers as input and returns the
second-largest number."""

def second_largest(numbers):
    sorted_nums = sorted(numbers)
    if len(sorted_nums) < 2:
        return "List should contain at least two numbers"
    return sorted_nums[-2]

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

result = second_largest(numbers)
print("Second largest number is:", result)