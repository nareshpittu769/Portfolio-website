import random

alphabets_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers_list = [
    "1","2","3","4","5","6","7","8","9","0"
]

symbols_list = [
    '@','%','+','/','!','#','$','?','^','(',')','{','}','[',']','~'
]

print('Welcome to the password genarator....')
alphabets_number = int(input('Enter count of alphabets in password : '))
number_number = int(input('Enter count of numbers in password : '))
symbols_number = int(input('Enter the count of symbols in passord : '))

password_list = []

for char in range(0,alphabets_number):
    password_list+= random.choice(alphabets_list)

for number in range(0,number_number):
    password_list += random.choice(numbers_list)
for symbol in range(0,symbols_number):
    password_list += random.choice(symbols_list)

# print(password_list)
random.shuffle(password_list)
password = ''
for i in password_list:
    password+=i
print(password)