"""16. Count the total number of uppercase characters in a file in Python"""

def count_and_get_uppercase_characters(file_path):
    uppercase_chars = []
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char.isupper():
                    count += 1
                    uppercase_chars.append(char)
    return count, uppercase_chars

file_path = "sreya u-trainee in backend development-Python Assessment 2/ques16.txt"
uppercase_count, uppercase_chars = count_and_get_uppercase_characters(file_path)
print("Total number of uppercase characters:", uppercase_count)
print("Uppercase characters found:", ''.join(uppercase_chars))
