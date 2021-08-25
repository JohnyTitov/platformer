import pygame
from collections import Counter


class SpritePlayer:

    def __init__(self):
        # счётчик анимации
        self.count = Counter({'run_right': 0, 'run_left': 0, 'stand_right': 0, 'stand_left': 0})

        # спрайты бега
        self.run_right = [pygame.image.load(f'sprite/run/right/run_{x}.png') for x in range(1, 9)]
        self.run_left = [pygame.image.load(f'sprite/run/left/run_{x}.png') for x in range(1, 9)]

        # спрайты стойки на месте
        self.stand_right = [pygame.image.load(f'sprite/stand/right/stand_{x}.png') for x in range(1, 9)]
        self.stand_left = [pygame.image.load(f'sprite/stand/left/stand_{x}.png') for x in range(1, 9)]

        self.buf_img = self.stand_right[0]

    def _update(self, name_sprite):

        sprites = {
            'run_right': self.run_right,
            'run_left': self.run_left,
            'stand_right': self.stand_right,
            'stand_left': self.stand_left,
        }
        # получить набор слайдов для текущего движения
        this_sprites = sprites[name_sprite]

        # получить счётчик для текущего набора слайдов
        this_count = self.count[name_sprite]

        if this_count < len(this_sprites) - 1:
            self.count.update({name_sprite: 1})
            self.buf_img = this_sprites[this_count]
        else:
            self.count[name_sprite] = 0

    def run(self, side, is_jump):
        if is_jump:
            return
        if side.is_right():
            self._update('run_right')
        elif side.is_left():
            self._update('run_left')

    def stand(self, side, is_jump):
        if is_jump:
            return
        if side.is_right():
            self._update('stand_right')
        elif side.is_left():
            self._update('stand_left')

    def get(self):
        return self.buf_img
