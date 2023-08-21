import random

def game() -> None:
    """The main game function."""

    options = ['rock', 'paper', 'scissors']
    your_score = 0
    
    while True:
        for a, b in enumerate(options):
            print(f'{a + 1}. {b}')

        pc = int(input('Enter your choice: ')) # player choice
        cc = random.randint(1, 3) # computer choice

        print(f'You chose {options[pc - 1]}')
        print(f'The computer chose {options[cc - 1]}')
        if pc == cc:
            print('It\'s a tie!')
        elif (pc == 1 and cc == 2) or (pc == 2 and cc == 3) or (pc == 3 and cc == 1):
            your_score -= 1
            print('The computer wins!')
        elif (pc == 1 and cc == 3) or (pc == 2 and cc == 1) or (pc == 3 and cc == 2):
            your_score += 1
            print('You win!')
        else:
            print('Invalid choice!')
            continue
        print(f'Your score: {your_score}')

        play_again = input('Play again? (y/n): ')

        if play_again == 'y':
            continue
        else:
            break





if __name__ == '__main__':
    print('Welcome to Rock, Paper, Scissors!')
    game()
