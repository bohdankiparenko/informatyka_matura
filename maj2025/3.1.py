folder = "dane/"
filename = "dron.txt"


with open(folder + filename) as f:
	lines = [tuple([int(l) for l in line.strip().split(" ")]) for line in f.readlines()]

a = 18
b = 0

def nwd(a, b):
	if b == 0:
		return a
	else:
		while b > 0:
			r = a % b
			a = b
			b = r
		return a

counter = 0
for line in lines:
	a, b = line
	if nwd(abs(a), abs(b)) > 1:
		counter += 1
print(counter)