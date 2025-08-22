import pandas as pd
import turtle

class GameManager:
    def __init__(self):
        self._data = pd.read_csv("game_data/50_states.csv")
        self._correct_answer = []
        self.score = 0
        self.items = len(self.states_list)

    @property
    def states_list(self):
        return self._data["state"].tolist()

    def get_coordinates(self, state_name: str) -> tuple:
        """Get the answer from the user as the state name and returns the location."""
        state =  self._data[self._data["state"] == state_name]
        x_cor = state["x"]
        y_cor = state["y"]
        location = (x_cor.item(), y_cor.item())
        return location

    def check_answer(self, answer: str):
        if answer in self.states_list:
            self._correct_answer.append(answer)
            squirtle = turtle.Turtle()
            squirtle.penup()
            squirtle.hideturtle()
            squirtle.goto(self.get_coordinates(answer))
            squirtle.write(answer, align="center", font=("Arial", 9, "normal"))
            self.score += 1

    def save_correct_answer(self):
        """Save correct answers in a CSV file."""
        data_dict = {
            "state": [],
            "x": [],
            "y": []
        }

        for state_name in self._correct_answer:
            state_row = self._data[self._data["state"] == state_name]#getting Row data
            if not state_row.empty:
                x = state_row["x"].item()
                y = state_row["y"].item()
                data_dict["state"].append(state_name)
                data_dict["x"].append(x)
                data_dict["y"].append(y)

        df = pd.DataFrame(data_dict)
        df.to_csv("game_data/correct_answers.csv", index=False)


