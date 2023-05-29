##Area Calculator

#Write your code below this line 👇

def paint_calc(height, width, cover):
    nr_of_pc = int((height*width)/cover) + ((height*width)%cover > 0)
    print(f"You will need atleast {nr_of_pc} paint cans.")





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


##Prime Numbers(FAILED HORRIBLY)

#Write your code below this line 👇
def prime_checker(number):
    prime = True
    for x in range(2, number):
        if number % x == 0:
            prime = False
    if prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

