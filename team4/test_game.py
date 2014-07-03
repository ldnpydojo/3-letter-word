import pytest
from game import Game, WinEvent


@pytest.fixture
def game():
    return Game('cat')


@pytest.fixture
def dictionary():
    all_words = open('/etc/dictionaries-common/words').readlines()
    words = [word.lower().strip() for word in all_words if len(word) == 3]
    return words


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
