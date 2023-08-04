# gameplay_specific.py

import random

class MathWhiz:
    # Other methods from the original MathWhiz class...

    def play_arithmetic_game(self, chosen_game):
        """
        Plays the arithmetic game (Addition, Subtraction, Multiplication, Division).

        :param chosen_game: The chosen arithmetic game.
        :type chosen_game: str
        """
        score = 0
        total_questions = 10
        operator = {'Addition': '+', 'Subtraction': '-', 'Multiplication': '*', 'Division': '/'}[chosen_game]

        for _ in range(total_questions):
            while True:
                num1, num2, _, question = self.generate_arithmetic_question(operator)
                if question not in self.questions_asked:
                    self.questions_asked.add(question)
                    break

            user_answer = input(question)
            try:
                user_answer = float(user_answer)
                correct_answer = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2}[operator]

                if self.round_two_decimal(user_answer) == self.round_two_decimal(correct_answer):
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {correct_answer:.2f}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.display_score_and_feedback(score, total_questions)

    # Other specific gameplay-related methods from the original MathWhiz class...

