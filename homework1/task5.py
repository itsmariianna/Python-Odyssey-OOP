# Write a generator function read_file_lines(file_path) that reads a file line by line and yields each line. Use this generator to print each line of a file without loading the entire file into memory.

def read_file_lines(file_path):

    file = open('my_file', 'r')
    for line in file:
        yield line

result = read_file_lines('my_file')

for i in result:
    print(i)
