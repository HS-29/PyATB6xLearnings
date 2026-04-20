def add_security (func):
    def wrapper():
        print("1. Before the function is called")
        print("2. Add Helmet, Dashcam, Gloves, Knee Guards, Lisense")
        func()
        print("3. After the function is called")
        print("4. Secure Driving, Leave all items")
    return wrapper()



@add_security
def drive_ola_scooter():
    print("I am driving ola scooter")
#drive_ola_scooter(350)

@add_security
def drive_Uber_car():
    print("I am driving Uber car")