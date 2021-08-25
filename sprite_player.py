import pygame


class SpritePlayer:

    def __init__(self):

        self.count_img = 0
        self.side = 'Right'

        self.sprite_right = [pygame.image.load(f'sprite/run/right/run_{x}.png') for x in range(1, 9)]
        self.sprite_left = [pygame.image.load(f'sprite/run/left/run_{x}.png') for x in range(1, 9)]
        self.sprite_stand = [pygame.image.load(f'sprite/stand/right/stand_{x}.png') for x in range(1, 9)]

    def right(self):
        if self.count_img >= len(self.sprite_right) - 1:
            self.count_img = 0
        else:
            self.count_img += 1
        self.side = 'Right'

    def left(self):
        if self.count_img >= len(self.sprite_left) - 1:
            self.count_img = 0
        else:
            self.count_img += 1
        self.side = 'Left'

    def stand(self):
        if self.count_img >= len(self.sprite_stand) - 1:
            self.count_img = 0
        else:
            self.count_img += 1
        self.side = 'Stand'

    def get(self):
        if self.side == 'Right':
            return self.sprite_right[self.count_img]
        elif self.side == 'Left':
            return self.sprite_left[self.count_img]
        elif self.side == 'Stand':
            return self.sprite_stand[self.count_img]
