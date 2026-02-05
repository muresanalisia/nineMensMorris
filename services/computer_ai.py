import random
from domain.game_state import Player


class ComputerAI:
    def choose_placement(self, board):
        for pos in board.empty_positions():
            test=board.copy()
            test.place(pos, Player.COMPUTER)
            if test.is_row(pos, Player.COMPUTER):
                return pos

        for pos in board.empty_positions():
            test=board.copy()
            test.place(pos, Player.HUMAN)
            if test.is_mill(pos, Player.HUMAN):
                return pos

        return random.choice(board.empty_positions())
