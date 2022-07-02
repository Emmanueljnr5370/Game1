# String Concatenation: The process of joining strings together.

#youtuber = 'Emmanuel Tom'
#print('subscribe to ' + youtuber)
#print('subscribe to {}'.format(youtuber))
#print(f'subscribe to {youtuber}') 


#adj = input('Adjective: ')
#verb1 = input('verb: ')
#verb2 = input('verb: ')
#famous_person = input('Famous person: ')
#madlib = f'Computer programming is so {adj}! it makes me so excited all the \
#time because I Love to {verb1}. Stay hydrated and {verb2} like you \
#are {famous_person}!'
#print(madlib) 

#from sample_madlibs import hp, code, zombie, hungergames
#import random

#if __name__ == '__main__':
#    m = random.choice([hp, code, zombie, hungergames])
#    m.madlib()

### GUESSING GAME1

#import random
#def guess(x):
#    random_number = random.randint(1, x)
#    guess = 0
#    while guess != random_number:

#        guess = int(input(f'Guess a number between 1 and {x} :'))
#        if guess <  random_number:
#            print('Sorry, guess again. Too low.') 

#        elif guess > random_number:
#            print('Sorry, guess again. Its too high!')
        
#    print(f'Yeah, congrats. You have guessed the number {random_number} correctly!')

#guess(10)


### GUESSING GAME2


#import random
#def computer_guess(x):
#    low = 1
#    high = x
#    feedback = ''
#    while feedback != 'c':
#        if low != high:
#            guess = random.randint(low,high)
#        else:
#            guess = low # could also be high because low = high
#        feedback = input(f'Is {guess} too high (H), too low (L), or correct ()?? ').lower()
#        if feedback == 'h':
#            high = guess - 1
#        elif feedback == 'l':
#            low = guess + 1

#   print(f'Yeah! The computer has guessed your number, {guess}, correctly!!')            

#computer_guess(1000)


###  ROCK PAPER SCISSORS


#import random
#def play():
#    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
#    computer = random.choice(['r','p','s'])

#    if user == computer:
#        return 'It\'s a tie' # or "It's a tie"


    # r > s, s > p, p > r
#    if is_win(user, computer):
#        return 'You won!'

#    return 'You lost!'

#def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r 
#    if (player == 'r'  and opponent == 's') or (player == 's' and opponent == 'p') \
#        or (player == 'p' and opponent == 'r'):
#        return True
  
## HANGMAN

#import random
#from words import words

#def get_valid_word(words):
#    word = random.choice(words) # randomly chooses something from the list
#    while '-' in word or ' ' in word:
#        word = random.choice(words)


#    return word


#def hangman():
#    word = get_valid_word(words)
#    word_letters = set(word) # letters in the word
#    alphabet = set(string.ascii_uppercase)
#    used_letters = set() # what the user has guessed

#    # getting user input
#    while len(word_letters) > 0:
#        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
#        print('You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
#        word_list = [letter if letter in used_letters else '-' for letter in word]
#        print('Current word: ', ' '.join(word_list))

#        user_letter = input('Guess a letter: ').upper()
#        if user_letter in alphabet - used_letters:
#            used_letters.add(user_letter)
#            if user_letter in word_letters:
#                word_letters.remove(user_letter)

#        elif user_letter in used_letters:
#            print('You have already used that character. Please try again.')

#        else:
#            print('Invalid character. Please try again.')         
 
 
#    hangman()
#user_input = input('Type something:')    
#print(user_input)

# TIC-TAC-TOE GAME

import math
import random


class Player:
    def __init__(self,letter):
        # letter is x or 0 tt
        self.letter = letter
        # we want all players to get their next move

        def get_move(self, game):
            pass

class RandomComputerPlayer(Player)
            

































































































































































































































































































































































