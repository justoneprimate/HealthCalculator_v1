def bmi(weight, height):
    bmi_const = 703
    bmi_calc = (weight * bmi_const) / (height ** 2)
    return bmi_calc



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






