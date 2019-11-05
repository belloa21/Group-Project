#Alex Bello
#Aly Batch
#Mike Suter

import random # This is the code that imports the function of random, which lets us generate the questions and prizes at random.


prizes = ["a new car", "a trip to the bahamas", "a banana", "$25,000", "a years supply of gummy bears"] # These are the prizes the player can win put into a list

trivia_questions = ["Do bears roar?n", "Are all cats evil?n", "Are cars faster than planes?n", "Can chickens fly?n", "Is Lichtman a good teacher?y"]
# These are going to be our trivia questions. They have also been put into a list.

def play_game(): # This is the function that tells the code how to play the game. 
    #It will randomly select a question, wait for the player to repond. hen it will go through the scenarios based on whether the player answered yes or no and if that is correct or not.
    list_pick = random.randint(1, 5)
    correct_answer = ''
    if list_pick == 1:
        question = trivia_questions[0]
        position = question.find('?') # The position code looks to find the value in the answer that is needed to determine the next step and cycle through the questions.
        correct_answer = question[-1]
        print(question[0:position+1])
        print(question[position+1:position:2])
    elif list_pick == 2: # This is the code for what will run in question 2 if that question is randoomly selected. It is the same for question 1 all the way until question 5.
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
    answer = input("Answer Y for yes or N for no. >>") # This is the code that lets the user input their answer for yes or no.
    if answer.lower() == correct_answer: # This is the code that appears when the user gets the correct answer.
        print("Correct!! Here is your prize!")
        pick_prize()
    else:
        print("Wrong answer, you suck at this!") # This is the code that appears when the user gets the wrong answer.


def pick_prize(): # This function tells the game to randomly select a prize for the player of they win
    print(random.choice(prizes))


play_again = True
while play_again: # This code lets the player play again when they get an answer right or wrong.
    play_game()
    print("Do you want to play again?")
    if input() == 'n':
        break

