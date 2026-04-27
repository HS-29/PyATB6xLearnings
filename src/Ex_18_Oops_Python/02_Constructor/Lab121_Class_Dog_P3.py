class Dog:
    # Attributes - Instance variable | Data variable
    name = None
    breed = None
    height = None
    weight = None
    run = None

    def __init__(self, nameGiven, breedGiven):
        print("PC")
        self.name = nameGiven
        self.breed = breedGiven

    # B
    def bark(self):
        print("Barking")

    def sleep(self):
        print("who is sleep ->", self.name)

    def talk(self):
        print("Who is talking ->", self.name)


chow = Dog("chow", "mistiff")
rancho = Dog("rancho", "desi")

chow.sleep()
rancho.talk()

rancho.sleep()
chow.talk()


