import turtle
from time import sleep

t = turtle
screen = turtle.Screen()
screen.bgcolor("black")
direc = "Right"

t.register_shape("player.gif")
t.register_shape("paperball.gif")
t.shape("paperball.gif")
flag = True


# draw a square
def square(start,end):
    t.pensize(10)
    t.penup()
    t.setpos((start[0],start[1]))
    t.pendown()
    t.setpos((start[0],end[1]))
    t.setpos((end[0],end[1]))
    t.setpos((end[0],start[1]))
    t.setpos((start[0],start[1]))
    t.pensize(1)
    return None


# draw the board
def draw():
    t.pencolor("green")
    t.speed(0)
    square((-325,-275),(325,275))
    square((175,75),(-175,-75))

    square((-225,-225),(-275,225))
    square((225,-225),(275,225))

    square((-175,-225),(175,-125))
    square((-175,225),(175,125))
    return None


# draw the dots
dotlist = []
dotpos_dic = {}

def make_dot(dotnum):
    for i in range(dotnum):
        x = t.stamp()
        dotlist.append(x)
        dotpos_dic[t.pos()] = x
        t.forward(50)


#   draw all dots
def dots():
    t.penup()
    t.pencolor("white")
    
    t.setpos(-300,-250)
    make_dot(13)
        
    t.setpos(-300,250)
    make_dot(13)

    t.setpos(-150,-100)
    make_dot(7)

    t.setpos(-150,100)
    make_dot(7)

    t.right(90)
    t.setpos(-300,200)
    make_dot(9)

    t.setpos(-200,200)
    make_dot(9)

    t.setpos(200,200)
    make_dot(9)

    t.setpos(300,200)
    make_dot(9)
    return None
 
score = 0


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction = RIGHT

corners = [(-300,250),(-200,250),(200,250),(300,250),(-200,100),(200,100),(-200,-100),
           (200,-100),(-300,-250),(-200,-250),(200,-250),(300,-250)]

directions = {(-300,250):(RIGHT,DOWN),(-200,250):(RIGHT,LEFT,DOWN),
              (200,250):(RIGHT,LEFT,DOWN),(300,250):(LEFT,DOWN),
              (-200,100):(RIGHT,UP,DOWN),(200,100):(LEFT,UP,DOWN),
              (-200,-100):(RIGHT,UP,DOWN),(200,-100):(LEFT,UP,DOWN),
              (-300,-250):(RIGHT,UP),(-200,-250):(RIGHT,LEFT,UP),
              (200,-250):(RIGHT,LEFT,UP),(300,-250):(LEFT,UP)}

def corner():
    x = t.pos()[0]
    y = t.pos()[1]    
    if (x,y) in corners:
        return True
    else:
        return False
def move():
    x = t.pos()[0]
    y = t.pos()[1]
    eat()
    if corner():
        if direction in directions[(x,y)]:
            go(True)
        else:
            go(False)
    else:
        go(True)
        
def go(flag):
    if flag:
        x = t.pos()[0]
        y = t.pos()[1]
        if direction == RIGHT:
            t.goto(x + 50, y)
        elif direction == LEFT:
            t.goto(x - 50, y)
        elif direction == UP:
            t.goto(x, y + 50)
        else:
            t.goto(x, y - 50)
    
    t.ontimer(move, 200)

score = 0


def eat():
    global score
    if dotpos_dic[t.pos()] in dotlist:
        dot = dotlist.pop(dotlist.index(dotpos_dic[t.pos()]))
        t.clearstamp(dot)
        score += 1
        print(score)

# keyboard functions


def pacLeft():
    global direction
    print("Left")
    if not corner():
        if direction == RIGHT:
            direction = LEFT
    else:
        direction = LEFT


def pacRight():
    global direction
    turtle.setheading(0)
    print("Right")
    if not corner():
        if direction == LEFT:
            direction = RIGHT
    else:
        direction = RIGHT


def pacUp():
    global direction
    turtle.setheading(90)
    print("UP")
    if not corner():
        if direction == DOWN:
            direction = UP
    else:
        direction = UP

def pacDown():
    global direction
    if not corner():
        if direction == UP:
            direction = DOWN
    else:
        direction = DOWN

t.onkey(pacLeft,"Left")
t.onkey(pacRight, "Right")
t.onkey(pacUp, "Up")
t.onkey(pacDown, "Down")
t.onkey(quit,"Escape")


def start():
    t.penup()
    t.setpos(0, 100)
    t.speed(1)
    t.shape("player.gif")
    pacRight()
    return None


draw()
dots()
start()

screen.listen()

turtle.ontimer(move, 200)

turtle.mainloop()
