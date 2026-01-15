# Task for the today
# Take a 3 input from the user
# Perform the sum, sum, mul and div

# Logic Building Formula

# Step 1
# What is the input -> num1, num2, num3 -> int
# What is the output -> sum, sub, multiplication, division (Always ask from the interviewer, It will be int, float)
# Step 2 -> Rough Logic

num1 = float(input("Enter the 1st number"))
num2 = float(input("Enter the 2nd number"))
num3 = float(input("Enter teh 3rd number"))

#Performing Operation
#print(num1 + num2 + num3)
Sum_Result = (num1 + num2 + num3)# Sub 2nd number from 1st
print(Sum_Result)

#print(num1 - num2 - num3)
Sub_Result = (num1 - num2 - num3) # Sub 3rd from 2nd
print(Sub_Result)

#print(num1 * num2 * num3)
Mul_Result = (num1 * num2 * num3) # Mul all three number
print(Mul_Result)

#print(num1 / num2 / num3)
Div_Result = (num1 / num2 ) / num3 # Div all three number
print(Div_Result)
