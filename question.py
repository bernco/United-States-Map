from turtle import Turtle, Screen
import pandas

# using the pandas library, read the csv and save in a file called state_files
STATE_FILES = pandas.read_csv("50_states.csv")


# Question class that inherits from Turtle class
class QuestionBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.score = 0
        self.STATES_READ = STATE_FILES.state.to_list()
        self.total_states = len(self.STATES_READ)



    def check_answer(self, state_answered):
        """returns True if the answered state is in the list of states"""
        if state_answered in self.STATES_READ:
            return True

    def ask_question(self):
        """:returns the inputted state by the user"""
        screen = Screen()
        inputted_state = screen.textinput(f"{self.score}/{self.total_states} gotten", "Type in a US state")
        return inputted_state.title()

    def add_score(self):
        """adds one to the current score of the user"""
        self.score += 1

    def set_position(self, state_answered):
        """:returns the x and y coordinates to be used to locate the state"""
        state_details = STATE_FILES[STATE_FILES.state == state_answered]
        position = (state_details.to_dict())
        state_num = self.STATES_READ.index(state_answered)
        position_x = position["x"][state_num]
        position_y = position["y"][state_num]
        return position_x, position_y
