import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor('lightgreen')
screen.tracer(2)

#fence
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, 300)
mypen.pendown()
mypen.pensize(3)

for x in range(4):
    mypen.forward(400)
    mypen.right(90)
mypen.hideturtle()

#bugs
maxbugs = 20
bugs = []
colors = ['red', 'blue', 'purple', 'white', 'black', 'pink', '#FFFF00'] 
shapes = ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle'] 
tcolors = ['#95B9D3', '#77ADD3', '#4497D2', '#2A84c5', '#1A5D8E', '#CE8F91', '#CB4E53', '#B4252A', '#8B1317', '#780409'] 

for i in range(maxbugs):
    c = random.randint(0,6)
    s = random.randint(0,5)

    bugs.append(turtle.Turtle())
    bugs[i].color(colors[c])
    bugs[i].shape(shapes[s])
    bugs[i].penup()
    bugs[i].speed(0)
    bugs[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
    bugs[i].right(random.randint(0,360))

#turtle
turtlesize = 1
turtle.Turtle.shape('turtle')
turtle.Turtle.turtlesize(turtlesize, turtlesize)
turtle.Turtle.color(tcolors[0])
turtle.Turtle.penup()
speed = 1
score = 0
def turnleft():
    turtle.Turtle.left(30)
def turnright():
    turtle.Turtle.right(30)
def increasespeed():
    global speed; speed += 1
def decreasespeed():
    global speed; speed -= 1

#score
def setScore(score):
    mypen.undo()
    mypen.penup()
    mypen.hideturtle()
    mypen.setposition(-290, 310)
    scorestring = 'score : %s' %score
    mypen.write(scorestring, False, align = 'left', font = ('Arial', 14, 'normal'))

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    coll = turtlesize * 10
    if d < coll:
        return True
    else:
        return False

#keyboard control 
screen.listen()
screen.onkey(turnleft, 'Left')
screen.onkey(turnright, 'Right')
screen.onkey(increasespeed, 'Up')
screen.onkey(decreasespeed, 'Down')

#play screen
while true