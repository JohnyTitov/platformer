from types import SimpleNamespace

from sprite_player import SpritePlayer


class Player:

    def __init__(self):
        self.width = 65 #40
        self.height = 96 #60
        self.x = 50
        self.y = 485 - self.height
        self.speed = 10
        self.isJump = False
        self.jumpCount = 10
        self.sprite = SpritePlayer()

    def left(self):
        if self.x > 5:
            self.x -= self.speed
            self._jump()
            self.sprite.left()

    def right(self):
        if self.x < 495 - self.width:
            self.x += self.speed
            self._jump()
            self.sprite.right()

    def stand(self):
        self._jump()
        self.sprite.stand()

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

