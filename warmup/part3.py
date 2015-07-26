import turtle as t

t.penup() #move pen without writing
t.ht()

## Change turtle to a square here.
t.shape('square')

STAMP_ID = 0
STAMP_IDs = []

def stamp_block():
    '''
    Places a block in the center of the canvas.
    '''
    ## HINT
    global STAMP_ID
    STAMP_ID = turtle.stamp()

def erase_block():
    '''
    Erases the block placed by stamp_block().
    '''
    ## HINT
    global STAMP_ID
    t.clearstamp(STAMP_ID)
    

def big_rectangle(x,y):
    '''
    Creates an x by y rectangle of stamps.
    '''
    global STAMP_IDs
    for i in range(x):
        for j in range(y):
            t.setpos(i*10,j*10)
            STAMP_IDs.append(t.stamp())

def erase_rectangle():
    '''
    Erases big_rectangle.
    '''
    global STAMP_IDs
    for stamp in STAMP_IDs:
        t.clearstamp(stamp)

t.mainloop()
