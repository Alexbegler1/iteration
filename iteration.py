# Make a local change
# Make another local change
# Make a change from home

# iteration pattern
# doing the same thing once for each item in the list

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def add_one(list):
	for i in range(0, len(list)):
		list[i] += 1

	print list

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
# exclude a calculation from list members
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"

# accumulation patter- a type of iteration
# keep track of other data as we go

def sum(numbers):
	total = 0
	for n in numbers:
		total += n

	return total

def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max

def average(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n
	average = sum / len(numbers)
	return average
	
def smallest_n(numbers):
	current_min1 = numbers[0]
	for n in numbers:
		if n > current_min1:
			current_min1 = n
	numbers.remove(current_min1)

	current_min2 = numbers[0]
	for n in numbers:
		if n > current_min2:
			current_min2 = n
	numbers.remove(current_min2)

def average_minus2(numbers):
	smallest_n(numbers)
	print average(numbers)

# function that finds average
# function that finds average but drops the lowest 2 scores