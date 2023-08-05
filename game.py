class Game:
    """
    The Game class contains methods for generating different types of game questions.
    """

    def generate_arithmetic_question(self, operator):
        """
        Generates an arithmetic question based on the given operator.

        Args:
            operator (str): The arithmetic operator (+, -, *, or /).

        Returns:
            tuple: A tuple containing the two operands, the operator, and the question string.
        """
        num1 = random.uniform(0.1, 10.0)
        num2 = random.uniform(0.1, 10.0)
        question = f"What is {num1:.2f} {operator} {num2:.2f}?"
        return num1, num2, operator, question

    def generate_square_root_question(self):
        """
        Generates a square root question.

        Returns:
            tuple: A tuple containing the number and the question string.
        """
        num = random.randint(1, 100)
        question = f"What is the square root of {num}?"
        return num, question

    def generate_cubic_root_question(self):
        """
        Generates a cubic root question.

        Returns:
            tuple: A tuple containing the number and the question string.
        """
        num = random.randint(1, 1000)
        question = f"What is the cubic root of {num}?"
        return num, question

    def generate_fraction_question(self):
        """
        Generates a fraction question.

        Returns:
            tuple: A tuple containing the numerator, the denominator, and the question string.
        """
        numerator = random.randint(1, 10)
        denominator = random.randint(2, 10)
        question = f"What is {numerator}/{denominator}?"
        return numerator, denominator, question

    def generate_decimal_question(self):
        """
        Generates a decimal question.

        Returns:
            tuple: A tuple containing the two operands, the operator, and the question string.
        """
        num1 = random.uniform(0.1, 10.0)
        num2 = random.uniform(0.1, 10.0)
        operator = random.choice(['+', '-', '*', '/'])
        question = f"What is {num1:.2f} {operator} {num2:.2f}?"
        return num1, num2, operator, question