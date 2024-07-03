import random
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '.', '/', '<', '>', '?', '~', '`'
]
print("Welcome to password generator designed by Amodh Nepal")
nr_letters=input("How many letters do you want in your password?\n")
nr_numbers=input("HOw many numbers do you want in  your password?\n")
nr_symbols= input("How many symbols do you want in your password?\n")

# Easy level
# password=""
# for char in range(1,nr_letters+1):
#     password+= random.choice(letters)
# for char in range(1,nr_symbols+1):
#     password+= random.choice(symbols)
# for char in range(1,nr_numbers+1):
#     password+= random.choice(numbers)

# print(password)

# Hard Level
password_list= []
for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols+1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers+1):
    password_list += random.choice(numbers)
print(password_list)
random.shuffle(password_list)
print(password_list)
for char in password_list:
    password +=char
print(f"Your password is : {password}")