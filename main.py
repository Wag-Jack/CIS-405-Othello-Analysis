import time
import constants as c

from othello import Board

def main():
    while True:
        print("--------------------------------------------")
        print("WELCOME TO OTHELLO, SELECTION OPTION")
        print("1.) Opponent w/ Minimax (Alpha-Beta Pruning)")
        print("2.) Opponent w/ Monte Carlo Tree Search")
        print("3.) Quit")
        print("--------------------------------------------")

        selection = int(input("Choice: ")) #Handle ValueError
        match selection:
            case 1:
                pass
            case 2:
                pass
            case 3:
                break
            case _:
                print("Invalid input, try again\n")


if __name__ == "__main__":
    main()