import math, random, json

class Utils:
	#Function to find the distance between 2 points (x, y) and (x_cent, y_cent)
	#(x, y) is a point in the dataset
	#(x_cent, y_cent) is the centroid
	def FindDistance(x_cent, y_cent, x, y):
		return int(math.sqrt((x-x_cent)*(x-x_cent) + (y-y_cent)*(y-y_cent)))


	#Generating 100 random tuples and storing them in the list 'data'
	#Normal chest size ranges from 4600mm(46cm) to 5100mm(51cm)
	#Normal shirt length ranges from 7200(72cm) to 7500(75cm)
	def GenRandomDataset(self, chest_sizes, shirt_lengths, data, constants):

		for tshirt in range(constants["samples"] + 1):
			chest_size = random.randrange(constants["chest_init"], constants["chest_fin"])
			chest_size = random.randrange(constants["chest_init"], constants["chest_fin"])
			shirt_length = random.randrange(constants["length_init"], constants["length_fin"])
			chest_sizes.append(chest_size)
			shirt_lengths.append(shirt_length)
			data.append((chest_size, shirt_length))

		return data

class KMeansUtil:

	#Constructor to initialize the value of K
	def __init__(self, k):
		self.k = k


	#A method to initialize all K clusters to empty lists
	def InitializeClusters(self, cluster, dist):
		
		[cluster.append([]) for i in range(self.k)]
		[dist.append(0) for i in range(self.k)]
		
		return cluster, dist


	#A method for generating K random centroids
	def GenRandomCentroids(self, centroid, OldCentroid, constants):
		for c in range(self.k):
			centroidx = random.randrange(constants["chest_init"], constants["chest_fin"])
			centroidy = random.randrange(constants["length_init"], constants["length_fin"])
			centroid.append((centroidx, centroidy))
			OldCentroid.append((centroidx, centroidy))
		return centroid, OldCentroid


	#A method to calculate the clusters
	def FindClusters(self,dist, cluster, centroid, data, constants):
		for Point in range(constants["samples"] + 1):
		
			#Calculate the distance of each point in the dataset from the centroids
			for cent in range(self.k):
				dist[cent] = Utils.FindDistance(centroid[cent][0], centroid[cent][1], data[Point][0], data[Point][1])

			CurrMin = constants["min"]
			CurrCluster = 0

			for i in range(self.k):
				if(dist[i] <= CurrMin):
					CurrMin = dist[i]
					CurrCluster = i

			cluster[CurrCluster].append(data[Point])

		return dist, cluster


	#A method to compute the new centroids
	def FindCentroids(self,cluster, centroid):
		for i in range(self.k):

			meanx = 0
			meany = 0

			if len(cluster[i]) != 0:
				for point in cluster[i]:
					meanx += point[0]
					meany += point[1]

				meanx /= len(cluster[i])
				meany /= len(cluster[i])
				centroid[i] = (int(meanx), int(meany))

		return centroid

	#A method to check if the new centroids are the same as the old ones
	def CheckEqualCentroids(self, centroid, OldCentroid):
		flag = 0

		for cent in range(len(centroid)):
			
			if OldCentroid[cent] != centroid[cent]:
				OldCentroid[cent] = centroid[cent]
				flag = 1
				return True

		if flag == 0:
			return False