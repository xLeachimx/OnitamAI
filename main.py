# File: main.py
# Package: <None>
# Author: Michael Huelsman
# Created On: 21 Dec 2018
# Purpose:
#   Entry point for running a game of OnitamAI.

from onitama.move import parse_moves, MoveCollection
from onitama.board import BoardState
from intelligence import decide
import sys
import time
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
    for move in moves:
        print(str(move))
    # Determine moves in use.
    oppMoves = []
    print("Opponent Moves:")
    while len(oppMoves) < 2:
        temp = raw_input("Move name:").strip()
        found = False
        for move in moves:
            if temp == move.name:
                oppMoves.append(move)
                found = True
                break
        if not found:
            print("Move not found.")
    selfMoves = []
    print("Self Moves:")
    while len(selfMoves) < 2:
        temp = raw_input("Move name:").strip()
        found = False
        for move in moves:
            if temp == move.name:
                selfMoves.append(move)
                found = True
                break
        if not found:
            print("Move not found.")
    queuedMove = None
    print("Floating Move:")
    while queuedMove is None:
        temp = raw_input("Move name:").strip()
        found = False
        for move in moves:
            if temp == move.name:
                queuedMove = move
                found = True
                break
        if not found:
            print("Move not found.")
    cards = MoveCollection(selfMoves,oppMoves,queuedMove)
    # Determine who goes first
    temp = raw_input("Do I go first(Y/N)?").strip()
    turn = False
    if temp.lower()[0] == 'y':
        turn = True
    # Begin the game
    board = BoardState()
    while board.winner() == None:
        if turn:
            # AI Move
            startTime = time.time()
            print("Red Move:")
            move = decide(board,cards,depth)
            print("From: ("+str(move[0][0])+ ","+str(move[0][1])+")")
            print("To: ("+str(move[1][0])+","+ str(move[1][1])+")")
            print(cards.redMoves[move[2]])
            cards.redRotate(move[2])
            board.move(move[0],move[1])
            print(time.time()-startTime)
        else:
            # Human Move
            print("Blue Move:")
            # Choose card
            count = 0
            for move in cards.blueMoves:
                print(str(count) + ". " + str(move))
                count += 1
            choice = -1
            while choice < 0 or choice >= count:
                choice = input('Card Used: ')
            # Choose Move vector
            count = 0
            for move in cards.blueMoves[choice].moves:
                print(str(count) + ". " + str(-move[0]) + ',' + str(-move[1]))
                count += 1
            choice2 = -1
            while choice2 < 0 or choice2 >= count:
                choice2 = input('Move Used: ')
            # Choose piece
            count = 0
            for piece in board.pieces():
                print(str(count) + ". " + str(piece))
                count += 1
            choice3 = -1
            while choice3 < 0 or choice3 >= count:
                choice3 = input('Piece Used: ')
            move = cards.blueMoves[choice].moves[choice2]
            cards.blueRotate[choice]
            to = board.pieces()[choice3].location
            to = (to[0]+move[0],to[1]+move[1])
            board.move(board.pieces()[choice3].location,to)
        turn = not turn
    return 0

main(sys.argv[1:len(sys.argv)])
