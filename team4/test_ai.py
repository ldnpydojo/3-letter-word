import random

from ai import main

def test_ai(capsys):
    random.seed(7) # secret is 'ate'
    main()
    out, err = capsys.readouterr()
    assert 'you won' in out
    assert not err
