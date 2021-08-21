import pygame
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




'''
    playerStand = pygame.image.load('sprite/right/right_1.png')
    background = pygame.image.load('background.png')

    walkRight = [pygame.image.load('sprite/right/right_1.png'),
                 pygame.image.load('sprite/right/right_2.png'),
                 pygame.image.load('sprite/right/right_3.png'),
                 pygame.image.load('sprite/right/right_4.png'),
                 pygame.image.load('sprite/right/right_5.png'),
                 pygame.image.load('sprite/right/right_6.png'),
                 pygame.image.load('sprite/right/right_7.png'),
                 pygame.image.load('sprite/right/right_8.png'),
                 ]

    walkLeft = [pygame.image.load('sprite/left/left_1.png'),
                pygame.image.load('sprite/left/left_2.png'),
                pygame.image.load('sprite/left/left_3.png'),
                pygame.image.load('sprite/left/left_4.png'),
                pygame.image.load('sprite/left/left_5.png'),
                pygame.image.load('sprite/left/left_6.png'),
                pygame.image.load('sprite/left/left_7.png'),
                pygame.image.load('sprite/left/left_8.png'),
                ]

    clock = pygame.time.Clock()

    width = 40
    height = 60
    x = 50
    y = 485 - height
    speed = 10

    isJump = False
    jumpCount = 10

    left = False
    right = False
    animCount = 0

    run = True

    def draw_window():
        global animCount

        win.blit(background, (0, 0))

        if animCount+1 >= 30:
            animCount = 0

        if left:
            win.blit(walkLeft[animCount // 5], (x, y))
            animCount += 1
        elif right:
            win.blit(walkRight[animCount // 5], (x, y))
            animCount += 1
        else:
            win.blit(playerStand, (x, y))

        pygame.display.update()

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and x < 495 - width:
            x += speed
            left = False
            right = True

        elif keys[pygame.K_LEFT] and x > 5:
            x -= speed
            left = True
            right = False

        else:
            left = False
            right = False
            animCount = 0

        if not isJump:
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                isJump = True
        else:
            if jumpCount >= -10:
                if jumpCount < 0:
                    y += (jumpCount ** 2) / 2
                else:
                    y -= (jumpCount ** 2) / 2
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10
        draw_window()

    pygame.quit()

'''