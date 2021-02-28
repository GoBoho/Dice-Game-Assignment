#############################################################################
#Name: George Bohorquez
#Date: 12/6/2018
#Assignment: Assignment 4
#############################################################################

import turtle
import random

listOfDice = [[],[],[],[],[]] #List of Dice
listOfButton = [[],[]] #List of Buttons
screen = turtle.Screen() #Screen
brush = turtle.Turtle() #pen

#Main function --------------------------------------------------------------------------------------------------------------------------------
def main():

    #Initializing Variables
    wide = 100 #Width of the Die
    numOfDie = 5 #Get num of Die
    numOfDots = 0 #Number of Dots to be Drawn
    xPos = -325 #Initial X position
    yPos = 425 #Initial Y position

    #Draws out 5 die of the same color, updating their x and y positions
    doneNum = 0 #Counter
    while (doneNum != numOfDie):
        yPos = yPos - 125 #Get Start Y
        line = "black" #Line Color
        fill = "white" #Fill color
        numOfDots = random.randint(1,6) #Randomly selects number of dots for each die

        drawDie(brush, xPos, yPos, wide, line, fill, numOfDots) #Literally draws the die

        #Adds Die parameters to List
        listOfDice[doneNum].append(xPos)
        listOfDice[doneNum].append(yPos)
        listOfDice[doneNum].append(wide)
        listOfDice[doneNum].append(line)
        listOfDice[doneNum].append(fill)
        listOfDice[doneNum].append(numOfDots)

        doneNum = doneNum + 1 #Updates the counter

    #Draws out two buttons
    drawRectangle(brush, 100, 100, 100, 50, line, "gray", "Roll")
    listOfButton[0].append(100)
    listOfButton[0].append(100)
    listOfButton[0].append(100)
    listOfButton[0].append(50)
    listOfButton[0].append(line)
    listOfButton[0].append("gray")
    listOfButton[0].append("Roll")
    drawRectangle(brush, 100, -100, 100, 50, line, "gray", "New-Roll")
    listOfButton[1].append(100)
    listOfButton[1].append(-100)
    listOfButton[1].append(100)
    listOfButton[1].append(50)
    listOfButton[1].append(line)
    listOfButton[1].append("gray")
    listOfButton[1].append("New-Roll")

    #Checks for the click on the screen
    screen.onscreenclick(mouseClick)


#Draws the Rectangle------------------------------------------------------------------------------------------------------------------------------
def drawRectangle(pen, x, y, width, height, lineColor, fillColor, text = None):

    pen.speed(120)
    if (text == None): #Will Draw just the rectangle
        pen.begin_fill()
        pen.pencolor(lineColor)
        pen.fillcolor(fillColor)
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.setheading(360)
        pen.forward(width)
        pen.setheading(270)
        pen.forward(height)
        pen.setheading(180)
        pen.forward(width)
        pen.setheading(90)
        pen.forward(height)
        pen.end_fill()
        pen.penup()

    if (text != None): #Will Draw the rectangle and write the text
        pen.begin_fill()
        pen.pencolor(lineColor)
        pen.fillcolor(fillColor)
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.setheading(360)
        pen.forward(width)
        pen.setheading(270)
        pen.forward(height)
        pen.setheading(180)
        pen.forward(width)
        pen.setheading(90)
        pen.forward(height)
        pen.end_fill()
        pen.penup()

        #Will write text within the buttons
        pen.setheading(300)
        pen.forward(40)
        pen.write(text, False, "left", font = ("Arial", 15, "normal"))
        pen.penup()

#Draws the Die-------------------------------------------------------------------------------------------------------------------------------------
def drawDie(pen, x, y, width, lineColor, fillColor, dotCount):

    drawRectangle(pen, x, y, width, width, lineColor, fillColor) #Draws the Die piece
    drawDots(pen, x, y, dotCount) #Draw Dots function
        

