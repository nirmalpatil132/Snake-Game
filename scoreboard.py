from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("#4ecdc4")  # Modern teal
        self.penup()
        self.hideturtle()
        self.goto(0, 255)
        self.update_scoreboard()
        
    def load_high_score(self):
        """Load high score from file, return 0 if file doesn't exist"""
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0
        except ValueError:
            return 0
    
    def save_high_score(self):
        """Save high score to file"""
        try:
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        except:
            pass  # Handle file write errors gracefully
        
    def update_scoreboard(self):
        self.clear()
        # Main score display with modern styling
        self.goto(0, 255)
        self.color("#4ecdc4")  # Modern teal
        self.write(f"🏆 SCORE: {self.score}", align="center", font=("Arial Black", 16, "bold"))
        
        # High score display
        self.goto(-100, 255)
        self.color("#feca57")  # Golden yellow
        self.write(f"⭐ HIGH: {self.high_score}", align="center", font=("Arial", 10, "normal"))
        
        # Game stats
        if self.score > 0:
            self.goto(100, 255)
            self.color("#96ceb4")  # Mint green
            length = self.score + 3  # Initial length is 3
            self.write(f"Length: {length}", align="center", font=("Arial", 10, "normal"))
        
    def increase_score(self):
        self.score += 1
        
        # Check for new high score
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
            
            # Show achievement message for new high score
            if self.score > 1:  # Don't show on first point
                self.goto(0, 100)
                self.color("#ff6b6b")  # Modern coral
                self.write("🎉 NEW HIGH SCORE! 🎉", align="center", font=("Arial", 14, "bold"))
        
        self.update_scoreboard()
        
    def game_over(self):
        # Game over background
        self.goto(0, 50)
        self.color("#ff6b6b")  # Modern coral red
        self.write("💥 GAME OVER 💥", align="center", font=("Arial Black", 24, "bold"))
        
        # Final score
        self.goto(0, 10)
        self.color("#ffffff")  # White
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 18, "normal"))
        
        # Performance message
        self.goto(0, -20)
        if self.score >= 20:
            self.color("#feca57")  # Golden
            self.write("🏆 SNAKE MASTER! 🏆", align="center", font=("Arial", 16, "bold"))
        elif self.score >= 10:
            self.color("#96ceb4")  # Mint green
            self.write("🌟 Great Job! 🌟", align="center", font=("Arial", 16, "normal"))
        elif self.score >= 5:
            self.color("#45b7d1")  # Sky blue
            self.write("👍 Not Bad!", align="center", font=("Arial", 16, "normal"))
        else:
            self.color("#ff9ff3")  # Pink
            self.write("🔄 Try Again!", align="center", font=("Arial", 16, "normal"))
            
        # Instructions for restart
        self.goto(0, -60)
        self.color("#4ecdc4")  # Teal
        self.write("Click anywhere to exit", align="center", font=("Arial", 12, "normal"))