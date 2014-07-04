from random import choice
from time import sleep

from game import build_dictionary, Game, WinEvent


def cull_word_list(word_list, ex_f, ex_s, ex_t):
  candidates = []
  for word in word_list:
    f, s, t = word
    if not f in ex_f and not s in ex_s and not t in ex_t:
      candidates.append(word)
  return candidates


def select_candidate_words(word_list, last_word, score, ex_f, ex_s, ex_t):
  if score == 0:
    return word_list
  candidates = []
  for word in word_list:
    f, s, t = word
    if f in ex_f or s in ex_s or t in ex_t:
      continue
    if score == 1:
      if (f in last_word or s in last_word or t in last_word):
        candidates.append(word)
    elif score == 2:
      if (f in last_word and (s in last_word or t in last_word)) or ((f in last_word or s in last_word) and t in last_word):
        candidates.append(word)
  return candidates


def guess(word_list, guess_function, sleep_time):
  score = 0
  first_letters, second_letters, third_letters = set(), set(), set()
  word = None
  try:
    print "Making initial guesses"
    while score == 0:
      if word:
        print "Forbidding all the letters in", word
        f, s, t = word
        first_letters.add(f)
        second_letters.add(s)
        third_letters.add(t)
        word_list = cull_word_list(word_list, first_letters, second_letters, third_letters)
        print len(word_list), "words remaining"
        print
        sleep(sleep_time)
      word = choice(word_list)
      print "Guessing", word
      score = guess_function(word)
      print "It has", score, "correct letters"
    print "Progessing to second stage"
    #import pdb; pdb.set_trace()
    while word_list:
      print "Selecting possible words"
      word_list = select_candidate_words(word_list, word, score, first_letters, second_letters, third_letters)
      try:
        new_word = choice(word_list)
        print len(word_list), "words remaining"
        print
        sleep(sleep_time)
        print "Guessing", new_word
        new_score = guess_function(new_word)
        word_list.remove(new_word)
        print "It has", new_score, "correct letters"
        if new_score >= score:
          print "This word is better, this is now the basis word"
          word = new_word
          score = new_score
        else:
          print "This word is worse, discard"
      except WinEvent, e:
        print e
        return True
  except WinEvent:
    return True
  return False


if __name__ == '__main__':
  game = Game()
  words = build_wordlist()
  guess(words, game.guess, sleep_time=0.3)
