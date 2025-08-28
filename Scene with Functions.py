from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 270, 20, 'purple')
    draw_cloud(canvas, 15, 40, 'pink')
    draw_tree(canvas, 20, 'green')
    draw_tree(canvas, 120, 'red')
    draw_tree(canvas, 260, 'orange')


def draw_cloud(canvas, x, y, color):
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )

def draw_tree(canvas, x, color):
    tree_start_y = CANVAS_HEIGHT - (3/2) * CLOUD_HEIGHT
    tree_end_y = LEAVES_SIZE + CANVAS_HEIGHT - (3/2) * CLOUD_HEIGHT
    tree_start_x = x
    tree_end_x = x + LEAVES_SIZE
    trunk_start_x = tree_start_x + 0.5 * LEAVES_SIZE - 0.5 * TRUNK_WIDTH
    trunk_start_y = tree_start_y + LEAVES_SIZE

    canvas.create_rectangle(
        trunk_start_x,
        trunk_start_y - 0.6 * TRUNK_HEIGHT,
        trunk_start_x + TRUNK_WIDTH,
        trunk_start_y + 0.6 * TRUNK_HEIGHT,
        "brown"
    )
    canvas.create_oval(
        tree_start_x,
        tree_start_y,
        tree_end_x,
        tree_end_y,
        color
    )

        



if __name__ == '__main__':
    main()
