import math, random

class Utils:
	#Function to find the distance between 2 points (x, y) and (x_cent, y_cent)
	#(x, y) is a point in the dataset
	#(x_cent, y_cent) is the centroid
	def findDistance(x_cent, y_cent, x, y):
		return int(math.sqrt((x-x_cent)*(x-x_cent) + (y-y_cent)*(y-y_cent)))


	#Generating 100 random tuples and storing them in the list 'data'
	#Normal chest size ranges from 4600mm(46cm) to 5100mm(51cm)
	#Normal shirt length ranges from 7200(72cm) to 7500(75cm)
	def genRandomDataset(self, chest_sizes, shirt_lengths, data):
		for tshirt in range(101):
			chest_size = random.randrange(4600, 5100)
			chest_size = random.randrange(4600, 5100)
			shirt_length = random.randrange(7200, 7500)
			chest_sizes.append(chest_size)
			shirt_lengths.append(shirt_length)
			data.append((chest_size, shirt_length))

		return data