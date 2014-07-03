import pytest
from game import Game

@pytest.fixture
def game():
    return Game('cat')

def test_send_word(game):
    assert game.guess('dog') == 0
