folder = "dane/"
filename = "symbole.txt"

with open(folder + filename) as f:
	lines = [line.strip() for line in f.readlines()]

for line in lines:
	if line[0:6][::-1] == line[6:]:
		print(line)