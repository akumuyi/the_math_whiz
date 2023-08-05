import random
import math


class MathWhiz:
    """
    The MathWhiz class represents the main application and handles user interactions.

    Attributes:
        user_name (str): The name of the user.
        proficiency_levels (list): A list of available proficiency levels.
        games (dict): A dictionary mapping proficiency levels to available games.
        questions_asked (set): A set to keep track of asked questions to avoid repetition.
    """

    def __init__(self):
        self.user_name = ""
        self.proficiency_levels = ['Beginner', 'Intermediate']
        self.games = {
            'Beginner': ['Addition', 'Subtraction', 'Multiplication', 'Division'],
            'Intermediate': ['Square Root of Numbers', 'Cubic Root of Numbers', 'Fractions', 'Decimals'],
        }
        self.questions_asked = set()

    def run(self):
        """
        Starts the Math Whiz application.
        """
        self.display_welcome_page()
        self.get_user_name()

        while True:
            proficiency_choice = self.get_user_proficiency_level()
            chosen_game = self.get_user_game_choice(proficiency_choice)

            if chosen_game == 'Back':
                continue

            self.play_game(chosen_game)

            play_again = input("Do you want to play another game? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thank you for feeding your brain, that was fun!")
                break
            else:
                print("Great! Let's play another game.")
                print("What proficiency level would you like to learn today?")
                for i, level in enumerate(self.proficiency_levels, 1):
                    print(f"{i}. {level}")
                continue