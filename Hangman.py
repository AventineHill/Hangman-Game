'''
Created on 28 Feb 2017

@author: ConnorF
'''
from pip._vendor.html5lib._ihatexml import letter


import random


def get_word():
    words = []
    
    with open('words.txt', 'r') as f:
        words = f.read().splitlines()

    return random.choice(words).upper()
    
def check(word,guesses,guess):
        guess = guess.upper()
        status = ''
        y = 0
        matches =0
        for letter in word:
                if letter in guesses:
                    status += letter
                else:
                    status += '*'
                if letter == guess:
                    matches += 1
        if matches > 1:
            print('Yes, the word contains',matches,'of the letter', guess, '.')
        elif matches == 1:
            print('Yes, the word contains the letter' ,guess, '.')
        else:
            print('Sorry, the word does not contain the letter', guess, '.')
        return status

def main():    
    word = get_word()
    guesses = []
    guessed = False
    print('The word contains', len(word),'letters.')
    while not guessed:
        text = 'Please enter one letter or a', format(len(word)), 'letter word.'
        guess = input(text)
        guess=guess.upper()
        if guess in guesses:
            print('You already guessed that.')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else: 
                print('Sorry, that is incorrect.')
        elif len(guess) == 1:
                guesses.append(guess)
                result = check(word,guesses,guess)
                if result == word:
                    guessed: True
                else:
                    print(result)
        else:
            print('Invalid entry.')
    print('Yes, the word is:', word) 
    print('You got it in', len(guesses), 'tries.')
    
main()   
            
