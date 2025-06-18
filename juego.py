#!/usr/bin/env python3
import curses
import random
import time


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.reset()

    def reset(self):
        # Initialize game state
        self.height, self.width = self.screen.getmaxyx()
        self.score = 0
        self.game_over = False
        self.speed = 0.1  # seconds between moves

        # Initialize snake
        self.snake = [(self.height // 2, self.width // 4)]
        self.direction = curses.KEY_RIGHT

        # Generate first food
        self.generate_food()

        # Clear messages
        self.message = ""

    def generate_food(self):
        while True:
            # Generate a random position for the food
            food = (random.randint(1, self.height - 2),
                    random.randint(1, self.width - 2))
            # Make sure it's not on the snake
            if food not in self.snake:
                self.food = food
                break

    def change_direction(self, key):
        # Change direction if valid (can't go directly backwards)
        if key == curses.KEY_UP and self.direction != curses.KEY_DOWN:
            self.direction = key
        elif key == curses.KEY_DOWN and self.direction != curses.KEY_UP:
            self.direction = key
        elif key == curses.KEY_LEFT and self.direction != curses.KEY_RIGHT:
            self.direction = key
        elif key == curses.KEY_RIGHT and self.direction != curses.KEY_LEFT:
            self.direction = key

    def move_snake(self):
        # Get current head position
        head_y, head_x = self.snake[0]

        # Calculate new head position based on direction
        if self.direction == curses.KEY_UP:
            head_y -= 1
        elif self.direction == curses.KEY_DOWN:
            head_y += 1
        elif self.direction == curses.KEY_LEFT:
            head_x -= 1
        elif self.direction == curses.KEY_RIGHT:
            head_x += 1

        new_head = (head_y, head_x)

        # Check for collisions with walls
        if (head_y <= 0 or head_y >= self.height - 1 or
                head_x <= 0 or head_x >= self.width - 1):
            self.game_over = True
            self.message = f"Game Over! You hit a wall. Final score: {self.score}"
            return

        # Check for collision with self
        if new_head in self.snake:
            self.game_over = True
            self.message = f"Game Over! You hit yourself. Final score: {self.score}"
            return

        # Add new head
        self.snake.insert(0, new_head)

        # Check if snake ate the food
        if new_head == self.food:
            self.score += 1
            # Speed up slightly with each food eaten
            self.speed = max(0.05, self.speed * 0.95)
            # Generate new food
            self.generate_food()
        else:
            # Remove tail if food wasn't eaten
            self.snake.pop()

    def draw(self):
        self.screen.clear()

        # Draw border
        self.screen.border(0)

        # Draw score
        self.screen.addstr(0, 2, f" Score: {self.score} ")

        # Draw snake
        for i, (y, x) in enumerate(self.snake):
            if i == 0:  # Head
                self.screen.addch(y, x, "O")
            else:  # Body
                self.screen.addch(y, x, "o")

        # Draw food
        if hasattr(self, 'food'):
            food_y, food_x = self.food
            self.screen.addch(food_y, food_x, "*")

        # Draw message if there is one
        if self.message:
            msg_y = self.height // 2
            msg_x = self.width // 2 - len(self.message) // 2
            self.screen.addstr(msg_y, max(0, msg_x), self.message)

        self.screen.refresh()

    def handle_resize(self):
        # Get new dimensions
        new_height, new_width = self.screen.getmaxyx()

        # Check if snake is now out of bounds
        for y, x in self.snake:
            if y >= new_height - 1 or x >= new_width - 1:
                self.game_over = True
                self.message = "Game Over! Terminal resize made snake hit wall."
                return

        # Update dimensions
        self.height, self.width = new_height, new_width

        # Check if food is out of bounds
        food_y, food_x = self.food
        if food_y >= new_height - 1 or food_x >= new_width - 1:
            self.generate_food()


def show_instructions(screen):
    screen.clear()
    h, w = screen.getmaxyx()

    instructions = [
        "Snake Game - Instructions",
        "",
      "Use arrow keys to move the snake",
        "Eat food (*) to grow and increase your score",
        "Avoid hitting walls and yourself",
        "Press 'q' to quit, 'r' to restart",
        "",
        "Press any key to start..."
    ]

    for i, line in enumerate(instructions):
        y = h // 2 - len(instructions) // 2 + i
        x = w // 2 - len(line) // 2
        screen.addstr(y, max(0, x), line)

    screen.refresh()
    screen.getch()


def main(screen):
    # Set up screen
    curses.curs_set(0)  # Hide cursor
    screen.timeout(0)  # Non-blocking input

    # Show instructions
    show_instructions(screen)

    # Initialize game
    game = Game(screen)

    # Main game loop
    last_update = time.time()

    while True:
        # Check for input
        key = screen.getch()

        # Handle input
        if key == ord('q'):
            break
        elif key == ord('r') and game.game_over:
            game.reset()
        elif key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            game.change_direction(key)
        elif key == curses.KEY_RESIZE:
            game.handle_resize()

        # Update game state at specific intervals
        current_time = time.time()
        if current_time - last_update > game.speed and not game.game_over:
            game.move_snake()
            last_update = current_time

        # Draw game
        game.draw()

        # Small delay to reduce CPU usage
        time.sleep(0.01)


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass  # Handle Ctrl+C gracefully