import calculator
import dictionary

# Get User's Information
print("Welcome to myHealth the all in one health calculator.\n"
      "Enter your personal details to get started!\n")

first_name = input("What is your first name?  ")

last_name = input("What is your last name?  ")

gender = input("Thank you, {} Are you M(male) or F(female): ".format(first_name))

# Text conversions for gender field
gender_upper = gender.upper()
if gender_upper == 'M':
    gender_full = 'Male'
else:
    gender_full = 'Female'

age = int(input("How old are you?  "))

height = int(input("How tall are you, in inches?(ex. 5\'10\" = 70)  "))

weight = int(input("How much do you weigh(lbs.)?  "))

goal_weight = int(input("Enter your goal weight:  "))

print(f"*" * 50 + "\n\n"
      f"Here is a summary of what you entered:\n"
      f"--------------------------------------\n"
      f"Name: {last_name}, {first_name}\n"
      f"Gender: {gender_full}\n"
      f"Height: {height} in.\n"
      f"Current Weight: {weight} lbs.\n\n"
      f"Goal: You would like to lose {weight - goal_weight} lbs.\n\n\n"
      f"Based on the information provided:\n"
      f"--------------------------------------\n"
      # Return BMI Value to user
      f"Your BMI is {float(calculator.bmi(weight, height)):.2f}\n"
      # Return Max Heart Rate to user
      f"Your Maximum Heart Rate is {int(calculator.hr(age))} bpm.\n"
      # Return optimal fat-burning heart rate
      f"Your Target Heart Rate for maximum fat-burn is {round(calculator.hr_fatburn(age))} bpm.\n")

print("----------------------------------------\n")
user_answer = (input("Would you like to learn more about these values, and what they mean? ").upper())
while True:
    if user_answer == 'N':
        print("Thank you for using myHealth")
        break
    else:
        info = input("What would you like to learn more about? Type the associated number\n"
                     "of your choice")
        weight_loss =

