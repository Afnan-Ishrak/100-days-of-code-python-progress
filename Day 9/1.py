# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
#     }


#Retrieveing items from dictionary
# print(programming_dictionary["Loop"])

#Adding new items to dictionary.
# programming_dictionary["Reloop"] = "The action of doing something over and over again.... again."
# # print(programming_dictionary)

# #Create an empty dictionary.
# empty_dictionary = {}

# #Wipe an existing dictionary.
# programming_dictionary = {}

#Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

######################################################################

###Grading Program

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TO DO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TO DO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     if student_scores[student] >= 91:
#         student_grades[student] = "Outstanding"
#     elif 81 <= student_scores[student] < 91:
#         student_grades[student] = "Exceeds Expectations"
#     elif 71 <= student_scores[student] < 80:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Failed"

    

# # 🚨 Don't change the code below 👇
# print(student_grades)

######################################################################

# #Nesting 
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# #Nesting a List in a Dictionary

# travel_log = {
#     "France": {"cities visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 6}
# }

# #Nesting Dictionary in a List

# travel_log = {
#     {
#         "country": "France", 
#         "cities visited": ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12
#     },
#     {   
#         "country": "Germany", 
#         "cities visited":["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visits": 6
#     },
# }

#########################################################################

##Dictionary in List

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TO DO: Write the function that will allow new countries
#to be added to the travel_log. 👇

# travel_log.append({"country": "Russia"})
# print(travel_log)

def add_new_country(country, visits_num, places_visited):
    new_log = {"country": country,
           "visits": visits_num,
           "cities": places_visited}
    travel_log.append(new_log)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

