# File: move.py
# Package: onitama
# Author: Michael Huelsman
# Created On: 21 Dec 2018
# Purpose:
#   This files details classes for representing moves in Onitama.


# Precond:
#   filename is the name of the file containing move descriptions.
#
# Postcond:
#   Returns a list of all parsed moves.
def parse_moves(filename):
    results = []
    with open(filename,'r') as fin:
        line = fin.readline().strip()
        line = line.split(';')
        name = line[0]
        moves = []
        for i in range(1,len(name)):
            moves.append(map(lambda x: int(x),line[i].split(',')))
        moves = map(lambda x: (x[0],x[1]), moves)
        results.append(Move(name,moves))
    return results

class Move:
    # Precond:
    #   name is a strings.
    #   moves is a list of pairs indicating the possible submoves.
    #
    # Postcond:
    #   Builds a Move object.
    def __init__(self, name, moves):
        self.name = name
        self.moves = moves

class MoveCollection:
    # Precond:
    #   redMoves is a list of Move objects.
    #   blueMoves is a list of Move objects.
    #   floating is a Move object.
    #
    # Postcond:
    #   Builds a new MoveCollection object.
    def __init__(self, redMoves, blueMoves, floating):
        self.redMoves = redMoves
        self.blueMoves = blueMoves
        self.floating = floating

    # Precond:
    #   index is the index of the redMove to rotate.
    #
    # Postcond:
    #   Rotates the specfied move to the floating pool and puts the floating
    #   move into the redMoves.
    def redRotate(self,index):
        temp = self.floating
        self.floating = self.redMoves[index]
        self.redMoves[index] = temp

    # Precond:
    #   index is thre index of the blueMove to rotate.
    #
    # Postcond:
    #   Rotates the specfied move to the floating pool and puts the floating
    #   move into the blueMoves.
    def blueRotate(self,index):
        temp = self.floating
        self.floating = self.blueMoves[index]
        self.blueMoves[index] = temp

    # Precond:
    #   None.
    #
    # Postcond:
    #   Returns a new copy of the MoveCollection object.
    def copy(self):
        return MoveCollection(self.redMoves[:],self.blueMoves[:],self.floating)
