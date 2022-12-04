import pygame as py

class Pixel(py.sprite.Sprite):
    def __init__(self, pos_x, pos_y, brightness):
        super().__init__()
        self.grid_size = 15

        self.image = py.Surface([self.grid_size, self.grid_size])
        self.image.fill((brightness,brightness,brightness))
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))

    def collision(self,current_screen):
        mouse_presses = py.mouse.get_pressed()
        if mouse_presses[0]:
            if self.rect.collidepoint((py.mouse.get_pos())):
                self.image.fill((0,0,0))
                current_screen[int((self.rect.y/self.grid_size*50)+(self.rect.x/self.grid_size))] = '000'
        if mouse_presses[2]:
            if self.rect.collidepoint((py.mouse.get_pos())):
                self.image.fill((255,255,255))
                current_screen[int((self.rect.y/self.grid_size*50)+(self.rect.x/self.grid_size))] = '255'

    def update(self,current_screen):
        self.collision(current_screen)