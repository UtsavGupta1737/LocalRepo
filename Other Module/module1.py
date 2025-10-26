import turtle as t
def ini():
    t.pensize(1)
    t.color('white','cyan')
    t.bgcolor('black')
    t.speed(0)
    t.ht()


def csg():
    while(True):
        for i in range(1):
            for color in['red','blue','magenta','green','yellow','white']:
                t.color(color)
                t.circle(100.0)
                t.lt(10)

def pvc():
    t.color('red','cyan')
    a = 0
    b = 0
    t.pu()
    t.goto(0,-150)
    t.pd()
    while(True):
        t.fd(a)
        t.lt(b)
        a+=3
        b+=1
        if b == 210:
            break

def heart():
    t.speed(0)
    t.pensize(2)
    def curve():
        for i in range(200):
            t.rt(1)
            t.fd(1)
    t.color('red','pink')
    t.begin_fill()
    t.lt(140)
    t.fd(111.65)
    curve()
    t.lt(120)
    curve()
    t.fd(111.65)
    t.end_fill()


def main():


    code = int(input("Enter the code for pattern: "))
    ini()
    if code == 1:
        csg()

    elif code == 2:
        pvc()

    elif code == 3:
        heart()

    else:
        print("invalid input: ")
if __name__ == '__main__':
    main()





















t.done()