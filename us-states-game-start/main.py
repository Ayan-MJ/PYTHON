# TODO 1: Convert the guess to title case
# TODO 2: Check if the guess is among 50 states
# TODO 3: Write guesses onto the map
# TODO 4: Use a loop to allow the user to keep guessing
# TODO 5: Record the correct guess in the list
# TODO 6: Keep track of the score

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_state = []

# To keep the game running until type exit
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"Guess the state {len(guessed_state)}/{len(states)}",
                                    prompt="What's another state are there?")
    if answer_state == "Exit":
        # List of states which have been missed
        missing_state = [i for i in states if i not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state.title() in states:
        x = int(data[data.state == answer_state.title()].x)
        y = int(data[data.state == answer_state.title()].y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(answer_state.title(), align="center")
        guessed_state.append(answer_state.title())
