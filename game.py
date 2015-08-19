from board import Board
from player import Player

class Game(object):
    def __init__(self):
        self.players = [Player(1,'X'),Player(2,'O')]

    def start(self):
        print "Welcome to Tic Tac Toe\n"
        board = Board()
        turn = 0
        while not board.is_end_game(self.players):
            board.display()
            print "_________________\n"
            active = self.players[turn % len(self.players)]
            board.claim(active, active.get_valid_move(board))
            turn += 1

game = Game()
game.start()