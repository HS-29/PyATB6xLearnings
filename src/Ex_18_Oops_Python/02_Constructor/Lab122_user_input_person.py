class Person:
    name = None
    age = None
    phone = None
    occupation = None

    def __init__(self):
        print("Lets take a user input, Please share the user name, age, phone number, occupation")
        self.name = input("Please enter your name\n: ")
        self.age = input("Please enter your age\n: ")
        self.phone = input("Please enter your phone number\n: ")
        self.occupation = input("Please enter your occupation\n: ")

        def display_values(self):
            print("name is " + self.name, "age is " + self.age, "phone number is " + self.phone, "occupation is " + self.occupation)



harsh = Person()
harsh. display_values(Person)