"""
	Projet Euler # 10
	Author:		David Warren II
	Date: 		4 May, 2017
	Objective:	Find the largest product of 4 adjacent numbers
"""

def log(message): # error reporter
	print(message)

"""
The explanation of the calculations function will be in the read me.
"""
def calculations(data):
	# direction1 = 1 => up otherwise => down
	# direction2 = 1 => right otherwise => left
	def vertical(x, y, data, direction1):
		if (direction1): # goes up
			return data[x][y] * data[x][y - 1] + data[x][y - 2] + data[x][y - 3]
		else: # goes down
			return data[x][y] * data[x][y + 1] + data[x][y + 2] + data[x][y + 3]

	def horizontal(x, y, data, direction2):
		if (direction2): # goes right
			return data[x][y] * data[x + 1][y] * data[x + 2][y] * data[x + 3][y]
		else: # goes left
			return data[x][y] * data[x - 1][y] * data[x - 2][y] * data[x - 3][y]

	def diagonal(x, y, data, direction1, direction2):
		if (direction1 and direction2): # up and right
			return data[x][y] * data[x + 1][y - 1] * data[x + 2][y - 2] * data[x + 3][y - 3]
		elif (direction1 and not direction2): # up and left
			return data[x][y] * data[x - 1][y - 1] * data[x - 2][y - 2] * data[x - 3][y - 3]
		elif (not direction1 and direction2): # down and right
			return data[x][y] * data[x + 1][y + 1] * data[x + 2][y + 2] * data[x + 3][y + 3]
		elif (not direction1 and not direction2): # down and left
			return data[x][y] * data[x - 1][y + 1] * data[x - 2][y + 2] * data[x - 3][y + 3]

	def check(a, b):
		if (a > b):
			return a
		else:
			return b

	biggest_product = 0
	for r in range(len(data) - 2):
		for c in range(len(data[r]) - 2):
			if (r < 17): # only have to do right
				biggest_product = check(biggest_product, horizontal(r, c, data, 1))
				if (c > 2 and c < 17): 
					biggest_product = check(biggest_product, diagonal(r, c, data, 1, 1))
					biggest_product = check(biggest_product, diagonal(r, c, data, 0, 1))
				elif(c < 2):
					biggest_product = check(biggest_product, diagonal(r, c, data, 0, 1))
				elif(c > 17):
					biggest_product = check(biggest_product, diagonal(r, c, data, 1, 1))

			else: # have to do left
				biggest_product = check(biggest_product, horizontal(r + 2, c, data, 0))
				if (c > 2 and c < 17): # both directions are fine
					biggest_product = check(biggest_product, diagonal(r + 2, c, data, 1, 0)) 
					biggest_product = check(biggest_product, diagonal(r + 2, c, data, 0, 0))
				elif(c < 2): # can only go down
					biggest_product = check(biggest_product, diagonal(r + 2, c, data, 0, 0))
				elif(c > 17): # can only go up
					biggest_product = check(biggest_product, diagonal(r + 2, c, data, 1, 0))

	print("The biggest product was: %d" % biggest_product)

def myParser(data):
	fixed_data = []

	for x in range(len(data)):
		fixed_data.append(data[x].split()) # separate all the numbers

	for x in range(len(fixed_data)):
		for y in range(len(fixed_data[x])):
			fixed_data[x][y] = int(fixed_data[x][y])

	return fixed_data

def input_data(file): # this gets all the data and puts in a list
	data = [] 
	while True:
		line = file.readline()
		if not line:
			break
		data.append(line)
	return myParser(data)

def main(file):
	data = input_data(file)
	calculations(data)

if __name__ == '__main__':
	filename = 'numbers'
	test = 0 # just to make sure it opened correctly
	try:
		file = open(filename, 'r')
		test = 1
	except:
		log("Trouble opening file.")

	if (test):
		main(file)