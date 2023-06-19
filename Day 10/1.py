#FUnctions with Outputs

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"{formated_f_name} {formated_l_name}"

# formated_string = format_name("afnan", "aFnAn")
# print(formated_string)

#######################################################################

#Days in Month

def is_leap(year):
  leap_year = False
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        leap_year = True
        return leap_year
      else:
        return leap_year
    else:
      leap_year = True
      return leap_year
  else:
    return leap_year
  
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year):
    month_days[1] = 29 
  month_picked = month_days[month-1]
  return year, month_picked
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
