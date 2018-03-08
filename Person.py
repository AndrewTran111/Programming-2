## Amari Townsend & Andrew Tran
## Lab 3.1 Object Interactions
## 3 / 7 / 18

from betterGraphics import *

class Person(object):
    """Draws the person"""

    def __init__(self, age, name, skinColor, eyeColor, hairColor):

        self.age = age
        self.name = name
        self.skinColor = skinColor
        self.eyeColor = eyeColor
        self.hairColor = hairColor




    def drawPerson(self, win):
        """Draws the person (without the uniform)"""

        self.skinColor = color_rgb(255,213,150)

        # Main body parts

        head = Circle(Point(225, 200),75)
        head.setFill(self.skinColor)
        head.draw(win)

        body = Rectangle(Point(175, 275), Point(275,450))
        body.setFill(self.skinColor)
        body.draw(win)

        leftArm = Rectangle(Point(125, 275), Point(175, 375))
        leftArm.setFill(self.skinColor)
        leftArm.draw(win)

        leftHand = Rectangle(Point(125, 375), Point(175, 400))
        leftHand.setFill(self.skinColor)
        leftHand.draw(win)


        rightArm = Rectangle(Point(275, 275), Point(325, 400))
        rightArm.setFill(self.skinColor)
        rightArm.draw(win)

        rightHand = Rectangle(Point(275, 375), Point(325, 400))
        rightHand.setFill(self.skinColor)
        rightHand.draw(win)

        legs = Rectangle(Point(175, 450), Point(275, 550))
        legs.setFill(self.skinColor)
        legs.draw(win)

        lineToSeperateLegs = Line(Point(225, 450), Point(225,550 ))
        lineToSeperateLegs.setWidth(2)
        lineToSeperateLegs.draw(win)

        # Deatils

        underwear = Polygon(Point(175,425), Point(275,425),Point(275,450),Point(250,450),
                            Point(250,475),Point(200,475),Point(200,450),Point(175,450))
        underwear.setFill("gray")
        underwear.draw(win)

    def drawName(self):
        self.name = "Human"




def main():
    """The main method"""

    window = GraphWin("People", 1000, 650)

    a = Person(6, "red" "red", "red", "red", "red")
    a.drawPerson(window)

    ## fill out later


    window.getMouse()
    window.close()

main()



