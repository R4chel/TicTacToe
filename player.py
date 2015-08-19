class Player(object):
    def __init__(self, index, symbol):
        self.index = index
        self.symbol = symbol

    def get_valid_move(self, board):
        valid_squares = board.valid_squares()
        move = raw_input( "Player %i choose a square:\n" % self.index)
        while not move.isdigit() or int(move) not in valid_squares:
            move = raw_input("Invalid input.\nValid squares are: " + str(valid_squares)+ "\nPlayer " + str(self.index) + " choose a square:\n" )
        return int(move)

