"""4. Merge Multiple Text Files into One """

def merge_files(input_files, output_file):

    with open(output_file, 'w') as output:
        for input_file in input_files:
            with open(input_file, 'r') as file:
                output.write(file.read())


input_files = ["sreya u-trainee in backend development-Python Assessment 2/quest1.txt2", "sreya u-trainee in backend development-Python Assessment 2/quest1.txt2"]  
output_file = "merged_file.txt"

merge_files(input_files, output_file)
