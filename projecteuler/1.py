
number = raw_input('Insert number: ')
summ = 0

for n in range(int(number)):
	print n
	if n % 3 == 0 or n % 5 == 0: # if there will be more than 2 "or"
		summ = summ + n

print summ


