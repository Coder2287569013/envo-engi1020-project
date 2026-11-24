#Note: we could continue using pygame for processing inputs, or switch to "keyboard" lib. - Vlad
import pygame
from motor_test import motor_sys

cell_size = 128
width = 5
height = 5

class MoveCell():
    def __init__(self,x,y,w,h,color):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = color
    def display(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

pygame.init()
screen = pygame.display.set_mode((width*cell_size, height*cell_size))
pygame.display.set_caption("Movement")
clock = pygame.time.Clock()

forward_cell = MoveCell(2*cell_size, cell_size, cell_size, cell_size, (255,0,0))
backward_cell = MoveCell(2*cell_size, 3*cell_size, cell_size, cell_size, (255,0,0))
left_cell = MoveCell(cell_size, 2*cell_size, cell_size, cell_size, (255,0,0))
right_cell = MoveCell(3*cell_size, 2*cell_size, cell_size, cell_size, (255,0,0))

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                forward_cell.color = (0,255,0)
                motor_sys.forward()
            elif event.key == pygame.K_s:
                backward_cell.color = (0,255,0)
                motor_sys.backward()
            elif event.key == pygame.K_a:
                left_cell.color = (0,255,0)
                motor_sys.left()
            elif event.key == pygame.K_d:
                right_cell.color = (0,255,0)
                motor_sys.right()
            motor_sys.move()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                forward_cell.color = (255,0,0)
            elif event.key == pygame.K_s:
                backward_cell.color = (255,0,0)
            elif event.key == pygame.K_a:
                left_cell.color = (255,0,0)
            elif event.key == pygame.K_d:
                right_cell.color = (255,0,0)
            motor_sys.stop()
            motor_sys.move()

    pygame.display.update()

    forward_cell.display(screen)
    backward_cell.display(screen)
    left_cell.display(screen)
    right_cell.display(screen)

    clock.tick(60)