output = ""


def convert(inp_base,out_base,number):
    global output
    value = 0    
    if inp_base != '10':
        index = len(number)-1
        indexValue = 1
        while index >= 0:
            value = value + int(number[index])*indexValue
            indexValue = indexValue * int(inp_base)
            index -= 1
    else:
        value = int(number)
    while value != 0:
        output += str(value % int(out_base))
        value /= (int(out_base))
        value = (int(value))
    print("\nConverted: "+output[::-1]+"\n")


def setup():
    number = input("\nEnter Number: ")
    input_base = input("Enter input base: ")
    output_base = input("Convert to base: ")
    convert(input_base,output_base,number)


setup()