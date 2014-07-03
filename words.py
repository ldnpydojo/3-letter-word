import random

def comparison(enter_word, selected_word):
    score = 0
    for x in range(len(enter_word)):
        if enter_word[x] == selected_word[x]:
            score += 1
    return score

"""
with open("CSW07.txt") as f:
	data = f.read().split('\n')
	for line in data:
		word_end = line.find(' ')
		if word_end == -1:
			continue
		word = line[:word_end]
		definition = line[word_end:]

		if len(word) == 3:
			print "%s,%s" % (word, definition)
"""

def ask_user(picked_word):
  guess = raw_input("> ")

  if guess == "LOSER":
    print "The picked word was %s" % picked_word
    return True

  if len(guess) != 3:
    print "You need to enter a 3 letters word"
    return False

  score = comparison(guess, picked_word)
  if score < 3:
    print "You've got a score of %d" % score
    return False

  print "You win !"
  return True



if __name__ == '__main__':

   with open("words.txt") as f:
       data = f.read().split('\n')
       selected_word = random.choice(data)
       word_end = selected_word.find(',')
       word = selected_word[:word_end]
       definition =  selected_word[word_end:]
       print "Type LOSER if you want to give up"
       print word, definition

       tries = 0
       while True:
        won = ask_user(word)
        if won:
          print "Game over"
          break

        tries += 1
        if tries > 10:
          print "A little help..."
          print "The word means: %s" % definition

