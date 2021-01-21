print("\nPlease enter the matrix rows as entire strings, seperated by commans!\n")
print("Example:\nInput: abc,def,ghi => for:\n [['a','b','c']\n ['d','e','f']\n ['g','h','i']]")
matrix = input("\n#> ").split(',')
word = input("Word to search for: ")          
print()


# Get a row from the matrix
def row(matrix, index_y):
    return matrix[index_y]


# Get a column from the matrix
# matrix - the matrix to extract a column from
# index_y - the first dimensional index
# index_x - the second dimensional index at which to start column extraction
# col - the column content
def column(matrix, index_y, index_x, col):
    if index_y >= len(matrix):
        return col
    col += matrix[index_y][index_x]
    return column(matrix, index_y+1, index_x, col)    
    
    
# Find a word in the matrix recursively
# matrix - the matrix to search through
# index_y - the first dimensional index
# index_x - the second dimensional index
def find_word(matrix,index_y,index_x,word):
    # Empty matrix check
    if len(matrix) < 1 or len(matrix[0]) < 1:
        print("not found\n")
        exit()
    # Empty word check
    if len(word) < 1:
        print("not found\n")
        exit()
    # Check if enough cells remaining in matrix
    if len(matrix) - index_y < len(word) - 1 and len(matrix[index_x]) - index_x < len(word) - 1:
        print("not found\n")
        exit()
    # Check downwards
    if len(matrix) - index_y >= len(word):
        col = column(matrix,index_y,index_x,"")
        if word in col and len(col) > 0 and col[0] == word[0]:
            print("(down,%s,%s,%s)\n" % (str(index_x),str(index_y),str(index_y+len(word))))
            exit()
    # Check across
    if len(matrix[index_y]) - index_x >= len(word):
        c_row = row(matrix, index_y)
        if word in c_row and len(c_row)>0 and c_row[0] == word[0]:
            print("(across,%s,%s,%s)\n" % (str(index_y),str(index_x),str(index_x+len(word))))
            exit()
    # Traverse matrix
    # Matrix traversed
    if index_x >= len(matrix[0]) and index_y >= len(matrix):
        print("not found\n")
        exit()
    # Change to next row
    elif index_x >= len(matrix[index_y])-1:
        index_x = 0
        index_y += 1
    # Change to next column
    else:
        index_x += 1
    find_word(matrix,index_y,index_x,word)


if __name__ == '__main__':
    find_word(matrix,0,0,word)