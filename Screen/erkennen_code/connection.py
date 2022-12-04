import pygame as py

class Connection(py.sprite.Sprite):
    def __init__(self, pos_x, pos_y, value, size_mul):
        super().__init__()
        self.grid_size = 15*size_mul

        self.image = py.Surface([self.grid_size, self.grid_size])
        self.image.fill((int(125-value*20),int(125-value*20),int(125-value*20)))
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))

