from simrobot import*

# classes
class ColorSensor:

    class Color:
        meassuredBrightnessValue = None
        upperEnd = None
        lowerEnd = None

        def __init__(self, value, band):
            self.meassuredBrightnessValue = value
            self.upperEnd = self.meassuredBrightnessValue + band
            self.lowerEnd = self.meassuredBrightnessValue - band

    whiteValue = None
    blackValue = None
    blueValue = None

    def __init__(self, SensorPort, whiteValue, blackValue, blueValue, band): # the variable @band is used to calculate bandwith of the color
        lightSensor = LightSensor(SensorPort)
        self.whiteValue = whiteValue
        self.blackValue = blackValue
        self.blueValue = blueValue

        self.white = ColorSensor.Color(whiteValue, band)
        self.black = ColorSensor.Color(blackValue, band)
        self.blue = ColorSensor.Color(blueValue, band)
        self.colors = [white, black, blue]
    
    def _convertToColor(value):
        for color in self.colors:
            for brightness in range(color.lowerEnd, color.upperEnd):
                if value == brightness:
                    return color
            
        pass

    def getColor():
        pass

class Robot:
    def __init__(self):
        robot = LegoRobot()
        gear = Gear()

        colorSensor = ColorSensor(SensorPort.S1)
        touchSensor = TouchSensor(SensorPort.S2)
        ultrasonicSensor = UltrasonicSensor(SensorPort.S3)

        robot.addPart(gear)
        robot.addPart(colorSensor.lightSensor)
        robot.addPart(touchSensor)
        robot.addPart(ultrasonicSensor)

    def findObject(self):
        pass

    def goToObject(self):
        pass

    def getColor(self):
        pass

    def hitObject(self):
        pass


# variables
ultraSonicSensorRange = 80

def main():
    pass

if __name__ == "__main__":
    main()