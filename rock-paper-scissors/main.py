##Rock-Paper-Scissors
import random, time, os

print(
"""

-------------------------------------
|     WELCOME TO MY R.P.S. GAME     |
|                 @aliugurtalay     |
-------------------------------------
|                                   |
|Enter Your Choose[R-P-S]           |
-------------------------------------
==
"""
       )

key_root= True
key = 0
Score = 0

while key_root== True:
    while key < 5:
        key+=1
        enter_data = input()
        
        stck = ["R","P","S"]
        finaldata =stck[random.randint(0, 2)]
        
        if enter_data == finaldata:
            Score+=1
            print("Congrulations!! You are win")
        else:
            
            print("You're a loser")
        
    print("Your Score:", Score)
    key = 0
    time.sleep(1)
    print("If you want to play new game write [OK]")
    Choose = input()
   
    if Choose == "OK":
        pass
    else:
        exit()
    print(
"""
-------------------------------------
"""
        )
    
    
    
    
    

    
    

    
    


