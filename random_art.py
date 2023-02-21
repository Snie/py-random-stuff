import turtle
import random
import time
import threading
b = ["black","green","red","blue","purple","yellow","lightblue","lightgreen","grey",'pink',"brown","orange"]
c = 0
d=0
color = ""
                   
tortino = turtle.Turtle()
torta = turtle.Turtle()
def drawer(vai):
    a = 0
    randomsize = random.randint(0,360)
    vai.speed("fast")
    vai.penup()
    vai.setposition(random.randint(-300,300),random.randint(-300,300))
    vai.pendown()
    vai.color(random.choice(b))
    vai.left(random.randint(0,360))
    vai.begin_fill()
    vai.circle(20)
    vai.end_fill()
    vai.left(90)
    vai.begin_fill()
    vai.circle(20)
    vai.end_fill()
    vai.backward(10)
    vai.begin_fill()
    vai.right(120)
    vai.forward(randomsize)
    vai.left(90)
    vai.forward(23)
    vai.left(90)
    vai.forward(randomsize)
    vai.left(90)
    vai.forward(23)
    vai.end_fill()
    vai.left(90)
    vai.forward(randomsize)
    vai.color(random.choice(b))
    vai.begin_fill()
    while a != 18:
        vai.left(10)
        vai.forward(2)
        a +=1
    vai.end_fill()    
    a = 0;
        
def start():
    while 1 != 0:
        drawer(torta)
        drawer(tortino)
start()
