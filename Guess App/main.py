##Number_Guessing_Game
import random




def game():
    """Function to play the game"""
    attempts = 5
    while True:
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            return True
        elif guess > number:
            print("Too high.")

        elif guess < number:
            print("Too low.")
        
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return False
        else:
            print(f"You have {attempts} attempts remaining to guess the number.")


              
if __name__ == "__main__":

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 attempts to guess the number.")
    
    number = random.randint(1,100)
    point = 0

    while True:
        if game():
            point += 1
        else:
            point -=0
        print(f"Your current score is {point}.")
        if input("Do you want to play again? Type 'y' or 'n': ") == 'y':
            continue
        else:
            print("Goodbye!")
            break   
    
    
