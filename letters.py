
with open("CSW07.txt") as f:
	data = f.read().split('\n')
	for line in data:
		parts = line.split(' ')
		if len(parts[0]) == 3:
			print parts[0]
