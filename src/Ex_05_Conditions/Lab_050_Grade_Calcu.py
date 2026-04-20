# Grade Calculater
# Write a program that calculates and displays the letter grade
# For a given numerical score (e.g., A, B, C, D, or F)
# Based on the following grade scale

# A: 90 - 100
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: 00 - 59

# Logic building Formula

# 1.What is input --> score is in int form
# 2.What is output --> It is in str --> A, B

Score = int(input("Enter Score: ").strip())
if Score >= 0 and Score >= 100:
    print("Enter the valid score")
else:
    print("Let me check the score")

if Score >100 or Score <= -1:
    print("You are superman!! you can't get a grade")
else:
    if Score>= 90 and Score <= 100:
        print("your grade is A")

    elif Score >= 80 and Score <= 89:
        print("your grade is B")

    elif Score >= 70 and Score <= 79:
        print("your grade is C")

    elif Score >= 60 and Score <= 69:
        print("your grade is D")

    else:
        print("your grade is F")
