folder = "dane/"
filename = "symbole.txt"

with open(folder + filename) as f:
	lines = [line.strip() for line in f.readlines()]

def to_ternary_system(text):
	keys = ["o", "+", "*"]
	values = ["0", "1", "2"]
	for k, v in zip(keys, values):
		text = text.replace(k, v)
	number = int(text)
	return number

def to_decimal_system(expression):
	new_expression = 0
	for i, n in enumerate(str(expression)[::-1]):
		n = int(n)
		new_expression += 3 ** i * n
	return new_expression

expression = 0
text = ""
for i, line in enumerate(lines):
	trit = to_ternary_system(line)
	lines[i] = to_decimal_system(trit)


suma = sum(lines)
reszta = ""
while suma > 0:
	reszta += str(suma % 3)
	suma = suma // 3

reszta = reszta[::-1]
keys = ["o", "+", "*"]
values = ["0", "1", "2"]
for k, v in zip(keys, values):
	reszta = reszta.replace(v, k)
print(sum(lines), reszta)








