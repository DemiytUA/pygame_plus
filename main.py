import pygame
from pygame_plus import scripts



WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caption")
clock = pygame.time.Clock()




running = True
while running:


    # your code here



    pygame.display.flip()


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
pygame.quit()