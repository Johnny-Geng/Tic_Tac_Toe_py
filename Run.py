# Johnny Geng, johnnyge@usc.edu

# Description:
# This program allows two player to play the game of Tic Tac Toe. The program will allow the two player to
# place an "x" or an "o" somewhere on the board and determine when someone wins or when a stalemate
# is reached.

import TicTacToeHelper


# Name: isValidMove
# Input:  a list representing the board, an integer corresponding to the
# index position that a user would like to place their letter on
# Output: a boolean value
# Side effect: none
# Description: This function should look at the specified spot on the board and return
# True if the spot is open or False if the spot is taken or out of range
def isValidMove(boardList, spot):
    try:
        if boardList[int(spot)] == "x" or boardList[int(spot)] == "o":
            return False
        elif int(spot) in range(0, 9):
            return True
    except:
        return False


# Name: updateBoard
# Input: a list representing the board, an integer corresponding to the
# index position that a user would like to place their letter on, a string
# representing the user’s letter (“x” or “o”)
# index position that a user would like to place their letter on
# Output: none
# Side effect: none
# Description: Takes the current board list and places the player’s letter in the specified
# spot on the board.
def updateBoard(boardList, spot, playerLetter):
    boardList[int(spot)] = playerLetter


# Name: playGame
# Input: none
# Output: none
# Side effect: Print out final board at the end of the game and a message about who
# won or if there was a stalemate.
# Description: The action process of the game.
def playGame():
    boardList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    move_counter = 0
    while move_counter < 9:
        TicTacToeHelper.printUglyBoard(boardList)
        if move_counter in [0, 2, 4, 6, 8]:
            playerLetter = "x"
        else:
            playerLetter = "o"
        print("Player " + playerLetter, end=", ")
        spot = input("pick a spot: ")
        check = isValidMove(boardList, spot)
        while not check:
            print("Invalid move, please try again.")
            print("Player " + playerLetter, end=", ")
            spot = input("pick a spot: ")
            check = isValidMove(boardList, spot)
        updateBoard(boardList, spot, playerLetter)
        result = TicTacToeHelper.checkForWinner(boardList, move_counter)
        if result == "n":
            move_counter += 1
        else:
            move_counter = 9
    TicTacToeHelper.printUglyBoard(boardList)
    print("Game Over!")
    if result == "x":
        print("Player x is the winner!")
    elif result == "o":
        print("Player o is the winner!")
    else:
        print("Stalemate reached!")


# Name: main
# Input: none
# Output: none
# Side effect: Print out welcome and ending statement.
# Description: Check if the player wants to play the game again.
def main():
    print("Welcome to the Tic Tac Toe!")
    playGame()
    i = True
    while i:
        another_round = input("Would you like to play another round? (y/n): ")
        if another_round.lower() == "y":
            playGame()
        elif another_round.lower() == "n":
            i = False
        else:
            print("Invalid answer. Please try again.")
    print("Goodbye!")


main()
