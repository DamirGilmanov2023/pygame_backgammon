import pygame
import pygame as pg
import sys
import os
import random
#import matplotlib.pyplot as plt
import asyncio

pg.init()
clock = pg.time.Clock()
FPS = 30
WINDOW_SIZE = (900, 1055)
fon = pg.image.load('nardy15.jpg') 
shahkaw = []
shahkab = []
x=[47, 106, 166, 226, 286, 346, 406, 485, 545, 605, 665, 725, 785, 845]
y=[37, 97, 158, 219, 280, 341, 402, 463, 524, 585, 646, 707, 768, 829, 890, 951, 1012]
shashkiw = 15
shashkib = 15
image_pos=[]
image_posb=[]
#[(1,0),(0,2)]


for i in range(shashkiw):
    shahkaw.append(pg.image.load('shashkaw.png'))
for i in range(shashkib):
    shahkab.append(pg.image.load('shashkab.png'))



(a,b) = (440,527)
(c, d) = (440,420)
r=0
r1=0
back = (150, 90, 30)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
YELLOW = (255, 255, 0)
RED = (255,0,0)

sc = pg.display.set_mode(WINDOW_SIZE)
#image_posb = ((sc.get_width() - shahkab.get_width())/2, (sc.get_height() - shahkab.get_height())/2)
#image_pos = ((sc.get_width() - shahkaw.get_width())/4, (sc.get_height() - shahkaw.get_height())/4)

d_i=len(y)-2
for i in range(15):
    image_pos.append((47,y[d_i]))
    d_i-=1

d_i=0
for i in range(15):
    image_posb.append((785,y[d_i]))
    d_i+=1
doMove = None
doMove2 = None


