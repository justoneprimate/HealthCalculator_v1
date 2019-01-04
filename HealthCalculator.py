# Simple BMI, Max HR and Weight Loss Calculator to exercise topics covered in "The Basics of Python" module of
# Learn Python Programming Masterclass by Tim Buchalka on Udemy

# Here is the Mifflin-St. Jeor equation for both men and women:

# Men: Calories per day = 10x(weight in kg) + 6.25x(height in cm) – 5x(age) + 5
# Women: Calories per day = 10x(weight in kg) + 6.25x(height in cm) – 5x(age) – 161
# To calculate your TDEE, the answer from the Mifflin. St. Jeor equation is then multiplied by
# a number corresponding to your level of activity, known as an activity factor (2).

# There are five different levels of activity:

# Sedentary: x 1.2 (sedentary individuals who perform little to no exercise)
# Lightly active: x 1.375 (light exercise fewer than 3 days per week)
# Moderately active: x 1.55 (moderate exercise most days of the week)
# Very active: x 1.725 (hard exercise every day)
# Extra active: x 1.9 (strenuous exercise 2 or more times per day)

# lbs > kg = mass(lb) / 2.205
# In > cm = len(in) * 2.54

# example
# 10 * (325/2.205) + 6.25 * (70 X 2.54) - (5 * age) + 5
# (10 * 151.93)  + (6.25 * 177.8) - (5 * 46) + 5
# (1519.3) + (1111.25) - (230) + 5 = 2865.55 * Sedentary value of 1.2 = 3438.66 Calories to Maintain
# current weight
# it takes about a 500 cal defecit to lose 1 lb per week
# to lose the safely recommended 2lbs per week...that would mean you need to cut 1000 calories
# meaning your goal cal per day is 2438.66


# Get User's Information

age = int(input("Enter your age: "))
height = int(input("Enter your height in inches: "))
weight = int(input("Enter your weight in pounds: "))
goal_weight = int(input("Enter your goal weight: "))
gender = input("Are you M(male) or F(female): ")


print("=" * 40)

# Text conversions for gender field
gender_upper = gender.upper()
if gender_upper == 'M':
    gender_full = 'male'
else:
    gender_full = 'female'

# Calculate BMI using Weight in Lbs. x 703 / height (inches **2)

bmi_const = 703
bmi_calc = (weight * bmi_const) / (height ** 2)

# Return BMI Value to user

print("Your BMI is {0:1.2f}\n".format(float(bmi_calc)))

# Compare user BMI to healthy levels to determine estimated fitness level.

if bmi_calc <= 18.5:
    print("Your BMI indicates you are underweight for a {0} year old {1} of your height.\n"
          "You should seek medical advice on achieving a healthy weight.\n".format(age, gender_full))
if 18.6 <= bmi_calc <= 24.9:
    print("Your BMI is normal for a {0} year old {1} of your height and weight.\n"
          "An exercise program can help you maintain your health.".format(age, gender_full))
if 25 <= bmi_calc <= 29.9:
    print("Your BMI indicates you are overweight for a {0} year old {1} of your height and weight\n"
          "You should start a diet and exercise program. Before beginning any exercise program, please seek\n"
          "medical advice".format(age, gender_full))

if 30 <= bmi_calc <= 39.9:
    print("Your BMI indicates you are obese for a {0} year old {1} of your height and weight.\n"
          "You should start a diet and exercise program. Before beginning any exercise program, please seek\n"
          "medical advice".format(age, gender_full))
if bmi_calc >= 40:
    print("Your BMI indicates you are dangerously obese for a {0} year old {1} of your height and weight.\n"
          "You should start a diet and exercise program. Before beginning any exercise program, please seek\n"
          "medical advice".format(age, gender_full))

print('\n\n')

# Calculate Max Heart Rate using MHR = 207 - (age x .7)

hr_const = 207
hr_calc = hr_const - age * .7

# Return Max Heart Rate to user
print("Your Maximum Heart Rate is {0} bpm.\n".format(int(hr_calc)))

hr_fatburn = (hr_calc * .70)
print("Research indicates that you burn the most fat when exercising at\n70% of your max heart rate. "
      "Based on this calculation, your ideal\nheart rate for fat burning is {0} bpm.\n".format(round(hr_fatburn)))

# Calculate and return Weight Loss data to user

print('\n\n')

weight_delta = weight - goal_weight
weight_weeks = weight_delta // 2
weight_months = weight_weeks // 4
weight_years = weight_months / 12

if goal_weight > weight:
    print("You said you want to gain {0} pounds. \n".format(abs(weight_delta)))
elif weight > goal_weight:
    print("You said you want to lose {0} pounds. \n".format(weight_delta))
    print("Doctors agree weight loss between 1 and 2 pounds per week is safe.")
    print("To lose {0} pounds safely, it would take you {1} weeks.\n".format(weight_delta, weight_weeks))
    if weight_months < 1:
        print("In less than a month you could be at your ideal weight.")
    else:
        print("Think about it! In just {0} short months, you could have the body you want.\n".format(weight_months))
    if weight_years < 1:
        print("In less than a year, you could be at your ideal weight.")
    else:
        print("By working hard for {0:.2f} years, you could add many more healthy ones!".format(float(weight_years)))
else:
    print("Fantastic, you are are at your ideal weight!")
