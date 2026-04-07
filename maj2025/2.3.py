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

expression = 0
text = ""
for line in lines:
	trit = to_ternary_system(line)
	if trit > expression:
		expression = trit
		text = line

new_expression = 0
for i, n in enumerate(str(expression)[::-1]):
	n = int(n)
	new_expression += 3 ** i * n

print(new_expression, text)






