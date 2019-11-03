#Alex Bello
#Aly Batch
#Mike Suter

import random


prizes = ["a_new_car", "a_trip_to_the_bahamas", "a_banana", "$25,000", "a_years_supply_of_gummy_bears"]

trivia_questions = ["", "", "", "4", "5"]


def play_game():
    pick = random.choice(trivia_questions)
    print(pick)


def pick_prize():
    print(random.choice(prizes))


play_game()
pick_prize()

