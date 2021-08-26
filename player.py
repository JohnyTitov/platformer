from types import SimpleNamespace

from sprite_player import SpritePlayer
from side import Side


class Player:

    def __init__(self):
        self.width = 65
        self.height = 96
        self.x = 50
        self.y = 485 - self.height
        self.speed = 10
        self.isJump = False
        self.jumpCount = 10
        self.sprite = SpritePlayer()        # визуальное представление игрока
        self.side = Side()                  # активная сторона

    def left(self):
        self.side.go_left()

    def right(self):
        self.side.go_right()

    def run(self):
        if self.side.is_right():
            if self.x < 495 - self.width:
                self.x += self.speed
            self._jump()
            self.sprite.run(self.side, self.isJump)

        elif self.side.is_left():
            if self.x > 5:
                self.x -= self.speed
            self._jump()
            self.sprite.run(self.side, self.isJump)

    def stand(self):
        self._jump()
        self.sprite.stand(self.side, self.isJump)

    def jump(self):
        if not self.isJump:
            self.isJump = True

    # гравитация при прыжке
    def _jump(self):
        if not self.isJump:
            return

        if self.jumpCount >= -10:
            if self.jumpCount < 0:
                self.y += (self.jumpCount ** 2) / 2
            else:
                self.y -= (self.jumpCount ** 2) / 2
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 10

    # Получение картинки
    def get_img(self):
        image_ = SimpleNamespace(
            img=self.sprite.get(),
            point=(self.x, self.y),
            )
        return image_

