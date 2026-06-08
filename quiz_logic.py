import random
import re
from quiz_dictionary import quiz_questions, tutorial_questions


def validate_name(name):
    """
        Validates a player's name against a set of rules.
        Strips blank spaces and converts to title case before validation.
        A valid name must be between 2 and 20 characters and contain only letters, hyphens, and spaces.

        Argument:
            name (str): The raw name string entered by the player.

        Return:
            tuple: A tuple of (bool, str)
            The bool indicates whether the name is valid, and the str is either the cleaned name if valid, or an error message if invalid.

        Examples:
            validate_name("rosie ")
                (True, "Rosie")
            validate_name("")
                (False, "Player name cannot be empty")
            validate_name("rose-anne")
                (True, "Rose-Anne")
    """
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
    """
    Manages the state and logic for a single quiz session.
    Handles player name validation, random shuffling of answers, recording player's matches, calculating the players score, and generating a sumaary of results. 
    This class is intentionally kept independent of any app code to ensure they are pure functions and remain testable.

    Attributes:
        quiz_questions (dict): The quiz questions dictionary where keys are HP codes and values are their definitions.
        player_name (str): The validated player name, None until set.
        matched_pairs (dict): Records the player's matches as {item: answer_given}.
        shuffled_answers (list): The shuffled list of answers for display in the righthand side column of the quiz.
    """
    def __init__(self, questions):
        """
        Initialises a new quiz session with an empty state.

        Arguments:
            quiz_questions (dict): The quiz questions dictionary to use for this session.
        """
        self.questions = quiz_questions
        self.player_name = None
        self.matched_pairs = {}
        self.shuffled_answers = []

    def set_player_name(self, name):
        """
        Validates and stores the player's name on the self instance.
        Calls validate_name to check the name against the validation rules. 
        Only stores the name if validation passes.

        Arguments:
            name (str): The raw name string entered by the player.

        Returns:
            tuple: A tuple of (bool, str) passed through from validate_name.
            Returns either (True, cleaned_name) or (False, error_message).
        """
        is_valid, result = validate_name(name)
        if is_valid:
            self.player_name = result
        return is_valid, result

    def prepare_options_for_definition_dropdown(self, item):
     """
     Generates a list of 6 answer options for a given definition.
     Includes the correct answer plus 5 randomly selected wrong answers from the remaining definitions.

     Arguments:
       - item (str): The HP code to generate options for.

     Returns:
       - list: A shuffled list of 6 answer strings.
    """
     correct_answer = self.questions[item]
     wrong_answers = [v for k, v in self.questions.items() if k != item]
     wrong_sample = random.sample(wrong_answers, 5)
     answer_options = [correct_answer] + wrong_sample
     random.shuffle(answer_options)
     return answer_options

    def attempt_match(self, item, answer):
        """
        Records a player's match attempt and checks if it is correct.
        Stores the match in matched_pairs if correct or incorrect, so all of the player's choices are available for the results summary.

        Arguments:
            item (str): The HP code the player selected from the lefthand column.
            answer (str): The description the player selected from the righthand column.

        Returns:
            bool: True if the answer matches the correct definition for the selected HP code, False otherwise.
        """
        self.matched_pairs[item] = answer
        return self.questions[item] == answer
    
    def can_submit(self):
        """
        Checks whether the player has matched all items.
        Compares the total recorded matches against the total number of questions to see if submission is allowed.

        Returns:
            tuple: A tuple of (bool, str) where the bool indicates whether submission is allowed. 
            (str) is either a confirmation message or an error message showing how many items are still to be matched.
        """
        if len(self.matched_pairs) < len(self.questions):
            remaining = len(self.questions) - len(self.matched_pairs)
            return False, f"You still have {remaining} unmatched item(s). Please match all items before you submit."
        return True, "All items matched"

    def get_score(self):
        """
        Calculates the player's score.
        Counts the number of matched pairs where the player's answer matches the correct answer in the questions dictionary.
        Recalculated each call to remain accurate.

        Returns:
            int: The number of correct matches made by the player.
        """
        return sum(
            1 for item, answer in self.matched_pairs.items()
            if self.questions[item] == answer)

    def is_complete(self, selected_answers):
     """
     Checks whether all dropdowns have been answered before submission.
     Raises a ValueError if any dropdown still shows the default placeholder, indicating the player hasn't made a selection for every HP code.

     Arguments:
        selected_answers (dict): Dictionary of {item: tk.StringVar} from the quiz screen dropdowns.

     Returns:
        bool: True if player has selected an answer in all dropdowns.

     Raises:
        ValueError: If one or more dropdowns still show the default value.
     """
     unanswered_dropdowns = [item for item, var in selected_answers.items()
                  if var.get() == "Please select a definition..."]
     if unanswered_dropdowns:
        remaining_to_fill = len(unanswered_dropdowns)
        raise ValueError(
            f"You still have {remaining_to_fill} unanswered question(s). "
            f"Please answer all questions before submitting.")
     return True

    def get_results_summary(self):
        """
        Generates a detailed summary of the player's results.
        Builds a list for each matched pair, containing the item, the player's answer, the correct answer, and whether the match was correct. 
        Used to display results back to the player at the end of the quiz.

        Returns:
            list: A list of dictionaries, one per question, each with the following keys:
                  - item (str): The HP code
                  - given_answer (str): The answer the player has chose
                  - correct_answer (str): The correct definition answer
                  - is_correct (bool): Whether the players match was correct
        """
        summary = []
        for item, given_answer in self.matched_pairs.items():
            correct_answer = self.questions[item]
            summary.append({
                "item": item,
                "given_answer": given_answer,
                "correct_answer": correct_answer,
                "is_correct": given_answer == correct_answer})
        return summary
