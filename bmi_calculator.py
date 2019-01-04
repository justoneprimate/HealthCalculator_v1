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