import pygame as py
import os, numpy as np, sys
import connection

cwd = os.getcwd()
cwd = cwd.replace('\erkennen_code','')
cwd += '/'


def add_connecions():
    index = 0
    for i in range(50):
        for j in range(50):
            connection_group.add(connection.Connection(j*grid_size,i*grid_size,int(connection_values[index]),1))
            index += 1


def add_scala():
    j = -6
    for i in range(22):
        scala_group.add(connection.Connection((1.5+i)*grid_size*2,53*grid_size,j,2))

        scale_surf = font.render(str(j), False, 'black')
        scale_surf = py.transform.scale(scale_surf, (grid_size+5, grid_size+5))
        scale_rect = scale_surf.get_rect(topleft = ((1.5+i)*grid_size*2,52*grid_size))
        screen.blit(scale_surf, scale_rect)
 
        j += 0.5

def berechnen():
    v1 = 'Bilder/viereck_1.txt'
    v2 = 'Bilder/viereck_2.txt'
    v3 = 'Bilder/viereck_3.txt'
    v4 = 'Bilder/viereck_4.txt'
    k1 = 'Bilder/kreis_1.txt'
    k2 = 'Bilder/kreis_2.txt'
    k3 = 'Bilder/kreis_3.txt'
    k4 = 'Bilder/kreis_4.txt'
    image_sauce = [v1,v2,v3,v4,k1,k2,k3,k4]

    current_screen = []
    np_connection_values = np.array(connection_values, float)

    for x in range(18):
        durchgang = []
        for index in range(8):
            with open(cwd+image_sauce[index], 'r') as filehandle:
                for line in filehandle:
                    currentnum = line[:-1]
                    current_screen.append(int(currentnum))

            np_current_screen = np.array(current_screen)
            np_current_screen = np_current_screen/255

            Zwischenrgebniss = np_current_screen * np_connection_values
            Ergebniss = np.sum(Zwischenrgebniss)

            if Ergebniss<1 and index>3:# zeigt Viereck als Ergebniss aber sieht Kreis Folge Kreis wird hinzugefügt E muss kleiner 1
                for i in range(len(np_connection_values)):
                    if np_current_screen[i]==1: np_connection_values[i] = np_connection_values[i]+0.5
            if Ergebniss>1 and index<4:# zeigt Kreis als Ergebniss aber sieht Viereck Folge Viereck wird abgezogen E muss kleiner 1
                for i in range(len(np_connection_values)):
                    if np_current_screen[i]==1: np_connection_values[i] = np_connection_values[i]-0.5

            if (Ergebniss<1 and index<4) or (Ergebniss>1 and index>3): correctness = "Richtig"
            else: correctness = "Falsch"
            if index<4: Bild = " Viereck"
            else: Bild= " Kreis"
            if Ergebniss<1:print(str(Ergebniss)+" Viereck "+correctness+Bild+ str(index))
            else: print(str(Ergebniss)+" Kreis "+correctness+Bild+ str(index))
                
            current_screen = []
            durchgang.append(np_connection_values.tolist())
        zwischenergebnisse.append(durchgang)    


    np.set_printoptions(threshold=sys.maxsize)
    np.set_printoptions(suppress=True)
    #print(np_connection_values)
    print(np_connection_values.min())

    with open(cwd+r'connections\finall.txt', 'w') as filehandle:
        for listofnum in np_connection_values:
            filehandle.write('%s\n' % str(listofnum))

py.init()

grid_size = 15
clock = py.time.Clock()
screen = py.display.set_mode((grid_size*50,grid_size*55))
screen.fill((102, 98, 93))

zwischenergebnisse = []

connection_group = py.sprite.Group()
scala_group = py.sprite.Group()

font = py.font.Font(cwd+'Pixeltype.ttf', 50)

connection_values = []
with open(cwd + 'connections\Test.txt', 'r') as filehandle:    #leere liste
#with open(cwd + r'connections\finall.txt', 'r') as filehandle:  #fertige Liste
    for line in filehandle:
        currentnum = line[:-1]
        connection_values.append(float(currentnum))


add_scala()
berechnen()

add_connecions()

Bildnummer = 0
Durchgang = 0

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()

    scala_group.draw(screen)

    if Durchgang<len(zwischenergebnisse):
        index = 0
        for i in range(50):
            for j in range(50):
                connection_group.add(connection.Connection(j*grid_size,i*grid_size,int(zwischenergebnisse[Durchgang][Bildnummer][index]),1))
                index += 1
        connection_group.draw(screen)
        py.time.wait(200)
        connection_group.empty()
        if Bildnummer == 7:
            Bildnummer = 0
            Durchgang += 1
        Bildnummer += 1

    
    #connection_group.draw(screen)

    py.display.update()
    clock.tick(60) 