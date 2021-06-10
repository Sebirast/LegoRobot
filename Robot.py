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
        self.lightSensor.activate(True)
        self.whiteValue = whiteValue
        self.blackValue = blackValue
        self.blueValue = blueValue

        self.white = ColorSensor.ComparativeColor(whiteValue, band, ColorSensor.Color.White)
        self.black = ColorSensor.ComparativeColor(blackValue, band, ColorSensor.Color.Black)
        self.blue = ColorSensor.ComparativeColor(blueValue, band, ColorSensor.Color.Blue)

        self.colors = [self.white, self.black, self.blue]
    
    def __convertToColor(self, value):
        for color in self.colors:
            if value > color.lowerEnd and value < color.upperEnd:
                return color.returnColor

            return ColorSensor.Color.NotFound

    def getColor(self):
        self.__convertToColor(self.lightSensor.getValue())

class Robot:
    # variables
    iSeeNothing = 80 # max ultrasonicSensor range
    objectFound = False
    delay = 10 # delay used for tools.delay(@delay)

    # declaring of objects
    robot = None
    gear = None

    colorSensor = None
    touchSensor = None
    ultrasonicSensor = None
    
    # constructor
    def __init__(self):
        self.robot = LegoRobot()
        self.gear = Gear()

        self.colorSensor = ColorSensor(SensorPort.S1, 100, 100, 100, 25)
        self.touchSensor = TouchSensor(SensorPort.S2)
        self.ultrasonicSensor = UltrasonicSensor(SensorPort.S3)

        self.robot.addPart(self.gear)
        self.robot.addPart(self.colorSensor.lightSensor)
        self.robot.addPart(self.touchSensor)
        self.robot.addPart(self.ultrasonicSensor)

    def start(self):
        self.gear.left()
        objectFound = False
        while objectFound == False:
            distance = self.ultrasonicSensor.getDistance()
            if distance < self.iSeeNothing:
                objectFound = True
                self.gear.stop()
                self.goToObject()

            Tools.delay(10)

    def goToObject(self):
        distance = self.ultrasonicSensor.getDistance()
        while distance > 10:
            self.gear.forward()
            Tools.delay(self.delay) 

        self.gear.stop()
        self.getColor()

    def getColor(self):
        currentObjectColor = self.colorSensor.getColor()
        if currentObjectColor == ColorSensor.Color.Black:
            self.hitObject()
        elif currentObjectColor == ColorSensor.Color.White or currentObjectColor == ColorSensor.Color.Blue:
            self.dodgeObject()
        elif currentObjectColor == ColorSensor.Color.NotFound:
            self.start()
        
    def dodgeObject():
        self.gear.backwards(10)
        

    def hitObject(self):
        pass
    
    def run(self):
        self.start()



# variables
ultraSonicSensorRange = 80

def main():
    r = Robot()
    r.run()

if __name__ == "__main__":
    main()