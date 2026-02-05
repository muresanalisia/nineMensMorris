from domain.exceptions import GameError


class Board:

    ROWS = [
        (0, 1, 2),
        (0, 3, 4),
        (0, 4, 5),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 7),
        (2, 4, 6)
    ]

    def __init__(self):
        self._cells = [None] * 9

    def place(self, pos, player):
        if self._cells[pos] is not None:
            raise GameError("Position is occupied")
        self._cells[pos] = player

    def move(self, pos, player):
        if self._cells[pos] is not None:
            raise GameError("Position is occupied")
        self._cells[pos] = player

    def empty_positions(self):
        return [i for i,v in enumerate(self._cells) if v is None]

    def positions_of(self, player):
        return [i for i,v in enumerate(self._cells) if v == player]

    def piece_count(self, player):
        return len(self.positions_of(player))

    def copy(self):
        b= Board()
        b._cells = self._cells[:]
        return b

    def __str__(self):
        return str(self._cells)

