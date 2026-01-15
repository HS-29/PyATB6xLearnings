# Task for the today
# Take a 2 input from the user
# Print the Quotient and Reminder

# Logic Building Formula

# Step 1
# What is the input -> num1, num2
# What is the output -> Quotient and Reminder (Always ask from the interviewer, It will be int, float)
# Step 2 -> Rough Logic
# // -> Double slash always gives Quotient.
# / -> Single slash always gives float result.
# % -> Use to find reminder

num1 = int(input("Enter the 1st number"))
num2 = int(input("Enter the 2nd  number"))

Quotient = num1 // num2
print(Quotient)

Remainder = num1 % num2
print(Remainder)