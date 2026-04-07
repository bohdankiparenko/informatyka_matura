folder = "dane/"
filename = "symbole.txt"

with open(folder + filename) as f:
	lines = [line.strip() for line in f.readlines()]

def find_middle_sign(line):
	temp = []
	for index, sign in enumerate(line):
		if index == 0:
			continue
		elif index == 11:
			break
		if line[index - 1] == sign == line[index + 1]:
			temp.append((index, sign))
	return temp

counter = 0
result = []
for index, line in enumerate(lines):
	if index == 1998:
		break
	temp = find_middle_sign(line)
	if temp:
		for t in temp:
			first = line[t[0]-1] + lines[index + 1][t[0]-1] + lines[index + 2][t[0]-1]
			second = line[t[0]] + lines[index + 1][t[0]] + lines[index + 2][t[0]]
			third = line[t[0]+1] + lines[index + 1][t[0]+1] + lines[index + 2][t[0]+1]
			if first[0] == second[0] == third[0] == first[1] == second[1] == third[1] == first[2] == second[2] == third[2]:
				counter += 1
				result.append(f"{str(index + 2)} {str(t[0] + 1)}")
print(counter, result)



