def if_prime(number):
	for j in range(2, int(1 + number ** 0.5)):
		if number % j == 0:
			return False
	return True

for i in range(1, 200000):
	if if_prime(i + 1):
			print(i + 1, end=" ")
print()


