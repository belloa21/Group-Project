#Alex Bello
#Aly Batch
#Mike Suter

import random


prizes = ["a_new_car", "a_trip_to_the_bahamas", "a_banana", "$25,000", "a_years_supply_of_gummy_bears"]

trivia_questions = ["Do bears roar?", "Are all cats evil?", "Are cars faster than planes?", "Can chickens fly?", "Is Lichtman a good teacher?"]


def play_game():
    for question in trivia_questions:
        answer = input("Answer Y for yes or N for no. >>")
        if answer == 'Y' or 'y':
            print("Correct!! Here is your prize!")
            pick_prize()
        else:
            if answer == 'N' or 'n':
                print("Wrong answer, you suck at this!")
    pick = random.choice(trivia_questions)
    print(pick)


def pick_prize():
    print(random.choice(prizes))


play_game()
pick_prize()

