import turtle

turtle.penup()
turtle.ht()

def up():
    print("You pressed Up!")

def down():
    print("You pressed Down!")

def left():
    print("You pressed Left!")

def right():
    print("You pressed Right!")
    
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

def repeat():
    turtle.ontimer(repeat, 500)

turtle.listen() # Remember to put this after your listeners!
