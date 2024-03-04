"""6. Write a Python function that takes a list of strings as input and returns a
new list with the strings sorted in descending order of their lengths."""

def string_sorted(strings):
    sorted_string = sorted(strings, key=len, reverse=True)
    return sorted_string

strings = ['apple', 'orange', 'guvi', 'kiwi']
sorted_string = string_sorted(strings)
print(sorted_string)
