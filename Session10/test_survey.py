import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """Fixture to provide a survey object for test functions."""
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)

def test_store_single_response(language_survey):
    """Test storing a single response with a fixture."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test storing three responses with a fixture."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
