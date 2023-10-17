gm = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

templete =""" 
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9 
"""
        
        
def enter(position,i,var):
    if gm[position-1]=='X':# this block checks whether the position is already taken 
        print(f'{p1} has already entered a value at {position}')
        position = int(input('Enter the new position : ')) # if it is taken then ask to enter a new position
        print()
    elif gm[position-1] == 'O': # same as above
        print(f'{p2} has already entered a value at {position}')
        position = int(input('Enter the new position : '))
        print()
    
    else:
        gm[position-1] = var
        
    for i in range(1,10):# this loop is to print the board with new values
        if i%3!=0:
            print(f" {gm[i-1]} ",end='|')
        else:
            print(f" {gm[i-1]}")
        if i%3==0 and i !=9:
            print('---|---|---')
            
    if i==9: # this block checks for the winner
            # returns true if there is a winner 
            # returns false if the game is tie
        
        if (gm[0]==gm[1]==gm[2]=='X'):
            print(f"\n\n{p1} is Winner!!!\n\n")
            return True
        elif (gm[0]==gm[1]==gm[2]=='O'):
            print(f"\n\n{p2} is Winner!!!\n\n")
            return True
            
        elif (gm[3]==gm[4]==gm[5]=='X'):
            print(f"\n\n{p1} is Winner!!!\n\n") 
            return True
        elif (gm[3]==gm[4]==gm[5]=='O'):
            print(f"\n\n{p2} is Winner!!!\n\n")
            return True
            
        elif (gm[6]==gm[7]==gm[8]=='X'):
            print(f"\n\n{p1} is Winner!!!\n\n")
            return True
        elif (gm[6]==gm[7]==gm[8]=='O'):
            print(f"\n\n{p2} is Winner!!!\n\n")
            return True
            
        elif (gm[0]==gm[3]==gm[6]=='X'):
            print(f"\n\n{p1} is Winner!!!\n\n")
            return True
        elif (gm[0]==gm[3]==gm[6]=='O'):
            print(f"\n\n{p2} is Winner!!!\n\n")
            return True
            
        elif (gm[1]==gm[4]==gm[7]=='X'):
            print(f"\n\n{p1} is Winner!!!\n\n")
            return True
        elif (gm[1]==gm[4]==gm[7]=='O'):
            print(f"\n\n{p2} is Winner!!!\n\n")
            return True
            
        elif (gm[2]==gm[5]==gm[8]=='X'):
            print(f"\n\n{p1} is Winner!!!\n\n")
            return True
        elif (gm[2]==gm[5]==gm[8]=='O'):
            print(f"\n\n{p2} is Winner!!!\n\n")
            return True
            
        elif (gm[0]==gm[4]==gm[8]=='X'):
            print(f"\n\n{p1} is Winner!!!\n\n")
            return True
        elif (gm[0]==gm[4]==gm[8]=='O'):
            print(f"\n\n{p2} is Winner!!!\n\n")
            return True
            
        elif (gm[2]==gm[4]==gm[6]=='X'):
            print(f"\n\n{p1} is Winner!!!\n\n")
            return True
        elif (gm[0]==gm[1]==gm[2]=='O'):
            print(f"\n\n{p2} is Winner!!!\n\n")
            return True
            
        else:
            return False   
        
print('                  ***Welcome to the Tic Tac Toe game ***')
p1 = input('\nEnter the name of the 1st player : ')
p2 = input('Enter the name of the 2nd player : ')
print(f"\n{p1}'s sign is X ",f"\n{p2}'s sign is O\n")
print(templete)
print('Enter the number where u want to enter your letter.\n\n')
for move in range(9):# this loop is to take the values
    if move%2==0:
        if move >0 and con == True:
            break                   # breaks if the player has won
        position = input(f'\n{p1} : ')
        if position.isdigit() and 0 < int(position) < 10:
            position = int(position)
            con = enter(position,move,'X')
        else:
            print('Please enter valid number input.\nYour input must be an interger and in range of 1-9 only')
            position = input(f'\n{p1} : ')
            position = int(position)
            con = enter(position,move,'X')
    else:
        if move > 0 and con == True:
            break                   # breaks if the player has won
        position = (input(f'\n{p2} : '))
        if position.isdigit() and 0 < int(position) < 10:
            position = int(position)
            con = enter(position,move,'O')
        else:
            print('Please enter valid number input.\nYour input must be an interger and in range of 1-9 only')
            position = input(f'\n{p2} : ')
            position = int(position)
            con = enter(position,move,')')
        
if con == False : # checks if the game is tie 
    print('\n\nOOPS!!! \nThis is a tie.....  \nPlay again...')