#Importing modules
import os
import time
from itertools import chain, repeat
from termcolor import colored
import random

#Giving range to the board
board = [' ' for x in range(10)]

a = '   |   |   '

#For clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

clear()

#For inserting letters to the board
def insertLetter(letter,pos):
    board[pos] = letter

#For checking if space in the board is free or not
def spaceIsFree(pos):
    return board[pos] == ' '

#For printing the board
def printBoard(board):

    print("\n")
    print(a)
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(a)
    print('------------')
    print(a)
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(a)
    print('------------')
    print(a)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(a)

#For printing the instructions of the board
def instructions():
    
    rules = ["\nThis board is divided into 9 blocks(1-9)", "Like 1st box represents number '1'.",
                "You have to select the number of the block on which you want to place your X.",
                "IN this game The 'TIC-TAC-AI' will be your opponent."]
    
    for i in chain.from_iterable(repeat(rules, 1)):
        time.sleep(3)
        print(i, "\n")
    time.sleep(1)
    print("\nLet the game begin...")
    time.sleep(2)
    
#For checking if the board is full or not
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

#For deciding the winner of the game
def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

#For player's move
def playerMove():
    run = True
    while run:
        time.sleep(1)
        move = input("Please select a position to enter the 'X' between(1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    time.sleep(1)
                    print(colored('\nSorry, this space is occupied!\n', 'magenta', attrs=['bold']))
            else:
                time.sleep(1)
                print(colored('\nplease type a number between(1-9)\n', 'red', attrs=['bold']))
                time.sleep(2)

        except ValueError:
            time.sleep(1)
            print(colored('\nPlease type a number.\n', 'red', attrs=['bold']))
            time.sleep(2)

#For computer's move
def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

#For selecting random
def selectRandom(li):

    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

#Main function for executing the other functions
def main():
    
    print(colored("Welcome to the Tic Tac Toe game!", 'blue', attrs=['bold']))
    
    time.sleep(2)
    printBoard(board)
    instructions()
    time.sleep(2)
    clear()

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            time.sleep(2)
            print(colored("\nSorry you loose!", 'yellow', attrs=['bold']))
            exit()

        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                time.sleep(2)
                insertLetter('O' , move)
                print("\ncomputer placed an 'O' on position" , move , ":")
                printBoard(board)
        else:
            time.sleep(2)
            print(colored("\nCongractulations..You Win!", 'cyan', attrs=['bold']))
            exit()

    if isBoardFull(board):
        time.sleep(2)
        print(colored("Tie game", 'green', attrs=['bold']))
        exit()

#While loop for running the main function again & again until winner is selected
while True:

    main()

