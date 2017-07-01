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
    tslow.shape('classic')
    tslow.speed(10)

    for i in range(18):
        draw_squa(tslow)
        tslow.right(20)
    tslow.forward(500)
    tslow.left(30)
    tslow.circle(30)
    tslow.left(150)
    tslow.circle(30)

    window.exitonclick()


draw_square()