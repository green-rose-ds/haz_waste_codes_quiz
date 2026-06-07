import pytest
from quiz_dictionary import quiz_questions, tutorial_questions
from quiz_logic import validate_name, QuizLogic

"""
Unit tests for quiz_logic.py — covers name validation, quiz matching,
scoring, and submission logic for the QuizLogic class.
"""

def test_smoke():
    """
    Smoke test to test pytest is functioning.
    """
    assert 1 + 1 == 2

def test_dictionary_items():
    """
    Tests that the quiz_question dictionary contains the correct 14 key:value pairs.
    """
    assert len(quiz_questions) == 14

def test_tutorial_items():
    """
    Tests that the tutorial_question dictionary contains the correct 2 key:value pairs.
    """
    assert len(tutorial_questions) == 2

def test_name_is_not_blank():
    """
    Tests that a empty string fails name validation.
    """
    is_valid, _ = validate_name("")
    assert is_valid == False

def test_name_is_not_too_short():
    """
    Tests that a string with less than 2 characters fails name validation.
    """
    is_valid, _ = validate_name("r")
    assert is_valid == False
    
def test_name_is_not_too_long():
    """
    Tests that a string with more than 20 characters fails name validation.
    """
    is_valid, _ = validate_name("rosieeeeeeeeeeeeeeeeee")
    assert is_valid == False

def test_name_is_alpha():
    """
    Tests that a string containing anything other than alpha characters fails name validation.
    """
    is_valid, _ = validate_name("rosi3")
    assert is_valid == False

def test_hyphenated_name_is_valid():
    """
    Tests that a string that uses a hyphen in the name passes validation.
    """
    is_valid, result = validate_name("rose-anne")
    assert is_valid == True
    assert result == "Rose-Anne"

def test_valid_name_is_stored():
    """
    Tests that if a name meets the validation requirements it is stored in player_name.
    """
    quiz = QuizLogic(quiz_questions)
    quiz.set_player_name("Rosie")
    assert quiz.player_name == "Rosie"

def test_correct_match_returns_true():
    """
    Tests that correct answers as per quiz_questions dict returns True.
    """
    quiz = QuizLogic(quiz_questions)
    item = list(quiz.questions.keys())[0]
    correct_answer = quiz_questions[item]
    result = quiz.attempt_match(item, correct_answer)
    assert result == True


def test_score_is_zero_at_start():
    """
    Tests that the quiz logic refreshes to 0 on each call.
    """
    quiz = QuizLogic(quiz_questions)
    assert quiz.get_score() == 0

def test_score_reflects_correct_matches():
    """
    Tests that the answer summary will correctly reflect the players correct or incorrect matches
    """
    quiz = QuizLogic(quiz_questions)
    for item, answer in list(quiz_questions.items())[:3]:
        quiz.attempt_match(item, answer)
    assert quiz.get_score() == 3

def test_quiz_not_complete_until_all_answered():
    """
    Tests that is_complete raises a ValueError when dropdowns still show the default placeholder value.
    Uses mocking with StringVar object to simulate unanswered dropdowns without requiring Tkinter to run.
    """
    quiz = QuizLogic(quiz_questions)
    mock_selections = {item: type('var', (), 
        {'get': lambda self: "Select a definition..."})() 
        for item in quiz_questions}
    with pytest.raises(ValueError):
        quiz.is_complete(mock_selections)

def test_quiz_complete_when_all_answered():
    """
    Tests that is_complete returns True when all dropdowns have a valid selection that is not the default placeholder value.
    Uses mocking with StringVar object populated with the correct answers to simulate a fully completed quiz without requiring Tkinter to run.
    """
    quiz = QuizLogic(quiz_questions)
    mock_selections = {item: type('var', (), 
        {'get': lambda self, a=answer: a})() 
        for item, answer in quiz_questions.items()}
    assert quiz.is_complete(mock_selections) == True