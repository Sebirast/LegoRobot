from simrobot import*
import enum

RobotContext.useBackground("pictures\playGround.GIF")

# classes
class ColorSensor:
    class Color(enum.Enum):
        White = 1
        Black = 1
        Blue = 1
        NotFound = 1

    class ComparativeColor:
        meassuredBrightnessValue = None
        upperEnd = None
        lowerEnd = None
        returnColor = None

        def __init__(self, value, band, returnColor):
            self.meassuredBrightnessValue = value
            self.upperEnd = self.meassuredBrightnessValue + band
            self.lowerEnd = self.meassuredBrightnessValue - band
            self.returnColor = returnColor

    whiteValue = None
    blackValue = None
    blueValue = None

    def __init__(self, SensorPort, whiteValue, blackValue, blueValue, band): # the variable @band is used to calculate bandwith of the color
        self.lightSensor = LightSensor(SensorPort)
        self.whiteValue = whiteValue
        self.blackValue = blackValue
        self.blueValue = blueValue

        self.white = ColorSensor.ComparativeColor(whiteValue, band, ColorSensor.Color.White)
        self.black = ColorSensor.ComparativeColor(blackValue, band, ColorSensor.Color.Black)
        self.blue = ColorSensor.ComparativeColor(blueValue, band, ColorSensor.Color.Blue)

        self.colors = [self.white, self.black, self.blue]
    
    def _convertToColor(self, value):
        for color in self.colors:
            if value > color.lowerEnd and value < color.upperEnd:
                return color.returnColorj
            return ColorSensor.Color.NotFound

    def getColor():
        self.convertToColor(self.lightSensor.getValue())

class Robot:
    iSeeNothing = 80
    
    def __init__(self):
        self.robot = LegoRobot()
        self.gear = Gear()

        self.colorSensor = ColorSensor(SensorPort.S1, 100, 100, 100, 25)
        self.touchSensor = TouchSensor(SensorPort.S2)
        self.ultrasonicSensor = UltrasonicSensor(SensorPort.S3)

        robot.addPart(gear)
        robot.addPart(colorSensor.lightSensor)
        robot.addPart(touchSensor)
        robot.addPart(ultrasonicSensor)

    def findObject(self):
        gear.left()
        objectFound = False
        while objectFound == False:
            distance = self.ultrasonicSensor.getDistance()
            if distance < self.iSeeNothing:
                gear.stop()
                while 

    def goToObject(self):
        pass

    def getColor(self):
        pass

    def hitObject(self):
        pass
    
    def run(self):
        pass



# variables
ultraSonicSensorRange = 80

def main():
    r = Robot()
    r.run()

if __name__ == "__main__":
    main()