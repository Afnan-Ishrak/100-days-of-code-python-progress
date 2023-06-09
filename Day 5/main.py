#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P



# letterx = random.choice(letters)
# print(letterx)

sum = ""
# for x in range(0, nr_letters):
#     letterx = random.choice(letters)
#     numberx = random.choice(numbers)
#     symbolx = random.choice(symbols)
#     sum += numberx
#     sum += letterx
#     sum += symbolx

for x in range(0, nr_letters):
    letterx = random.choice(letters)
    sum += letterx
for x in range(0, nr_numbers):
    numberx = random.choice(numbers)
    sum += numberx
for x in range(0, nr_symbols):
    symbolx = random.choice(symbols)
    sum += symbolx
    
ltr = [x for x in sum]
random.shuffle(ltr)
print("".join(ltr))

