from math_whiz import Game, Score

class ArithmeticGame:
    """
    The ArithmeticGame class handles the gameplay for arithmetic-related questions.
    """

    def __init__(self):
        self.game = Game()
        self.score = Score()

    def play_game(self, chosen_game):
        """
        Plays the arithmetic game.

        Args:
            chosen_game (str): The chosen arithmetic game (Addition, Subtraction, Multiplication, or Division).
        """
        score = 0
        total_questions = 10
        operator = '+' if chosen_game == 'Addition' else '-' if chosen_game == 'Subtraction' else '*' if chosen_game == 'Multiplication' else '/'
        for _ in range(total_questions):
            while True:
                num1, num2, _, question = self.game.generate_arithmetic_question(operator)
                if question not in self.questions_asked:
                    self.questions_asked.add(question)
                    break

            user_answer = input(question)
            try:
                user_answer = float(user_answer)
                if operator == '+':
                    correct_answer = num1 + num2
                elif operator == '-':
                    correct_answer = num1 - num2
                elif operator == '*':
                    correct_answer = num1 * num2
                else:
                    correct_answer = num1 / num2

                if self.score.round_two_decimal(user_answer) == self.score.round_two_decimal(correct_answer):
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {correct_answer:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.score.display_score_and_feedback(score, total_questions)