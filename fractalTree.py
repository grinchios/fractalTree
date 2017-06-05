import turtle

def intree(branchLen,t,th):
    if branchLen < 20:
        t.color('green')
    else:
        t.color('brown')
    if branchLen > 5:
        t.pensize(th)
        t.forward(branchLen)
        t.right(40)
        intree(branchLen-10,t,th-2)
        t.left(20)
        intree(branchLen-10,t,th-2)
        t.left(40)
        intree(branchLen-10,t,th-2)
        t.left(20)
        intree(branchLen-10,t,th-2)
        t.right(40)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    #turtle.tracer(0, 0)
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.hideturtle()
    t.color("brown")
    th = 14
    intree(80,t,th)
    #turtle.update()
    myWin.exitonclick()

main()

