folder = "dane/"
filename = "dron_przyklad.txt"


with open(folder + filename) as f:
	lines = [tuple([int(l) for l in line.strip().split(" ")]) for line in f.readlines()]

i = 0
point = (0, 0)
points = []
while i < len(lines):
	point = point[0] + lines[i][0], point[1] + lines[i][1]
	points.append(point)
	i += 1

print(points)


