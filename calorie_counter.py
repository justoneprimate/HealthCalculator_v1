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