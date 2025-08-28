from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    middle_x = CANVAS_WIDTH
    middle_y = CANVAS_HEIGHT/2
    canvas.create_rectangle(0, 0, middle_x, middle_y, 'red')

if __name__ == '__main__':
    main()
