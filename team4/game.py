import random
import re


def build_dictionary():
    with open('/etc/dictionaries-common/words') as f:
        all_words = f.readlines()
    return [word.lower().strip() for word in all_words if re.match(r'^\w{3}$', word.strip())]


class WinEvent(Exception):
    pass


class Game(object):
    def __init__(self, secret=None):
        self.secret = secret or random.choice(build_dictionary())
        self.guesses = 0

    def guess(self, word):
        self.guesses += 1
        matches = sum(a == b for a, b in zip(self.secret, word))
        if matches == len(self.secret):
            msg = "It took {} guesses to guess {!r}\nWell done, you won!".format(
                self.guesses, self.secret)
            raise WinEvent(msg)
        return matches

def run_cmd_line():
    game = Game()
    try:
        while True:
            print 'Take a guess> ',
            print game.guess(raw_input())
    except KeyboardInterrupt:
        print
        print
        print "Gave up? The secret was {!r}".format(game.secret)
    except WinEvent, e:
        print e

if __name__ == '__main__':
    run_cmd_line_game()
