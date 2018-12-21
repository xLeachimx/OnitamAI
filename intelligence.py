# File: intelligence.py
# package: <None>
# Author: Michael Huelsman
# Created On: 21 Dec 2018
# Purpose:
#   Uses the max-min tree search algorithm to determine the best next move in
#   a game of Onitama.
# Notes:
#   It is assumed that the AI is playing red (since colors are easily
#   interchangable).

from onitama.board import *
from onitama.move import *

# Precond:
#   board is the current board state.
#   depth is the number of plies to consider.
#   cards is a list of the current cards:
#       0: Cards for red
#       1: Cards for blue
#       2: Intermediate
#
# Postcond:
#   Builds a mx-min tree of the given ply-depth and uses that to decide the next
#   move.
def decide(board, cards, depth):
    return None


# Defines a class for max-min tree nodes
class TreeNode:
    # Precond:
    #   board is a valid BoardState object
    #   cards is a list of the current cards:
    #       0: Cards for red
    #       1: Cards for blue
    #       2: Intermediate
    #   turn indicates whether to maximize or minimize value:
    #       True: max
    #       False: min
    #   move is the move used to produce the given node consists of two pairs:
    #       0: from location
    #       1: to location
    #   depth indicates the remaining depth.
    #
    # Postcond:
    #   Builds a new max-min tree node.
    def __init__(self, board, cards, turn, move, depth):
        self.board = board
        self.cards = cards
        self.turn = turn
        self.depth = depth
        self.move = move
        self.decision = None
        self.score = self.eval()

    # Precond:
    #   None.
    #
    # Postcond:
    #   If the depth remaining for the node is zero then uses a custom
    #   evaluation metric.
    #   Otherwise all children are generated and used to determine final eval.
    def eval(self):
        if depth == 0:
            winner = self.board.winner()
            if winner == 'red':
                return 1.0
            if winner == 'blue':
                return 0.0
            pieces = self.board.pieces()
            redCount = 0
            distance = 0.0
            for piece in pieces:
                if piece.color == 'red':
                    redCount += 1
                    if piece.piece == 'Master':
                        xcomp = (piece.location[0]-3.0)**2
                        ycomp = (piece.location[1]-4.0)**2
                        distance = Math.sqrt(xcomp+ycomp)
            distance = 1.0/(distance+1.0)
            redCount = redCount/(float(len(pieces)))
            return (distance+redCount)/2.0
        else:
            children = []
            cards = []
            if self.turn:
                cards = self.cards[0]
            else:
                cards = self.cards[1]
            # Select card.
            for i in range(2):
                if self.turn:
                    nextCards.append([])
                    for j in range(len(cards[0])):
                        if j == i:
                            continue
                        nextCards[0].append(self.cards[0][j])
                    nextCards[0].extend(self.cards[2])
                    nextCards.append(self.cards[1])
                    nextCards.append([self.cards[0][i]])
                else:
                    nextCards.append(self.cards[0])
                    nextCards.append([])
                    for j in range(len(cards[1])):
                        if j == i:
                            continue
                        nextCards[1].append(self.cards[1][j])
                    nextCards[1].extend(self.cards[2])
                    nextCards.append([self.cards[1][i]])
                # Select move from cards.
                for move in cards[i].moves:
                    # Select the Piece.
                    for piece in self.pieces.pieces():
                        # Ensure proper turn order.
                        if piece.color == 'red' and not self.turn:
                            continue
                        if piece.color == 'blue' and self.turn:
                            continue
                        start = piece.location
                        xCoord = start[0]
                        yCoord = start[1]
                        if self.turn:
                            xCoord = start[0] + move[0]
                            yCoord = start[1] + move[1]
                        else:
                            xCoord = start[0] - move[0]
                            yCoord = start[1] - move[1]
                        end = (xCoord,yCoord)
                        nextState = BoardState(self.board)
                        if nextState.move(start,end):
                            child = TreeNode(nextState, nextCards, !self.turn, [start,end], self.depth-1)
                            children.append(child)
            return 0
            if self.turn:
                max = children[0].score
                for i in range(1,len(children)):
                    if children[i].score > max:
                        max = children[i].score
                return max
            else:
                min = children[0].score
                for i in range(1,len(children)):
                    if children[i].score < min:
                        min = children[i].score
                return min
        return -1 # Indicates odd execution
