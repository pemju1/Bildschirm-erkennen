import pygame as py
import os

class Pixel(py.sprite.Sprite):
    def __init__(self, pos_x, pos_y, brightness):
        super().__init__()
        # self.rect = py.Rect(pos_x,pos_y,grid_size,grid_size)
        # self.image = py.draw.rect(screen,(brightness,brightness,brightness),self.rect)

        self.image = py.Surface([grid_size, grid_size])
        self.image.fill((brightness,brightness,brightness))
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))

    def collision(self):
        mouse_presses = py.mouse.get_pressed()
        if mouse_presses[0]:
            if self.rect.collidepoint((py.mouse.get_pos())):
                self.image.fill((0,0,0))
                current_screen[int((self.rect.y/grid_size*50)+(self.rect.x/grid_size))] = '000'

    def update(self):
        self.collision()

def add_pixel():
    index = 0
    for i in range(50):
        for j in range(50):
            pixel_group.add(Pixel(j*grid_size,i*grid_size,int(start_screen[index])))
            index += 1



py.init()

cwd = os.getcwd()#current working directory
cwd = cwd+'/'


clock = py.time.Clock()
test_font = py.font.Font(cwd+'Pixeltype.ttf', 50)

grid_size = 15
screen = py.display.set_mode((grid_size*50,grid_size*55))
screen.fill((102, 98, 93))

# Rect = py.Rect(50,50,50,50)
# py.draw.rect(screen,(0,0,0),Rect)

pixel_group = py.sprite.Group()

start_screen = []
for i in range(50):
    for j in range(50):
        start_screen.append(255)

add_pixel()

current_screen = []
for i in range(50):
    for j in range(50):
        current_screen.append(255)


reset_button_image = py.Surface([7*grid_size, 3*grid_size])
reset_button_image.fill((40, 125, 94))
reset_button_rect = reset_button_image.get_rect(topleft=(1*grid_size, 51*grid_size))
screen.blit(reset_button_image, reset_button_rect)

reset_text_surf = test_font.render('Reset', False, 'black')
reset_text_surf = py.transform.scale(reset_text_surf, (7*grid_size, 3*grid_size))
reset_text_rect = reset_text_surf.get_rect(topleft = (1*grid_size+3, 51*grid_size+7))
screen.blit(reset_text_surf,reset_text_rect)

appendlist_buton_surf = py.Surface([7*grid_size, 3*grid_size])
appendlist_buton_surf.fill((40, 125, 94))
appendlist_buton_rect = appendlist_buton_surf.get_rect(topleft=(40*grid_size, 51*grid_size))
screen.blit(appendlist_buton_surf, appendlist_buton_rect)

appendlist_text_surf = test_font.render('append', False, 'black')
appendlist_text_surf = py.transform.scale(appendlist_text_surf, (7*grid_size, 3*grid_size))
appendlist_text_rect = appendlist_text_surf.get_rect(topleft = (40*grid_size+1, 51*grid_size+2))
screen.blit(appendlist_text_surf,appendlist_text_rect)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.MOUSEBUTTONDOWN:
                if reset_button_rect.collidepoint(event.pos):
                    pixel_group.empty()
                    add_pixel()
                    current_screen = start_screen.copy()
        if event.type == py.MOUSEBUTTONDOWN:
                if appendlist_buton_rect.collidepoint(event.pos):
                    pixel_group.empty()
                    start_screen = current_screen.copy()
                    add_pixel()

    pixel_group.draw(screen)
    pixel_group.update()  
    

    py.display.update()
    clock.tick(60) 