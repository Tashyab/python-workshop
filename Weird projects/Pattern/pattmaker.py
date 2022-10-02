import turtle
from pygame import mixer
import time

wn = turtle.Screen()
wn.setup(400, 400)
wn.bgcolor("white")
wn.title("Lock Screen Patterns")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(4)

def sound():
    mixer.init()
    mixer.music.load("tune.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()
    input("Press enter key to stop.")
    mixer.music.stop()

def runtimer(t):
    ti = time.time()
    while (True):
        tk = time.time()
        if tk-ti >= t:
            sound()
            break
        else:
            continue

def one(n):
    if(n == 2):
        pen.forward(50)
    elif(n==3):
        if(2 in diglist):
            pen.forward(100)
    elif(n == 4):
        pen.right(90)
        pen.forward(50)
        pen.left(90)
    elif(n == 5):
        pen.right(45)
        pen.forward(71)
        pen.left(45)
    elif(n==6):
        pen.right(26.565)
        pen.forward(112)
        pen.left(26.565)
    elif(n==8):
        pen.right(63.435)
        pen.forward(112)
    elif(n==7):
        if(4 in diglist):
            pen.right(90)
            pen.forward(100)
            pen.left(90)
        pen.left(63.435)
    elif(n==9):
        if(5 in diglist):
            pen.right(45)
            pen.forward(142)
            pen.left(45)

def two(n):
    if(n==1):
        pen.backward(50)
    elif(n==3):
        pen.forward(50)
    elif(n==4):
        pen.right(135)
        pen.forward(71)
        pen.left(135)
    elif(n==5):
        pen.right(90)
        pen.forward(50)
        pen.left(90)
    elif(n==6):
        pen.right(45)
        pen.forward(71)
        pen.left(45)
    elif(n==7):
        pen.right(116.565)
        pen.forward(112)
        pen.left(116.565)
    elif(n==8):
        if(5 in diglist):
            pen.right(90)
            pen.forward(100)
            pen.left(90)
    elif(n==9):
        pen.right(63.435)
        pen.forward(112)
        pen.left(63.435)
    
def three(n):
    if(n==1):
        if(2 in diglist):
            pen.backward(100)
    elif(n==2):
        pen.backward(50)
    elif(n==4):
        pen.right(153.565)
        pen.forward(112)
        pen.left(153.565)
    elif(n==5):
        pen.right(135)
        pen.forward(71)
        pen.left(135)
    elif(n==6):
        pen.right(90)
        pen.forward(50)
        pen.left(90)
    elif(n==7):
        if(5 in diglist):
            pen.right(135)
            pen.forward(142)
            pen.left(135)
    elif(n==8):
        pen.right(116.565)
        pen.forward(112)
        pen.left(116.565)
    elif(n==9):
        if(6 in diglist):
            pen.right(90)
            pen.forward(100)
            pen.left(90)
    
def four(n):
    if(n==1):
        pen.left(90)
        pen.forward(50)
        pen.right(90)
    elif(n==2):
        pen.left(45)
        pen.forward(71)
        pen.right(45)
    elif(n==3):
        pen.left(26.435)
        pen.forward(112)
        pen.right(26.435)
    elif(n==5):
        pen.forward(50)
    elif(n==6):
        if(5 in diglist):
            pen.forward(100)
    elif(n==7):
        pen.right(90)
        pen.forward(50)
        pen.left(90)
    elif(n==8):
        pen.right(45)
        pen.forward(71)
        pen.left(45)
    elif(n==9):
        pen.right(26.435)
        pen.forward(112)
        pen.left(26.435)

def five(n):
    if(n==1):
        pen.left(135)
        pen.forward(71)
        pen.right(135)
    elif(n==2):
        pen.left(90)
        pen.forward(50)
        pen.right(90)
    elif(n==3):
        pen.left(45)
        pen.forward(71)
        pen.right(45)
    elif(n==4):
        pen.backward(50)
    elif(n==6):
        pen.forward(50)
    elif(n==7):
        pen.right(135)
        pen.forward(71)
        pen.left(135)
    elif(n==8):
        pen.right(90)
        pen.forward(50)
        pen.left(90)
    elif(n==9):
        pen.right(45)
        pen.forward(71)
        pen.left(45)

def six(n):
    if(n==1):
        pen.left(153.565)
        pen.forward(112)
        pen.right(153.565)
    elif(n==2):
        pen.left(135)
        pen.forward(71)
        pen.right(135)
    elif(n==3):
        pen.left(90)
        pen.forward(50)
        pen.right(90)
    elif(n==4):
        if(5 in diglist):
            pen.backward(100)
    elif(n==5):
        pen.backward(50)
    elif(n==7):
        pen.right(153.565)
        pen.forward(112)
        pen.left(153.565)
    elif(n==8):
        pen.right(135)
        pen.forward(71)
        pen.left(135)
    elif(n==9):
        pen.right(90)
        pen.forward(50)
        pen.left(90)
    
def seven(n):
    if(n==1):
        if(4 in diglist):
            pen.left(90)
            pen.forward(100)
            pen.right(90)
    elif(n==2):
        pen.left(63.565)
        pen.forward(112)
        pen.right(63.565)
    elif(n==3):
        if(5 in diglist):
            pen.left(45)
            pen.forward(172)
            pen.right(45)
    elif(n==4):
        pen.left(90)
        pen.forward(50)
        pen.right(90)
    elif(n==5):
        pen.left(45)
        pen.forward(71)
        pen.right(45)
    elif(n==6):
        pen.left(26.435)
        pen.forward(112)
        pen.right(26.435)
    elif(n==8):
        pen.forward(50)
    elif(n==9):
        if(8 in diglist):
            pen.forward(100)

def eight(n):
    if(n==1):
        pen.left(116.435)
        pen.forward(112)
        pen.right(116.435)
    if(n==2):
        if(5 in diglist):
            pen.left(90)
            pen.forward(100)
            pen.right(90)
    elif(n==3):
        pen.left(63.565)
        pen.forward(71)
        pen.right(63.565)
    elif(n==4):
        pen.left(135)
        pen.forward(71)
        pen.right(135)
    elif(n==5):
        pen.left(90)
        pen.forward(50)
        pen.right(90)
    elif(n==6):
        pen.left(45)
        pen.forward(71)
        pen.right(45)
    elif(n==7):
        pen.backward(50)
    elif(n==9):
        pen.forward(50)
    
def nine(n):
    if(n==1):
        if(5 in diglist):
            pen.left(45)
            pen.forward(142)
            pen.right(45)
    elif(n==2):
        pen.right(26.435)
        pen.forward(112)
        pen.left(26.435)
    elif(n==3):
        pen.left(90)
        pen.forward(100)
        pen.right(90)
    elif(n==4):
        pen.left(153.565)
        pen.forward(112)
        pen.right(153.565)
    elif(n==5):
        pen.left(135)
        pen.forward(71)
        pen.right(135)
    elif(n==6):
        pen.left(90)
        pen.forward(50)
        pen.right(90)
    elif(n==7):
        if(8 in diglist):
            pen.backward(100)
    elif(n==8):
        pen.backward(50)

def join(n, m):
    if(n==1):
        one(m)
    elif(n==2):
        two(m)
    elif(n==3):
        three(m)
    elif(n==4):
        four(m)
    elif(n==5):
        five(m)
    elif(n==6):
        six(m)
    elif(n==7):
        seven(m)
    elif(n==8):
        eight(m)
    elif(n==9):
        nine(m)

def setinpen(n):
    if(n == 1):
        pen.up()
        pen.goto(-50, 50)
        pen.down()

    elif(n == 2):
        pen.up()
        pen.goto(0, 50)
        pen.down()

    elif(n == 3):
        pen.up()
        pen.goto(50, 50)
        pen.down()

    elif(n == 4):
        pen.up()
        pen.goto(-50, 0)
        pen.down()

    elif(n == 5):
        pen.up()
        pen.goto(0, 0)
        pen.down()

    elif(n == 6):
        pen.up()
        pen.goto(0, 50)
        pen.down()

    elif(n == 7):
        pen.up()
        pen.goto(-50, -50)
        pen.down()

    elif(n == 8):
        pen.up()
        pen.goto(0, -50)
        pen.down()
    
    elif(n == 9):
        pen.up()
        pen.goto(50, -50)
        pen.down()
    
def button_dots():
    pen.speed(8)
    cody = -50
    for _ in range(3):
        codx = -50
        for _ in range(3):
            pen.penup()
            pen.goto(codx, cody)
            pen.pendown()
            pen.dot()
            codx+=50
        cody+=50

    pen.penup()
    pen.goto(-40, -120)
    pen.pendown()
    for _ in range(2):
        pen.forward(84)
        pen.left(90)
        pen.forward(30)
        pen.left(90)

    pen.penup()
    pen.goto(-16, -114)
    pen.write("NEXT", font=("Courier", 12, "normal"))
    pen.goto(0, 0)
    pen.pendown()
    pen.speed(4)

nlist = []
strnum = ''
with open("patternexact4.txt", "r") as f:
    txt = f.read()
    for num in txt:
        if(num != '\n'):
            strnum = strnum + num
        else:
            nlist.append(int(strnum))
            strnum = ''

for i, num in enumerate(nlist, 0):
    button_dots()

    diglist=[int(d) for d in str(nlist[i])]

    setinpen(diglist[0])
    
    for i in range(len(diglist)-1):
        join(diglist[i], diglist[i+1])

    time.sleep(1)
    pen.clear()

turtle.done()