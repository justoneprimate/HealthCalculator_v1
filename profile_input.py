# Get User's Information

print("Welcome to myHealth the all in one health calculator."
      "Enter your personal details to get started!")
first_name = input("Please enter your first name: ")
last_name = input("What is your last name?")
age = int(input("Enter your age: "))
height = int(input("Enter your height in inches: "))
weight = int(input("Enter your weight in pounds: "))
goal_weight = int(input("Enter your goal weight: "))
gender = input("Are you M(male) or F(female): ")

# Text conversions for gender field
gender_upper = gender.upper()
if gender_upper == 'M':
    gender_full = 'male'
else:
    gender_full = 'female'