run = True
async def main():
    global doMove,doMove2,r,r1
    while run:
        sc.blit(fon, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                #run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pg.mouse.get_pos()
                if event.button == 1:
                    for i in range(15):
                        if ((image_pos[i][0]+31-mouse_x)**2+(image_pos[i][1]+31-mouse_y)**2)<=31**2:
                            doMove=i
                            break
                        else:
                            doMove=None
                    for i in range(15):
                        if ((image_posb[i][0]+31-mouse_x)**2+(image_posb[i][1]+31-mouse_y)**2)<=31**2:
                            doMove2=i
                            break
                        else:
                            doMove2=None
            if event.type == pygame.MOUSEBUTTONUP: 
                doMove = None
                doMove2 = None
        if doMove!=None:
            for i in range(15):
                if doMove==i:
                    mouse_x,mouse_y=pg.mouse.get_pos()
                    image_pos[i] = (mouse_x-31,mouse_y-31)
        if doMove2!=None:
            for i in range(15):
                if doMove2==i:
                    mouse_x,mouse_y=pg.mouse.get_pos()
                    image_posb[i] = (mouse_x-31,mouse_y-31)

        for i in range(len(x)):
            pg.draw.line(sc,BLACK,[x[i],y[0]],[x[i],y[len(y)-1]],3)
        for i in range(len(y)):
            pg.draw.line(sc,BLACK,[x[0],y[i]],[x[len(x)-1],y[i]],3)


        for itert in range(15):
            image_posx, image_posy = image_pos[itert]
            image_posbx, image_posby = image_posb[itert]
            i=0
            while i<len(x)-1:
                j=0
                while j<len(y)-1:
                    if x[i]<image_posx and image_posx<x[i+1] and y[j]<image_posy and image_posy<y[j+1]:
                        image_pos[itert] = (x[i], y[j])
                        i=len(x)
                        break
                    j+=1
                i+=1
            i=0
            while i<len(x)-1:
                j=0
                while j<len(y)-1:
                    if x[i]<image_posbx and image_posbx<x[i+1] and y[j]<image_posby and image_posby<y[j+1]:
                        image_posb[itert] = (x[i], y[j])
                        i=len(x)
                        break
                    j+=1
                i+=1
        
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                r=random.randint(1,6)
                r1=random.randint(1,6)
        if r==1:
            pygame.draw.rect(sc, WHITE, [a-30, b-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [a,b,15,15])
        elif r==2:
            pygame.draw.rect(sc, WHITE, [a-30, b-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [a-20,b,15,15])
            pygame.draw.rect(sc, BLACK, [a+20,b,15,15])
        elif r==3:
            pygame.draw.rect(sc, WHITE, [a-30, b-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [a,b-20,15,15])
            pygame.draw.rect(sc, BLACK, [a,b,15,15])
            pygame.draw.rect(sc, BLACK, [a,b+20,15,15])
        elif r==4:
            pygame.draw.rect(sc, WHITE, [a-30, b-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [a-30,b-20,15,15])
            pygame.draw.rect(sc, BLACK, [a+30,b-20,15,15])
            pygame.draw.rect(sc, BLACK, [a+30,b+20,15,15])
            pygame.draw.rect(sc, BLACK, [a-30,b+20,15,15])
        elif r==5:
            pygame.draw.rect(sc, WHITE, [a-30, b-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [a,b,15,15])
            pygame.draw.rect(sc, BLACK, [a-30,b-20,15,15])
            pygame.draw.rect(sc, BLACK, [a+30,b-20,15,15])
            pygame.draw.rect(sc, BLACK, [a+30,b+20,15,15])
            pygame.draw.rect(sc, BLACK, [a-30,b+20,15,15])
        elif r==6:
            pygame.draw.rect(sc, WHITE, [a-30, b-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [a,b+20,15,15])
            pygame.draw.rect(sc, BLACK, [a,b-20,15,15])
            pygame.draw.rect(sc, BLACK, [a-30,b-20,15,15])
            pygame.draw.rect(sc, BLACK, [a+30,b-20,15,15])
            pygame.draw.rect(sc, BLACK, [a+30,b+20,15,15])
            pygame.draw.rect(sc, BLACK, [a-30,b+20,15,15])
        else:
            pass

        if r1==1:
            pygame.draw.rect(sc, WHITE, [c-30, d-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [c,d,15,15])
        elif r1==2:
            pygame.draw.rect(sc, WHITE, [c-30, d-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [c-20,d,15,15])
            pygame.draw.rect(sc, BLACK, [c+20,d,15,15])
        elif r1==3:
            pygame.draw.rect(sc, WHITE, [c-30, d-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [c,d-20,15,15])
            pygame.draw.rect(sc, BLACK, [c,d,15,15])
            pygame.draw.rect(sc, BLACK, [c,d+20,15,15])
        elif r1==4:
            pygame.draw.rect(sc, WHITE, [c-30,d-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [c-30,d-20,15,15])
            pygame.draw.rect(sc, BLACK, [c+30,d-20,15,15])
            pygame.draw.rect(sc, BLACK, [c+30,d+20,15,15])
            pygame.draw.rect(sc, BLACK, [c-30,d+20,15,15])
        elif r1==5:
            pygame.draw.rect(sc, WHITE, [c-30, d-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [c,d,15,15])
            pygame.draw.rect(sc, BLACK, [c-30,d-20,15,15])
            pygame.draw.rect(sc, BLACK, [c+30,d-20,15,15])
            pygame.draw.rect(sc, BLACK, [c+30,d+20,15,15])
            pygame.draw.rect(sc, BLACK, [c-30,d+20,15,15])
        elif r1==6:
            pygame.draw.rect(sc, WHITE, [c-30, d-30, 70, 70])
            pygame.draw.rect(sc, BLACK, [c,d+20,15,15])
            pygame.draw.rect(sc, BLACK, [c,d-20,15,15])
            pygame.draw.rect(sc, BLACK, [c-30,d-20,15,15])
            pygame.draw.rect(sc, BLACK, [c+30,d-20,15,15])
            pygame.draw.rect(sc, BLACK, [c+30,d+20,15,15])
            pygame.draw.rect(sc, BLACK, [c-30,d+20,15,15])
        else:
            pass
            
        for i in range(15):
            sc.blit(shahkaw[i], image_pos[i])
            sc.blit(shahkab[i], image_posb[i])

        clock.tick(FPS)
        pg.display.update()
        await asyncio.sleep(0)

asyncio.run(main())
