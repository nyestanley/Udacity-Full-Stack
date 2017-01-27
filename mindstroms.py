import turtle

def create_window():
    global window
    window = turtle.Screen()
    #window.bgcolor("blue")

def draw_flower(niesha):
    niesha.speed(1)
    niesha.color("yellow")
    niesha.fillcolor("yellow")
    niesha.fill(True)
    niesha.circle(50)
    niesha.right(90)
    niesha.circle(50)
    niesha.right(90)
    niesha.circle(50)
    niesha.right(90)
    niesha.circle(50)
    niesha.fill(False)

    niesha.color("white")
    niesha.fillcolor("white")
    niesha.fill(True)
    niesha.backward(30)
    niesha.right(90)
    niesha.circle(30)
    
    niesha.fill(False)

    niesha.penup()
    niesha.right(90)
    niesha.forward(70)

    niesha.pendown()
    niesha.color("green")
    niesha.forward(80)

    for i in range(1,3):
        niesha.left(90)
        niesha.forward(1)
        niesha.left(90)
        niesha.forward(80)

        niesha.right(90)
        niesha.forward(1)
        niesha.right(90)
        niesha.forward(80)

    niesha.right(90)
    niesha.forward(5)
    niesha.right(90)
    niesha.forward(80)

    for i in range(1,3):
        niesha.left(90)
        niesha.forward(1)
        niesha.left(90)
        niesha.forward(80)

        niesha.right(90)
        niesha.forward(1)
        niesha.right(90)
        niesha.forward(80)

    niesha.penup()
    niesha.right(180)
    niesha.forward(35)
    niesha.right(135)
    niesha.pendown()
    niesha.fillcolor("green")
    niesha.fill(True)
    niesha.forward(10)
    niesha.right(15)
    niesha.forward(10)

    niesha.right(15)
    niesha.forward(10)

    niesha.right(15)
    niesha.forward(10)

    niesha.right(135)
    niesha.forward(10)

    niesha.left(15)
    niesha.forward(10)

    niesha.left(15)
    niesha.forward(10)
    niesha.fill(False)

    niesha.hideturtle()

    
    
    #niesha.fillcolor("white")
    #niesha.right(50)
    #niesha.left(10)
    #niesha.right(90)
    #niesha.right(90)
    #niesha.right(90)
    #niesha.back(30)
    #niesha.back(20)
    #niesha.fill(True)
    #niesha.circle(30)
    #niesha.fill(False)
    

    window.exitonclick()
    
def draw_square(niesha):
    #number_of_squares = 20
    #number_of_rotations = 360/number_of_squares
    #for r in range(1,number_of_rotations):
    for i in range(1,5):
        niesha.forward(100)
        niesha.right(90)
    #niesha.right(18)  


   # brandon = turtle.Turtle()
    #brandon.circle(50)
    #brandon.color("green")

    #zoe = turtle.Turtle()
    #zoe.forward(50)
    #zoe.dot(20, "red")


create_window()

niesha = turtle.Turtle() #how to create an instance
#niesha.ht()
niesha.shape("turtle")

#for r in range(1,19):
    #draw_square(niesha)
    #niesha.right(18)

#draw_square(niesha)
draw_flower(niesha)
