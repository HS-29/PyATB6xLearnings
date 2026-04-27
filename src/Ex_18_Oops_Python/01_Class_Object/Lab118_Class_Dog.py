class Dog:
    # A
    name = None
    breed = None
    height = None
    weight = None

    # B
    def bark(self):
        print("He is barking")
        print(self.name)
        print(self.breed)
        print(self.height)
        print(self.weight)

    def talk(self):
        print("I am talking")


print("Outside")
chow = Dog()

# Dog() - Object
# chow - Object Ref.



