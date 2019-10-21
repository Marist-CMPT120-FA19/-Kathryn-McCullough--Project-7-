# name: Kathryn McCullough
# email: kathryn.mccullough1@marist.edu
# description: archery bullseye with scoring functions that add up points after five clicks

from graphics import *
import math


#distance formula 
def distance(point, circle):
    x = point.getX() - circle.getCenter().getX()
    y = point.getY() - circle.getCenter().getY()
    dist = math.sqrt(x*x + y*y)

    return dist <= circle.getRadius()

    
def main():

    score=0
    
    win = GraphWin('Archery',300,300)
    center=Point(150, 150)
# Outter circle 
    white=Circle(center,100)
    white.setFill("white")
    white.draw(win)

    black=Circle(center,80)
    black.setFill("black")
    black.draw(win)

    blue=Circle(center, 60)
    blue.setFill("blue")
    blue.draw(win)

    red=Circle(center, 40)
    red.setFill("red")
    red.draw(win)
#Inner circle
    yellow=Circle(center,20)
    yellow.setFill("yellow")
    yellow.draw(win)

    for x in range(5):
        click= win.getMouse()
        
        if(distance(click, yellow)):
            score += 9
            print("+9")
        elif(distance(click, red)):
            score += 7
            print("+7")
        elif(distance(click, blue)):
            score += 5
            print("+5")
        elif(distance(click, black)):
            score += 3
            print("+3")
        elif(distance(click, white)):
            score += 1
            print("+1")
        else:
            score += 0
            print("+0")
    
    
    print("Your total points are: ", score)

                    
    win.getMouse()
    win.close()
    
main()

    
