import keyboard
import time
import os
import random
sleep_time = 0.1
plX=9
plY=9
field=[]


def createField():
    for i in range(20):
        field.append(['.']*20)
        field[i][0]='#'
        field[i][19]='#'
    for i in range(20):
        for j in range(20):
            field[0][j]='#'
            field[19][j]='#'
    field[9][9]='@'
    

def showMas(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end=" ")

        print()

def move():
    global plX
    global plY
    key = keyboard.read_key()
    
    if  (key == 'w' or key=='up') and plX!=1:
        field[plX][plY]='.'
        plX = plX-1
        field[plX][plY]='@'
        os.system('cls')
        showMas(field)
        print(plX, plY)
        time.sleep(sleep_time)


    if  (key == 'a' or key=='left') and plY!=1:
        field[plX][plY]='.'
        plY = plY-1
        field[plX][plY]='@'

        os.system('cls')
        showMas(field)
        print(plX, plY)
        time.sleep(sleep_time)

    if  (key == 's' or key == 'down') and  plX!=18:
        field[plX][plY]='.'
        plX = plX+1
        field[plX][plY]='@'
        os.system('cls')
        showMas(field)
        print(plX, plY)
        time.sleep(sleep_time)

    if  (key == 'd' or key == 'right') and plY!=18:
        field[plX][plY]='.'
        plY = plY+1
        field[plX][plY]='@'
        os.system('cls')
        showMas(field)
        print(plX, plY)
        time.sleep(sleep_time)

def createEnemy():
    enX = random.randint(1,18)
    if enX==plX:
        enX == enX+1 # Если повторяется координата X у героя и врага, то добавляе к последней +1
    enY = random.randint(1,18)
    if enY == plX:
        enX == enX+1
    field[enX][enY] = '&'
    
createField()
showMas(field)

while True: 
   # a=keyboard.read_key()
    #print(a)
    createEnemy()
    move()
    






        
        

