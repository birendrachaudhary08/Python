
# Stone Paper Scissor Game

import random
option=["stone","paper","Scissor"]

'''
stone vs paper ---> paper win
stone vs scissor --->stone wins
paper vs scissor --->scissor wins
'''
while True:
    count=0
    ucount=0
    uc = int(input('''
Game Start..........
1: Yes
2: NO | Exit             
      '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input(''' 
1 Stone
2 Scissor
3 Paper                                    
'''))    
            if userInput==1:
                uchoice="stone"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            choice=random.choice(option)
            if choice==uchoice:
                print("Computer Valie: ",choice)
                print("User Value: ",uchoice)
                print("Game Draw: ")
                ucount=ucount+1
                count=count+1
            elif((uchoice=="rock" and choice=="scissor") or (uchoice=="paper"and 
            choice=="rock") or (uchoice=="scissor" and choice=="paper")):
                print("Computer value: ",choice)
                print("User Value: ",uchoice)
                print("You Win and Computer Lose")
                ucount=ucount+1
            else:
                print("Computer value: ",choice)
                print("User Value: ",uchoice)
                print("You lose And Computer Win")
                count=count+1
    else:
        break
