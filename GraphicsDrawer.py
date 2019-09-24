from graphics import *
from TIGr import AbstractDrawer
from Dest import *


# Note: You have to install the graphics.py package to use this class
class GraphicsDrawer(AbstractDrawer):
    def __init__(self):
        self.graphics = GraphWin("graphics.py", 500, 500)
        self.x = 250
        self.y = 250
        self.penDown = False
        self.color = "blue"
        self.myDest = Dest()  # returns your new destination
        self.penlist = ["", "white", "black", "red", "yellow", "blue"]
        self.check = EC().check  # error checking class

    def select_pen(self, pen_num):
        if int(pen_num) > 5 or int(pen_num) < 1:
            print("Only use pens 1-5")
        else:
            self.color = self.penlist[int(pen_num)]

    def pen_down(self):
        self.penDown = True

    def pen_up(self):
        self.penDown = False

    def go_along(self, along):
        self.check(along, "int")  # checking if arguments are of correct type
        self.graphics.move(self.graphics, along, self.y)
        self.x = along

    def go_down(self, down):
        self.check(down, "int")
        self.graphics.move(self.graphics, self.x, down)
        self.y = down

    def draw_line(self, direction, distance):
        if direction == 0:
            direction = 180
        elif direction == 180:
            direction = 0
        self.check(direction, "int")
        self.check(distance, "int")
        # putting your current coordinates into an array for use with
        # getDestination
        myPosition = [self.x, self.y]
        distance = int(distance)
        newCoords = self.myDest.getDestination(
            myPosition, direction, distance)  # getting the new destination
        point1 = Point(self.x, self.y)
        # creating the two points for use with the graphics library
        point2 = Point(newCoords[0], newCoords[1])

        if self.penDown:
            # the actual movement using the library
            line = Line(point1, point2)
            line.setOutline(self.color)
            line.draw(self.graphics)
        # updating the x,y position recorded in the class
        self.x = newCoords[0]
        self.y = newCoords[1]

    def draw_circle(self, radius):
        self.check(radius, "int")
        c = Circle(Point(self.x, self.y), radius)
        c.draw(self.graphics)

    def draw_rectangle(self, size):
        self.check(size, "int")
        arrayDir = (0, 90, 180, 270)
        for i in range(4):
            self.draw_line(arrayDir[i - 1], size)

    def draw_triangle(self, size):
        p1 = Point(55, 85)
        p2 = Point(155, 85)
        p3 = Point(105, 180)
        vertices = [p1, p2, p3]
        triangle = Polygon(vertices)
        triangle.draw(self.graphics)

    def end(self):
        self.graphics.getMouse()
