from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Modern color palette
COLORS = {
    'bg': '#0a0a0a',           # Deep black
    'border': '#00ff88',       # Neon green
    'grid': '#1a1a2e',         # Dark blue-gray
    'title': '#ff6b6b',        # Coral red
    'text': '#ffffff',         # White
    'accent': '#4ecdc4',       # Teal
    'warning': '#ffd93d',      # Golden yellow
}

# Create background border decoration
def create_border():
    border = Turtle()
    border.speed(0)
    border.color(COLORS['border'])
    border.penup()
    border.goto(-290, 250)
    border.pendown()
    border.pensize(4)
    for _ in range(4):
        border.forward(580)
        border.right(90)
    border.hideturtle()

# Create grid pattern
def create_grid():
    grid = Turtle()
    grid.speed(0)
    grid.color(COLORS['grid'])
    grid.pensize(1)
    
    # Vertical lines
    for x in range(-280, 280, 20):
        grid.penup()
        grid.goto(x, -240)
        grid.pendown()
        grid.goto(x, 240)
    
    # Horizontal lines
    for y in range(-240, 260, 20):
        grid.penup()
        grid.goto(-280, y)
        grid.pendown()
        grid.goto(280, y)
    
    grid.hideturtle()

# Add game title
def create_title():
    title = Turtle()
    title.speed(0)
    title.color(COLORS['title'])
    title.penup()
    title.goto(0, 280)
    title.write("🎮 MODERN SNAKE 🐍", align="center", font=("Arial Black", 14, "bold"))
    title.hideturtle()

# Add instructions
def create_instructions():
    instructions = Turtle()
    instructions.speed(0)
    instructions.color(COLORS['text'])
    instructions.penup()
    instructions.goto(0, -280)
    instructions.write("Arrow Keys: Move • Space: Start/Pause • +/-: Speed", 
                      align="center", font=("Arial", 10, "normal"))
    instructions.hideturtle()

# Show start message
def show_start_message():
    global start_msg
    start_msg = Turtle()
    start_msg.speed(0)
    start_msg.color(COLORS['warning'])
    start_msg.penup()
    start_msg.goto(0, 0)
    start_msg.write("🚀 Press SPACE to Start! 🚀", align="center", font=("Arial", 18, "bold"))
    start_msg.hideturtle()

# Game control functions
def start_or_pause():
    global game_started, game_paused
    if not game_started:
        game_started = True
        start_msg.clear()
    else:
        game_paused = not game_paused

def increase_speed():
    global game_speed
    if game_speed > 0.05:
        game_speed -= 0.01

def decrease_speed():
    global game_speed
    if game_speed < 0.3:
        game_speed += 0.01

# Setup screen
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor(COLORS['bg'])
screen.title("🎮 Modern Snake Game 🐍")
screen.tracer(0)

# Add visual enhancements
create_border()
create_grid()
create_title()
create_instructions()

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Game variables
game_started = False
game_paused = False
game_speed = 0.15

# Show start message
show_start_message()

# Add control instructions
controls = Turtle()
controls.speed(0)
controls.color(COLORS['accent'])
controls.penup()
controls.goto(-340, 200)
controls.write("Controls:\n↑↓←→ Move\nSPACE Start/Pause\n+ Speed Up\n- Speed Down", 
              align="left", font=("Arial", 9, "normal"))
controls.hideturtle()

# Setup controls - SIMPLE AND DIRECT
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(start_or_pause, "space")
screen.onkey(increase_speed, "plus")
screen.onkey(decrease_speed, "minus")

# Main game loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    if game_started and not game_paused:
        time.sleep(game_speed - 0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()
            
        # Detect collision with wall
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or 
            snake.head.ycor() > 240 or snake.head.ycor() < -240):
            game_is_on = False
            scoreboard.game_over()
            
        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                
    elif game_started and game_paused:
        # Show pause message
        pause_msg = Turtle()
        pause_msg.speed(0)
        pause_msg.color(COLORS['warning'])
        pause_msg.penup()
        pause_msg.goto(0, 0)
        pause_msg.write("⏸️ PAUSED ⏸️\nPress SPACE to continue", 
                       align="center", font=("Arial", 18, "bold"))
        pause_msg.hideturtle()
        time.sleep(0.1)
        pause_msg.clear()
    
screen.exitonclick()