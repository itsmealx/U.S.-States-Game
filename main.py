import turtle
from game_manager import GameManager
from game_loader import GameLoader

#Screen Setup
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=730, height=500)
screen.cv._rootwindow.resizable(False, False)
bg_img = "game_data/blank_states_img.gif"
screen.addshape(bg_img)
turtle.shape(bg_img)

game = GameManager()

load_savepoint = screen.textinput("Load previous game.", prompt="Continue game? (Y/N):").title()
if load_savepoint == "Y":
    game.load_previous_score()
    GameLoader.savepoint()

    while game.score < game.items:
        answer = screen.textinput(f"{game.score}/{game.items} States Correct", prompt="Enter a state name: ").title()
        if answer == "Exit": #exit the game and save correct answer as a csv file
            game.save_correct_answer()
            break

        if answer in game.states_list and not game.is_already_guessed(answer):
            game.check_answer(answer)
        elif game.is_already_guessed(answer):
            print(f"You've already guessed {answer}.")
else:
    GameLoader.new_game()


