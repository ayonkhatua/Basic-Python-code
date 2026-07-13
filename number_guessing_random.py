import random

num = random.randint(1, 10)
user_input = ""
chances = 3  # Humne user ko 3 zindagi di

# Loop tab tak chalega jab tak guess galat hai AND zindagi bachi hai
while user_input != num and chances > 0:
    user_input = int(input(f"Enter a number (1-10) [Chances left: {chances}]: "))
    
    if user_input > num:
        print("Too High! Thoda chota number socho.")
        chances -= 1  # Ek chance kam ho gaya
    elif user_input < num:
        print("Too Low! Thoda bada number socho.")
        chances -= 1  # Ek chance kam ho gaya
    else:
        print("Congratulations, You won!")

# Loop ke bahar aane par check karo ki kya zindagi khatam ho gayi thi?
if chances == 0 and user_input != num:
    print(f"Game Over! Sahi number {num} tha.")