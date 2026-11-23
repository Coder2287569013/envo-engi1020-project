import pygame

pygame.init()

while True:
    keys = pygame.key.get_pressed()

    pygame.event.pump

    if keys[pygame.K_w]:
        print('forwards')
    elif keys[pygame.K_s]:
        print('backwards')

