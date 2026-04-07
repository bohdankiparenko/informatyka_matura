def fibonacci(n):
	if n <= 1:
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)


fib = []

for f in range(15):
	fib.append(fibonacci(f))
print(fib)
