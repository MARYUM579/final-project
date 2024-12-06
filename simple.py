import pygame
import random

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game variables
player_width, player_height = 50, 50
player_x = WIDTH // 4
player_y = HEIGHT - player_height - 10
player_speed = 10
obstacle_width, obstacle_height = 50, 50
obstacle_speed = 10
score = 0

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Temple Run")

# Font for score
font = pygame.font.SysFont("Arial", 30)

# Clock to control game speed
clock = pygame.time.Clock()

# Player and obstacle classes
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = player_width
        self.height = player_height
        self.speed = player_speed
    
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

class Obstacle:
    def __init__(self):
        self.x = random.choice([WIDTH // 4, WIDTH // 2, 3 * WIDTH // 4])
        self.y = -obstacle_height
        self.width = obstacle_width
        self.height = obstacle_height
        self.speed = obstacle_speed

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# Function to check collision
def check_collision(player, obstacle):
    if player.x < obstacle.x + obstacle.width and player.x + player.width > obstacle.x:
        if player.y < obstacle.y + obstacle.height and player.y + player.height > obstacle.y:
            return True
    return False

# Game loop
player = Player(player_x, player_y)
obstacles = [Obstacle()]
running = True
while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")
    
    # Move obstacles and check for collisions
    for obstacle in obstacles[:]:
        obstacle.move()
        obstacle.draw(screen)
        
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
            obstacles.append(Obstacle())
            score += 1  # Increment score as obstacle moves off screen
        
        if check_collision(player, obstacle):
            running = False  # End the game if there is a collision
    
    # Draw player
    player.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    # Update the display
    pygame.display.flip()
    
    # Frame rate control
    clock.tick(30)

# Game over message
game_over_text = font.render("Game Over! Final Score: " + str(score), True, RED)
screen.fill(WHITE)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)  # Wait for 3 seconds before closing the game

# Quit pygame
pygame.quit()
