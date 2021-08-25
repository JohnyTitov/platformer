# Класс запоминающий активную сторону

class Side:
    LEFT = False
    RIGHT = True

    def __init__(self):
        self.side = self.RIGHT

    def go_right(self):
        self.side = self.RIGHT

    def go_left(self):
        self.side = self.LEFT

    def is_right(self):
        return self.side == self.RIGHT

    def is_left(self):
        return self.side == self.LEFT
