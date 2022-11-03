##Number_Guessing_Game
import random

key = True

while key == True:
    print("="*30,"\n",
          "Hello Welcome to My New Program\n",
          "I guessed a number from[0-100]\n",
          "Try to find it\n",
          "="*30
          , sep= ""      
          )
    
    Number_Guessing = random.randint(0, 100)
    
    User_Guess = 101
    
    while User_Guess != Number_Guessing:
        
        User_Guess = int(input())
        
        if User_Guess < Number_Guessing:
            
            print(
                "="*30,"\n",
                "Your Guess Small Than Mine\n",
                "="*30
                , sep= ""  
                )
            continue
        
        if User_Guess > Number_Guessing:
            
            print(
                "="*30,"\n",
                "Your Guess Big Than Mine\n",
                "="*30
                , sep= ""  
                )
            continue
    
    
    
    if User_Guess == Number_Guessing:
        print("Congrulations!! You win this game\n",
              "If you want a new game say me [new]\n",
              "For exit say me [exit]               ",
              sep = ""
              )
        
        choice_user = input()
        
        if choice_user == "exit":
            key = False
            
        if choice_user == "new":
            pass
    






    