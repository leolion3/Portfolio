a = 10
print(type(a)) # int
a = 's'
print(type(a)) # string
a = [1,2,3]
print(type(a)) # list
a = b'hello world'
print(type(a)) # bytes


a = 11.5
print(type(a)) # float
a = int(a)
print(type(a)) # int


text = input('Give me your name: ')
print(f'Hello {text}!')


def sum(a,b):
	return a + b
print(sum(1,2))


a = [0, 1, 2]
for element in a:
	if not element:
		pass
	print(element)

for element in a:
	if not element:
		continue
	print(element)


import requests

r = requests.get('https://www.google.com')
print(r.status_code)