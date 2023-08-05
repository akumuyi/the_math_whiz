from math_whiz import Game, Score

class FractionGame:
    """
    The FractionGame class handles the gameplay for fraction questions.
    """

    def __init__(self):
        self.game = Game()
        self.score = Score()

    def play_game(self, chosen_game):
        """
        Plays the fraction game.

        Args:
            chosen_game (str): The chosen game (Fractions).
        """
        score = 0
        total_questions = 10
        for _ in range(total_questions):
            numerator, denominator, question = self.game.generate_fraction_question()

            while True:
                if question not in self.questions_asked:
                    self.questions_asked.add(question)
                    break

            user_answer = input(question)
            try:
                user_answer = eval(user_answer)  # Safely evaluate the user's input as a Python expression
                correct_answer = numerator / denominator

                if self.score.round_two_decimal(user_answer) == self.score.round_two_decimal(correct_answer):
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {correct_answer:.2f}.")
            except (ValueError, ZeroDivisionError, SyntaxError):
                print("Invalid input. Please enter a valid fraction (e.g., 1/2, 0.75).")

        self.score.display_score_and_feedback(score, total_questions)