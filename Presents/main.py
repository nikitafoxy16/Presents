import pygame

from Presents.components.game_status import GameStatus
from Presents.config import Config
from Presents.game_phases import main_menu_phase, gameplay_phase, exit_game_phase
from Presents.global_state import GlobalState
from Presents.services.music_service import MusicService

pygame.init()


FramePerSec = pygame.time.Clock()

def update_game_display():
    pygame.display.update()
    FramePerSec.tick(Config.FPS)


def main():
    while True:
        if GlobalState.GAME_STATE == GameStatus.MAIN_MENU:
            main_menu_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAMEPLAY:
            gameplay_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAME_END:
            exit_game_phase()

        MusicService.start_background_music()
        update_game_display()


if __name__ == "__main__":
    main()