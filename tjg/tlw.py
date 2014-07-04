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

    @staticmethod
    def score(w1, w2):
        return sum(1 for i1, i2 in zip(w1, w2) if i1 == i2)

    def words_from(self, filepath):
        print("Reading from", filepath)
        with open(filepath) as f:
            for word in re.findall(r"\b[A-Za-z]{%d}\b" % self.length, f.read()):
                yield word.lower()

    def read_usable_words(self):
        print("Loading usable_words")
        for source in glob.glob("corpus/*.txt"):
            self.usable_words.update(self.words_from(source))

    def select_word(self):
        return random.choice(list(self.usable_words))

    def update_stats(self, word, score):
        self.usable_words.remove(word)
        if score == 0:
            for usable_word in set(self.usable_words):
                if any(i1 == i2 for i1, i2 in zip(word, usable_word)):
                    self.usable_words.remove(usable_word)
                    self.unusable_words.add(usable_word)
        print("There are %d words left" % len(self.usable_words))

    def run(self):
        with open("words.txt") as f:
            self.usable_words = set(w.strip() for w in f if len(w) == 1 + self.length)
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
