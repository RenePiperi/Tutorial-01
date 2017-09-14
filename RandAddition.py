import random
count_var = 0
result = 0

while count_var < 10:
	result += random.randint(1,10)
	count_var += 2

print("Adding 5 random integers ranging 1-10", result)
