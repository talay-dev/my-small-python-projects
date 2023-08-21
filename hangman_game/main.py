import random
import time
import os
from art import pics, logo, word_list

print(logo)

while True:
    health = 6
    print(pics[6-health])
    selected_word = random.choice(word_list)

    blank = '_'*len(selected_word)
    print(blank)

    while True:
        
        print('guess a letter')
        guess = input().lower()
        os.system('cls')

        if len(guess) == 1:
            
            if guess in selected_word:
                blank = list(blank)
                timer = 0
                for i in selected_word:
                    if i == guess:
                        blank[timer] = guess
                    timer += 1
                blank = "".join(blank)

                if '_' not in blank:
                    print('congrats! you won')
                    time.sleep(3)
                    break
            else:
                health -= 1
                print('mistake!')
                if health == 0:
                    print('game over')
                    time.sleep(3)
                    break
            print('='*20)
            print(pics[6-health])
            print(blank)

    print('if you want to play again? (y/n)= ')
    answer = input()

    if answer == 'y':
        pass
    if answer == 'n':
        break
