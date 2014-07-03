
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
