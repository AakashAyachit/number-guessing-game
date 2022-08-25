#randomly selects a number from 1-10
#user has to guess the number, hints given using if,elif,else

import random
main_num = random.randint(1,10)
guess = int(input("Enter your guess(1-10): "))

while main_num != guess:

    if main_num > guess:
        print("Your guess is lesser than the number!")
        guess = int(input("Enter another number: "))

    elif main_num < guess:
        print("Your guess is larger than the number!")
        guess = int(input("Enter another number: "))

    else:
        break

print("You have guessed the correct number!!")

