"""
This is an example of what a MEET student's mini-project might look like
"""
import turtle as t

#Get boundaries
bg = t.clone()
#bg.bgpic()
t.pu() 
t.ht()
t.shape('square')
snake = t.clone()

block_pos = []
UP,DOWN,LEFT,RIGHT = 0,1,2,3
SNAKE_LENGTH = 5
DIRECTION = RIGHT

for i in range(SNAKE_LENGTH):
    snake.stamp()
    block_pos.append(snake.pos())
    x,y = snake.pos()
    snake.setpos(x+20,y)
    
def move_snake():
    '''
    Moves a multiple-block snake
    '''
    global block_pos
    global DIRECTION
    BLOCK_POS = block_pos[-1]
    snake.clearstamps(1)
            
    if DIRECTION == 0: #move up    
        BLOCK_POS = (BLOCK_POS[0],BLOCK_POS[1]+20)
    elif DIRECTION == 1: #move down
        BLOCK_POS = (BLOCK_POS[0],BLOCK_POS[1]-20)
    elif DIRECTION == 2: #move left
        BLOCK_POS = (BLOCK_POS[0]-20,BLOCK_POS[1])
    elif DIRECTION == 3: #move right
        BLOCK_POS = (BLOCK_POS[0]+20,BLOCK_POS[1])

    nx,ny = BLOCK_POS
    snake.setpos(nx,ny)
    snake.stamp()
    block_pos.append(snake.pos())
    

def up():
    global DIRECTION
    DIRECTION = UP

def down():
    global DIRECTION
    DIRECTION = DOWN

def left():
    global DIRECTION
    DIRECTION = LEFT

def right():
    global DIRECTION
    DIRECTION = RIGHT

def collide_detect():
    '''
    Takes the snake's head position as x,y, checks whether
    it is touching a wall, itself, and returns a bool
    '''
    global block_pos
    x,y = snake.pos()
    if (x,y) in block_pos():
        return True
    

t.onkey(up, "Up")
t.onkey(down, "Down")
t.onkey(left, "Left")
t.onkey(right, "Right")
t.listen()
m = move_snake
t.mainloop()
