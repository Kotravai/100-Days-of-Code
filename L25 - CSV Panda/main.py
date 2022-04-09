import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

correct_guesses = []
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
x = data.x.to_list()
y = data.y.to_list()

while len(correct_guesses) < 50:
    answer_text = screen.textinput(title=f"{len(correct_guesses)}/50 states correct",
                                   prompt="Enter Name of the state: ").title()
    # if answer_text == "Exit":
    #     # csv with states missed by the user and exit game
    #     missed_states = []
    #     for state in states:
    #         if state not in correct_guesses:
    #             missed_states.append(state)
    #     # states_dict = {"Missed states": missed_states}
    #     df = pandas.DataFrame(missed_states)
    #     df.to_csv("Missed states list")
    #     break

    if answer_text == "Exit":
        # csv with states missed by the user and exit game with LIST COMPREHENSION
        missed_states = [state for state in states if state not in correct_guesses]
        df = pandas.DataFrame(missed_states)
        df.to_csv("Missed states list")
        break

    if answer_text in states and answer_text not in correct_guesses:
        correct_guesses.append(answer_text)
        position = states.index(answer_text)
        state_x = int(x[position])
        state_y = int(y[position])
        writer.goto(state_x, state_y)
        writer.write(answer_text, True, "center")











screen.exitonclick()
