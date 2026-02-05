import unittest

from domain.board import Board
from domain.game_state import Player


class TestBoard(unittest.TestCase):
    def test_row(self):
        b= Board()
        b.place(0, Player.HUMAN)
        b.place(1, Player.HUMAN)
        b.place(2, Player.HUMAN)
        self.assertTrue(b.is_row(1))

if __name__ == '__main__':
    unittest.main()