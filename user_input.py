class UserInput:
    """
    The UserInput class contains methods for handling user input.
    """

    def get_user_proficiency_level(self):
        """
        Gets the user's proficiency level choice.
        """
        choice = input("Enter the number of your proficiency level choice: ")
        while not choice.isdigit() or int(choice) not in range(1, len(self.proficiency_levels) + 1):
            print("Invalid choice. Please enter a valid number.")
            choice = input("Enter the number of your proficiency level choice: ")
        return int(choice)

    def get_user_game_choice(self, proficiency_choice):
        """
        Gets the user's game choice for the selected proficiency level.
        """
        proficiency_level = self.proficiency_levels[proficiency_choice - 1]
        print(f"Fantastic {self.user_name}! Learning is so much fun!")
        print(f"Here are the available games for {proficiency_level} Level:")
        games_list = self.games[proficiency_level]
        for i, game in enumerate(games_list, 1):
            print(f"{i}. {game}")
        print(f"{len(games_list) + 1}. Back")
        game_choice = input("Enter the number of your preferred game: ")
        while not game_choice.isdigit() or int(game_choice) not in range(1, len(games_list) + 2):
            print("Invalid choice. Please enter a valid number.")
            game_choice = input("Enter the number of your preferred game: ")

        if int(game_choice) == len(games_list) + 1:
            return 'Back'

        chosen_game = games_list[int(game_choice) - 1]
        print(f"You have selected {chosen_game}, let's play!")
        return chosen_game