#1
def greet ():
    print("Hello!")
greet()
#greet()

print("----")

#2
def greet (name):
    print("Hi", name)
greet("Harsh Sharma")
#greet("Kush sharma")

print("----")

#3
def greet (a, b):
    print(a+b)
greet(a=1, b=2)
#greet(4,6)

print("----")

def greet_first_last_name (firstname, lastname):
    print("your full name is", firstname, lastname)
greet_first_last_name("Harsh", "Sharma")
#greet_first_last_name(firstname="Harsh", lastname="Sharma")

print("----")

def sign ():
    return 5
result = sign()
print(result)

print("----")

def add(a, b):
    return a + b
result = add(5, 6)
#result = add(a=7, b=8)
print(result)

print("----")

user_input = input("Please enter your name\n ")
#print("your name is",user_input)

def say_your_name (name):
    print("my name is", name)
#say_your_name('Harsh Sharma')
say_your_name(user_input)
