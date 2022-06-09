import pygame
import random

def main():
    pygame.init()
    pantalla=pygame.display.set_mode((600,480))
    salir=False
    color=(255,064,024)
    reloj1=pygame.time.Clock()
    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
        reloj1.tick(30)
        pantalla.fill(color)
        pygame.display.update()
        print random.randint(0,50)
    
    pygame.quit()

main()