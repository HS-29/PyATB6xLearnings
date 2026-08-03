# Find the positive no. is even or odd

num = int(input("Enter a number\n:"))

if num >= 0:
    if num % 2 == 0:
        print("Even")

    else:
        print("Odd")

else:
    print("Negative number")