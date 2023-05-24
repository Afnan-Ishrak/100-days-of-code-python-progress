# number = int(input("Which number do you want to check?"))

# if number == 0:
#     print("Do not input 0, dummy!")
# elif number%2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

##BMI Calculator

# height = float(input("enter your height in m:"))
# weight = float(input("enter your weight in kg:"))

# bmi = weight/(height*height)

# if bmi < 18.5:
#     print(f"Your bmi is {bmi}. You are underweight")
# elif 18.5 <= bmi < 25:
#     print(f"Your bmi is {bmi}. You have normal weight.")
# elif 25 <= bmi < 30:
#     print(f"Your bmi is {bmi}. You are overweight.")
# elif 30 <= bmi < 35:
#     print(f"Your bmi is {bmi}. You are obese.")
# else:
#     print(f"Your bmi is {bmi}. You are clinically obese")


#Leap Year Checker

# year = int(input("Which year do you want to check?:\n"))

# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 ==0:
#             print("It is a leap year!")
#         else:
#             print("It is not a leap year")
#     else:
#         print("It is a leap year!")
# else:
#     print("It is not a leap year.")

#Pizza Order Bill Calculator

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L?\n").lower()
# add_pepperoni = input("Do you want pepperoni?Y or N\n").lower()
# extra_cheese = input("Do you want extra cheese?Y or N\n").lower()

# if size == "s":
#     bill = 15
#     if add_pepperoni == "y":
#         bill +=2
# elif size == "m":
#     bill = 20
#     if add_pepperoni == "y":
#         bill +=3
# else:
#     bill = 25
#     if add_pepperoni == "y":
#         bill +=3
# if extra_cheese == "y":
#     bill +=1

# print(f"Your Total bill is: ${bill}")

##Love Calculator

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name?\n").lower()
# name2 = input("What is their name?\n").lower()

# t = str(name1+name2).count("t")
# r = str(name1+name2).count("r")
# u = str(name1+name2).count("u")
# e = str(name1+name2).count("e")
# v = str(name1+name2).count("v")
# o = str(name1+name2).count("o")
# l = str(name1+name2).count("l")

# first_number = t+r+u+e
# second_number = l+o+v+e
# love_number = int(str(first_number)+str(second_number))

# print("*"*30)
# print(" ")

# if love_number <=10 or love_number >= 90:
#     print(f"Your score is {love_number}, you go together like coke and mentos.")
# elif love_number >=40 and love_number <=50:
#     print(f"Your score is {love_number}, you are alright together.")
# else:
#     print(f"Your score is {love_number}")