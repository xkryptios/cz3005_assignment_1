import json
import numpy

# Python program to print DFS traversal from a given
# given graph
from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation
class Graph:

	def __init__(self,vertices):

		# No. of vertices
		self.V = vertices
		self.path = []
		self.visited_nodes = []

		# default dictionary to store graph
		self.graph = numpy.zeros([vertices,vertices])

	# function to add an edge to graph
	def addEdge(self,u,v,value):
		self.graph[u][v] = value
	def addPath(self,node):
		self.path.append(node)
	def addDelete(self,node):
		self.path.append(node)
	# A function to perform a Depth-Limited search
	# from given source 'src'
	def DLS(self,src,target,maxDepth):

		if src == target : return True

		# If reached the maximum depth, stop recursing.
		if maxDepth <= 0 : return False

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[src]:
				if(self.DLS(i,target,maxDepth-1)):
					self.path.append(i)
					return True
		return False

	# IDDFS to search if target is reachable from v.
	# It uses recursive DLS()
	def IDDFS(self,src, target, maxDepth):

		# Repeatedly depth-limit search till the
		# maximum depth
		for i in range(maxDepth):
			if (self.DLS(src, target, i)):
				return True
		return False

# Create a graph given in the above diagram

target = 50; maxDepth = 3; src = 1

if g.IDDFS(src, target, maxDepth) == True:
	print ("Target is reachable from source " +
		"within max depth")
else :
	print ("Target is NOT reachable from source " +
		"within max depth")

if __name__ == "__main__":
    # NUMBER_OF_NODES = 264346
    matrix = numpy.zeros([264347, 264347])

    # coord = json.load(open("Coord.json"))
    # cost = json.load(open("Cost.json"))
    g = json.load(open("G.json"))
    dist = json.load(open("Dist.json"))
    
    for key, value in g.items():
        for node in value:
            u = int(key)
            v = int(str(node))
            matrix[u][v] = int(dist[key+","+str(node)])
    print(matrix)

