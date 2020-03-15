import time
import traitlets
from traitlets.config.configurable import SingletonConfigurable
from Adafruit_MotorHAT import Adafruit_MotorHAT
from .motor import Motor


class Robot(SingletonConfigurable):
    left_motor = traitlets.Instance(Motor)
    right_motor = traitlets.Instance(Motor)
    left_motor_2 = traitlets.Instance(Motor)
    right_motor_2 = traitlets.Instance(Motor)
    
    # config
    i2c_bus = traitlets.Integer(default_value=1).tag(config=True)
    left_motor_channel = traitlets.Integer(default_value=1).tag(config=True)
    left_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    right_motor_channel = traitlets.Integer(default_value=2).tag(config=True)
    right_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    left_motor_channel_2 = traitlets.Integer(default_value=3).tag(config=True)
    left_motor_alpha_2 = traitlets.Float(default_value=1.0).tag(config=True)
    right_motor_channel_2 = traitlets.Integer(default_value=4).tag(config=True)
    right_motor_alpha_2 = traitlets.Float(default_value=1.0).tag(config=True)   
    
    def __init__(self, *args, **kwargs):
        super(Robot, self).__init__(*args, **kwargs)
        self.motor_driver = Adafruit_MotorHAT(i2c_bus=self.i2c_bus)
        self.left_motor = Motor(self.motor_driver, channel=self.left_motor_channel, alpha=self.left_motor_alpha)
        self.right_motor = Motor(self.motor_driver, channel=self.right_motor_channel, alpha=self.right_motor_alpha)
        self.left_motor_2 = Motor(self.motor_driver, channel=self.left_motor_channel_2, alpha=self.left_motor_alpha_2)
        self.right_motor_2 = Motor(self.motor_driver, channel=self.right_motor_channel_2, alpha=self.right_motor_alpha_2)
               
    def set_motors(self, left_speed, right_speed):
        self.left_motor.value = left_speed
        self.right_motor.value = right_speed
        self.left_motor.value_2 = left_speed_2
        self.right_motor.value_2 = right_speed_2
        
    def forward(self, speed=1.0, duration=None):
        self.left_motor.value = speed
        self.right_motor.value = speed
        self.left_motor.value_2 = speed
        self.right_motor.value_2 = speed
        
    def backward(self, speed=1.0):
        self.left_motor.value = -speed
        self.right_motor.value = -speed
        self.left_motor.value_2 = -speed
        self.right_motor.value_2 = -speed
        
    def left(self, speed=1.0):
        self.left_motor.value = -speed
        self.right_motor.value = speed
        self.left_motor.value_2  = -speed
        self.right_motor.value_2  = speed
        
    def right(self, speed=1.0):
        self.left_motor.value = speed
        self.right_motor.value = -speed
        self.left_motor.value_2 = speed
        self.right_motor.value_2 = -speed
        
    def stop(self):
        self.left_motor.value = 0
        self.right_motor.value = 0
        self.left_motor.value_2 = 0
        self.right_motor.value_2 = 0
