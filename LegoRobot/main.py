#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# classes
WHEEL_DIAMETER = 55.4
AXEL_TRACK = 104
    
class LegoRobot:
    def __init__(self):
        self.robot = EV3Brick()
        self.leftMotor = Motor(Port.A)
        self.rightMotor = Motor(Port.B)
        self.driveTrain = DriveBase(self.leftMotor, self.rightMotor, wheel_diameter = WHEEL_DIAMETER,  axle_track = AXEL_TRACK)

        self.colorSensor = ColorSensor(Port.S1)
        self.touchSensor = TouchSensor(Port.S2)
        self.ultraSonicSensor = UltrasonicSensor(Port.S3)

        # variables
        self.range = 500  
        self.colorSensorRange = 40  # TODO

        self.objectFound = False

        self.delay = 10

        self.driveSpeed = 100  # TODO
        self.turnRate = 50  # TODO

        self.objectCounter = 0
        
        self.deadZone = 10

    def findObject(self):
        print("entered findObject")
        self.checkObjectNumber()
        self.driveTrain.drive(0, 40)

        distance = self.ultraSonicSensor.distance()

        while distance > self.range:
            distance = self.ultraSonicSensor.distance()
            wait(self.delay)
        
        self.robot.speaker.beep()

        if distance > 1000:
            self.findObject()

        self.goToObject()


    def goToObject(self):
        print("entered goToObject")
        distance = self.ultraSonicSensor.distance()
        oldDistance = distance
        self.driveTrain.drive(self.driveSpeed, 0)

        while distance > self.colorSensorRange:

            # check if robot is moving exactly towards an object:
            if distance > 70:
                if distance > oldDistance + self.deadZone:
                    print("hello")
                    self.driveTrain.stop()
                    self.findObject()

            oldDistance = distance

            distance = self.ultraSonicSensor.distance()

            print(oldDistance, distance)        
            wait(self.delay)

        self.driveTrain.stop()

        self.getColor()


    def getColor(self):
        print("entered getColor method")
        color = self.colorSensor.color()
        if color == Color.BLUE or color == Color.BLACK or color == None or color == Color.YELLOW:
            self.goToNewPlace()

        elif color == Color.BLACK:
            self.hitObject()


    def hitObject(self):
        print("entered hitObjectMethdo")
        self.driveTrain.drive(self.driveSpeed, 0)

        while not self.touchSensor.pressed():
            wait(self.delay)
        
        self.driveTrain.stop()
        self.driveTrain.drive(self.driveSpeed, 0)

        while self.touchSensor.pressed():
            wait(self.delay)
        
        self.objectCounter += 1
        self.goToNewPlace()


    def goToNewPlace(self):
        print("entered goToNewPlace")
        self.driveTrain.straight(-100)
        self.driveTrain.turn(90)
        self.driveTrain.straight(200)
        self.findObject()
    

    def run(self):
        self.findObject()


    def exitProgram(self):
        print(self.objectCounter)
        exit()


    def checkObjectNumber(self):
       if self.objectCounter > 5:
           self.exitProgram()
       pass

r = LegoRobot()
r.run()