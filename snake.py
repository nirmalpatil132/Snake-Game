from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Modern color schemes for snake
SNAKE_COLORS = [
    ["#ff6b6b", "#ff5252", "#d32f2f"],  # Red gradient
    ["#4ecdc4", "#26a69a", "#00695c"],  # Teal gradient  
    ["#45b7d1", "#2196f3", "#0d47a1"],  # Blue gradient
    ["#96ceb4", "#66bb6a", "#2e7d32"],  # Green gradient
    ["#feca57", "#ff9800", "#e65100"],  # Orange gradient
    ["#ff9ff3", "#e91e63", "#880e4f"]   # Pink gradient
]

class Snake:
    
    def __init__(self):
        self.segments = []
        self.color_scheme = random.choice(SNAKE_COLORS)
        self.create_snake()
        self.head = self.segments[0]
        self.setup_head_design()
        
    def create_snake(self):
        for i, position in enumerate(STARTING_POSITIONS):
            self.add_segment(position, i)
            
    def add_segment(self, position, segment_index=None):
        new_segment = Turtle("square")
        
        # Color gradient for snake body
        if segment_index == 0:  # Head
            new_segment.color(self.color_scheme[0])
            new_segment.shape("square")
        elif segment_index is not None and segment_index < 3:
            new_segment.color(self.color_scheme[1])
        else:
            new_segment.color(self.color_scheme[2])
            
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def setup_head_design(self):
        # Make head slightly different
        self.head.shape("square")
        self.head.color(self.color_scheme[0])
        self.head.shapesize(1.1, 1.1)  # Slightly larger head
            
    def extend(self):
        # Add a new segment to the snake with gradient coloring
        new_segment = Turtle("square")
        
        # Determine color based on snake length
        segment_count = len(self.segments)
        if segment_count < 5:
            new_segment.color(self.color_scheme[1])
        else:
            new_segment.color(self.color_scheme[2])
            
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
    
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
        # Add subtle animation to head
        if len(self.segments) > 5:
            self.head.shapesize(1.05 + 0.05 * (len(self.segments) % 3), 
                               1.05 + 0.05 * (len(self.segments) % 3))
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
            
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
            
    def left(self): 
        if self.head.heading() != 0:
            self.head.setheading(180)   
            
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)