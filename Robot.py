from simrobot import*

robot = LegoRobot()

gear = Gear()
lightSensor = LightSensor(SensorPort.S1)
touchSensor = TouchSensor(SensorPort.S2)
ultrasonicSensor = UltrasonicSensor(SensorPort.S3)

robot.addPart(gear)
robot.addPart(lightSensor)
robot.addPart(touchSensor)
robot.addPart(ultrasonicSensor)

# variables
ultraSonicSensorRange = 80

# functions
def findObject():
    pass

def goToObject():
    pass

def getColor():
    pass

def hitObject():
    pass

while not robot.isEscapeHit():
    gear.right()
    if ultrasonicSensor.getDistance() < ultraSonicSensorRange:
        currentMotorTicks = getRightMotorCount()
        while ultrasonicSensor.getDistance < ultraSonicSensorRange:
            gear.right()
        gear.stop()
        driveTicks = gear.getRightMotorCount()