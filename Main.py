``` import time
import random

def game():
 try:
    print(f'1. snake')
    time.sleep(0.1)
    print('2. gun')
    time.sleep(0.1)
    print('3. water\n')
    time.sleep(0.3)
    user=int(input('enter your choice : '))
    comp=random.randint(1,3)
    time.sleep(0.3)
    print(f'the computer choice is : {comp}')
    if user==1 and comp==3:
        print('●●●●●●●●●●you won the game●●●●●●●●●●\n')      
        game()
    
    if user==1 and comp==2:
        print('!!!!!!!!!!!!!!!!!!!!you lose!!!!!!!!!!!!!!!!!!!!\n')
        
        game()
        
    if user==2 and comp==1:
        print('●●●●●●●●●●you won the game●●●●●●●●●●\n')      
        
        game()
        
    if user==2 and comp==3:
        print('!!!!!!!!!!!!!!!!!!!!you lose!!!!!!!!!!!!!!!!!!!!\n')
        
        game()
        
    if user==3 and comp==1:
        print('!!!!!!!!!!!!!!!!!!!!you lose!!!!!!!!!!!!!!!!!!!!\n')
        
        game()
        
    if user==3 and comp==2:
        print('●●●●●●●●●●you won the game●●●●●●●●●●\n')   
        
        game()
        
    if user == comp:
        print('@@@@@@@@@@ game is draw @@@@@@@@@@\n')
        game()
                
    else:
        print('invalid input please input 1,2,and 3 only ')
        game()
        
 except ValueError:
        print('\ninvalid input! \n please try again....\n')
        game()
        
print('****************WELCOME TO SNAKE WATER GUN GAME****************')
print('****************CREATED BY SAKSHAM SHRIVASTAV***************\n')
time.sleep(0.4)       
game() ```
        
