# game_choice.py

class MathWhiz:
    # Other methods from the original MathWhiz class...

    def get_user_game_choice(self, proficiency_choice):
        """
        Gets the user's chosen game based on their proficiency level.

        :param proficiency_choice: The chosen proficiency level index.
        :type proficiency_choice: int
        :return: The chosen game or 'Back' to go back to the main menu.
        :rtype: str
        """
        proficiency_level = self.proficiency_levels[proficiency_choice - 1]
        print(f"Fantastic {self.user_name}! Learning is so much fun!")
        print(f"Here are the available games for {proficiency_level} Level:")
        games_list = self.games[proficiency_level]
        for i, game in enumerate(games_list, 1):
            print(f"{i}. {game}")
        print(f"{len(games_list) + 1}. Back")

        prompt = "Enter the number of your preferred game: "
        valid_range = range(1, len(games_list) + 2)
        while True:
            choice = self.get_user_input(prompt, valid_range)
            if choice == len(games_list) + 1:
                return 'Back'
            chosen_game = games_list[choice - 1]
            print(f"You have selected {chosen_game}, let's play!")
            return chosen_game

    # Other game choice-related methods from the original MathWhiz class...

