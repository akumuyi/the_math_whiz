# math_whiz.py

import random
import math


class MathWhiz:
    def __init__(self):
        """
        Initializes the MathWhiz class with attributes.
        """
        self.user_name = ""
        self.proficiency_levels = ['Beginner', 'Intermediate']
        self.games = {
            'Beginner': ['Addition', 'Subtraction', 'Multiplication', 'Division'],
            'Intermediate': ['Square Root of Numbers', 'Cubic Root of Numbers', 'Fractions', 'Decimals'],
        }
        self.questions_asked = set()

    # Other methods from the original MathWhiz class...

