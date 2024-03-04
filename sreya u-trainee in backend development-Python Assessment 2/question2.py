"""2. Count the Number of Lines, Words, and Characters in a Text File"""

def count_line_words_char(file):
    with open(file, 'r') as file_name:
        lines = file_name.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)

    print("Number of lines:", line_count)
    print("Number of words:", word_count)
    print("Number of characters:", char_count)

    with open(file, 'r') as file_name:
        content = file_name.read()
        print("Content of the file:")
        print(content)

file = "sreya u-trainee in backend development-Python Assessment 2/ques2.txt"

count_line_words_char(file)
