import random

hangman_objects = []
object_file = open('HangmanObjects.txt')
text = object_file.read()

new_word = ''
for word in text:
    if word != '\n':
        new_word = new_word + word
    if word == '\n':
        hangman_objects.append(new_word)
        new_word = ''

answer = hangman_objects[random.randint(0, len(hangman_objects) - 1)]

alive = True
guessed = False
lives = 5
game_space = []
letters_guessed = 0

for letter in answer:
    game_space.append('__  ')

while alive and not guessed:
    #Game will run in this loop:
    print('\n\n' + ''.join(game_space))
    print('You have ' + str(lives) + ' lives remaining.')
    guess = str(input('Enter a guess: '))
    for i in range(len(answer)):
        if guess.lower() == answer[i]:
            game_space[i] = guess.upper() + '   '
            letters_guessed += 1
    if guess not in answer:
        lives -= 1
        print(guess + ' is not in answer. Guess again!')
    if lives == 0:
        alive = False
        print('\n\nYou have 0 guesses remaining. The answer was: ' + answer.upper())
    if letters_guessed == len(answer):
        print('\n\n' + ''.join(game_space))
        print('\n\nCongrats, you guessed correctly!')
        guessed = True
    



object_file.close()

