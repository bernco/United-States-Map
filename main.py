from turtle import Turtle, Screen
from question import QuestionBoard

question = QuestionBoard()

my_screen = Screen()
my_screen.title("Name a US state")
image = "blank_states_img.gif"
my_screen.addshape(image)
my_turtle = Turtle()
my_turtle.shape(image)
state_turtle = Turtle()
state_turtle.hideturtle()
state_turtle.pu()

while question.score <= 50:
    answered_question = question.ask_question()
    if question.check_answer(answered_question):
        question.add_score()
        state_turtle.goto(question.set_position(answered_question))
        state_turtle.write(answered_question)
    else:
        question.ask_question()
my_screen.exitonclick()
