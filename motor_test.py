from engi1020.arduino.api import *
# from time import sleep

# IN1 = 8
# IN2 = 9
# IN3 = 10
# IN4 = 11


class MotorSystem():
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

# motors = MotorSystem(IN1, IN2, IN3, IN4)
# motors.forward()
# sleep(1)
# motors.stop()

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
