# Write a python program to calculate the
# area of a circle given its radius using formula
# area = pi * r^2 (Take pi is 3.14)
# input -> Radius of circle-> float
# output -> string formatted output the area

# Logic Building Formula
# Step -> 1
# Figure out the input and output
# input -> Radius -> float (data type)
#pi = 3.14
# power -> pow or ** -> Any we can use
# Output -> String -> float -> area, print area
# Step -> 2
# Area = pi * (radius**2)
# Rough Logic -> area = 3.14 * pow(r, 2) or area = 3.14 * (r ** 2)

pi = 3.14
radius_of_circle = float(input("Enter radius of the circle"))
print(radius_of_circle)

# area = 3.1487654 * pow(radius_of_circle, 2)
area = pi * (radius_of_circle ** 2)
print("Area of the circle is", area)

# String data formating, Python f-String
print(f"Area of the circle is, {area: .2f}")
