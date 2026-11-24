from engi1020.arduino.api import *
from time import sleep

IN1 = 8
IN2 = 9
IN3 = 10
IN4 = 11


class MotorSystem():
    def __init__(self, in1, in2, in3, in4):
        self.m = (in1, in2, in3, in4)
        self.pin_vals = ()
        self.movement = ""

    def move(self):
        getattr(self, self.movement)
        for i in range(len(self.pin_vals)):
            digital_write(self.m[i], self.pin_vals[i])

    def forward(self):
        self.pin_vals = (1,0,1,0)

    def backward(self):
        self.pin_vals = (0,1,0,1)

    def stop(self):
        self.pin_vals = (0,0,0,0)

    def right(self):
        self.pin_vals = (1,0,0,1)

    def left(self):
        self.pin_vals = (0,1,1,0)

motors = MotorSystem(IN1, IN2, IN3, IN4)
motors.movement = "forward"
motors.move()
sleep(1)
motors.movement = "stop"
motors.move()

# sleep(2)
# motors.right()
# sleep(2)
# motors.stop()

# #Turn both motors in the same direction
# digital_write(IN1, True)
# digital_write(IN2, False)
# digital_write(IN3, True)
# digital_write(IN4, False)
# sleep(2)
# Other direction
# digital_write(IN1, False)
# digital_write(IN2, True)
# digital_write(IN3, False)
# digital_write(IN4, True)
# sleep(2)
# #Stop both motors
# digital_write(IN1, False)
# digital_write(IN2, False)
# digital_write(IN3, False)
# digital_write(IN4, False)
# #Turn Right
