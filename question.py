from turtle import Turtle, Screen
import pandas

STATE_FILES = pandas.read_csv("50_states.csv")
STATES_READ = STATE_FILES.state.to_list()
STATES_X = STATE_FILES.x.to_list()
STATES_Y = STATE_FILES.y.to_list()
TOTAL_STATES = len(STATES_READ)


class QuestionBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.score = 0

    def check_answer(self, state_answered):
        if state_answered in STATES_READ:
            return True

    def ask_question(self):
        screen = Screen()
        inputted_state = screen.textinput(f"{self.score}/{TOTAL_STATES} gotten", "Type in a US state")
        return inputted_state

    def add_score(self):
        self.score += 1

    def set_position(self, state_answered):
        state_details = STATE_FILES[STATE_FILES.state == state_answered]
        position = (state_details.to_dict())
        state_num = STATES_READ.index(state_answered)
        position_x = position["x"][state_num]
        position_y = position["y"][state_num]
        return position_x, position_y
