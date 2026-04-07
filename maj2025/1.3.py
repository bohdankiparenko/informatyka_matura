n = 0
def przestaw2(n):
	w = 0
	mnozyc = 10
	while n > 0:
		if n < 10:
			w += n * (mnozyc / 10)
			return w
		koncowka = n % 100
		dziesiatka = koncowka // 10
		jednosc = koncowka % 10
		w += jednosc * mnozyc + dziesiatka * (mnozyc / 10)
		n = n // 100
		mnozyc *= 100
	return w

print(przestaw2(n))


