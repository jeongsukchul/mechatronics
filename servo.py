from gpiozero import AngularServo
import time

class Servo:

    def __init__(self,pin1,pin2,pin3):
        servo_pin1 = pin1
        servo_pin2 = pin2
        servo_pin3 = pin3

        # Set the pulse width range of the PWM signal
        pulse_width_min = 0  # in degrees
        pulse_width_max = 180  # in degrees

        # Create an AngularServo object with the specified pin and pulse width range
        self.servo1 = AngularServo(servo_pin1, min_angle=pulse_width_min, max_angle=pulse_width_max)
        self.servo2 = AngularServo(servo_pin2, min_angle=pulse_width_min, max_angle=pulse_width_max)
        self.servo3 = AngularServo(servo_pin3, min_angle=pulse_width_min, max_angle=pulse_width_max)
        # Move the servo to its minimum angle (0 degrees)
        self.servo1.angle = 0
        self.servo2.angle = 0
        self.servo3.angle = 0
    def move(self,n,sig):
        if n==1:
            servo = self.servo1
        if n==2:
            servo = self.servo2
        if n==3:
            servo = self.servo3

        if sig==1:
            servo.angle = 180
        else:
            servo.angle = 0

        # we have to update this for the interrupt
    def turnoff(self):
        self.servo1.detach()
        self.servo2.detach()
        self.servo3.detach()

