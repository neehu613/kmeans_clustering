'''
@Author : Shaheed Nehal A
Application of K-Means Clustering Algorithm to solve the following problem:
Given 100 random tshirt sizes, create 'k' clusters

Input : A dataset of 100 randomly generated datapoints
Output : 'k' number of datapoints representing the centroids of the clusters
'''

import random, math, os, utils, KMeansUtil, argparse, PlotClusters
os.system('clear')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--plot", help="Gives a plot of the clusters", action="store_true", default=False)
	args = parser.parse_args()
	k = KMeansUtil.kmeans()
	data, clusters, centroids = k.PerformKMeans()

	if args.plot == True:
		plot = PlotClusters.PlotClusters(data, clusters, centroids)
		plot.ExtractCoords()
		plot.plot()
		