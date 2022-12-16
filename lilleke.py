import turtle
from turtle import *
from math import sqrt
from math import cos
from math import pi
from random import randrange


n = int(input('Palun sisesta õielehtede arv: '))
r = float(input('Palun sisesta ringi raadius: '))


nurk = 360/n

### Kolmandat külge on võimalik arvutada valemiga a**2=b**2+c**2-2*b*c*cos(nurk). Nurk peab väljenduma radiaanides.

nurk_rad = (nurk*pi)/180

kolmas = sqrt(2*(r**2)-2*(r**2)*cos(nurk_rad))
              
### Kolmas külg on tippu joonistava poolringi raadius.
              
r_2 = kolmas/2

### Hakkame joonistama!
### Aga enne lisame natuke värvi. Iga õielehe jaoks valib juhuslike arvude generaator välja uue värvi.

kuva = turtle.Screen()
kuva.setup(1000,1000, startx = 300, starty = 50)

kuva.bgcolor('gold')
kuva.title('Lilleke rohus')
värvid = ['green','red','blue','crimson','aqua','brown','chocolate','darkorchid','deepskyblue1','lawngreen']

t = turtle.Pen()
t.pensize(5)
speed(1)
delay(0)

for i in range (n):
    t.color(värvid[randrange(9)])
    t.begin_fill()
    t.forward(r)
    t.left(nurk/2)
    t.circle(r_2,180)
    t.left(nurk/2)
    t.forward(r)
    t.left(180)
    t.end_fill()
exitonclick()
