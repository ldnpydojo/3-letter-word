import pytest
from game import Game, WinEvent, dictionary


@pytest.fixture
def game():
    return Game('cat')


dictionary = pytest.fixture(dictionary)


def test_pick_secret(dictionary):
    game = Game()
    assert game.secret in dictionary


def test_send_word(game):
    assert game.guess('dog') == 0
    assert game.guess('cog') == 1
    assert game.guess('cot') == 2


def test_cheat(game):
    assert game.guess('c') == 1


def test_win(game):
    with pytest.raises(WinEvent):
        game.guess('cat')
    with pytest.raises(WinEvent):
        assert game.guess('cats') == 1
