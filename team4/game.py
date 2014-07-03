import random


def dictionary():
    with open('/etc/dictionaries-common/words') as f:
        all_words = f.readlines()
    return [word.lower().strip() for word in all_words if len(word) == 3]


class WinEvent(Exception):
    pass


class Game(object):

    def __init__(self, secret=None):
        self.secret = secret or random.choice(dictionary())

    def guess(self, word):
        matches = sum(a == b for a, b in zip(self.secret, word))
        if matches == len(self.secret):
            raise WinEvent("Well done, you won!")
        return matches
