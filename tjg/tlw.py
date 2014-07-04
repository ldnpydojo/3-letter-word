#!python3
import os, sys
import glob
import random
import re
import string
import time

class Game(object):

    def __init__(self, length_or-word):
        self.discarded_words = set()
        self.words = set()
        try:
            self.length = int(length)
        except ValueError:


        #
        # Technique 2
        #
        self.definite = [set() for i in range(self.length)]
        self.possible = [set(string.ascii_lowercase) for i in range(self.length)]
        self.impossible = [set() for i in range(self.length)]

    @staticmethod
    def score(w1, w2):
        return sum(1 for i1, i2 in zip(w1, w2) if i1 == i2)

    def discard_word(self, word):
        self.words.remove(word)
        self.discarded_words.add(word)

    #
    # Technique 1 is basically brute-force: select a word at random;
    # if you get the full score, you've won; if you score zero, eliminate
    # any word with any letters matching; otherwise, do nothing.
    #
    def select_word1(self):
        return random.choice(list(self.words))

    def update_stats1(self, word, score):
        #
        # Remove any words with any of the letters in our zero-score
        # word.
        #
        if score == 0:
            for usable_word in set(self.words):
                if any(i1 == i2 for i1, i2 in zip(word, usable_word)):
                    discard_word(usable_word)

        print("There are %d words left" % len(self.words))

    def select_word2(self):
        candidate_letters = [a | b for a, b in zip(self.definite, self.possible)]
        for word in self.words:
            if all(i1 in i2 for i1, i2 in zip(word, candidate_letters)):
                return word

    def update_stats2(self, word, score):
        if score == 0:
            for i, c in enumerate(word):
                self.possible[i].remove(c)
                self.impossible[i].add(c)

    select_word = select_word1
    update_stats = update_stats1

    def run(self):
        self.words = set(w.strip() for w in open("words.txt") if len(w) == 1 + self.length)
        target_word = random.choice(list(self.words))
        print("Guess:", target_word)
        while True:
            word = self.select_word()
            print("Trying", word)
            score = self.score(word, target_word)
            print("%s gives score %d" % (word, score))
            if score == self.length:
                break
            else:
                self.discard_word(word)
                self.update_stats(word, score)
                time.sleep(0.5)

        print("Complete: the word was %s" % target_word)

if __name__ == '__main__':
    Game(*sys.argv[1:]).run()
