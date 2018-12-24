# File: main.py
# Package: <None>
# Author: Michael Huelsman
# Created On: 21 Dec 2018
# Purpose:
#   Entry point for running a game of OnitamAI.

from onitama.move import parse_moves, MoveCollection
from onitama.board import BoardState
from intelligence import decide
# Precond:
#   args are the command-line arguments:
#       0: file containing move cards
#       1: Ply-depth number
#
# Postcond:
#   Runs a game with the OnitamAI.
def main(args):
    depth = (int(args[1]) * 2) - 1
    moves = parse_moves(args[0])
    # Determine moves in use.
    oppMoves = []
    print("Opponent Moves:")
    while len(oppMoves) < 2:
        temp = raw_input("Move name:").strip()
        for move in moves:
            if temp == move.name:
                oppMoves.append(move)
                break
        print("Move not found.")
    selfMoves = []
    print("Self Moves:")
    while len(selfMoves) < 2:
        temp = raw_input("Move name:").strip()
        for move in moves:
            if temp == move.name:
                selfMoves.append(move)
                break
        print("Move not found.")
    queuedMove = None
    print("Floating Move:")
    while len(queuedMove) < 1:
        temp = raw_input("Move name:").strip()
        for move in moves:
            if temp == move.name:
                queuedMove = move
                break
        print("Move not found.")
    cards = MoveCollection(selfMoves,oppMoves,queuedMove)
    # Determine who goes first
    temp = raw_input("Do I go first(Y/N)?").strip()
    turn = False
    if temp.lowercase()[0] == 'Y':
        turn = True
    # Begin the game
    board = BoardState()
    while board.winner() == None:
        if turn:
            print("Red Move:")
            print(decide(board,cards,depth))
        else:
    return 0

main(sys.argv[1:len(sys.argv)])
