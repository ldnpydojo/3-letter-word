#!python3
import os, sys
import glob
import random
import re
import time

class Game(object):

    def __init__(self, length=3):
        self.unusable_words = set()
        self.usable_words = set()
        self.length = int(length)

        #~ self.definite = [set() for i in range(self.length)]
        #~ self.possible = [set() for i in range(self.length)]
        #~ self.impossible = [set() for i in range(self.length)]

    @staticmethod
    def score(w1, w2):
        return sum(1 for i1, i2 in zip(w1, w2) if i1 == i2)

    def select_word1(self):
        return random.choice(list(self.usable_words))

    select_word = select_word1

    def discard_word(self, word):
        self.usable_words.remove(word)
        self.unusable_words.add(word)

    def update_stats(self, word, score):
        self.discard_word(word)
        #
        # Remove any words with any of the letters in our zero-score
        # word.
        #
        if score == 0:
            for usable_word in set(self.usable_words):
                if any(i1 == i2 for i1, i2 in zip(word, usable_word)):
                    self.discard_word(usable_word)

        print("There are %d words left" % len(self.usable_words))

    def run(self):
        self.usable_words = set(w.strip() for w in open("words.txt") if len(w) == 1 + self.length)
        target_word = random.choice(list(self.usable_words))
        print("Guess:", target_word)
        while True:
            word = self.select_word()
            score = self.score(word, target_word)
            print("%s gives score %d" % (word, score))
            if score == self.length:
                break
            else:
                self.update_stats(word, score)
                time.sleep(0.5)

        print("Complete: the word was %s" % target_word)

if __name__ == '__main__':
    Game(*sys.argv[1:]).run()
