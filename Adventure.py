#Alex Bello
#Aly Batch
#Mike Suter

import random


prizes = ["a new car", "a trip to the bahamas", "a banana", "$25,000", "a years supply of gummy bears"]

trivia_questions = ["Do bears roar?n", "Are all cats evil?n", "Are cars faster than planes?n", "Can chickens fly?n", "Is Lichtman a good teacher?y"]


def play_game():
    list_pick = random.randint(1, 5)
    correct_answer = ''
    if list_pick == 1:
        question = trivia_questions[0]
        position = question.find('?')
        correct_answer = question[-1]
        print(question[0:position+1])
        print(question[position+1:position:2])
    elif list_pick == 2:
        question = trivia_questions[1]
        position = question.find('?')
        correct_answer = question[-1]
        print(question[0:position+1])
        print(question[position+1:position:2])
    elif list_pick == 3:
        question = trivia_questions[2]
        position = question.find('?')
        correct_answer = question[-1]
        print(question[0:position+1])
        print(question[position+1:position:2])
    elif list_pick == 4:
        question = trivia_questions[3]
        position = question.find('?')
        correct_answer = question[-1]
        print(question[0:position+1])
        print(question[position+1:position:2])
    elif list_pick == 5:
        question = trivia_questions[4]
        position = question.find('?')
        correct_answer = question[-1]
        print(question[0:position+1])
        print(question[position+1:position:2])
    answer = input("Answer Y for yes or N for no. >>")
    if answer.lower() == correct_answer:
        print("Correct!! Here is your prize!")
        pick_prize()
    else:
        print("Wrong answer, you suck at this!")


def pick_prize():
    print(random.choice(prizes))


play_again = True
while play_again:
    play_game()
    print("Do you want to play again?")
    if input() == 'n':
        break

