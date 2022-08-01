import pygame, sys, pygame.freetype
from shader import Shader, VIRTUAL_RES

FPS = 120

font = pygame.freetype.SysFont(None, 20)
clock = pygame.time.Clock()
loadedImage = pygame.transform.scale(pygame.image.load("image.png"), VIRTUAL_RES)
screen = pygame.Surface(VIRTUAL_RES).convert((255, 65280, 16711680, 0))

screen.blit(loadedImage, (0,0))
shader = Shader(screen)

while True:
   font.render_to(screen, (5, 5), str(int(clock.get_fps())), (0, 0, 0), (255, 255, 255))
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
   shader()
   clock.tick(FPS)