class WinEvent(Exception):
    pass


class Game:

    def __init__(self, secret):
        self.secret = secret

    def guess(self, word):
        matches = sum(a == b for a, b in zip(self.secret, word))
        if matches == len(self.secret):
            raise WinEvent("Well done, you won!")
        return matches
