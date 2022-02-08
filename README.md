# cz3005_assignment_1
Find a shortest path with an energy budget between two locations.

We are given a problem of finding a shortest traverse path between two locations within a certain
energy budget. This scenario often happens in the transportation where a shorter path is not
necessarily more energy efficient (e.g., the road may be very bumpy or has heavy traffic). We illustrate
our problem with the following example:

*picture*

Suppose we are given a graph with a predefined source node (𝑆) and a target node (𝑇). Each edge in
the graph is associated with a pair of values (𝑋, 𝑌) where 𝑋 denotes the distance and 𝑌 denotes the
energy cost. Also see Figure 1 for an illustration. The job is to find the shortest path between 𝑆 and 𝑇
such that the accumulated energy cost along the path does not exceed an energy budget. Specifically,
we want to find the shortest path from Jurong East to Changi Airport not exceeding an energy budget
11. We can observe that although the path S->2->T has the shortest travel distance 10, its accumulated
energy cost 12 exceeds the energy budget 11. Thus, this path is infeasible. In this example, the path
S->1->T is the shortest feasible path.

# 1.1 Problem instance
You will be given a problem instance of New York city (NYC) road network of the United State. This
instance is taken and modified from the 9th DIMACS implementation challenge. This instance has
264346 nodes and 730100 edges. You will be given four python dictionary files:
1.1.1 Graph dictionary G
The graph is given as an adjacency list where the neighbor list of node ‘v’ can be accessed with G[‘v’].
1.1.2 Node coordination dictionary Coord
The coordination of a node ‘v’ is a pair (X, Y) which can be accessed with Coord[‘v’]
1.1.3 Edge distance dictionary Dist
The distance between a pair of node (v, w) can be accessed with Dist[‘v,w’].
1.1.4 Edge cost dictionary Cost
The energy cost between a pair of node (v, w) can be accessed with Cost[‘v,w’.]


# 2.1 Tasks and marking criteria
You will need to solve three tasks that are listed as follow:\n
Task 1: You will need to solve a relaxed version of the NYC instance where we do not have the energy
constraint. You can use any algorithm we discussed in the lectures. Note that this is equivalent to
solving the shortest path problem.
(30 marks)\n
Task 2: You will need to implement an uninformed search algorithm (e.g., the DFS, BFS, UCS) to solve
the NYC instance.
(30 marks)\n
Task 3: You will need to develop an A* search algorithm to solve the NYC instance. The key is to
develop a suitable heuristic function for the A* search algorithm in this setting.
(40 marks)
For tasks 2 and 3, the energy budget is set to be 287932. For all the 3 tasks, the starting and ending
nodes are set to be ‘1’ and ‘50’, respectively.
(Please note that the NYC instance is provided separately as formatted in section 1.1)

# 2.2 Output format
The output of your algorithm should be formatted as the following (using Figure 1 as an example):
Shortest path: S->1->T.
Shortest distance: 12.
Total energy cost: 10.
