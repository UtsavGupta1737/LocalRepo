import time
import random as r
import turtle as t
delay = 0.1 #initial score
score = 0
high_score = 0
#creating a window screen
w = t.Screen()
w.title("Snake Game")
w.bgcolor('black')
w.setup(600,600)
w.tracer(0)
h = turtle.Turtle()
h.shape('square')
h.color('white')
h.pu()
h.goto(0,0)
h.direction = 'Stop'
t.done()
