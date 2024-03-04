"""3. Search for a String in a Text File"""

def search_string(file_name, string_search):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        line_num = 1
        for line in lines:
            if string_search in line:
                print(f"Found '{string_search}' in line {line_num}: {line.strip()}")
            line_num += 1  

file_name = "sreya u-trainee in backend development-Python Assessment 2/ques3.txt"
string_search = input("Enter the string you want to search: ")

search_string(file_name, string_search)
