
"""
This is an example of what students might make out of the mini project.
"""

import turtle
import random

turtle.penup()
turtle.ht()

turtle.tracer()

# draw wall
wall = turtle.clone()
wall.shape("square")
wall.shapesize(20, 40, 20)
wall.pencolor('green')
wall.fillcolor("light green")
wall.stamp()

# get the wall boundaries
wall_poly = wall.get_shapepoly()
x_points = []
y_points = []
for point in wall_poly:
    y_points.append(point[0])
    x_points.append(point[1])
MAX_X = max(x_points)
MIN_X = min(x_points)
MAX_Y = max(y_points)
MIN_Y = min(y_points)

# Initialize variables
RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

INITIAL_SNAKE_LENGTH = 3
SQUARE_WIDTH = 20

current_direction = RIGHT
temp_current_direction = current_direction

MAX_FOOD = 50
MAX_TRASH = 25

food_remaining = MAX_FOOD
times_recycled = 0
trash_count = 0

can_recycle = False
game_over = False
power_up_present = False

move_step_time = 1000
food_step_time = 5000
trash_step_time = 5000
power_up_step_time = 3000 #attempt to spawn powerup every 3 seconds
power_up_chance = .1*(1+trash_count/10.)
POWER_UP_TIME = 10000

score = 0
scoreboard = turtle.clone()
food_score = 20
recycle_score = 50
trash_penalty = 30

# Write the initial scoreboard. This will increment every 100 points.
scoreboard.setpos(MIN_X, MIN_Y-50)
scoreboard.write("Score: %s" % score, align="center", font=("Arial", 20, "bold"))

scoreboard.setpos(MIN_X-64, MIN_Y-100)
scoreboard.write("Food remaining: %s" %food_remaining, align="left", font=("Arial", 20, "bold"))

scoreboard.setpos(MIN_X-64,MIN_Y-150)
scoreboard.write("Trash on board "+str(trash_count)+"/"+str(MAX_TRASH), \
                 align="left", font=("Arial", 20, "bold"))

                 
# Create and draw the initial snake
snake_positions = []
snake_stamps = []

# Add a segment to the front of the snake
def add_segment_to_front():
    snake_positions.append(snake.pos())
    snake_stamps.append(snake.stamp())

# create the snake
snake = turtle.clone()
snake.shape("square")
for i in range(INITIAL_SNAKE_LENGTH):
    snake.setpos(snake.pos()[0] + SQUARE_WIDTH, snake.pos()[1])
    add_segment_to_front()

# Determine which moves are allowed from current heading
def allowed_move(direction):
    return direction%2 != current_direction%2

# Determine what the next position of the snake should be and set the position of the
# snake turtle to match.
def calculate_next_pos():
    if current_direction==RIGHT:
        snake.setpos(snake.pos()[0] + SQUARE_WIDTH, snake.pos()[1])
    elif current_direction==LEFT:
        snake.setpos(snake.pos()[0] - SQUARE_WIDTH, snake.pos()[1])
    elif current_direction==UP:
        snake.setpos(snake.pos()[0], snake.pos()[1] + SQUARE_WIDTH)
    elif current_direction==DOWN:
        snake.setpos(snake.pos()[0], snake.pos()[1] - SQUARE_WIDTH)

# Increase the score on the scoreboard. Increase the level if appropriate.
def calculate_score():
    global score
    score = (MAX_FOOD - food_remaining)*food_score +\
             recycle_score*times_recycled - trash_penalty*trash_count
    scoreboard.clear()

    scoreboard.setpos(MIN_X, MIN_Y-50)
    scoreboard.write("Score: %s" % score, align="center", font=("Arial", 20, "bold"))

    scoreboard.setpos(MIN_X-64, MIN_Y-100)
    scoreboard.write("Food remaining: %s" %food_remaining, align="left", font=("Arial", 20, "bold"))

    scoreboard.setpos(MIN_X-64,MIN_Y-150)
    scoreboard.write("Trash on board "+str(trash_count)+"/"+str(MAX_TRASH), \
                     align="left", font=("Arial", 20, "bold"))
    
    if score != 0 and score%100==0:
        global move_step_time
        move_step_time = int(move_step_time * 2/3)

# Change to golden snake, speed up, can remove trash
def power_up():
    print('RECYCLE TIME!')
    global can_recycle, move_step_time, POWER_UP_TIME
    can_recycle = True
        
    snake.pencolor("yellow")
    snake.fillcolor('yellow')
    move_step_time = int(move_step_time * 2/3)
    
    turtle.ontimer(power_down, POWER_UP_TIME) #power down after POWER_UP_TIME seconds    

# Change color to normal, slow down, stop recycling
def power_down():
    global can_recycle
    can_recycle = False

    global power_up_present
    power_up_present = False
    
    snake.pencolor('black')
    snake.fillcolor('black')
    global move_step_time
    move_step_time = int(move_step_time * 3/2)

