import sys

if len(sys.argv) < 2:
    print("No file specified!")
    exit()

with open(sys.argv[1], 'r') as f:
    file_data = f.read()

file_data = file_data.replace('\n','')
print(file_data)
