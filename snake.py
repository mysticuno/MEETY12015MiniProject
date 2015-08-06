
"""
This is an example of what students might make out of the mini project.
"""

import turtle
import random

turtle.penup()
turtle.ht()
turtle.title("Python the Python Python")
#turtle.tracer()

# draw wall
wall = turtle.clone()
wall.shape("square")
wall.shapesize(20, 40, 20)
wall.pencolor("green")
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

game_over = False

move_step_time = 1000
food_step_time = 5000
trash_step_time = 7500


score = 0
scoreboard = turtle.clone()
food_score = 20
# Write the initial scoreboard. This will increment every 100 points.
scoreboard.setpos(MIN_X, MIN_Y-50)
scoreboard.write("Score: %s" % score, align="center", font=("Arial", 20, "bold"))

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
def increment_score():
    global score
    score += food_score
    scoreboard.clear()
    scoreboard.write("Score: %s" % score, align="center", font=("Arial", 20, "bold"))
    
    if score%100==0:
        global move_step_time
        move_step_time = int(move_step_time * 2/3)

# Detect collision with any other objects on the screen and take appropriate action
def detect_collision():
    x_ok = MIN_X < snake.pos()[0] and snake.pos()[0] < MAX_X
    y_ok = MIN_Y < snake.pos()[1] and snake.pos()[1] < MAX_Y
    collides_with_self = snake_positions.count(snake.pos()) > 1
    collides_with_trash = trash_positions.count(snake.pos()) > 0

    if snake.pos() in food_positions:
        food_index = food_positions.index(snake.pos())
        food.clearstamp(food_stamps.pop(food_index))
        food_positions.pop(food_index)
        
        current_snake_pos = snake.pos()
        snake.setpos(snake_positions[0])

        snake_positions.insert(0, snake.pos())
        snake_stamps.insert(0, snake.stamp())
        snake.setpos(current_snake_pos)

        increment_score()
    return (not (x_ok and y_ok)) or collides_with_self or collides_with_trash

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
    food.setpos(random.randint(int(MIN_X/20)+1,int(MAX_X)/20-1)*20, 
                random.randint(int(MIN_Y)/20+1, int(MAX_Y)/20-1)*20)
    food_positions.append(food.pos())
    food_stamps.append(food.stamp())
    turtle.ontimer(spawn_food, food_step_time)
    if len(food_stamps) > 5:
        food.clearstamp(food_stamps.pop(0))
        food_positions.pop(0)

# Initialize trash
trash = turtle.clone()
trash_positions = []
turtle.register_shape("cokebottle.gif")
trash.shape("cokebottle.gif")

# Spawns a new trash
def spawn_trash():
    if game_over:
        return
    trash.setpos(random.randint(int(MIN_X/20)+1, int(MAX_X)/20-1)*20 - 10, 
                 random.randint(int(MIN_Y)/20+1, int(MAX_Y)/20-1)*20 - 10)
    trash.stamp()
    trash_positions.append((trash.pos()[0]+10, trash.pos()[1]+10))
    trash_positions.append((trash.pos()[0]+10, trash.pos()[1]-10))
    trash_positions.append((trash.pos()[0]-10, trash.pos()[1]-10))
    trash_positions.append((trash.pos()[0]-10, trash.pos()[1]+10))
    
    turtle.ontimer(spawn_trash, trash_step_time)

# Deals with the timing of the animations
turtle.ontimer(move_step, move_step_time)
turtle.ontimer(spawn_food, food_step_time)
turtle.ontimer(spawn_trash, trash_step_time)

turtle.mainloop()
