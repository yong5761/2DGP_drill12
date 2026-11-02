from pico2d import load_image


class Grass2:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,00)

    def update(self):
        pass
