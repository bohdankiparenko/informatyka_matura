folder = "dane/"
filename = "dron.txt"


with open(folder + filename) as f:
	lines = [tuple([int(l) for l in line.strip().split(" ")]) for line in f.readlines()]

point = (0, 0)
points = []
for disloc in lines:
	point = point[0] + disloc[0], point[1] + disloc[1]
	points.append(point)

i = 0


kopia_points = points[:] # Tworzy kopię listy krotek points
while i < len(points) - 1:
	first = points.pop(i)
	for third in points:
		second = (first[0] + third[0]) / 2, (first[1] + third [1]) / 2
		if second in kopia_points:
			print(first, second, third)

