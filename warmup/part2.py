
import turtle as t

t.penup() #move pen without writing
t.ht()

UP = "You pressed Up!"
DOWN = "You pressed Down!"
LEFT = "You pressed Left!"
RIGHT = "You pressed Right!"

STEPSIZE = 500

direction = LEFT

def up():
    global direction
    direction = UP

def down():
    global direction
    direction = DOWN

def left():
    global direction
    direction = LEFT

def right():
    global direction
    direction = RIGHT
    
t.onkey(up, 'Up')
t.onkey(down, 'Down')
t.onkey(left, 'Left')
t.onkey(right, 'Right')

def repeat():
    print(direction)
    t.ontimer(repeat, STEPSIZE)

t.listen()
