
import random
import hangman_ascci
words_list = ['apple', 'banana','attitude', 'train','icecream','bike']

lives = 6

choosen_word = random.choice(words_list)
# print(display)

display = []

for i in range(len(choosen_word)):
    display += '_'
length = len(choosen_word)

for i in range(2):
    position = random.randint(0,length-1)
    display[position] = choosen_word[position]

print(f'{display}')
game_over = False
while not game_over:

    user_guess = input("Guess the word : ").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == user_guess:
            display[position] = user_guess
    print(f'\n{display}\n\n')
    if user_guess not in choosen_word:
        lives-=1
        if lives == 0:
            game_over = True
            print("You Loose...")
    if '_' not in display:
        game_over = True
        print("You Win ")
    print(hangman_ascci.HANGMANPICS[lives])