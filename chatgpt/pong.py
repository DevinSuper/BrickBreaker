import tkinter as tk
import random

# Constants
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
BALL_DIAMETER = 20
PADDLE_SPEED = 10
BALL_SPEED = 5

# Variables for player scores
score_left = 0
score_right = 0

# Function to move the paddles
def move_paddle(event):
    if event.keysym == "Up":
        canvas.move(paddle_right, 0, -PADDLE_SPEED)
    elif event.keysym == "Down":
        canvas.move(paddle_right, 0, PADDLE_SPEED)
    elif event.keysym == "w":
        canvas.move(paddle_left, 0, -PADDLE_SPEED)
    elif event.keysym == "s":
        canvas.move(paddle_left, 0, PADDLE_SPEED)

# Function to update the ball's position
def update_ball():
    global ball_x, ball_y, ball_dx, ball_dy, score_left, score_right

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if (ball_x <= PADDLE_WIDTH and
            paddle_left_coords[1] <= ball_y <= paddle_left_coords[3]):
        ball_dx = -ball_dx

    if (ball_x >= WIDTH - PADDLE_WIDTH - BALL_DIAMETER and
            paddle_right_coords[1] <= ball_y <= paddle_right_coords[3]):
        ball_dx = -ball_dx

    # Ball out of bounds
    if ball_x <= 0:
        score_right += 1
        reset_ball()
    elif ball_x >= WIDTH:
        score_left += 1
        reset_ball()

    canvas.move(ball, ball_dx, ball_dy)
    canvas.after(10, update_ball)
    update_score()

# Function to update the score display
def update_score():
    canvas.itemconfig(score_display, text=f"Player 1: {score_left}  Player 2: {score_right}")

# Function to reset the ball
def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_dx = BALL_SPEED * random.choice((1, -1))
    ball_dy = BALL_SPEED * random.choice((1, -1))
    canvas.coords(ball, ball_x - BALL_DIAMETER // 2, ball_y - BALL_DIAMETER // 2,
                  ball_x + BALL_DIAMETER // 2, ball_y + BALL_DIAMETER // 2)

# Create the main window
root = tk.Tk()
root.title("Pong with Score")

# Create a canvas widget
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Create paddles
paddle_left = canvas.create_rectangle(10, 10, 10 + PADDLE_WIDTH, 10 + PADDLE_HEIGHT, fill="white")
paddle_right = canvas.create_rectangle(WIDTH - 10 - PADDLE_WIDTH, 10, WIDTH - 10, 10 + PADDLE_HEIGHT, fill="white")

# Create the ball
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = BALL_SPEED * random.choice((1, -1))
ball_dy = BALL_SPEED * random.choice((1, -1))
ball = canvas.create_oval(ball_x - BALL_DIAMETER // 2, ball_y - BALL_DIAMETER // 2,
                          ball_x + BALL_DIAMETER // 2, ball_y + BALL_DIAMETER // 2, fill="white")

# Get the initial coordinates of the paddles
paddle_left_coords = canvas.coords(paddle_left)
paddle_right_coords = canvas.coords(paddle_right)

# Create a score display
score_display = canvas.create_text(WIDTH // 2, 20, text="Player 1: 0  Player 2: 0", fill="white", font=("Helvetica", 16))

# Bind key presses to paddle movement
canvas.bind_all("<KeyPress-Up>", move_paddle)
canvas.bind_all("<KeyPress-Down>", move_paddle)
canvas.bind_all("<KeyPress-w>", move_paddle)
canvas.bind_all("<KeyPress-s>", move_paddle)

# Initialize the game loop
update_ball()

# Start the Tkinter event loop
root.mainloop()
