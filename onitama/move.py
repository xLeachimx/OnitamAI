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
