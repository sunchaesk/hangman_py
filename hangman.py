import sys
import random
word = ""
curr = []

def new_word():
    w = generate_word()
    global word
    word = ""
    word = w
    global curr
    for i in range(len(word)):
        curr.append('*')

def generate_word():
    words = ['hello','name','example']
    i = random.randint(0,len(words))
    return words[i]

new_word()

while True:
    inp = input('Enter a character to guess: ')
    if type(inp) == int or len(inp) > 1:
        print('Wrong input')
    else:
        if inp in word:
            print('Guess was correct')
            for i in range(len(word)):
                if inp == word[i]:
                    curr[i] = inp
                    if '*' not in curr:
                        print('You solved it!')
                        inp = input('Play again? y or n: ')
                        if inp == 'n':
                            print('thxs for play')
                            sys.exit()
                        elif inp == 'y':
                            print('generated a new word')
                            word = generate_word()
            print(''.join(curr))
        else:
            print('Guess was wrong')
            print(''.join(curr))
