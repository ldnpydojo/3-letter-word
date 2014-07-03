class WinEvent(Exception):
    pass


class Game:

    def __init__(self, secret):
        self.secret = secret

    def guess(self, word):
        return sum(a == b for a, b in zip(self.secret, word))
