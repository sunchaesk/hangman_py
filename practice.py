import sys
import random

word_list = ['hello', 'water', 'italy', 'coronavirus', 'toronto','default']
def create_word():
  word = random.choice(word_list)
  return word

def restart_prompt(word):
    print(word)
    restart = input('Do you want to play again? (Y/N) *If the input is neither of Y | N, it will by default restart: ').upper()
    if restart == 'N':
       print('Thanks for playing my hangman game!')
       sys.exit()
    else:
        main()


def main():
    word = create_word().upper() 
    guess_chance = 10
    guessed = set() 
    word_unsolved = list('_' * len(word))

    while guess_chance > 0:
        print(','.join(word_unsolved) + ' Length of the word: ' + str(len(word)))
        guess = input('Enter a character || a word to guess: ')
        if not guess.isalpha():
            print('WARNING: The input has to be alpha!')
            continue
        guess = guess.upper()

        if guess in guessed :
            print("You've already guessed this! Guessed:"   + ','.join(guessed))
            continue
        else:
           guessed.add(guess)

        if len(guess) == 1:
            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        word_unsolved[i] = guess
            else:
               print('Sorry Pfft...Incorrect!') 
               guess_chance -= 1
        elif len(guess) == len(word):
            if guess == word:
                print('Wow! You got it! Congrats!')
                restart_prompt(word)
            else:
                guess_chance -= 1
        else:
            print('WARNING: Your guess is not in valid length')

        if '_' not in word_unsolved:
            print('Well done! You won!')
            restart_prompt(word)

        print('Guesses left: ' + str(guess_chance))

    print('No more guesses left. Better next time')
    restart_prompt(word)


if __name__ == '__main__':
    main()
