import pygame


class Window:

    def __init__(self, setting):
        pygame.init()
        pygame.display.set_caption(setting.name)                    # заголовок с названием
        self.win = pygame.display.set_mode(setting.resolution)      # окно
        self.fps = setting.fps                                      # частота кадров

        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('background.png')

    # Обновление окна
    def refresh(self, player):
        self.clock.tick(self.fps)

        # если нажат выход - зкарыть окно
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        # получить нажатые кнопки
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
            player.stand()

        elif keys[pygame.K_RIGHT]:
            player.right()

        elif keys[pygame.K_LEFT]:
            player.left()

        else:
            player.stand()

        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            player.jump()

        # получить спрайт игрока на текущий момент
        sprite = player.get_img()

        self.win.blit(self.background, (0, 0))      # отобразить фон
        self.win.blit(sprite.img, sprite.point)     # отобразить игрока
        pygame.display.update()

        return True
