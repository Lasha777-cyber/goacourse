from turtle import *

#we want to paint a house

#step 1:  draw a square
speed(20)
width(7)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square 

#drawing a door


forward(70)
color("brown")
begin_fill()
left(90)

forward(100)
right(90)

forward(60)
right(90)

forward(100)
end_fill()
#drawing a roof
penup()
goto(200, 200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows
color("gray")
penup()
goto(20,170)
pendown()
left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
penup()
goto(40,170)
pendown()
right(90)
forward(40)
penup()
goto(180,170)
pendown()
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(40)
penup()
goto(180,150)
pendown()
right(90)
forward(40)
penup()
goto(0,0)
pendown()
color("light green")
begin_fill()
forward(475)
left(90)
forward(395)
left(90)
forward(950)
left(90)
forward(395)
left(90)
forward(475)
end_fill()


exitonclick()