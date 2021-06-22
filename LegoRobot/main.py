#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# classes

WHEEL_DIAMETER = 55.4
AXEL_TRACK = 104

class LegoRobot:
    class ColorCalculator:
        def __init__(self, sensorPort):
            self.cs = ColorSensor(sensorPort)

        def calculateColor(self):
            rgb = self.cs.rgb()
            color = None

            if rgb[0] != 0:
                return "WHITE"
            else:
                brightness = rgb[0] + rgb[1] + rgb[2]

                if brightness == 0:
                    return "BLACK"
                else:
                    return "BLUE"

    def __init__(self):
        self.robot = EV3Brick()
        self.leftMotor = Motor(Port.A)
        self.rightMotor = Motor(Port.B)
        self.driveTrain = DriveBase(
        self.leftMotor, self.rightMotor, wheel_diameter=WHEEL_DIAMETER,  axle_track=AXEL_TRACK)

        self.cc = LegoRobot.ColorCalculator(Port.S1)
        self.touchSensor = TouchSensor(Port.S2)
        self.ultraSonicSensor = UltrasonicSensor(Port.S3)

        # variables
        self.range = 500
        self.colorSensorRange = 40  # TODO

        self.objectFound = False

        self.delay = 10

        self.driveSpeed = 90  # TODO
        self.turnRate = 50  # TODO

        self.objectCounter = 0

        self.deadZone = 12

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
            if distance > 100:
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
        color = None

        # I use this loop to avoid faults in the colorDetection
        # When I testet the program, the color wasnt right at the beginning of the measuringsection
        # so I use not the very first measured color

        for i in range(10):
            color = self.cc.calculateColor()
        
        print(color)

        if color == "BLACK":
            self.robot.speaker.beep()
            self.hitObject()

        self.goToNewPlace()

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
r.getColor()