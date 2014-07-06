import random
import pytest

from ai import main

@pytest.mark.parametrize("seed", xrange(100, 120))
def test_ai(seed, capsys):
    """
    These seed ranges include a scenario where
    the guess is correct on the first try
    """
    random.seed(seed)
    won = main()
    assert won
    out, err = capsys.readouterr()
    assert 'you won' in out
    assert not err
