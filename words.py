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

if __name__ == '__main__':
    

   with open("words.txt") as f:
       data = f.read().split('\n')
       selected_word = random.choice(data)
       word_end = selected_word.find(',')
       word = selected_word[:word_end]
       definition =  selected_word[word_end:]

