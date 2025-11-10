import pygame
import sys

# Define constants outside the class for easy access (e.g., in a separate config.py or at the top of this file)
FPS = 60
TITLE = "AI PACMAN"
BG_COLOR = (0, 0, 0) # Black

# Add these constants near the top of your file
TILE_SIZE = 30
WALL_COLOR = (0, 0, 255)  # Blue
PELLET_COLOR = (255, 255, 255) # White

# Define the maze structure (a simple example)
MAP_DATA = [
    "########################",
    "#......................#",
    "#.###.####.####.###..#.#",
    "#P..#....#.....#...#..G#",
    "#.###.####.####.###..#.#",
    "#......................#",
    "########################",
]

class Game:
    def __init__(self):
        # 1. Initialize Pygame modules
        pygame.init()
        
        # 2. Set up the display surface
        pygame.display.set_caption(TITLE)
        
        # 3. Create a clock object for frame rate management
        self.clock = pygame.time.Clock()
        
       # 4. Set the initial game state
        self.running = True
        
        # 5. Initialize Map Data
        self.map_data = MAP_DATA 
        self.rows = len(self.map_data)
        self.cols = len(self.map_data[0])
        
        # Calculate screen dimensions based on the map size for proper scaling
        global SCREEN_WIDTH, SCREEN_HEIGHT
        SCREEN_WIDTH = self.cols * TILE_SIZE
        SCREEN_HEIGHT = self.rows * TILE_SIZE
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Placeholder for characters
        self.pacman = None
        # Placeholder for handling events, drawing, and updates (Step 5)
        self.game_state = "START"

    def run(self):
        while self.running:
            # 1. Frame Rate Control
            self.clock.tick(FPS)
            
            # 2. Handle Events (user input, closing the window)
            self.events()
            
            # 3. Update Game State (movement, scoring, AI decisions)
            self.update()
            
            # 4. Draw Everything
            self.draw()
            
        # 5. Quit Pygame when the loop exits
        pygame.quit()
        sys.exit() # You'll need to import 'sys' at the top if you use this

    # Inside class Game:
    # ...
    def events(self):
        # Handle all input and system events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # You'd check for key presses here later if you need user interaction (e.g., to quit or restart)

    def update(self):
        # This is where game logic and AI decisions happen
        # self.pacman.update(self.map_data) 
        # self.ghosts.update() 
        pass 

    def draw(self):
        # 1. Fill the screen with the background color
        self.screen.fill(BG_COLOR)
        
        # 2. Draw the maze, pellets, score, and characters here
        self.draw_map()
        # self.pacman.draw(self.screen)
        
        # 3. Update the full display surface to make changes visible
        pygame.display.flip()

    # Inside class Game:
    # ...
    def draw_map(self):
        for row_index, row in enumerate(self.map_data):
            for col_index, tile in enumerate(row):
                # Calculate the pixel position for the current tile
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if tile == '#':
                    # Draw a blue rectangle for a wall
                    pygame.draw.rect(self.screen, WALL_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
                
                elif tile == '.':
                    # Draw a white circle (pellet) in the center of the tile
                    center_x = x + TILE_SIZE // 2
                    center_y = y + TILE_SIZE // 2
                    PELLET_RADIUS = TILE_SIZE // 8
                    pygame.draw.circle(self.screen, PELLET_COLOR, (center_x, center_y), PELLET_RADIUS)
                
                # 'P' (Pacman start) and 'G' (Ghost start) tiles are left as background for now

if __name__ == '__main__':
    # Create an instance of the game
    game = Game()
    # Run the game loop
    game.run()