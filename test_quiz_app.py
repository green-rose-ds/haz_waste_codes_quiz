from quiz_dictionary import quiz_questions, tutorial_questions
from quiz_logic import validate_name, QuizLogic

def test_smoke():
    assert 1 + 1 == 2

def test_dictionary_items():
    assert len(quiz_questions) == 14

def test_tutorial_items():
    assert len(tutorial_questions) == 2

def test_name_is_not_blank():
    is_valid, _ = validate_name("")
    assert is_valid == False

def test_name_is_not_too_short():
    is_valid, _ = validate_name("r")
    assert is_valid == False
    
def test_name_is_not_too_long():
    is_valid, _ = validate_name("rosieeeeeeeeeeeeeeeeee")
    assert is_valid == False

def test_name_is_alpha():
    is_valid, _ = validate_name("rosi3")
    assert is_valid == False

def test_hyphenated_name_is_valid():
    is_valid, result = validate_name("rose-anne")
    assert is_valid == True
    assert result == "Rose-Anne"

def test_valid_name_is_stored():
    quiz = QuizLogic(quiz_questions)
    quiz.set_player_name("Rosie")
    assert quiz.player_name == "Rosie"

def test_correct_match_returns_true():
    quiz = QuizLogic(quiz_questions)
    item = list(quiz.questions.keys())[0]
    correct_answer = quiz_questions[item]
    result = quiz.attempt_match(item, correct_answer)
    assert result == True

def test_wrong_match_returns_false():
    quiz = QuizLogic(quiz_questions)
    item = list(quiz_questions.keys())[0]
    result = quiz.attempt_match(item, "That's an incorrect answer")
    assert result == False

def test_score_is_zero_at_start():
    quiz = QuizLogic(quiz_questions)
    assert quiz.get_score() == 0

def test_score_reflects_correct_matches():
    quiz = QuizLogic(quiz_questions)
    for item, answer in list(quiz_questions.items())[:3]:
        quiz.attempt_match(item, answer)
    assert quiz.get_score() == 3

def test_quiz_not_complete_until_all_matched():
    quiz = QuizLogic(quiz_questions)
    assert quiz.is_complete() == False