from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_pyramid(canvas)   

def draw_pyramid(canvas):
    base_width = BRICKS_IN_BASE * BRICK_WIDTH
    start_x = (CANVAS_WIDTH - base_width) / 2
    start_y = CANVAS_HEIGHT - BRICK_HEIGHT

    for r in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - r
        row_start_x = start_x + (BRICKS_IN_BASE - bricks_in_row) * BRICK_WIDTH / 2
        for brick in range(bricks_in_row):
            x1 = row_start_x + brick * BRICK_WIDTH
            y1 = start_y - r * BRICK_HEIGHT
            x2 = x1 + BRICK_WIDTH
            y2 = y1 + BRICK_HEIGHT
            canvas.create_rectangle(x1, y1, x2, y2,'yellow','black')

if __name__ == '__main__':
    main()
