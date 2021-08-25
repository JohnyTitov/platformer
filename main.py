from types import SimpleNamespace

from window import Window
from player import Player

if __name__ == '__main__':

    # Настройки игры
    setting_win = SimpleNamespace(name="Dante's hell",      # название игры
                                  resolution=(500, 500),    # разрешение окна
                                  fps=30)                   # частота кадров

    win = Window(setting_win)       # Игровое окно
    player = Player()               # Игрок

    while True:
        if not win.refresh(player):
            break
