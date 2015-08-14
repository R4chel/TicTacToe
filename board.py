solutions = [
    set([0,1,2]), set([3,4,5]), set([6,7,8]),
    set([0,3,6]), set([1,4,7]), set([2,5,8]),
    set([0,4,8]), set([2,4,6])
]

class Square(object):
    def __init__(self, index):
        self.index = index
        self.player = None

    def claim(self, player):
        assert self.player is None
        self.player = player

class Board(object):
    def __init__(self):
        self.squares = [Square(i) for i in range(9)]

    def valid_squares(self):
        [s.index for s in self.squares if s.player is None]

    def display(self):
        vals = [str(s.index) if s.player is None else s.player for s in self.squares]
        line = " %s | %s | %s \n"
        div = "---+---+---\n"
        formatted = line + div + line + div + line
        print formatted % tuple(vals)

board = Board()
board.display()
