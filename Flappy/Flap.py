import pygame as pg
pg.init()
screen = pg.display.set_mode((700,700))
pg.display.set_caption('Flap')
clock = pg.time.Clock()
bg = pg.image.load(r'files/background-day.png')
crashed = False
while not crashed:
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            crashed = True
    pg.display.update()
    clock.tick(120)
