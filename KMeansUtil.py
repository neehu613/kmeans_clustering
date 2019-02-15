import math, utils, random, json

class kmeans:

	def __init__(self):
		#Stores all the t-shirt sizes
		self.data = []				

		#Stores the width of the t-shirt
		self.chest_sizes = []		

		#Stores the length of the t-shirt
		self.shirt_lengths = []		
		
		#To store the previously calculated centroids
		self.OldCentroid = list()	
		
		#To store the newly calculated centroids
		self.centroid = list()		
		
		#To store the points in each cluster
		self.cluster = []			

		#To store the distance from each centroid
		self.dist = []

		#To store all constants of json file
		self.constants = {}

		with open("constants.json") as f:
			self.constants = json.load(f)
		
		
	def PerformKMeans(self):
		#Creating a utils object
		UtilObj = utils.Utils()
		
		#Generating 100 random tuples and storing them in the list 'data'
		data = UtilObj.GenRandomDataset(self.chest_sizes, self.shirt_lengths, self.data, self.constants)

		#Creating a Kmeans Utility Object and taking in the value of K
		k = int(input("Enter the number of clusters: "))
		KMeansObj = utils.KMeansUtil(k)

		#Initializing the 3 clusters to empty list
		self.cluster, self.dist = KMeansObj.InitializeClusters(self.cluster,self.dist)		

		#Generating k random centroids	
		self.centroid, self.OldCentroid = KMeansObj.GenRandomCentroids(self.centroid, self.OldCentroid, self.constants)

		#Performing kmeans clustering till the OldCentroids = newcentroids
		#NO_OF_ITERS = 0
		NO_OF_ITERS = 0
		while 1:
			NO_OF_ITERS += 1

			#Calculate the distance of each point in the dataset from the centroids
			self.dist, self.cluster = KMeansObj.FindClusters(self.dist, self.cluster, self.centroid, self.data, self.constants)

			#Find the centroids based on mean
			self.centroid = KMeansObj.FindCentroids(self.cluster, self.centroid)

			#If old and new centroids are the same, break out and stop.
			if(KMeansObj.CheckEqualCentroids(self.centroid, self.OldCentroid)):
				continue
			else:
				break
		

		print ("Randomly generated 100 tshirt sizes\n")
		for size in self.data:
			print (size[0]/self.constants["samples"], size[1]/self.constants["samples"])

		for cluster in range(KMeansObj.k):
			print ("Cluster ", cluster+1, " = ", self.centroid[cluster][0]/self.constants["samples"], self.centroid[cluster][1]/self.constants["samples"])

		print ("Number of iterations to converge : ", NO_OF_ITERS)

		return self.data, self.cluster, self.centroid
