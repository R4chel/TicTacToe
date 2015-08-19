class Square(object):
    def __init__(self, index):
        self.index = index
        self.player = None

    def claim(self, player):
        assert self.player is None
        self.player = player