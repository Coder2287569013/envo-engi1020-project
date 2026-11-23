#Note: we could continue using pygame for processing inputs, or switch to "keyboard" lib. - Vlad
import pygame

pygame.init()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        print('forwards')
    elif keys[pygame.K_s]:
        print('backwards')

    clock.tick(60)