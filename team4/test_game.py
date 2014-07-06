import random
from textwrap import dedent

import mock
import pytest

from game import build_dictionary, Game, run_cmd_line, WinEvent


@pytest.fixture
def game():
    return Game('cat')


build_dictionary = pytest.fixture(build_dictionary)


def test_pick_secret(build_dictionary):
    game = Game()
    assert game.secret in build_dictionary


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


@mock.patch('game.raw_input', create=True)
def test_fail_at_run_cmd_line(mock_raw_input, capsys):
    random.seed(7) # secret is now 'ate'

    mock_raw_input.side_effect = [
        'apt',
        'ape',
    ]
    with pytest.raises(StopIteration):
        run_cmd_line()
    out, err = capsys.readouterr()
    assert out == dedent('''\
        Take a guess>  1
        Take a guess>  2
        Take a guess> ''')
    assert not err


@mock.patch('game.raw_input', create=True)
def test_win_at_run_cmd_line(mock_raw_input, capsys):
    random.seed(7) # secret is now 'ate'

    mock_raw_input.side_effect = [
        'apt',
        'ape',
        'ate',
    ]
    run_cmd_line()
    out, err = capsys.readouterr()
    assert 'you won' in out
    assert 'FAIL' not in out
    assert not err
