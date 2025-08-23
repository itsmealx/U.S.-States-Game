from turtle import Turtle, Screen
import pandas as pd
from game_manager import GameManager

class GameLoader:
    @staticmethod
    def savepoint():
        try:
            saved_data = pd.read_csv("game_data/correct_answers.csv")
        except FileNotFoundError:
            print("No previous game data.")
        else:
            for _, row in saved_data.iterrows():
                state_name = row["state"]
                x_cor = row["x"]
                y_cor = row["y"]
                coordinates = (x_cor, y_cor)

                squirtle = Turtle()
                squirtle.penup()
                squirtle.hideturtle()
                squirtle.goto(coordinates)
                squirtle.write(state_name, align="center", font=("Arial", 9, "normal"))

    @staticmethod
    def new_game():
        screen = Screen()
        game = GameManager()
        while game.score < game.items:
            answer = screen.textinput(f"{game.score}/{game.items} States Correct", prompt="Enter a state name: ").title()
            if answer == "Exit":
                game.save_correct_answer()
                break
            game.check_answer(answer)
