#exercise 20
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Be kind and rewind when you're done!")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = 2
print_a_line(current_line, current_file)

current_line = 3
print_a_line(current_line, current_file)
