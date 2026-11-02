import game_world
from pico2d import load_image, get_canvas_width


class Ball:
    def __init__(self, x, y, dx):
        self.x = x
        self.y = y
        self.dx = dx
        self.image = load_image('ball21x21.png')

    def update(self):
        self.x += self.dx
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
