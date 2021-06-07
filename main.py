import pygame
pygame.init()
##################
Width = 800
Height = 600
screen = pygame.display.set_mode((Width,Height))
title = pygame.display.set_caption("Plants VS Zombies")
icon = pygame.image.load("icon.ico")
pygame.display.set_icon(icon)
#############menu#############
menuimg = pygame.image.load("assets/images/menubox.png")
menux = 400
menuy = 300
def MenuboxChange(x,y):
  screen.blit(menuimg,(x,y))
