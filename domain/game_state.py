from domain.board import Board


class Player:
    HUMAN = "H"
    COMPUTER = "C"

class Phase:
    PLACING = 1
    DONE = 2

class GameState:
    def __init__(self):
        self.board = Board()
        self.turn = Player.HUMAN
        self.phase = Phase.PLACING
        self.to_place = {Player.HUMAN: 4, Player.COMPUTER: 4}