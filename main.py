import turtle

def draw_square(t, side):
    for i in range(4):
        t.forward(side)
        t.left(90)


def draw_triangle(t, side):
    for i in range(3):
        t.forward(side)
        t.left(120)


def draw_house(t):
    side = 150
    
    # Draw the square base
    draw_square(t, side)
    
    # Move turtle to top of square
    t.left(90)
    t.forward(side)
    t.right(90)
    
    # Draw the roof
    draw_triangle(t, side)


if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(1)

    draw_house(t)

    turtle.done()

