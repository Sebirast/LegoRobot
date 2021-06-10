from simrobot import *

class Mesh:
	def __init__(self, lentgh, hight, x, y):
		self.length = lentgh
		self.hight = hight
		self.x = x
		self.y = y

	def calculateEdges(self):
		halfLength = self.length / 2
		halfHight = self.hight / 2
		rightUpperEdge = [self.x + halfLength, self.y + halfHight]
		leftUpperEdge = [self.x - halfLength, self.y + halfHight]
		rightLowerEdge = [self.x + halfLength, self.y - halfHight]
		leftLowerEdge = [self.x - halfLength, self.y - halfHight]
		result = [rightUpperEdge, leftUpperEdge, rightLowerEdge, leftLowerEdge]
		return result


lenght = 31

mesh_bar0 = [[50,20],[50,40],[450,20],[450,40]]
mesh_bar1 = [[50,465],[50,485],[450,465],[450,485]]
mesh_bar3 = [[20,50],[40,50],[450,465],[450,485]]   #hier weitermachen

RobotContext.useTarget ("sprites/bar0.gif",mesh_bar0, 250,30)
RobotContext.useTarget ("sprites/bar0.gif",mesh_bar1, 250,475)
RobotContext.useTarget ("sprites/bar1.gif",mesh_bar3, 30,250)
RobotContext.useTarget ("sprites/bar1.gif",mesh_bar0, 465,250)


mesh_seat_1 = [[200, 10], [-200, 10], [-200, -10], [200, -10]]
mesh_seat_1 = [[200, 10], [-200, 10], [-200, -10], [200, -10]]  

RobotContext.useTarget("sprites/seat_1.gif", Mesh(lenght, lenght, 278, 50).calculateEdges(), 278, 50)
RobotContext.useTarget("sprites/seat_1.gif", Mesh(lenght, lenght, 209, 408).calculateEdges() , 209, 408)
RobotContext.useTarget("sprites/seat_1.gif", Mesh(lenght, lenght, 209, 408).calculateEdges() , 80, 303)
RobotContext.useTarget("sprites/seat_1.gif", Mesh(lenght, lenght, 325, 215).calculateEdges() , 325, 215)
RobotContext.useTarget("sprites/seat_0.gif", Mesh(lenght, lenght, 200, 303).calculateEdges() , 200, 303)
RobotContext.useTarget("sprites/seat_1.gif", Mesh(lenght, lenght, 450, 466).calculateEdges() , 450, 466)
RobotContext.useTarget("sprites/seat_1.gif", Mesh(lenght, lenght, 41, 171).calculateEdges() , 41, 171)
RobotContext.useTarget("sprites/seat_0.gif", Mesh(lenght, lenght, 82, 71).calculateEdges() , 82, 71)
RobotContext.useTarget("sprites/seat_0.gif", Mesh(lenght, lenght, 67, 450).calculateEdges() , 67, 450)
RobotContext.useTarget("sprites/seat_0.gif", Mesh(lenght, lenght, 412, 118).calculateEdges() , 412, 118)
RobotContext.useTarget("sprites/seat_2.gif", Mesh(lenght, lenght, 310, 140).calculateEdges() , 310, 140)
RobotContext.useTarget("sprites/seat_2.gif", Mesh(lenght, lenght, 284, 398).calculateEdges() , 284, 398)
RobotContext.useTarget("sprites/seat_2.gif", Mesh(lenght, lenght, 380, 271).calculateEdges() , 380, 271)
RobotContext.useTarget("sprites/seat_2.gif", Mesh(lenght, lenght, 142, 175).calculateEdges() , 142, 175)
RobotContext.useTarget("sprites/seat_2.gif", Mesh(lenght, lenght, 135, 383).calculateEdges() , 135, 385)