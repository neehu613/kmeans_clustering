import math, utils, random

class KMeansUtil:

	#Constructor to initialize the value of K
	def __init__(self):
		self.k = int(input("Enter the number of clusters: "))


	#A method to initialize all K clusters to empty lists
	def initialize(self, cluster, dist):
		for i in range(self.k):
			clusterList = []
			cluster.append(clusterList)
			dist.append(0)

		return cluster, dist


	#A method for generating K random centroids
	def genRandomCentroids(self, centroid, oldCentroid):
		for c in range(self.k):
			centroidx = random.randrange(4600, 5100)
			centroidy = random.randrange(7200, 7500)
			centroid.append((centroidx, centroidy))
			oldCentroid.append((centroidx, centroidy))
		return centroid, oldCentroid


	#A method to calculate the clusters
	def findClusters(self,dist, cluster, centroid, data):
		for Point in range(101):
		
			#Calculate the distance of each point in the dataset from the centroids
			for cent in range(self.k):
				dist[cent] = utils.Utils.findDistance(centroid[cent][0], centroid[cent][1], data[Point][0], data[Point][1])

			currMin = 1000000
			currCluster = 0

			for i in range(self.k):
				if(dist[i] <= currMin):
					currMin = dist[i]
					currCluster = i

			cluster[currCluster].append(data[Point])

		return dist, cluster


	#A method to compute the new centroids
	def findCentroids(self,cluster, centroid):
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
	def checkEqualCentroids(self, centroid, oldCentroid):
		flag = 0

		for cent in range(len(centroid)):
			
			if oldCentroid[cent] != centroid[cent]:
				oldCentroid[cent] = centroid[cent]
				flag = 1
				return True

		if flag == 0:
			return False