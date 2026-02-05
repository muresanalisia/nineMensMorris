from domain.game_state import Player


class GameService:
    def __init__(self, repo):
        self.repo = repo

    def place_piece(self, pos):
        state = self._repo.get_state()
        state.baord.place(pos, state.turn)
        state.to_place[state.turn] -=1
        row= state.board.is_row(pos, state.turn)

        if state.to_place[Player.HUMAN] == 0 and state.to_place[Player.HUMAN] == 0:
            state.phase = Phase.DONE
        return row

    def move_piece(self, pos):
        state= self.repo.get_state()
        state.baord.move(pos, state.turn)
        return state.board.is_row(pos, state.turn)

    def switch_turn(self):
        state= self.repo.get_state()
        state.turn = Player.Computer if state.turn == Player.HUMAN else Player.HUMAN

    def game_over(self):
        state= self.repo.get_state()
        return state.board.piece_count(Player.HUMAN) == 0 or \
            state.board.piece_count(Player.COMPUTER) == 0