# user_input.py

class MathWhiz:
    # Other methods from the original MathWhiz class...

    @staticmethod
    def get_user_input(prompt, valid_range):
        """
        Gets user input for numerical choices within a valid range.

        :param prompt: The prompt message for the user.
        :type prompt: str
        :param valid_range: The valid range of choices.
        :type valid_range: range
        :return: The user's choice within the valid range.
        :rtype: int
        """
        while True:
            choice = input(prompt)
            if choice.isdigit() and int(choice) in valid_range:
                return int(choice)
            print("Invalid choice. Please enter a valid number.")

    def get_user_proficiency_level(self):
        """
        Gets the user's chosen proficiency level.

        :return: The chosen proficiency level as an index.
        :rtype: int
        """
        prompt = "Enter the number of your proficiency level choice: "
        valid_range = range(1, len(self.proficiency_levels) + 1)
        return self.get_user_input(prompt, valid_range)

    # Other user input-related methods from the original MathWhiz class...

