print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill?\n$"))
people_no = float(input("How many people to split the bill?\n"))
percentage_tip = float(input("What percentage top would you like to give? 10, 12 or 15?\n"))
total_bill_with_tip = ((percentage_tip*0.01)+1)*total_bill
total_split = total_bill_with_tip/people_no

print("*"*30)
print("Each person should pay: ${:.2f}".format(total_split))