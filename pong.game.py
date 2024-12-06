import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
player1_x, player2_x = 50, WIDTH - 50 - PADDLE_WIDTH
player1_y, player2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2, HEIGHT // 2 - PADDLE_HEIGHT // 2

# Set up the ball
BALL_SIZE = 15
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])

# Set up the game clock
clock = pygame.time.Clock()

# Score variables
player1_score = 0
player2_score = 0
font = pygame.font.SysFont('Arial', 30)

def draw():
    screen.fill(BLACK)
    
    # Draw paddles
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    
    # Draw the ball
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    
    # Draw the score
    player1_score_text = font.render(str(player1_score), True, WHITE)
    player2_score_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_score_text, (WIDTH // 4, 20))
    screen.blit(player2_score_text, (WIDTH * 3 // 4 - player2_score_text.get_width(), 20))
    
    # Draw the middle line
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    pygame.display.update()

def handle_input():
    global player1_y, player2_y

    keys = pygame.key.get_pressed()

    # Player 1 controls (W/S keys)
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= 6
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += 6

    # Player 2 controls (Up/Down arrows)
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 6
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += 6

def move_ball():
    global ball_x, ball_y, ball_dx, ball_dy, player1_score, player2_score

    ball_x += ball_dx
    ball_y += ball_dy

    # Ball bouncing off the top and bottom walls
    if ball_y <= 0 or ball_y + BALL_SIZE >= HEIGHT:
        ball_dy = -ball_dy

    # Ball hitting the left paddle
    if ball_x <= player1_x + PADDLE_WIDTH and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx

    # Ball hitting the right paddle
    if ball_x + BALL_SIZE >= player2_x and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx

    # Ball goes out of bounds on the left or right
    if ball_x < 0:
        player2_score += 1
        reset_ball()

    if ball_x + BALL_SIZE > WIDTH:
        player1_score += 1
        reset_ball()

def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_dx = random.choice([-4, 4])
    ball_dy = random.choice([-4, 4])

def main():
    global player1_score, player2_score

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input()
        move_ball()
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
player1_x, player2_x = 50, WIDTH - 50 - PADDLE_WIDTH
player1_y, player2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2, HEIGHT // 2 - PADDLE_HEIGHT // 2

# Set up the ball
BALL_SIZE = 15
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])

# Set up the game clock
clock = pygame.time.Clock()

# Score variables
player1_score = 0
player2_score = 0
font = pygame.font.SysFont('Arial', 30)

def draw():
    screen.fill(BLACK)
    
    # Draw paddles
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    
    # Draw the ball
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    
    # Draw the score
    player1_score_text = font.render(str(player1_score), True, WHITE)
    player2_score_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_score_text, (WIDTH // 4, 20))
    screen.blit(player2_score_text, (WIDTH * 3 // 4 - player2_score_text.get_width(), 20))
    
    # Draw the middle line
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    pygame.display.update()

def handle_input():
    global player1_y, player2_y

    keys = pygame.key.get_pressed()

    # Player 1 controls (W/S keys)
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= 6
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += 6

    # Player 2 controls (Up/Down arrows)
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 6
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += 6

def move_ball():
    global ball_x, ball_y, ball_dx, ball_dy, player1_score, player2_score

    ball_x += ball_dx
    ball_y += ball_dy

    # Ball bouncing off the top and bottom walls
    if ball_y <= 0 or ball_y + BALL_SIZE >= HEIGHT:
        ball_dy = -ball_dy

    # Ball hitting the left paddle
    if ball_x <= player1_x + PADDLE_WIDTH and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx

    # Ball hitting the right paddle
    if ball_x + BALL_SIZE >= player2_x and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx

    # Ball goes out of bounds on the left or right
    if ball_x < 0:
        player2_score += 1
        reset_ball()

    if ball_x + BALL_SIZE > WIDTH:
        player1_score += 1
        reset_ball()

def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_dx = random.choice([-4, 4])
    ball_dy = random.choice([-4, 4])

def main():
    global player1_score, player2_score

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input()
        move_ball()
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
player1_x, player2_x = 50, WIDTH - 50 - PADDLE_WIDTH
player1_y, player2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2, HEIGHT // 2 - PADDLE_HEIGHT // 2

# Set up the ball
BALL_SIZE = 15
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])

# Set up the game clock
clock = pygame.time.Clock()

# Score variables
player1_score = 0
player2_score = 0
font = pygame.font.SysFont('Arial', 30)

def draw():
    screen.fill(BLACK)
    
    # Draw paddles
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    
    # Draw the ball
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    
    # Draw the score
    player1_score_text = font.render(str(player1_score), True, WHITE)
    player2_score_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_score_text, (WIDTH // 4, 20))
    screen.blit(player2_score_text, (WIDTH * 3 // 4 - player2_score_text.get_width(), 20))
    
    # Draw the middle line
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    pygame.display.update()

def handle_input():
    global player1_y, player2_y

    keys = pygame.key.get_pressed()

    # Player 1 controls (W/S keys)
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= 6
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += 6

    # Player 2 controls (Up/Down arrows)
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 6
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += 6

def move_ball():
    global ball_x, ball_y, ball_dx, ball_dy, player1_score, player2_score

    ball_x += ball_dx
    ball_y += ball_dy

    # Ball bouncing off the top and bottom walls
    if ball_y <= 0 or ball_y + BALL_SIZE >= HEIGHT:
        ball_dy = -ball_dy

    # Ball hitting the left paddle
    if ball_x <= player1_x + PADDLE_WIDTH and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx

    # Ball hitting the right paddle
    if ball_x + BALL_SIZE >= player2_x and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx

    # Ball goes out of bounds on the left or right
    if ball_x < 0:
        player2_score += 1
        reset_ball()

    if ball_x + BALL_SIZE > WIDTH:
        player1_score += 1
        reset_ball()

def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_dx = random.choice([-4, 4])
    ball_dy = random.choice([-4, 4])

def main():
    global player1_score, player2_score

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input()
        move_ball()
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
player1_x, player2_x = 50, WIDTH - 50 - PADDLE_WIDTH
player1_y, player2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2, HEIGHT // 2 - PADDLE_HEIGHT // 2

# Set up the ball
BALL_SIZE = 15
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])

# Set up the game clock
clock = pygame.time.Clock()

# Score variables
player1_score = 0
player2_score = 0
font = pygame.font.SysFont('Arial', 30)

def draw():
    screen.fill(BLACK)
    
    # Draw paddles
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    
    # Draw the ball
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    
    # Draw the score
    player1_score_text = font.render(str(player1_score), True, WHITE)
    player2_score_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_score_text, (WIDTH // 4, 20))
    screen.blit(player2_score_text, (WIDTH * 3 // 4 - player2_score_text.get_width(), 20))
    
    # Draw the middle line
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    pygame.display.update()

def handle_input():
    global player1_y, player2_y

    keys = pygame.key.get_pressed()

    # Player 1 controls (W/S keys)
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= 6
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += 6

    # Player 2 controls (Up/Down arrows)
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= 6
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += 6

def move_ball():
    global ball_x, ball_y, ball_dx, ball_dy, player1_score, player2_score

    ball_x += ball_dx
    ball_y += ball_dy

    # Ball bouncing off the top and bottom walls
    if ball_y <= 0 or ball_y + BALL_SIZE >= HEIGHT:
        ball_dy = -ball_dy

    # Ball hitting the left paddle
    if ball_x <= player1_x + PADDLE_WIDTH and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx

    # Ball hitting the right paddle
    if ball_x + BALL_SIZE >= player2_x and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT:
        ball_dx = -ball_dx

    # Ball goes out of bounds on the left or right
    if ball_x < 0:
        player2_score += 1
        reset_ball()

    if ball_x + BALL_SIZE > WIDTH:
        player1_score += 1
        reset_ball()

def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_dx = random.choice([-4, 4])
    ball_dy = random.choice([-4, 4])

def main():
    global player1_score, player2_score

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input()
        move_ball()
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
