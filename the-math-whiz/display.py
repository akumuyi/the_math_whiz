# display.py

class MathWhiz:
    # Other methods from the original MathWhiz class...

    def display_welcome_page(self):
        """
        Displays the welcome message for the Math Whiz application.
        """
        print("Welcome to The Math Whiz!")

    def get_user_name(self):
        """
        Gets the user's name and welcomes them.
        """
        self.user_name = input("Enter your name: ")
        print(f"Welcome, {self.user_name}! What proficiency level would you like to learn today?")
        for i, level in enumerate(self.proficiency_levels, 1):
            print(f"{i}. {level}")

    # Other display-related methods from the original MathWhiz class...

