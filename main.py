from turtle import Turtle, Screen
from question import QuestionBoard
import pandas

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

answered_list = []
# continues asking for user input until all states have been gotten
while question.score <= question.total_states:
    answered_question = question.ask_question()
    # if the user inputs exit, create a csv file of the remaining states of which the user did not answer
    if answered_question == "Exit":
        remaining_list = [states for states in question.STATES_READ if states not in answered_list]
        remaining_states = pandas.DataFrame(remaining_list)
        remaining_states.to_csv("remaining-states.csv")
        break
    elif question.check_answer(answered_question):
        if answered_question not in answered_list:
            question.add_score()
            state_turtle.goto(question.set_position(answered_question))
            state_turtle.write(answered_question)
            answered_list.append(answered_question)
    else:
        question.ask_question()

# my_screen.exitonclick()
