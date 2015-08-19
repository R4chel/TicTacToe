from player import Player
from square import Square

solutions = [
    set([0,1,2]), set([3,4,5]), set([6,7,8]),
    set([0,3,6]), set([1,4,7]), set([2,5,8]),
    set([0,4,8]), set([2,4,6])
]

class Board(object):
    def __init__(self):
        self.squares = [Square(i) for i in range(9)]

    def valid_squares(self):
        return [s.index for s in self.squares if s.player is None]

    def display(self):
        vals = [str(s.index) if s.player is None else s.player.symbol for s in self.squares]
        line = " %s | %s | %s \n"
        div = "---+---+---\n"
        formatted = line + div + line + div + line
        print formatted % tuple(vals)

    def claim(self, player, index):
        self.squares[index].claim(player)

    def is_end_game(self, players):
        for player in players:
            players_squares = [s.index for s in self.squares if s.player is player]
            if any([solution <= players_squares for solution in solutions]):
                print "Congradulations Player %i! You won!\n" % player.index
                return True
        if len(self.valid_squares()) is 0:
            print "TIE GAME!\n"
            return True
        return False

board = Board()
board.display()
player = Player(1,'X')
board.claim(player, player.get_valid_move(board))
board.display()