class Display:
    """
    The Display class contains methods for displaying various messages to the user.
    """

    @staticmethod
    def display_welcome_page():
        """
        Displays the welcome message.
        """
        print("Welcome to The Math Whiz!")

    def get_user_name(self):
        """
        Gets the user's name.
        """
        self.user_name = input("Enter your name: ")
        print(f"Welcome, {self.user_name}! What proficiency level would you like to learn today?")
        for i, level in enumerate(self.proficiency_levels, 1):
            print(f"{i}. {level}")