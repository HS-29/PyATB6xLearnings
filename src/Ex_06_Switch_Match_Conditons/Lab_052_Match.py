user_statement = "Enter the which test you want to run"
print(user_statement)
test_type = input("Enter your test type: API, UI, Performance, security")
match test_type:
    case "API":
        print("we are running a POSTMAN API test case")
    case "UI":
        print("we are running a SELENIUM test case")
    case "Performance":
        print("we are running a PERFORMANCE test case")
    case "Security":
        print("we are running a SECURITY test case")
    case _:
        print("invalid input")