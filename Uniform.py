##Andrew and Amari
##Lab 3.1
##3 / 7 / 2018

from graphics import *



class Uniform(object):
    """Creates a Uniform"""
    def __init__(self, topColor, bottomColor):
        self.topColor = topColor
        self.bottomColor = bottomColor


    def drawUniform(self,win:GraphWin):
        body = Rectangle(Point(175, 275), Point(275, 450))
        body.setFill(self.topColor)
        body.draw(win)

        leftArm = Rectangle(Point(125, 275), Point(175, 375))
        leftArm.setFill(self.topColor)
        leftArm.draw(win)

        leftHand = Rectangle(Point(125, 375), Point(175, 400))
        leftHand.setFill(self.topColor)
        leftHand.draw(win)

        rightArm = Rectangle(Point(275, 275), Point(325, 400))
        rightArm.setFill(self.topColor)
        rightArm.draw(win)

        rightHand = Rectangle(Point(275, 375), Point(325, 400))
        rightHand.setFill(self.topColor)
        rightHand.draw(win)

        legs = Rectangle(Point(175, 450), Point(275, 550))
        legs.setFill(self.bottomColor)
        legs.draw(win)

        lineToSeperateLegs = Line(Point(225, 450), Point(225, 550))
        lineToSeperateLegs.setWidth(2)
        lineToSeperateLegs.draw(win)




def main():
    window = GraphWin("Uniform", 1000, 650)

    a = Uniform("blue", "blue")
    a.drawUniform(window)

    window.getMouse()
    window.close()



main()
