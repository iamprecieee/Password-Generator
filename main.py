import random

#create the lists of keys
letter_key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol_key = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#get user input
print("Welcome to my Password Generator, Anon!\n")
letters = int(input("How many letters should your password have?\n")) 
numbers = int(input("How many numbers should your password have?\n"))
symbols = int(input("How many symbols should your password have?\n"))

#create a list for the password's characters
password_key = []
#loop through the keys and randomly select characters based on the user's preference for the length of each character type
for x in range(letters):
  password_key += random.choice(letter_key)

for x in range(symbols):
  password_key += random.choice(symbol_key)

for x in range(numbers):
  password_key += random.choice(number_key)

#shuffle the list's items
for x in range(letters + symbols + numbers):
  random.shuffle(password_key)

#convert the list to a string and generate an output 
password = "".join(password_key)
print(f"\nYour password is:\n{password}")