'''
@Author : Shaheed Nehal A
Application of K-Means Clustering Algorithm to solve the following problem:
Given 100 random tshirt shirts, create 'k' clusters

Input : A dataset of 100 randomly generated datapoints
Output : 'k' number of datapoints representing the centroids of the clusters

'''

import random, math, time, numpy, os
os.system('clear')

'''
Function to find the distance between 2 points (x, y) and (x_cent, y_cent)
(x, y) is a point in the dataset
(x_cent, y_cent) is the centroid
'''
def findDistance(x_cent, y_cent, x, y):
	return int(math.sqrt((x-x_cent)*(x-x_cent) + (y-y_cent)*(y-y_cent)))



'''
Function to reset the cluster list after every iteration
At each iteration , a new cluster is formed. This function initializes
the clusters to be empty
'''
def initializeClusters(k, clusterList, cluster, dist):
	for i in range(k):
		clusterList = []
		cluster.append(clusterList)
		dist.append(0)

	return clusterList, cluster, dist



'''
Function to find the new mean for the newly created cluster
At each iteration a new cluster is created. This function finds the mean
of the newly formed cluster of datapoints
'''
def findNewMeans(cluster, centroid, k):
	for i in range(k):

		meanx = 0
		meany = 0

		if len(cluster[i]) != 0:
			for point in cluster[i]:
				meanx += point[0]
				meany += point[1]

			meanx /= len(cluster[i])
			meany /= len(cluster[i])
			centroid[i] = (int(meanx), int(meany))

	return cluster, centroid



'''
We perform K-Means Clustering on 100 randomly generated tshirt sizes.
This function generates 100 random tshirt sizes and creates a dataset called 'data'
'''
def generate():

	data = []				#Stores all the t-shirt sizes
	chest_sizes = []		#Stores the width of the t-shirt
	shirt_lengths = []		#Stores the length of the t-shirt
	
	for tshirt in range(101):
		#Normal chest size ranges from 4600mm(46cm) to 5100mm(51cm)
		chest_size = random.randrange(4600, 5100)

		#Normal shirt length ranges from 7200(72cm) to 7500(75cm)
		chest_size = random.randrange(4600, 5100)
		shirt_length = random.randrange(7200, 7500)
		chest_sizes.append(chest_size)
		shirt_lengths.append(shirt_length)
		data.append((chest_size, shirt_length))

	return data



'''
Function to generate 'k' random centroids. This is done at the beginning of
kmeans clustering
'''
def generateRandomCentroids(k):
	#To store the previously calculated centroids
	oldCentroid = list()

	#To store the newly calculated centroids
	centroid = list()

	#Generating k random centroids
	for c in range(k):
		centroidx = random.randrange(4600, 5100)
		centroidy = random.randrange(7200, 7500)
		centroid.append((centroidx, centroidy))
		oldCentroid.append((centroidx, centroidy))

	return centroid, oldCentroid


'''
Function to perform kmeans clustering on the 100 randomly generated tshirt sizes
This function takes in the value of 'k' (no. of clusters required) and 
gives the centroids of the final 'k' clusters
'''
def kmeans():
	#We try to cluster the tshirt sizes into 3 clusters(k=3) - Small(S), Medium(M) and Large(L)
	k = int(input("Enter the number of clusters: "))

	#To store the points in each cluster
	cluster = []

	#To store the distance from each centroid
	dist = []

	centroid, oldCentroid = generateRandomCentroids(k)

	#Generate random datapoints
	data = generate()

	#Performing kmeans clustering till the oldcentroids = newcentroids
	NO_OF_ITERS = 0
	while 1:
		NO_OF_ITERS += 1
		for Point in range(101):

			#Initializing the 3 clusters to empty list
			clusterList = []
			clusterList, cluster, dist = initializeClusters(k, clusterList, cluster, dist)
			
			
			#Calculate the distance of each point in the dataset from the centroids
			for cent in range(k):
				dist[cent] = findDistance(centroid[cent][0], centroid[cent][1], data[Point][0], data[Point][1])

			currMin = 1000000
			currCluster = 0

			#Finding the smallest distance and assigning the datapoint to the nearest cluster
			for i in range(k):
				if(dist[i] <= currMin):
					currMin = dist[i]
					currCluster = i

			cluster[currCluster].append(data[Point])

		#Calculating the new means for the new clusters formed.
		cluster, centroid = findNewMeans(cluster, centroid, k)
		
		flag = 0

		for cent in range(len(centroid)):
			
			if oldCentroid[cent] != centroid[cent]:
				oldCentroid[cent] = centroid[cent]
				flag = 1
				continue

		if flag == 0:
			break


	print ("Randomly generated 100 tshirt sizes\n")
	for size in data:
		print (size[0]/100, size[1]/100)

	for cluster in range(k):
		print ("Cluster ", cluster+1, " = ", centroid[cluster][0]/100, centroid[cluster][1]/100)

	print ("Number of iterations to converge : ", NO_OF_ITERS)


#########################################################################
#							MAIN PROGRAM								#
#########################################################################
kmeans()
