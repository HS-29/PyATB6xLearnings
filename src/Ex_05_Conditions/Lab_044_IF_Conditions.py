# Write a program to take a user age and
# let him know IF can go the club
# 21

age = int(input("Enter your age\n:"))

if (age <=0 or age > 100):
    print("Enter the valid age")

else:
    if age >= 21:
        print("Yes,You can go to club")

    else:
        print("No,You can not go to club")