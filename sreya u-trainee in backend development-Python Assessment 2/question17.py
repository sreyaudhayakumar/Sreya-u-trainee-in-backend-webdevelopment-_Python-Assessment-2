"""17. Python program to delay printing of line from a file using sleep function""" 

import time

def print_with_delay(file_path, delay):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
                time.sleep(delay)
    except FileNotFoundError:
        print("File not found.")

file_path = input("Enter the file path: ")
delay = float(input("Enter the delay between lines (in seconds): "))

print_with_delay(file_path, delay)
