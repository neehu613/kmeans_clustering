import matplotlib.pyplot as plt
import random
import json

class PlotClusters:

	def __init__(self, data, clusters, centroids):
		self.data = data
		self.centroids = centroids
		self.clusters = clusters
		self.x_coords = [[0] for i in range(len(centroids))]
		self.y_coords = [[0] for i in range(len(centroids))]
		self.x_coords_centroids = []
		self.y_coords_centroids = []
		
	def ExtractCoords(self):
		constants = {}
		with open("constants.json") as f:
			constants = json.load(f)
		for i in range(len(self.clusters)):
			for j in range(len(self.clusters[i])):
				self.x_coords[i].append(self.clusters[i][j][0]/constants["samples"])
				self.y_coords[i].append(self.clusters[i][j][1]/constants["samples"])
			self.x_coords_centroids.append(self.centroids[i][0]/constants["samples"])
			self.y_coords_centroids.append(self.centroids[i][1]/constants["samples"])
			


	def plot(self):
		for i in range(len(self.centroids)):
			rand_r = random.uniform(0,1)
			rand_g = random.uniform(0,1)
			rand_b = random.uniform(0,1)
			plt.scatter(self.x_coords[i][1:], self.y_coords[i][1:], marker=".", color=(rand_r, rand_g, rand_b))
			plt.scatter(self.x_coords_centroids[i], self.y_coords_centroids[i], marker="*", color='k')
		plt.show()