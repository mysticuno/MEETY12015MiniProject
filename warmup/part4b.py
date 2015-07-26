import turtle as t

t.penup() #move pen without writing
t.ht()
t.shape('square')

BLOCK_POS = (0,0)
STAMP_ID = 0
UP,DOWN,LEFT,RIGHT = 0,1,2,3
DIRECTION = 0

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

t.onkey(up, "Up")
t.onkey(down, "Down")
t.onkey(left, "Left")
t.onkey(right, "Right")
t.listen()

def flashing_block():
    global STAMP_ID
    global BLOCK_POS
    
    t.clearstamp(STAMP_ID)
    nx,ny = BLOCK_POS
    t.setpos(nx,ny)
    STAMP_ID = t.stamp()
    
    t.ontimer(flashing_block,100)

def left_block():
    '''
    Makes a block move to the left, 
    until it disappears off the screen
    '''
    global STAMP_ID
    global BLOCK_POS
    
    t.clearstamp(STAMP_ID)
    BLOCK_POS = (BLOCK_POS[0] - 10,BLOCK_POS[1])
    nx,ny = BLOCK_POS
    t.setpos(nx,ny)
    STAMP_ID = t.stamp()
    
    t.ontimer(left_block,100)

def controlled_block():
    '''
    Moves a block directly left, right, up,
    or down from where it was before,
    depending on DIRECTION
    '''
    global STAMP_ID
    global BLOCK_POS
    global DIRECTION

    t.clearstamp(STAMP_ID)
    
    if DIRECTION == 0: #move up    
        BLOCK_POS = (BLOCK_POS[0],BLOCK_POS[1]+10)
    elif DIRECTION == 1: #move down
        BLOCK_POS = (BLOCK_POS[0],BLOCK_POS[1]-10)
    elif DIRECTION == 2: #move left
        BLOCK_POS = (BLOCK_POS[0] - 10,BLOCK_POS[1])
    elif DIRECTION == 3: #move right
        BLOCK_POS = (BLOCK_POS[0]+10,BLOCK_POS[1])

    nx,ny = BLOCK_POS
    t.setpos(nx,ny)
    STAMP_ID = t.stamp()
        


t.mainloop()
