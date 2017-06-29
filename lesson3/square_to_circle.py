import turtle


def draw_squa(go):
    for i in range(4):
        go.forward(100)
        go.right(90)


def draw_square():
    window = turtle.Screen()
    window.bgcolor('blue')

    tslow = turtle.Turtle()
    tslow.color('yellow')
    tslow.shape('turtle')
    tslow.speed(10)

    for i in range(18):
        draw_squa(tslow)
        tslow.right(20)


    window.exitonclick()


draw_square()
