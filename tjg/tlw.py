#!python3
import os, sys
import glob
import random
import re
import time

class Game(object):

    def __init__(self, length=3):
        self.unusable_words = set()

        #
        # Technique 1
        #
        self.usable_words = set()
        self.length = int(length)

        #
        # Technique 2
        #
        self.definite = [set() for i in range(self.length)]
        self.possible = [set() for i in range(self.length)]
        self.impossible = [set() for i in range(self.length)]

    @staticmethod
    def score(w1, w2):
        return sum(1 for i1, i2 in zip(w1, w2) if i1 == i2)

    #
    # Technique 1 is basically brute-force: select a word at random;
    # if you get the full score, you've won; if you score zero, eliminate
    # any word with any letters matching; otherwise, do nothing.
    #
    def select_word1(self):
        return random.choice(list(self.usable_words))

    def update_stats1(self, word, score):

        def discard_word(w):
            self.usable_words.remove(w)
            self.unusable_words.add(w)

        discard_word(word)
        #
        # Remove any words with any of the letters in our zero-score
        # word.
        #
        if score == 0:
            for usable_word in set(self.usable_words):
                if any(i1 == i2 for i1, i2 in zip(word, usable_word)):
                    discard_word(usable_word)

        print("There are %d words left" % len(self.usable_words))

    def select_word2(self):
        raise NotImplementedError

    def update_stats2(self, word, score):
        raise NotImplementedError

    select_word = select_word1
    update_stats = update_stats1

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
