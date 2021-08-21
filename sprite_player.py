import pygame


class SpritePlayer:

    def __init__(self):

        self.count_img = 0
        self.side = 'Right'

        self.sprite_right = [
            pygame.image.load('sprite/right/right_1.png'),
            pygame.image.load('sprite/right/right_2.png'),
            pygame.image.load('sprite/right/right_3.png'),
            pygame.image.load('sprite/right/right_4.png'),
            pygame.image.load('sprite/right/right_5.png'),
            pygame.image.load('sprite/right/right_6.png'),
            pygame.image.load('sprite/right/right_7.png'),
            pygame.image.load('sprite/right/right_8.png'),
            ]

        self.sprite_left = [
            pygame.image.load('sprite/left/left_1.png'),
            pygame.image.load('sprite/left/left_2.png'),
            pygame.image.load('sprite/left/left_3.png'),
            pygame.image.load('sprite/left/left_4.png'),
            pygame.image.load('sprite/left/left_5.png'),
            pygame.image.load('sprite/left/left_6.png'),
            pygame.image.load('sprite/left/left_7.png'),
            pygame.image.load('sprite/left/left_8.png'),
            ]

    def right(self):
        if self.count_img >= len(self.sprite_right) - 1:
            self.count_img = 0
        else:
            self.count_img += 1
        self.side = 'Right'

    def left(self):
        if self.count_img >= len(self.sprite_right) - 1:
            self.count_img = 0
        else:
            self.count_img += 1
        self.side = 'Left'

    def get(self):
        if self.side == 'Right':
            return self.sprite_right[self.count_img]
        elif self.side == 'Left':
            return self.sprite_left[self.count_img]
