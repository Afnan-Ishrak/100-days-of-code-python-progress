##Average Student Height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# sumstudent = sum(student_heights)
# print(sumstudent)

# print(sumstudent/len(student_heights))

total_height = 0 
for student in student_heights:
    total_height += student

no_of_students = 0
for student in student_heights:
    no_of_students += 1

print("This is the average height of the students:\n")
print(round(total_height/no_of_students))

##HighScore

student_scores = input("Input a list of student scores: \n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for student in student_scores:
    if student>highest_score:
        highest_score = student
print(f"The highest score in the class is : {highest_score}")


## Addition of all even numbers from 0-100

sum=0
for x in range(0,101,2):
    sum += x
    print(sum)

##FizzBuzz

total = 0
for x in range(1,101):
    if x%15==0:
        print("FizzBuzz")
    elif x%5==0:
      print("Buzz")
    elif x%3==0:
      print("Fizz")
    else:
      print(x)