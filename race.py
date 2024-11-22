import turtle
import random


screen = turtle.Screen()
screen.title("Simple Pen Race")


colors = ["red", "blue", "green", "yellow", "purple"]
positions = [(50, 100), (50, 50), (50, 0), (50, -50), (50, -100)]


pen1 = turtle.Turtle()
pen1.color(colors[0])
pen1.penup()
pen1.goto(positions[0])
pen1.pendown()

pen2 = turtle.Turtle()
pen2.color(colors[1])
pen2.penup()
pen2.goto(positions[1])
pen2.pendown()

pen3 = turtle.Turtle()
pen3.color(colors[2])
pen3.penup()
pen3.goto(positions[2])
pen3.pendown()

pen4 = turtle.Turtle()
pen4.color(colors[3])
pen4.penup()
pen4.goto(positions[3])
pen4.pendown()

pen5 = turtle.Turtle()
pen5.color(colors[4])
pen5.penup()
pen5.goto(positions[4])
pen5.pendown()
pen1.shape("turtle")
pen2.shape("turtle")
pen3.shape("turtle")
pen4.shape("turtle")
pen5.shape("turtle")


for _ in range(100):  
    pen1.forward(random.randint(1, 10))
    pen2.forward(random.randint(1, 10))
    pen3.forward(random.randint(1, 10))
    pen4.forward(random.randint(1, 10))
    pen5.forward(random.randint(1, 10))


turtle.done()