#Draws the Dots on the Die-------------------------------------------------------------------------------------------------------------------------
def drawDots(circle, x, y, numberOfDots):

    #The Brush turtle
    circle.pencolor("black")
    circle.penup()
    circle.goto(x, y)

    #Dot coordinates
    sideOne = [50, -50]
    sideTwo = [50, -33, 50, -66]
    sideThree = [25, -25, 50, -50, 75, -75]
    sideFour = [25, -25, 75, -25, 25, -75, 75, -75]
    sideFive = [25, -25, 75, -25, 25, -75, 75, -75, 50, -50]
    sideSix = [25, -25, 75, -25, 25, -50, 75, -50, 25, -75, 75, -75]
    side = []

    #Dot coordinates are copied to be used
    if (numberOfDots == 1):
        side = sideOne.copy()
    if (numberOfDots == 2):
        side = sideTwo.copy()
    if (numberOfDots == 3):
        side = sideThree.copy()
    if (numberOfDots == 4):
        side = sideFour.copy()
    if (numberOfDots == 5):
        side = sideFive.copy()
    if (numberOfDots == 6):
        side = sideSix.copy()

    #Drawing the Dot and updating the position
    i = 0
    while (i != ((numberOfDots * 2))):
        circle.begin_fill()
        circle.fillcolor("Black")
        circle.penup()

        #Updating the Postition for Dot drawing
        xPos = side[i] + x + 10
        yPos = side[i + 1] + y
        i = i + 2

        #Drawing the Dot
        circle.goto(xPos, yPos)
        circle.pendown()
        circle.circle(10)
        circle.end_fill()
      
#Checks if point is within a square--------------------------------------------------------------------------------------------------------------
def isWithin(startX, startY, width, height, endX, endY):
    withinX = False
    withinY = False
    withinSquare = False
    
    if ((endX >= startX) and (endX <= (startX + width))): #Checks to see if position is within the x bounds
        withinX = True
    if ((endY <= startY) and (endY >= (startY - height))): #Checks to see if position is within the y bounds
        withinY = True
    if ((withinX == True) and (withinY == True)): #Is true if both withinX and withinY is true
        withinSquare = True

        for i in range(len(listOfDice)):
            if (listOfDice[i][1] == startY): #Each die can be identified individually by their Y values 
                dieClicked(i)

        for i in range(len(listOfButton)):
            if (listOfButton[i][1] == startY): #Each button can be identified individually by their Y values
                buttonClicked(i)
        
#Mouse Click Listener-----------------------------------------------------------------------------------------------------------------------------
def mouseClick(x, y):

    brush.goto(x, y)
    brush.pendown()

    for i in range(len(listOfDice)): #Goes through the list of Dice
        isWithin(listOfDice[i][0], listOfDice[i][1], listOfDice[i][2], listOfDice[i][2], x, y) #Checks each die along with the 
    for i in range(len(listOfButton)):
        isWithin(listOfButton[i][0], listOfButton[i][1], listOfButton[i][2], listOfButton[i][3], x, y)

    brush.penup()
    
#Checks if a Die has been clicked------------------------------------------------------------------------------------------------------------------
def dieClicked(ind):

    numOfDots = random.randint(1,6) #Randomly selects number of dots for each die
    listOfDice[ind][4] = "gray" #Changes selected die color
    listOfDice[ind][5] = numOfDots #Changes number of dots in selected die
    drawDie(brush, listOfDice[ind][0], listOfDice[ind][1], listOfDice[ind][2], listOfDice[ind][3], listOfDice[ind][4], listOfDice[ind][5])
    
#Checks if button has been clicked-----------------------------------------------------------------------------------------------------------------
def buttonClicked(ind):

    if (listOfButton[ind][6] == "New-Roll"): #Checks to see if the button is a new roll button
        for i in range(len(listOfDice)): #Goes through the list of dice
            listOfDice[i][4] = "white" #Changes die color back to normal
            numOfDots = random.randint(1,6) #Randomly selects number of dots for die
            listOfDice[i][5] = numOfDots #Changes number of dots in selected die
            drawDie(brush, listOfDice[i][0], listOfDice[i][1], listOfDice[i][2], listOfDice[i][3], listOfDice[i][4], listOfDice[i][5])

    if (listOfButton[ind][6] == "Roll"): #Checks to see if the button is a roll button
        for i in range(len(listOfDice)): #Goes through the list of dice
           if listOfDice[i][4] == "white": #Checks to see if the dice has not been clicked on
               numOfDots = random.randint(1,6) #Randomly selects number of dots for die
               listOfDice[i][5] = numOfDots #Changes number of dots in selected die
               drawDie(brush, listOfDice[i][0], listOfDice[i][1], listOfDice[i][2], listOfDice[i][3], listOfDice[i][4], listOfDice[i][5]) 

main()






