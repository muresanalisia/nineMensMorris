from domain.game_state import GameState
from repository.game_repository import GameRepository
from services.game_services import GameService
from ui.console_ui import ConsoleUI


def main():
    state = GameState()
    repo = GameRepository(state)
    service=GameService(repo)
    ui = ConsoleUI(service, repo)
    ui.run()

if __name__ == '__main__':
    main()