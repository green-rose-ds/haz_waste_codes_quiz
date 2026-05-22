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
