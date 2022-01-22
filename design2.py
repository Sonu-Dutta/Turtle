
import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)
n=200
h=0
for i in range(360):
    c=colorsys.hls_to_rgb(h,1,0.6)
    h+=1/n
    t.color(c)
    for j in range(2):
        t.left(100)
        t.forward(5*i**j)
        