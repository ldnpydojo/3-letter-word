import random
import re
from time import sleep


def build_wordlist(file="/etc/dictionaries-common/words"):
  words = []
  with open(file) as word_file:
    for line in word_file:
      word = line.strip().lower()
      if len(word) == 3 and "'" not in word:
        words.append(word)
  return words


def dictionary():
    with open('/etc/dictionaries-common/words') as f:
        all_words = f.readlines()
    return [word.lower().strip() for word in all_words if re.match(r'^\w{3}$', word.strip())]


class WinEvent(Exception):
    pass


class Game(object):

    def __init__(self, secret=None):
        self.secret = secret or random.choice(build_wordlist())
        self.guesses = 0

    def guess(self, word):
        self.guesses += 1
        sleep(0.2)
        matches = sum(a == b for a, b in zip(self.secret, word))
        if matches == len(self.secret):
            print "It took", self.guesses, "guesses to guess", self.secret
            raise WinEvent("Well done, you won!")
        return matches

if __name__ == '__main__':
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
