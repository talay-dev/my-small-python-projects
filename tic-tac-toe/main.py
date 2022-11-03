# My TicTacToe Game
import time
import random

print(
    '''
---------------------------
|     TIC-TAC-TOE GAME    |
|                 -AUT    |     
---------------------------
|      -------------      |             
|      | {} | {} | {} |      |
|      |-----------|      |
|      | {} | {} | {} |      |
|      |-----------|      | 
|      | {} | {} | {} |      |
|      -------------      |
---------------------------
'''.format(1, 2, 3, 4, 5, 6, 7, 8, 9), end='')

container = dict.fromkeys(range(1, 10))
for a in range(1, 10):
    container[a] = '_'

box = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def board_make():
    print(

        '''
|      -------------      |
|      | {} | {} | {} |      |
|      -------------      |
|      | {} | {} | {} |      |
|      -------------      |
|      | {} | {} | {} |      |
|      -------------      |
|-------------------------|
	'''.format(container[1], container[2], container[3], container[4], container[5], container[6], container[7],
               container[8], container[9]), end=''    )

Scores = [0,0]

def add(x):
    x+=1
    
    if container[x] == 'X':
        Scores[0]+=1
    elif container[x] == 'O':
        Scores[1]+=1


def check():
    cl = [] 
    
    for i in container:
        cl.append(container[i])
       
    
    for i in range(0,3):
    
        if cl[3*i]  == cl[3*i+1] == cl[3*i+2]:
            add(3*i)
        if cl[i] == cl[i+3] == cl[i+6]:
            add(i)
     
    
    for i in range(0,2):
        if cl[2*i] == cl[4] == cl[(i+3)*2]:
            add(2*i)
    

        
def user_interact():
    print(
        '''
|    Make Your Choose     |
|    ==                   |
	''', end=''
    )

    choice = input()
    box.remove(int(choice))
    container[int(choice)] = 'X'
    board_make()

#Machine Desicion Section[Burada for bolumunde hata var !!]
waste_box = []
machine_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                [1, 4, 7], [2, 5, 8], [3, 6, 9],
                [1, 5, 9], [3, 5, 7]]


def machine_interact():
    test_box = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    desicion_list = []

    check_elements_semi = list(set(test_box) - set(box))
    check_elements = list(set(check_elements_semi) - set(waste_box))
    print(waste_box, box, test_box)

    if len(check_elements)==1:
        for i in machine_list:
            for ii in i:
               if check_elements[0] == ii:
                    i.remove(check_elements[0])
    else:
        for i in machine_list:
            for ii in i:
                if check_elements[0] == ii:
                    i.remove(check_elements[0])
        for i in machine_list:
            for ii in i:
               if check_elements[1] == ii:
                    i.remove(check_elements[1])

    print(check_elements, check_elements_semi)
    waste_box.append(check_elements[0])
    check_elements.clear()
    check_elements_semi.clear()

    for i in machine_list:
        desicion_list.append(len(i))

    min_v = min(desicion_list)

    if min_v == 0:
        min_v+=1

    des_v = desicion_list.index(min_v)
    print(desicion_list, des_v)

    desicion = machine_list[des_v][random.randint(0,len(machine_list[des_v])-1)]
    desicion_list.clear()
    print(box, desicion)
    container[desicion] = 'O'
    box.remove(desicion)
    board_make()

while len(box) != 0:
    user_interact()

    if len(box) == 0:
        break

    else:
        machine_interact()


check()

Result = ["Congrulations!! You're a Winner", "Sorry :( You're a Loser" ]
if Scores[0]>Scores[1]:
    del Result[1]
else:
    del Result[0]


print(
    '''
Game Finished 
{}
Users Score     = {}
Computers Score = {}


    '''.format( Result[0], Scores[0], Scores[1])
)        
        
        
time.sleep(5)
