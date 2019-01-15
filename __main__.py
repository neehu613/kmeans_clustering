'''
@Author : Shaheed Nehal A
Application of K-Means Clustering Algorithm to solve the following problem:
Given 100 random tshirt sizes, create 'k' clusters

Input : A dataset of 100 randomly generated datapoints
Output : 'k' number of datapoints representing the centroids of the clusters
'''

import random, math, os, utils, KMeansUtil
os.system('clear')

class kmeans:

	def kmeans():
		data = []				#Stores all the t-shirt sizes
		chest_sizes = []		#Stores the width of the t-shirt
		shirt_lengths = []		#Stores the length of the t-shirt
		oldCentroid = list()	#To store the previously calculated centroids
		centroid = list()		#To store the newly calculated centroids
		cluster = []			#To store the points in each cluster
		dist = []				#To store the distance from each centroid

		#Creating a utils object
		utilObj = utils.Utils()

		#Generating 100 random tuples and storing them in the list 'data'
		data = utilObj.genRandomDataset(chest_sizes, shirt_lengths, data)

		#Creating a Kmeans Utility Object and taking in the value of K
		kmeansObj = KMeansUtil.KMeansUtil()

		#Initializing the 3 clusters to empty list
		cluster, dist = kmeansObj.initialize(cluster,dist)		

		#Generating k random centroids	
		centroid, oldCentroid = kmeansObj.genRandomCentroids(centroid, oldCentroid)

		#Performing kmeans clustering till the oldcentroids = newcentroids
		NO_OF_ITERS = 0
		while 1:
			NO_OF_ITERS += 1

			#Calculate the distance of each point in the dataset from the centroids
			dist, cluster = kmeansObj.findClusters(dist, cluster, centroid, data)

			#Find the centroids based on mean
			centroid = kmeansObj.findCentroids(cluster, centroid)

			#If old and new centroids are the same, break out and stop.
			if(kmeansObj.checkEqualCentroids(centroid, oldCentroid)):
				continue
			else:
				break
			


		print ("Randomly generated 100 tshirt sizes\n")
		for size in data:
			print (size[0]/100, size[1]/100)

		for cluster in range(kmeansObj.k):
			print ("Cluster ", cluster+1, " = ", centroid[cluster][0]/100, centroid[cluster][1]/100)

		print ("Number of iterations to converge : ", NO_OF_ITERS)

if __name__ == '__main__':
	kmeans.kmeans()