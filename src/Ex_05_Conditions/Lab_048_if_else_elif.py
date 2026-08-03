# To find the max b/w three numbers

num1 = int(input("Enter a 1st number\n:")) # 5, 10
num2 = int(input("Enter a 2nd number\n:")) # 3, 12
num3 = int(input("Enter a 3rd number\n:")) # 2, 10

if num1 >= num2 and num1 >= num3:
    print("Max, Num1")

elif num2 >= num1 and num2 >= num3:
    print("Max, Num2")

else:
    print("Max, Num3")