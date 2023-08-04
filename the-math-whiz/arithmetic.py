# arithmetic.py

class MathWhiz:
    # Other methods from the original MathWhiz class...

    def generate_arithmetic_question(self, operator):
        """
        Generates an arithmetic question with random operands and operator.

        :param operator: The arithmetic operator ('+', '-', '*', '/').
        :type operator: str
        :return: The operands, operator, and the question string.
        :rtype: tuple
        """
        num1 = random.uniform(0.1, 10.0)
        num2 = random.uniform(0.1, 10.0)
        question = f"What is {num1:.2f} {operator} {num2:.2f}?"
        return num1, num2, operator, question

    # Other arithmetic-related methods from the original MathWhiz class...

