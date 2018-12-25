# File: board.py
# Package: onitama
# Author: Michael Huelsman
# Created On: 21 Dec 2018
# Purpose:
#   This files details classes for representing the board state of a game of
#   Onitama

class GamePiece:
    # Precond:
    #   piece is a string denoting the piece name.
    #   color is a string denoting the color of the pieces.
    #   location is a pair of values indicating (x,y) coordinates.
    #
    # Postcond:
    #   Creates a new game piece with specified name, color, and location.
    def __init__(self, piece, color, location):
        self.piece = piece
        self.color = color
        self.location = location

    # Precond:
    #   None.
    #
    # Postcond:
    #   Returns a string representation of the piece.
    def __str__(self):
        loc = "(" + str(self.location[0]) + "," + str(self.location[1]) + ")"
        return "[" + str(self.color) + "]" + str(self.piece) + ": " + loc

    # Precond:
    #   None.
    #
    # Postcond:
    #   Returns a new GamePiece object that is a copy of this one.
    def copy(self):
        return GamePiece(self.piece, self.color, self.location)

class BoardState:
    # Precond:
    #   copy is a BoardState object to copy.
    #
    # Postcond:
    #   If copy is None:
    #       Builds a new BoardState which is consistent with the starting board
    #       state.
    #   Else:
    #       Copies the board state from copy.
    def __init__(self, copy=None):
        self.board = [[None for j in range(5)] for i in range(5)]
        if copy is not None:
            for i in range(5):
                for j in range(5):
                    if copy.board[i][j] is not None:
                        self.board[i][j] = copy.board[i][j].copy()
        else:
            for i in range(5):
                if i == 3:
                    # Place Masters
                    self.board[i][0] = GamePiece('Master','red',(i,0))
                    self.board[i][4] = GamePiece('Master','blue',(i,4))
                else:
                    # Place students
                    self.board[i][0] = GamePiece('Student','red',(i,0))
                    self.board[i][4] = GamePiece('Student','blue',(i,4))

    # Precond:
    #   loc is a pair of integers indicating a position vector.
    #
    # Postcond:
    #   Returns true if location is in bounds.
    def inBounds(self, loc):
        return (loc[0] >= 0 and loc[0] < 5) and (loc[1] >= 0 and loc[1] < 5)

    # Precond:
    #   start is the location where the piece starts.
    #   to is the location where the piece moves to.

    # Postcond:
    #   Returns true if the move is performed.
    #   Returns false if the move is illegal.
    def move(self, start, to):
        if not self.inBounds(start) or not self.inBounds(to):
            return False
        if self.board[start[0]][start[1]] is None:
            return False
        if self.board[to[0]][to[1]] is not None and self.board[start[0]][start[1]].color == self.board[to[0]][to[1]].color:
            return False
        self.board[to[0]][to[1]] = None
        self.board[to[0]][to[1]] = self.board[start[0]][start[1]]
        self.board[to[0]][to[1]].location = to
        self.board[start[0]][start[1]] = None
        return True

    # Precond:
    #   None.
    #
    # Postcond:
    #   Returns a list of all GamePiece object currently on the board.
    def pieces(self):
        results = []
        for i in range(5):
            for j in range(5):
                if self.board[i][j] is not None:
                    results.append(self.board[i][j])
        return results

    # Precond:
    #   None.
    #
    # Postcond:
    #   Returns the color of the winning team.
    #   If there is no winner None is returned instead.
    def winner(self):
        redMaster = None
        blueMaster = None
        for piece in self.pieces():
            if piece.piece == 'Master':
                if piece.color == 'red':
                    redMaster = piece
                elif piece.color == 'blue':
                    blueMaster = piece
        if redMaster is None:
            return 'blue'
        if blueMaster is None:
            return 'red'
        if redMaster.location[0] == 3 and redMaster.location[1] == 4:
            return 'red'
        if blueMaster.location[0] == 3 and blueMaster.location[1] == 0:
            return 'blue'
        return None
