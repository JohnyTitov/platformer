import pygame
from collections import Counter


class SpritePlayer:

    def __init__(self):
        # счётчик анимации
        self.count = Counter()

        # спрайты бега
        self.run_right = [pygame.image.load(f'sprite/run/right/run_{x}.png') for x in range(1, 9)]
        self.run_left = [pygame.image.load(f'sprite/run/left/run_{x}.png') for x in range(1, 9)]

        # спрайты стойки на месте
        self.stand_right = [pygame.image.load(f'sprite/stand/right/stand_{x}.png') for x in range(1, 9)]
        self.stand_left = [pygame.image.load(f'sprite/stand/left/stand_{x}.png') for x in range(1, 9)]

        # спрайты прыжка
        self.jump_right = [pygame.image.load(f'sprite/jump/right/jump_{x}.png') for x in range(1, 3)]
        self.jump_left = [pygame.image.load(f'sprite/jump/left/jump_{x}.png') for x in range(1, 3)]

        self.buf_img = self.stand_right[0]

    def _update(self, name):

        sprites = {
            'run_right': self.run_right,
            'run_left': self.run_left,
            'stand_right': self.stand_right,
            'stand_left': self.stand_left,
            'jump_right': self.jump_right,
            'jump_left': self.jump_left,
        }
        # получить набор спрайтов для текущего движения
        this_sprites = sprites[name]

        # получить счётчик для текущего набора спрайтов
        this_count = self.count[name]

        if this_count < len(this_sprites) - 1:
            self.count.update({name: 1})
            self.buf_img = this_sprites[this_count]
        else:
            self.count[name] = 0

    def run(self, side, is_jump):
        name = 'jump' if is_jump else 'run'
        name += '_right' if side.is_right() else '_left'
        self._update(name)

    def stand(self, side, is_jump):
        name = 'jump' if is_jump else 'stand'
        name += '_right' if side.is_right() else '_left'
        self._update(name)

    def get(self):
        return self.buf_img
