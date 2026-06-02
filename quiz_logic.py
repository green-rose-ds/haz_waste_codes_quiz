import random
import re
from quiz_dictionary import quiz_questions


def validate_name(name):
    name = name.strip().title()
    if len(name) == 0:
        return False, "Player name cannot be empty"
    if len(name) < 2:
        return False, "Player name must be at least 2 characters"
    if len(name) > 20:
        return False, "Player name must be no more than 20 characters"
    if not re.fullmatch(r'[a-zA-Z-\s]+', name):
        return False, "Player name can only contain letters, hyphens, and spaces"
    return True, name

class QuizLogic:
    def __init__(self, questions):
        self.questions = quiz_questions
        self.player_name = None
        self.matched_pairs = {}
        self.shuffled_answers = []

    def set_player_name(self, name):
        is_valid, result = validate_name(name)
        if is_valid:
            self.player_name = result
        return is_valid, result

    def prepare_answers(self):
        self.shuffled_answers = list(self.questions.values())
        random.shuffle(self.shuffled_answers)
        return self.shuffled_answers

    def attempt_match(self, item, answer):
        self.matched_pairs[item] = answer
        return self.questions[item] == answer

    def get_score(self):
        return sum(
            1 for item, answer in self.matched_pairs.items()
            if self.questions[item] == answer)

    def is_complete(self):
        return len(self.matched_pairs) == len(self.questions)

    def get_results_summary(self):
        summary = []
        for item, given_answer in self.matched_pairs.items():
            correct_answer = self.questions[item]
            summary.append({
                "item": item,
                "given_answer": given_answer,
                "correct_answer": correct_answer,
                "is_correct": given_answer == correct_answer})
        return summary
