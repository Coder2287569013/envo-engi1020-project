import pygame
from engi1020.arduino.api import *

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Car Controller')


class MotorSystem:
    def __init__(self, in1, in2, in3, in4):
        self.m1 = (in1, in2)
        self.m2 = (in3, in4)

    def forward(self):
        digital_write(self.m1[0], True)
        digital_write(self.m1[1], False)
        digital_write(self.m2[0], True)
        digital_write(self.m2[1], False)

    def backward(self):
        digital_write(self.m1[0], False)
        digital_write(self.m1[1], True)
        digital_write(self.m2[0], False)
        digital_write(self.m2[1], True)

    def stop(self):
        digital_write(self.m1[0], False)
        digital_write(self.m1[1], False)
        digital_write(self.m2[0], False)
        digital_write(self.m2[1], False)

    def right(self):
        digital_write(self.m1[0], True)
        digital_write(self.m1[1], False)
        digital_write(self.m2[0], False)
        digital_write(self.m2[1], True)

    def left(self):
        digital_write(self.m1[0], False)
        digital_write(self.m1[1], True)
        digital_write(self.m2[0], True)
        digital_write(self.m2[1], False)
in1 = 8
in2 = 9
in3 = 10
in4 = 11

motors = MotorSystem(in1, in2, in3, in4)

font = pygame.font.Font(None, 42)
current_direction = "Waiting for input..."

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        current_direction = "Forward"
        motors.forward()

    elif keys[pygame.K_s]:
        current_direction = "Backward"
        motors.backward()

    elif keys[pygame.K_a]:
        current_direction = "Left"
        motors.left()

    elif keys[pygame.K_d]:
        current_direction = "Right"
        motors.right()

    else:
        current_direction = "Stopped"
        motors.stop()

    screen.fill((0, 0, 0))

    text = font.render(current_direction, True, (255, 255, 255))
    screen.blit(text, (100, 130))

    pygame.display.update()

motors.stop()
pygame.quit()
