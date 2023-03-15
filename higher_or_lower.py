from random import randrange
random_number = randrange(10)
check = False
while check==False:
    user_input = int(input("Please enter your number from 1 to 10:"))
    if user_input==random_number:
        check = True
        print("Good job")
    elif user_input<random_number:
        print("Your number is too small")
    else:
        print("Your number is too big")