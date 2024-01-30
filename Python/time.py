import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_ball(position):
    clear_screen()
    print(" " * position + "O")

def animate_bouncing_ball():
    max_position = 20
    direction = 1

    while True:
        draw_ball(max_position)
        time.sleep(0.1)

        max_position += direction

        if max_position >= 40 or max_position <= 0:
            direction *= -1

if __name__ == "__main__":
    animate_bouncing_ball()
