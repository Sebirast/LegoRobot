#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import random

# classes

WHEEL_DIAMETER = 55.4
AXEL_TRACK = 104

class LegoRobot:

    # we use this class to convert the rgbvalues to a string which represents the color
    # this class has to be in the legorobot-class because otherwhise the compiler couldnt find this class (i dont really know why)
    class ColorCalculator:
        def __init__(self, sensorPort):
            self.cs = ColorSensor(sensorPort)

        def calculateColor(self):
            rgb = self.cs.rgb()
            color = None

            # we meassured that white has values in all rgb values (also in the red value)
            # blue and black dont have any red in it
            if rgb[0] != 0:
                return "WHITE"
            else:
                # black = (0, 0, 0) => brightness = 0
                # blue = (0, g > 0, b > 0) => brightness > 0

                brightness = rgb[0] + rgb[1] + rgb[2]

                if brightness == 0:
                    return "BLACK"
                else:
                    return "BLUE"

    def __init__(self):
        # in the constructor we initiate all the motors, sensors..
        # and of course one robotobject (ev3Brick) and a gear (driveBase)
        self.robot = EV3Brick()
        self.leftMotor = Motor(Port.A)
        self.rightMotor = Motor(Port.B)
        self.driveTrain = DriveBase(
        self.leftMotor, self.rightMotor, wheel_diameter=WHEEL_DIAMETER,  axle_track=AXEL_TRACK)

        self.cc = LegoRobot.ColorCalculator(Port.S1)
        self.ultraSonicSensor = UltrasonicSensor(Port.S3)

        # variables
        self.range = 600
        self.colorSensorRange = 50 # TODO

        # this delay is called every loop
        self.delay = 10

        # this speeds are used in the driveTrain.drive() mehtods
        self.driveSpeed = 90  # TODO
        self.hitSpeed = 200
        self.turnRate = 30  # TODO

        self.objectCounter = 0

        self.deadZone = 20

    def findObject(self):
        print("entered findObject")
        self.checkObjectNumber()

        distance = self.ultraSonicSensor.distance()
        self.driveTrain.reset()
        currentTraveldAngle = self.driveTrain.angle()

        self.driveTrain.drive(0, self.turnRate)

        # turn as long the distance is greater than the range of the robot
        while distance > self.range:
            if currentTraveldAngle > 360:
                self.goToOtherPlace()

            distance = self.ultraSonicSensor.distance()
            currenTraveldAngle = self.driveTrain.angle()
            wait(self.delay)

        self.robot.speaker.beep()

        if distance > 1000:
            self.findObject()

        self.goToObject()

    def goToObject(self):
        distance = self.ultraSonicSensor.distance()
        oldDistance = distance
        self.driveTrain.drive(self.driveSpeed, 0)

        # drive to the object:
        while distance > self.colorSensorRange:

            # check if robot is moving exactly towards an object:
            if distance > oldDistance + 50:
                self.driveTrain.stop()
                self.findObject()
            
            # check if robot is not driving into something
            oldDistance = distance

            distance = self.ultraSonicSensor.distance()

            wait(self.delay)

        self.driveTrain.stop()

        self.getColor()

    def getColor(self):
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
        self.driveTrain.straight(100)
        self.driveTrain.straight(-100)
        self.driveTrain.turn(180)
        
        self.objectCounter += 1
        self.goToNewPlace()

    def goToNewPlace(self):
        # when I tested the program i had problems that the robot is stuck in a loop => the robot went allways to the same objects
        # so I tried to create a random number which then says which action should be executed
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:   # the robot drives backwards, turn 90d right and drives straight forward
            self.driveTrain.straight(-100)
            self.driveTrain.turn(90)
            self.driveTrain.straight(200)

        elif randomNumber == 2: # the robot drives backwards, turns around and drives straight forward
            self.driveTrain.straight(-100)
            self.driveTrain.turn(-90)
            self.driveTrain.straight(200)

        elif randomNumber == 3: # the robot drives backwards, turns 90d left and drives straight forward
            self.driveTrain.straight(-100)
            self.driveTrain.turn(180)
            self.driveTrain.straight(100)
        
        self.findObject()


    def run(self):
        self.findObject()

    def exitProgram(self):
        print(self.objectCounter)
        exit()

    # this function is used to check if the robot has already knocked 5 objects over
    def checkObjectNumber(self):
        if self.objectCounter > 5:
            self.exitProgram()
        pass


r = LegoRobot()
r.run()