class Person:
    # Attributes
    name = None
    age = None
    id = None
    email = None
    height = None
    gender = None
    phone = None
    address = None

    # Behavior
    def talk(self):
        print("I am talking")

    def speak(self, name):  # Arg with no return
        print("I am Method")
        print("speak", name)

    def sleep(self, name): # Arg with return
        print("I am Method")
        return None

    def walk(self):
        print("I am walking")

    def eat_return(self ):
        return "I am eating"

    # Create an object of the class
    # ObjectRef = ClassName() -> Object

    Harsh = Person()
    print(Harsh.name)
    Harsh.age = 20
    Harsh.sleep ("Kush")