import random
from quiz_dictionary import quiz_questions

class QuizLogic:
    def __init__(self, questions):
        self.questions = quiz_questions
        self.player_name = None
        self.matched_pairs = {}
    