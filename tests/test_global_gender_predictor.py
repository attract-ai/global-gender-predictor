import pytest
from global_gender_predictor import GlobalGenderPredictor


@pytest.fixture(scope='session') 
def predictor():
    return GlobalGenderPredictor()


@pytest.mark.parametrize("test_input, expected", [("tim", "Male"), ("kim", "Unknown"), ("emily", "Female")])
def test_find_gender(predictor, test_input, expected):
    assert predictor.predict_gender(test_input) == expected


def test_find_gender_case_insensitive(predictor):
    assert predictor.predict_gender("tim") == predictor.predict_gender("Tim")


@pytest.mark.parametrize("test_input_name, test_input_threshold, expected", [("taylor", 0.8, "Unknown"), ("taylor", 0.7, "Unknown"), ("taylor", 0.6, "Female")])
def test_find_gender_threshold(predictor, test_input_name, test_input_threshold, expected):
    assert predictor.predict_gender(test_input_name, threshold=test_input_threshold) == expected
