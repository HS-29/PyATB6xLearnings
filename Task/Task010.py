# Program to check page load time

load_time = float(input("Enter page load time (seconds): "))

if load_time <= 3:
    print("Page loaded within acceptable time", load_time, "seconds")

else:
    print("Page load too slow", load_time, "seconds")
