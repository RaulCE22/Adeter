import pygame
import time
import os

pantalla = pygame.display.set_mode((0,0),pygame.FULLSCREEN) #pygame.FULLSCREEN ( pantalla completa )

im = pygame.image.load('Botones/CuentaAtras4.png')
im =  pygame.transform.scale(im,(1324,1080))
pantalla.blit(im,(0,0))
pygame.display.flip()

pantalla.blit(im,(400,600))
pygame.display.flip()


os.system("raspistill -o f.jpg -w 1920 -h 1080 -t 5000 -p '0,0,1920,1080' -op 200")
im = pygame.image.load('f.jpg')
pantalla.blit(im,(0,0))
pygame.display.flip()

time.sleep(5)
