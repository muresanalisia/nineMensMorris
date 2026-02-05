from domain.game_state import Phase
from services.computer_ai import ComputerAI


class ConsoleUI:

    def __init__(self, service, repo):
        self._service = service
        self._repo = repo
        self._ai = ComputerAI()

    def run(self):
        while not self._service.game_over():
            state=self._repo.get_state()
            print(state.board)

            if state.turn == Player.HUMAN:
                self._human_turn()
            else:
                self._computer_turn()
            self._service.switch_turn()

        print("The game is over")

    def _human_turn(self):
        state= self._repo.get_state()
        try:
            if state.phase == Phase.PLACING:
                pos = int(input("Place at (0-8"))
                row = self._service.place_piece(pos)
            if row:
                self._service.game_over()
        except Exception as e:
            print("Invalid move: ", e)

    def _computer_turn(self):
        state= self.repo.get_state()
        print("Computer turn...")
        if state.phase == Phase.PLACING:
            pos = self._ai.choose_placement(state.board)
            row = self._service.place_piece(pos)
        if row:
            rem = self._service.game_over()



