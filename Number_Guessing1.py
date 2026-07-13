import random

num = random.randint(1, 10)
user_input = ""

while user_input != num:
    user_input = int(input("Enter a number (1-10): "))
    
    if user_input > num:
        print("Too High! Thoda chota number socho.")
    elif user_input < num:
        print("Too Low! Thoda bada number socho.")
    else:
        print("Congratulations, You won!")