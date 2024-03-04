"""15. Copy odd lines of one file to another file in Python"""

def copy_odd_lines(input_file, output_file):
    with open(input_file, 'r') as file_in:
        with open(output_file, 'w') as file_out:
            lines = file_in.readlines()
            odd_lines = [lines[i] for i in range(len(lines)) if i % 2 == 0]
            file_out.writelines(odd_lines)

input_file = "input.txt"
output_file = "output.txt"
copy_odd_lines(input_file, output_file)  
