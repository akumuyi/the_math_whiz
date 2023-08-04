# gameplay.py

import random

class MathWhiz:
    # Other methods from the original MathWhiz class...

    def play_game(self, chosen_game):
        """
        Initiates the selected game and handles user interaction.

        :param chosen_game: The chosen game.
        :type chosen_game: str
        """
        if chosen_game in ['Addition', 'Subtraction', 'Multiplication', 'Division']:
            self.play_arithmetic_game(chosen_game)
        elif chosen_game == 'Square Root of Numbers':
            self.play_square_root_game()
        elif chosen_game == 'Cubic Root of Numbers':
            self.play_cubic_root_game()
        elif chosen_game == 'Fractions':
            self.play_fractions_game()
        elif chosen_game == 'Decimals':
            self.play_decimals_game()

    # Other gameplay-related methods from the original MathWhiz class...

