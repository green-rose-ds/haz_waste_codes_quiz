import quiz_dictionary
from quiz_logic import QuizLogic

def test_smoke():
    assert 1 + 1 == 2

def test_dictionary_items():
    assert len(quiz_dictionary.quiz_questions) == 16

def test_name_is_not_blank():
    assert QuizLogic.player_name("") == False

def test_name_length():
    assert QuizLogic.player_name("r") == False
    assert QuizLogic.player_name("rosieeeeeeeeeeeeeeeee") == False 

def test_name_is_alpha():
    assert QuizLogic.player_name("rosi3") == False

def test_correct_match_returns_true():
    quiz = QuizLogic(questions)
    item = list(questions.keys())[0]
    correct_answer = questions[item]
    result = quiz.attempt_match(item, correct_answer)
    assert result == True

def test_wrong_match_returns_false():
    quiz = QuizLogic(questions)
    item = list(questions.keys())[0]
    result = quiz.attempt_match(item, "definitely wrong answer")
    assert result == False

def test_score_is_zero_at_start():
    quiz = QuizLogic(questions)
    assert quiz.get_score() == 0

def test_score_reflects_correct_matches():
    quiz = QuizLogic(questions)
    for item, answer in list(questions.items())[:3]:
        quiz.attempt_match(item, answer)
    assert quiz.get_score() == 3

def test_quiz_not_complete_until_all_matched():
    quiz = QuizLogic(questions)
    assert quiz.is_complete() == False