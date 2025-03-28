number = 5
user_input = 0

while user_input != number:
    user_input = int(input("Please enter number: "))

    if user_input == number:
        print("You Won")
    else:
        print("Try again")