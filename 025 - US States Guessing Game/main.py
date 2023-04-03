import pandas
import turtle

IMG_PATH = "blank_states_img.gif"
DATA_PATH = "50_states.csv"
OUTPUT_PATH = "missed_states.csv"
NUM_STATES = 50
FONT = ("Arial", 14, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

screen.addshape(IMG_PATH)
turtle.shape(IMG_PATH)

data = pandas.read_csv(DATA_PATH)
score = 0
guessed_states = []


def get_user_answer():
    global score
    return screen.textinput(
        title=f"Guess the State | Score: {score}/{NUM_STATES}", prompt="Enter a state name, or 'exit' to leave the game: ")


def add_state_name_to_map(state, x, y):
    pen.goto(x, y)
    pen.write(state, font=FONT)


def output_missed_states():
    data[~data.state.isin(guessed_states)].state.to_csv(OUTPUT_PATH)


def main():
    global score
    while score < NUM_STATES:
        answer = get_user_answer()
        if answer == "exit":
            output_missed_states()
            break
        if answer not in guessed_states:
            query = data[data.state == answer]
            if not query.empty:
                row = query.iloc[0]
                add_state_name_to_map(row.state, row.x, row.y)
                score += 1
                guessed_states.append(row.state)


main()
screen.exitonclick()
