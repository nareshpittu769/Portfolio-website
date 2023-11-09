import random

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5
answer = random.randint(1,50)


def guessGame():

    def set_dificulty_level(level):
        lev = level.lower()
        if lev == 'easy':
            return EASY_DIFFICULTY
        elif lev == 'hard':
            return HARD_DIFFICULTY
        else:
            return 
        
    def check_answer(gussednumber,answer,attempts):
        if gussednumber<answer:
            print('Your guess is too low')
            return attempts-1
        elif gussednumber>answer:
            print('Your guess is too high')
            return attempts - 1
        else:
            print(f'Awsome you guess the answer.... The answer is {answer}')


    gussed_number = 0
    print('Think a number between 1 to 50')
    level = input("Choose a level of difficulty type 'easy' or 'Hard':")

    attempts = set_dificulty_level(level)
    while gussed_number!= answer:
        print(f'You have {attempts} attempts remaining to guess the number')
        gussed_number = int(input('Enter a number: '))
        attempts = check_answer(gussed_number,answer,attempts)
        
        if attempts == 0:
            print("You have reached the max attempts!")
            return
        elif gussed_number!=answer:
            print("Guess again..")
    
guessGame()