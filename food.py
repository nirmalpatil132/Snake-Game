from turtle import Turtle
import random

# Modern food colors
FOOD_COLORS = ["#ff6b6b", "#feca57", "#ff9ff3", "#45b7d1", "#96ceb4"]

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.8, 0.8)
        self.color("#ff6b6b")  # Modern coral red
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        # Generate random position within the game boundaries
        random_x = random.randint(-260, 260)
        random_y = random.randint(-220, 220)
        
        # Snap to grid (20x20 grid system)
        random_x = (random_x // 20) * 20
        random_y = (random_y // 20) * 20
        
        self.goto(random_x, random_y)
        
        # Simple food appearance without effects to prevent stress
        if random.randint(1, 8) == 1:  # 12.5% chance for special food
            self.color("#feca57")  # Golden yellow
            self.shape("square")
            self.shapesize(0.9, 0.9)
        else:
            self.color(random.choice(FOOD_COLORS))
            self.shape("circle")
            self.shapesize(0.8, 0.8)