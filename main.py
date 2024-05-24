# main.py

import pygame
import sys
from settings import *
from generate_maze import generate_maze

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Maze Game')
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    def move(self, dx, dy):
        self.rect.x += dx * CELL_SIZE
        self.rect.y += dy * CELL_SIZE

def draw_maze(maze, player):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            cell = maze[y][x]
            if cell == 'W':
                screen.blit(WALL_IMAGE, (x * CELL_SIZE, y * CELL_SIZE))
            elif cell == 'F':
                screen.blit(FINISH_IMAGE, (x * CELL_SIZE, y * CELL_SIZE))
            else:
                screen.blit(PATH_IMAGE, (x * CELL_SIZE, y * CELL_SIZE))
    screen.blit(PLAYER_IMAGE, player.rect)

def is_path(maze, x, y):
    if 0 <= x < len(maze[0]) and 0 <= y < len(maze) and (maze[y][x] == 'P' or maze[y][x] == 'F'):
        return True
    return False

def process_events(player, maze, game_won):
    """Handle all Pygame events and return a boolean status for the game loop."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            new_maze = process_keydown(event.key, player, maze, game_won)
            if new_maze is False:
                return False
            if new_maze is not None:
                return new_maze

    return maze  # Keep the game loop running by default

def process_keydown(key, player, maze, game_won):
    """Process keydown events and move the player if the path is valid."""
    if game_won:
        # Handle restart on 'R' key press after winning
        if key == pygame.K_r:
            # Generate a new maze
            new_maze = generate_maze(SCREEN_WIDTH // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE)
            # Reset player position
            player.rect.x = CELL_SIZE
            player.rect.y = CELL_SIZE
            return new_maze

        # Handle exit on 'E' key press after winning
        if key == pygame.K_e:
            pygame.quit()
            sys.exit()
    else:
        directions = {
            pygame.K_LEFT: (-1, 0),
            pygame.K_RIGHT: (1, 0),
            pygame.K_UP: (0, -1),
            pygame.K_DOWN: (0, 1)
        }

        if key in directions:
            dx, dy = directions[key]
            new_x = player.rect.x // CELL_SIZE + dx
            new_y = player.rect.y // CELL_SIZE + dy
            if is_path(maze, new_x, new_y):
                player.move(dx, dy)
                if maze[new_y][new_x] == 'F':
                    return 'won'  # Return a special value indicating the player has won

    return None  # Continue the game loop for other key handling


def display_message(message):
    """Display a message in the center of the screen."""
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(text, text_rect)

def display_info():
    """Display the info message at the bottom of the screen."""
    font = pygame.font.Font(None, 36)
    text = font.render(INFO_MESSAGE, True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 20))
    screen.blit(text, text_rect)

def main():
    maze = generate_maze(SCREEN_WIDTH // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE)
    player = Player(1, 1)
    game_won = False  # Track whether the player has won the game

    running = True
    while running:
        result = process_events(player, maze, game_won)
        if result == 'won':
            game_won = True  # Set the game won flag
        elif result is not None:
            maze = result
            game_won = False  # Reset the game won flag

        screen.fill(BACKGROUND_COLOR)
        draw_maze(maze, player)
        if game_won:
            display_message(FINAL_CELL_MESSAGE)
            display_info()
        pygame.display.flip()
        clock.tick(FPS)

        # If the game is won, wait for 'R' or 'E' key press
        while game_won:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_won = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        maze = generate_maze(SCREEN_WIDTH // CELL_SIZE, SCREEN_HEIGHT // CELL_SIZE)
                        player = Player(1, 1)
                        game_won = False  # Exit the inner loop and continue the game
                    if event.key == pygame.K_e:
                        pygame.quit()
                        sys.exit()

            screen.fill(BACKGROUND_COLOR)
            draw_maze(maze, player)
            display_message(FINAL_CELL_MESSAGE)
            display_info()
            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
