from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

    
def random_color():
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "white")
    for i in range(N_CIRCLES):
        draw_circle(canvas)

def draw_circle(my_canvas):
    random_top_x = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
    random_top_y = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)
    bottom_x = random_top_x + CIRCLE_SIZE
    bottom_y = random_top_y + CIRCLE_SIZE
    color = random_color()
    my_canvas.create_oval(
        random_top_x, 
        random_top_y, 
        bottom_x,     
        bottom_y,     
        color         
    )        
    

if __name__ == '__main__':
    main()
