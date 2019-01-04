import calculator

# Get User's Information
print("Welcome to myHealth the all in one health calculator."
      "Enter your personal details to get started!")
first_name = input("What is your first name?  ")
last_name = input("What is your last name?  ")
gender = input("Thank you, {} Are you M(male) or F(female): ".format(first_name))
gender_upper = gender.upper()
if gender_upper == 'M':
    gender_full = 'Male'
else:
    gender_full = 'Female'
age = int(input("How old are you?  "))
height = int(input("How tall are you, in inches?(ex. 5\'10\" = 70)  "))
weight = int(input("How much do you weigh(lbs.)?  "))
goal_weight = int(input("Enter your goal weight:  "))
print('*' * 50)
print("Here is a summary of what you entered:")
print('-' * 50)
print("Name: " + last_name + ", " + first_name)
print("Gender: {} ".format(gender_full))
print("Height: {} in. ".format(height))
print("Current Weight: {}lbs.".format(weight))
print("You would like to lose {} lbs.".format(weight - goal_weight))
print('-' * 50 + '\n')
print("Based on the information provided:")
print('-' * 50)
# Return BMI Value to user
# print("Your BMI is {0:1.2f}\n".format(float(calculator.bmi)))
print(calculator.bmi)









# Text conversions for gender field



