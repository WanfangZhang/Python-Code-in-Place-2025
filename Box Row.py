from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES
r=(CANVAS_HEIGHT/BOX_SIZE-1)*BOX_SIZE

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for c in range(N_BOXES):
        draw_square(canvas,r,c)

def draw_square(canvas,r,c):
    x=c*BOX_SIZE
    y=r
    end_x=x+BOX_SIZE
    end_y=y+BOX_SIZE
    canvas.create_rectangle(x,y,end_x,end_y,"white","black")



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    
