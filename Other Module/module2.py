import turtle as t
t.pensize(5)
t.speed(1)
t.color('white','cyan')
t.ht()
turtle.bgcolor('black')
t.pu()
t.goto(00.00,200.00)
t.pd()
t.write("Yash Gupta",align = "center", font =("candara",30,"bold"))
t.begin_fill()
t.goto(0.0,0.0)
for i in range (5):
    if i == 2:
        t.fd(200.0)
        t.rt(90)
    else:
        t.fd(100.0)
        t.rt(90)
t.end_fill()
turtle.mainloop()