# Detect collision with any other objects on the screen and take appropriate action
def detect_collision():
    x_ok = MIN_X < snake.pos()[0] and snake.pos()[0] < MAX_X
    y_ok = MIN_Y < snake.pos()[1] and snake.pos()[1] < MAX_Y
    global trash_position_values
    collides_with_self = snake_positions.count(snake.pos()) > 1
    collides_with_trash = snake.pos() in trash_position_values
    collides_with_recycle = recycle_positions.count(snake.pos()) > 0

    if snake.pos() in food_positions: #food is eaten
        food_index = food_positions.index(snake.pos())
        food.clearstamp(food_stamps.pop(food_index))
        food_positions.pop(food_index)
        global food_remaining
        food_remaining -= 1

        #lengthen snake
        current_snake_pos = snake.pos()
        snake.setpos(snake_positions[0])

        snake_positions.insert(0, snake.pos())
        snake_stamps.insert(0, snake.stamp())
        snake.setpos(current_snake_pos)
        calculate_score() 
    
    if can_recycle and collides_with_trash: #recycled trash! :D
        tpvc = trash_position_values.copy()
        stamp_id = trash_position_values[snake.pos()]
        
        for value in trash_position_values:
            if trash_position_values[value] == stamp_id:
                tpvc.pop(value)
                
        trash_position_values = tpvc
        trash_positions.pop(stamp_id)
        trash.clearstamp(stamp_id)
        
        global times_recycled
        times_recycled += 1

        global trash_count
        trash_count -= 1
        
        calculate_score() 

    #Power up! Change color, move faster, recycle!
    if collides_with_recycle:
        power_up()
        despawn_power_up()

    #calculate_score()
    return (not (x_ok and y_ok)) or collides_with_self or \
           (not(can_recycle) and collides_with_trash)


# Called when the game is over.
def trigger_game_over():
    global game_over
    game_over = True
    turtle.setpos(0,0)
    turtle.write("GAME OVER!", align="center", font=("Arial", 48, "bold"))

# Move the snake by a step
def move_step():
    global current_direction
    current_direction = temp_current_direction
    if detect_collision():
        trigger_game_over()
    else:
        snake.clearstamp(snake_stamps.pop(0))
        calculate_next_pos()
        snake_positions.pop(0)
        add_segment_to_front()

        turtle.ontimer(move_step, move_step_time)
    

# Functions that are called on keypress
def move_left():
    global temp_current_direction
    if allowed_move(LEFT):
        temp_current_direction = LEFT
    
def move_right():
    global temp_current_direction
    if allowed_move(RIGHT):
        temp_current_direction = RIGHT

def move_up():
    global temp_current_direction
    if allowed_move(UP):
        temp_current_direction = UP

def move_down(): 
    global temp_current_direction
    if allowed_move(DOWN):
        temp_current_direction = DOWN

# Keypress listeners
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")
turtle.listen()

# Initialize food
food_positions = []
food_stamps = []
food = turtle.clone()
turtle.register_shape("apple.gif") 
food.shape("apple.gif")

# Spawns a new food, removes the oldest food if there are too many on the board
def spawn_food():
    if game_over:
        return
    global food_remaining
    food.setpos(random.randint(int(MIN_X/20)+1,int(MAX_X)/20-1)*20, 
                random.randint(int(MIN_Y)/20+1, int(MAX_Y)/20-1)*20)
    food_positions.append(food.pos())
    food_stamps.append(food.stamp())
    turtle.ontimer(spawn_food, food_step_time)
    if len(food_stamps) > min(5, food_remaining):
        food.clearstamp(food_stamps.pop(0))
        food_positions.pop(0)
  
    if food_remaining == 0:
        trigger_game_over()
    
# Initialize trash
trash = turtle.clone()
trash_positions = {}
trash_position_values = {}
trash_stamps = []
turtle.register_shape("cokebottle.gif")
trash.shape("cokebottle.gif")

# Spawns a new trash
def spawn_trash():
    if game_over:
        return
    #-10 is needed so that the snake can crash into the trash
    trash.setpos(random.randint(int(MIN_X/20)+1, int(MAX_X)/20-1)*20 - 10, 
                 random.randint(int(MIN_Y)/20+1, int(MAX_Y)/20-1)*20 - 10)

    #keep track of trash stamps
    stamp = trash.stamp()
    trash_stamps.append(stamp)

    #keep track of trash positions for each stamp
    positions = []
    positions.append((trash.pos()[0]+10, trash.pos()[1]+10))
    positions.append((trash.pos()[0]+10, trash.pos()[1]-10))
    positions.append((trash.pos()[0]-10, trash.pos()[1]-10))
    positions.append((trash.pos()[0]-10, trash.pos()[1]+10))
    trash_positions[stamp] = positions

    #keep reverse mapping of position to stamp id
    for position in positions:
        trash_position_values[position] = stamp

    global trash_count
    trash_count += 1

    if trash_count > MAX_TRASH:
        trigger_game_over()

    calculate_score()
    turtle.ontimer(spawn_trash, trash_step_time)

# Initialize power up
power_up_turtle = turtle.clone()
recycle_positions = []
turtle.register_shape('recycle.gif')
power_up_turtle.shape('recycle.gif')

# Spawns a power up that allows the player to remove trash
def spawn_power_up():
    if game_over:
        return
    global power_up_present, can_recycle
    if not (power_up_present or can_recycle):
        chance = random.random()
        if chance <= power_up_chance:
            power_up_present = True
            power_up_turtle.setpos(random.randint(int(MIN_X/20)+1,int(MAX_X)/20-1)*20, 
                    random.randint(int(MIN_Y)/20+1, int(MAX_Y)/20-1)*20)
            power_up_turtle.stamp()
            recycle_positions.append(power_up_turtle.pos())
            turtle.ontimer(despawn_power_up,10000)
    turtle.ontimer(spawn_power_up, power_up_step_time)

def despawn_power_up():
    global power_up_present
    if power_up_present:
        power_up_present = False
        recycle_positions.pop()
        power_up_turtle.clearstamps()
        turtle.ontimer(spawn_power_up, power_up_step_time)

# Deals with the timing of the animations
turtle.ontimer(move_step, move_step_time)
turtle.ontimer(spawn_food, food_step_time)
turtle.ontimer(spawn_trash, trash_step_time)
turtle.ontimer(spawn_power_up, power_up_step_time)

turtle.mainloop()
