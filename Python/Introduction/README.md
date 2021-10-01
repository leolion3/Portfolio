# Getting Started with Python

## Installing Python

### Windows

- Go to

```
https://www.python.org/
```

- Hover over the "Downloads" button and click on "Python 3.x.x"
- Run the executeable and go through the installation wizard

## Adding Python to PATH

*If python wasn't automatically added*

- Navigate to "C:\Python39" if you chose "Install for All Users" or to "C:\Users\Your-Username\AppData\Local\Programs\Python\Python3x\" if you chose "Install only for Current User"
- Copy the current file path
- Go to "This PC", right click on the empty space and select "Properties"
- Click on "Advanced system settings"
- Open the "Advanced" tab (if it didn't automatically open) and click on "Environment Variables..." at the bottom
- Under the second section "System Variables", scroll down until you find a Variable named "Path". Click on it and then click the "Edit" button.
- Click on "New" and paste in the file path you copied earlier
- Ok/apply and exit out of everything

To check if you correctly defined the Python system variable, fire up your favourite terminal and type the command 

```bash
python --version
```

If you correctly defined the variable, you should get a prompt with your Python version, for instance:

```bash
#> python --version
Python 3.9.5
```

### Linux

Fire up a terminal and type in

```bash
sudo apt update && sudo apt install python3 python3-pip -y
```

To check if Python got installed correctly, type in the command

```bash
python3 --version
```

If you correctly defined the variable, you should get a prompt with your Python version, for instance:

```bash
#> python3 --version
Python 3.9.5
```

## Comments

In Python, single line comments can be added using *#*. Multi-line comments are added using triple quotation marks '"""'. Example:

```python
# This is a single-line comment
"""
This is a
multi-line
comment
"""
```

## Data Types

Python has the following data types:

- Text: Strings (consists of a list of characters, each of which is also a string on its own. Strings can be defined either with single, or with double quotes)
- Numeric types: int, float, complex
- Sequence types: list (defined using [ ]), tuples and range
- Mapping types: dictionary (defined using { })
- Set types: set, frozenset
- Booleans: bool (True/False, first letter uppercase)
- Binary types: bytes, bytearray, memoryview

Unlike other programming languages (Java/C/etc.) the type keyword of a variable does not need to be provided, and the type of a variable can change dynamically throughout a program. Example:

```python
a = 10
print(type(a)) # int
a = 's'
print(type(a)) # string
a = [1,2,3]
print(type(a)) # list
a = b'hello world'
print(type(a)) # bytes
```

Type casting can be done using the corresponding method call:

```python
a = 11.5
print(type(a)) # float
a = int(a)
print(type(a)) # int
```

## Input/Output

Python offers its own input/output engine using the *input* and *print* methods. The *input* method takes in a string that is displayed before the user's input. The print method takes in a string and prints it to the screen. (Note: special characters like backslash and single ticks will be printed as escaped out characters, e.g. "\'" instead of "'")  

Example program to get a user's name. Note the usage of 'f' before the string's quotation marks, this is used to format the string and can also be done similarily to C with '%s' (e.g. ```print('Hello %s' % (variable_name))```):

```python
text = input('Give me your name: ')
print(f'Hello {text}!')
```

Will yield the output:

```bash
#> python input_output.py
Give me your name: Test
Hello Test!
#> 
```

## Indentation

Unlike programming languages like Java and C, python does not use curly brackets for indentation. Instead it uses a uniform amount of spaces or tabs. These need to be uniformally used throughout the program (E.g. you can't use tabs at one location and spaces at another and you can't change the amount of tabs/spaces used for indentation throughout the program).

Method definitions, loops and conditionals use ':' before an indented block. The following example demonstrates this.

Java code:

```java
void someMethod(){
	// Your code
}
```

Equivalent python code:

```python
def some_method():
	# Your code
``` 

## Main Method

Although not necessarily required (except in a dozen scenarios, but you should know that simple scripts can be written without a main method) the "main" method in python is defined using:

```python
if __name__ == '__main__':
	# Your code
```

## Methods

Methods in python are defined using the *def* keyword. The below code gives an example of a method that takes in two variables and gives the sum of them:

```python
def sum(a,b):
	return a + b
```

Methods can have a return type (which can also be dynamic! Pay close attention to your variable types!) or have none (You may also use the *return* keyword without a provided value).

## Conditionals

Python uses the keywords *if*, *elif* and *else* for conditionals. The *elif* is a keyword for an *else if* scenario. Example:

```python
if something:
	# Do something
elif something_else:
	# Do something else
else: 
	# Whatever
```

## Loops

Python uses *for* and *while* loops. The special thing is that a while loop allows an *else* statement at the end of it to execute some code when the loop conditional becomes false. Example:

```python
# A simple counting loop
for _ in range(10): # _ is a wildcard, range(n) creates a list containing the elements k..n-1. 
# Additional paramters define k and the stepping per iteration. By default k=0 and step=1.
	# Do something

# A simple while loop
while something:
	# Do something
else:
	# Executed when something == False
```

Loops also include the *pass*, *break* and *continue* keywords. The latter two of which work just like in any other prgramming language. 
pass however, works differently. pass and continue do completely different things. pass simply does nothing, while continue goes on with the next loop iteration.

The following example demonstrates this:

```python
a = [0, 1, 2]
for element in a:
	if not element:
		pass
	print(element)

for element in a:
	if not element:
		continue
	print(element)
```

The outputs respectively:

```python
0
1
2

1
2
```

Source: https://stackoverflow.com/a/9484008/13399409

## Importing modules

Modules/Libraries may be imported using the *import* keyword. Example:

```python
import requests

r = requests.get('https://www.google.com')
print(r.status_code) # returns http status code, 200 - OK, 404 - Not Found, etc.
```

To run the abovementioned code snippet, the library *requests* must be installed using pip:

**Windows**:

```bash
pip install requests
```

**Linux**:

```bash
pip3 install requests
```

To install requirements out of a file (most repos come with a *requirements.txt* file), use the command:

```bash
pip install -r requirements.txt
```