# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:10:22 2022

@author: suman
"""

def string_compare(secret_string, guess_string):
    exclude = []
    output = []
    if secret_string == guess_string:
        return 'You guessed it right'
    for i in range(len(secret_string)):
        if secret_string[i] == guess_string[i]:
            output.append('Fermi')
            exclude.append(i)
    for i in range(len(secret_string)):
        if i not in exclude:
            for char in secret_string:
                if guess_string[i] == char:
                    output.append('Pico')
                    exclude.append(i)
                    break
    if len(output) == 0:
        output.append('bagels')
    return output    

import random
# def 

def start_bagels():
    #x = int(input('Enter number of digits of secret number: ')) # len of secret number
    print("""Game Rules:
 When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.""")
    x = 3
    secret_number = random.randrange(10**(x-1), 10**(x), x)
    print('I have decided the secret number you have 10 guess.')
    num_guess = 1
    while num_guess<= 10:
        guess_number = input('Enter 3 digit number: ')
        sc = string_compare(str(secret_number), guess_number)
        if sc == 'You guessed it right':
            print(sc)
            break
        else:
            print(sc)
            num_guess +=1
    else:
        print('You turn is up, I won and the secret number is: ', secret_number)
        
    
start_bagels()    