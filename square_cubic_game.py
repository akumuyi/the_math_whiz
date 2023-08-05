from math_whiz import Game, Score

class SquareCubicGame:
    """
    The SquareCubicGame class handles the gameplay for square root and cubic root questions.
    """

    def __init__(self):
        self.game = Game()
        self.score = Score()

    def play_game(self, chosen_game):
        """
        Plays the square root or cubic root game.

        Args:
            chosen_game (str): The chosen game (Square Root of Numbers or Cubic Root of Numbers).
        """
        score = 0
        total_questions = 10
        for _ in range(total_questions):
            if chosen_game == 'Square Root of Numbers':
                num, question = self.game.generate_square_root_question()
                correct_answer = math.sqrt(num)
            else:
                num, question = self.game.generate_cubic_root_question()
                correct_answer = num ** (1 / 3)

            while True:
                if question not in self.questions_asked:
                    self.questions_asked.add(question)
                    break

            user_answer = input(question)
            try:
                user_answer = float(user_answer)
                if self.score.round_two_decimal(user_answer) == self.score.round_two_decimal(correct_answer):
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {correct_answer:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.score.display_score_and_feedback(score, total_questions)