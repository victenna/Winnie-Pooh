import turtle,random
import time
wn=turtle.Screen()
wn.setup(1300,1000)
wn.bgcolor('gold')
turtle.tracer(2)

image0='wpooh.gif'
wn.addshape(image0)
wpooh0=turtle.Turtle()
wpooh0.shape(image0)
wpooh0.up()
wpooh0.goto(400,150)

TEXT_FONT=('Arial', 20,'bold')
text=turtle.Turtle()
text.hideturtle() 
text.up()
text.setposition(100,-300)
text.write('Build a Winnue Pooh', font=TEXT_FONT)
text.up()
text.goto(-450,320)
text.down()
text.write(' Drag the parts of the Winnie Pooh with \
the left button of the computer mouse',font=TEXT_FONT)

text.up()
text.goto(-500,280)
text.down()
text.color('blue')
text.write('After you built Winnie Pooh press keyboard\
"space" button to animate him',font=TEXT_FONT)


image=['1.gif','2.gif','3.gif','4.gif','5.gif','6.gif','7.gif']
t=[]
for n in range(7):
    wn.addshape(image[n])
    t.append(turtle.Turtle())
    t[n].up()
    t[n].shape(image[n])
    if n>0:
        t[n].goto(random.randint(-400,400),\
                  random.randint(-300,300))


for m in range(1,7):
    t[m].ondrag(t[m].goto)
    
image1='wpooh1_.gif'
image2='wpooh2_.gif'
wn.addshape(image1)
wn.addshape(image2)
wpooh=turtle.Turtle()
wpooh.hideturtle()
wpooh.up()
wpooh.goto(0,-150)
def move():
    global j
    q=1
    delta=2
    if t[1].xcor()<150 and t[1].xcor()>110 and t[1].ycor()<-15 and t[1].ycor()>-75:
        if t[2].xcor()<-120 and t[2].xcor()>-180 and t[2].ycor()<-40 and t[2].ycor()>-110:
            if abs(t[3].xcor())<35 and t[3].ycor()<-190 and t[3].ycor()>-250:
                if abs(t[4].xcor())<40 and t[4].ycor()<-60 and t[4].ycor()>-130:
                    if t[5].xcor()<-105 and t[5].xcor()>-165 and t[5].ycor()<-250 and t[5].ycor()>-310:
                        if t[6].xcor()<105 and t[6].xcor()>45 and t[6].ycor()<-285 and t[6].ycor()>-345:
                            move1()
n=-1
def move1():
    global n
    n=n+1
    if n==0:
        wn.clear()
        wn.bgcolor('gold')
    wpooh.showturtle()
    wpooh.shape(image1)
    time.sleep(0.2)
    wpooh.shape(image2)
    time.sleep(0.2)
    wn.ontimer(move1)
move()

wn.onkey(move,'space')
wn.listen()
