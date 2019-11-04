#Alex Bello
#Aly Batch
#Mike Suter

import random


prizes = ["a_new_car", "a_trip_to_the_bahamas", "a_banana", "$25,000", "a_years_supply_of_gummy_bears"]

trivia_questions = ["Do bears roar?n", "Are all cats evil?n", "Are cars faster than planes?n", "Can chickens fly?n", "Is Lichtman a good teacher?y"]


def play_game():
    list_pick = random.randint(1, 5)
    if list_pick == 1:
        question = trivia_questions[0]
        position = question.find('?')
        print(question[0:position+1])
        print(question[position+1:position:2])
    elif list_pick == 2:
        question = trivia_questions[1]
        position = question.find('?')
        print(question[0:position+1])
        print(question[position+1:position:2])
    elif list_pick == 3:
        question = trivia_questions[2]
        position = question.find('?')
        print(question[0:position+1])
        print(question[position+1:position:2])
    elif list_pick == 4:
        question = trivia_questions[3]
        position = question.find('?')
        print(question[0:position+1])
        print(question[position+1:position:2])
    elif list_pick == 5:
        question = trivia_questions[4]
        position = question.find('?')
        print(question[0:position+1])
        print(question[position+1:position:2])
    answer = input("Answer Y for yes or N for no. >>")
    if answer == 'Y' or 'y':
        print("Correct!! Here is your prize!")
        pick_prize()
    else:
        if answer == 'N' or 'n':
            print("Wrong answer, you suck at this!")


def pick_prize():
    print(random.choice(prizes))


play_game()
