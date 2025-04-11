import random

try:
    print("Welcome to connect four")
    print("-----------------------")

    possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
    gameBoard = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""]]
    rows = 6
    cols = 7

    def printGameBoard():
        print("\n   A   B   C   D   E   F   G   ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+----+----+----+")
        print(x, "  |", end="")
        for y in range(cols):
            if(gameBoard[x][y] == "🔵"):
                print("", gameBoard[x][y], end="    |")
            elif(gameBoard[x][y] == "🔴"):
                print("", gameBoard[x][y], end="    |")
            else:
                print(" ", gameBoard[x][y], end="    |")
        print("\n   +----+----+----+----+----+----+----+----+----+----+")

    def modifyTurn(spacePicked, turn):
        gameBoard[spacePicked[0]][spacePicked[1]] = turn

    print("Game board initialized.")
    printGameBoard()

except Exception as e:
    print(f"An error occurred: {e}")

input("\nPress Enter to exit...")