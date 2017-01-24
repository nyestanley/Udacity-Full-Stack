import turtle

def create_window():
    window = turtle.Screen()
    window.bgcolor("blue")
    
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
niesha.shape("turtle")

for r in range(1,19):
    draw_square(niesha)
    niesha.right(18)

draw_square(niesha)

window.exitonclick()
