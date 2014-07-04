#!python3
import os, sys
import glob
import re

def words_from(filepath):
    print("Reading from", filepath)
    with open(filepath) as f:
        for word in re.findall(r"\b[A-Za-z]{3,}\b", f.read()):
            yield word.lower()

def read_usable_words():
    print("Loading usable_words")
    usable_words = set()
    for source in glob.glob("corpus/*.txt"):
        usable_words.update(words_from(source))
    return usable_words

def main():
    words = set()
    with open("words.txt", "w") as f:
        f.writelines("%s\n" % w for w in read_usable_words())

if __name__ == '__main__':
    main(*sys.argv[1:])
