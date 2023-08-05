class Score:
    """
    The Score class contains methods for calculating and displaying scores and feedback.
    """

    @staticmethod
    def round_two_decimal(num):
        """
        Rounds a number to two decimal places.

        Args:
            num (float): The number to round.

        Returns:
            float: The rounded number.
        """
        return round(num, 2)

    def display_score_and_feedback(self, score, total_questions):
        """
        Displays the user's score and feedback based on their performance.

        Args:
            score (int): The user's score.
            total_questions (int): The total number of questions.
        """
        overall_score_percentage = (score / total_questions) * 100

        print(f"Your overall score: {overall_score_percentage:.2f}%")

        if overall_score_percentage >= 90:
            print(f"Congratulations {self.user_name}, you are a math genius!")
        elif 70 <= overall_score_percentage < 90:
            print(f"Excellent {self.user_name}, stay focused!")
        elif 50 <= overall_score_percentage < 70:
            print(f"Average performance {self.user_name}, you can do better!")
        elif 30 <= overall_score_percentage < 50:
            print(f"Below-par performance {self.user_name}, keep at it!")
        else:
            print(f"Keep going {self.user_name}, you'll improve!")