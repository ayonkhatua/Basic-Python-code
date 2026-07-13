num = 8
user_input = ""

while user_input != num:
    user_input = int(input("Enter a number (1-10): "))
    if user_input != num:
        print("Wrong, Please try again: ", user_input)
    else:
        print("Congratulations, You are won")
