folder = "dane/"
filename = "dron.txt"


with open(folder + filename) as f:
	lines = [tuple([int(l) for l in line.strip().split(" ")]) for line in f.readlines()]

i = 0
point = (0, 0)
points = []
while i < len(lines):
	point = point[0] + lines[i][0], point[1] + lines[i][1]
	points.append(point)
	i += 1

counter = 0
for point in points:
	x_disloc = 0 < point[0] < 5000
	y_disloc = 0 < point[1] < 5000
	if x_disloc and y_disloc:
		counter += 1

print(counter)



