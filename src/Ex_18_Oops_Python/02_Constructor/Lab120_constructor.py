print("outside the class")

class MobilePhone:
    model = None

    def __init__(self):
        print("DC")

    def talk(self):
        print("Hi, talking")

Android = MobilePhone()
Android.talk()


print("outside the class2")