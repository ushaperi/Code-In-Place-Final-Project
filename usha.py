import turtle

bg = turtle.Screen()
bg.bgcolor("pink")

cat = turtle.Turtle()
cat.shape('circle')
cat.color('black')
cat.speed(3)
cat.pensize(2)


def move(cat, x, y):
    cat.penup()
    cat.setposition(x,y)
    cat.pendown()

move(cat, -65, 0)
cat.left(90)
cat.forward(65)
cat.left(240)
cat.forward(30)
cat.left(30)
cat.forward(60)
cat.left(45)
cat.forward(30)
cat.left(230)
cat.forward(65)
cat.right(45)
cat.forward(25)

move(cat, -65, 0)

cat.left(90)
cat.forward(25)
cat.right(65)
cat.forward(150)
cat.left(105)
cat.forward(160)
cat.left(106)
cat.forward(155)

move(cat,-30,25)
cat.begin_fill()
cat.fillcolor('black')
cat.circle(5)
cat.end_fill()

move(cat,25,25)
cat.begin_fill()
cat.fillcolor('black')
cat.circle(5)
cat.end_fill()

move(cat, -15, 5)
cat.right(106)
cat.forward(20)

cat.hideturtle()


