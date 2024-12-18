'''import pyxel

class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)

        # Set the initial position of the square
        self.x = 75
        self.y = 55
        self.score = 0

        # Set the initial position and velocity of the sprite
        self.sprite_x = 80
        self.sprite_y = 60
        self.sprite_dx = 2
        self.sprite_dy = 2

        # Start the game loop
        pyxel.run(self.update, self.draw)

    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2

        # Simple interaction: Increase score when square reaches top-left corner
        if self.x < 10 and self.y < 10:
            self.score += 1

        # Update the sprite's position
        self.sprite_x += self.sprite_dx
        self.sprite_y += self.sprite_dy

        # Bounce the sprite off the edges of the screen
        if self.sprite_x <= 0 or self.sprite_x >= 160:
            self.sprite_dx *= -1
        if self.sprite_y <= 0 or self.sprite_y >= 120:
            self.sprite_dy *= -1

    def draw(self):
        # Clear the screen with black (color 0)
        pyxel.cls(0)

        # Draw a square (color 9)
        pyxel.rect(self.x, self.y, 10, 10, 9)

        # Draw the moving sprite (color 11)
        pyxel.circ(self.sprite_x, self.sprite_y, 5, 11)

        # Display the score
        pyxel.text(5, 5, f"Score: {self.score}", 7)

        # Display a message when score is high
        if self.score >= 5:
            pyxel.text(50, 50, "You’re doing grrrrate!", 8)'''

# Run the game
import pyxel
Screen_width = 256
Screen_height = 256
class Target:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.alive = True  
        pyxel.load("my_resource.pyxres")
    
    def update(self):
        # Implement target movement logic here (if applicable)
        pass
    def draw(self):
        if self.alive:
            #pyxel.circ(self.x, self.y, self.size, self.color)
            pyxel.blt(self.x, self.y, 0, 0, 0, 64, 64, 0)
    def check_hit(self, player_x, player_y):
        # Check if the click is within the target's bounds
        if self.x <= player_x <= self.x + 64 and self.y <= player_y <= self.y + 64:
            self.alive = False
            return True
        return False
class App:
    def __init__(self):
        pyxel.init(Screen_width, Screen_height, title="Aim Trainer", capture_scale=1)
        pyxel.mouse(True)
        self.targets = []
        self.score = 0  # Initialize the score
        self.game_started = False
        self.time_left = 10  # Initial time in seconds
        self.win = False
        pyxel.run(self.update, self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if not self.game_started:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                self.game_started = True
        else:
            # Target generation logic (replace with your preferred method)
            if pyxel.frame_count % 30 == 0:  # Generate a target every 30 frames
                self.targets.append(Target(
                    pyxel.rndf(10, Screen_width - 10),
                    pyxel.rndf(10, Screen_height - 10),
                    pyxel.rndf(5, 15),
                    pyxel.rndi(1, 15)
                ))
            # Remove hit targets
            for i in range(len(self.targets) - 1, -1, -1):
                if not self.targets[i].alive:
                    del self.targets[i]
            # Handle player shot
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                player_x = pyxel.mouse_x
                player_y = pyxel.mouse_y
                for target in self.targets:
                    if target.check_hit(player_x, player_y):
                        self.score += 1  # Increment the score
            # Update timer
            if self.time_left > 0:
                self.time_left -= 1 / 30  # Update time every frame (30fps)
            else:
                # Game over logic
                print("Game Over!")
                #self.game_started = False  # Reset for a new game
                self.time_left = 0
                if self.score >= 5:
                    self.win = True
                
    def draw(self):
        pyxel.cls(3) # Set background to color 1
        if not self.game_started:
            self.start_screen()
        elif self.game_started and self.time_left == 0:
            # Draw the score screen
            pyxel.text(Screen_width // 2 - 40, Screen_height // 2 - 10, "Game Over!", 7)
            pyxel.text(Screen_width // 2 - 40, Screen_height // 2 + 10, f"Your score: {self.score}", 7)  # Display the score
            #self.game_started = False  # Reset for a new game
        else:
            # Draw targets
            for target in self.targets:
                target.draw()
                #pyxel.blt(50, 50, 0, 0, 0, 16, 16, 0)
            # Display score
            pyxel.text(5, 5, f"Score: {self.score}", 7)
            # Display time
            pyxel.text(Screen_width - 50, 5, f"Time: {int(self.time_left)}", 7)
    def start_screen(self):
        pyxel.text(Screen_width // 2 - 40, Screen_height // 2 - 10, "Aim Trainer", 7)
        pyxel.text(Screen_width // 2 - 30, Screen_height // 2 + 10, "Click to start", 7,)
App()

