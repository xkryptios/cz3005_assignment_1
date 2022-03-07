
from dis import dis
import json
import math
from collections import deque

from sklearn.metrics import euclidean_distances

# implementation of question 2 with Uniform cost search


class Graph:

    BUDGET_CONSTRAINT = 287932
    BUDGET_MULTIPLIER = 0.5
    EUCLIDEAN_DISTANCE_MULTIPLIER = 0.5

    def __init__(self, graph, dist, cost, cord):
        # graph -> disctionary => graph["node"] = ["node1","node2"]
        self.graph = graph
        # dist -> dictionary => dist["node,node2"]
        self.dist = dist
        self.cost = cost
        self.cord = cord
        self.V = len(graph)

    def uniform_cost_search(self, start, goal):
        # start and goal are string of node index
        # assuming only 1 goal

        total_expanded_nodes_counter = 0

        # initialisation
        start = str(start)
        goal = str(goal)
        parent = {}
        final_cost = 10**8
        visited = []

        pq = []
        # [heuristic(straight line + cost), cost to this node, total budget to this node, node_index, parent_node, heuristic]
        pq_node = [self.h(0, start) + 0, 0, 0, start, "-1"]

        pq.append(pq_node)

        while (len(pq) > 0):  # while pq is not empty
            pq.sort()
            current_pq_node = pq.pop(0)

            # heuristic_cost = current_pq_node[0] # do not need to use this value
            cost_to_this_node = current_pq_node[1]
            total_budget_to_this_node = current_pq_node[2]
            node_index = current_pq_node[3]
            parent_node_index = current_pq_node[4]
            # dist_from_goal = current_pq_node[5]

            if (node_index == goal):
                final_cost = cost_to_this_node
                parent[node_index] = parent_node_index
                self.get_path(parent, start, goal)
                print("\nShortest distance: ", final_cost)
                print("\nTotal energy cost: ", total_budget_to_this_node)
                print("\nTotal Number of expanded nodes: ",
                      total_expanded_nodes_counter)
                return
            elif (node_index not in visited):
                total_expanded_nodes_counter += 1

                visited.append(node_index)
                parent[node_index] = parent_node_index

                for child in self.graph[node_index]:
                    string_param = node_index+','+child

                    budget_to_child = self.cost[string_param]

                    total_budget_to_child = budget_to_child + total_budget_to_this_node

                    if total_budget_to_child > self.BUDGET_CONSTRAINT:  # if budget too high, do not add this node to the pq
                        continue

                    cost_to_child = self.dist[string_param] + cost_to_this_node
                    heuristic = self.h(budget_to_child, child)
                    heuristic_cost = heuristic + cost_to_child

                    pq_node = [heuristic_cost, cost_to_child,
                               total_budget_to_child, child, node_index]
                    pq.append(pq_node)

    def get_path(self, parent, start, goal):
        # assuming start , goal are strings
        # parent is a dictionary
        # temp = goal
        # count = 1
        # print(goal, "<-", end="")
        # while parent[temp] != start:
        #     count = count+1
        #     print(parent[temp], "<-", end="")
        #     temp = parent[temp]
        # print(start, end="")
        # print("length = ", count+1)
        stack = deque()
        size = 0
        temp = goal
        while parent[temp] != start:
            stack.append(parent[temp])
            temp = parent[temp]
            size += 1
        print('Shortest path:')
        print(start, "->", end="")
        while(size > 0):
            temp = stack.pop()
            print(int(temp), "->", end="")
            size -= 1
        print(goal)

    def h(self, budget_to_child, n):
        val = math.sqrt((cord["50"][0] - cord[str(n)][0])
                        ** 2 + (cord["50"][1] - cord[str(n)][1])**2)
        h = int(val
                )
        # print(h)
        return h
        # return val


if __name__ == "__main__":
    g = json.load(open("G.json"))
    dist = json.load(open("Dist.json"))
    cost = json.load(open("Cost.json"))
    cord = json.load(open("Coord.json"))
    #combined_cost = {}
    #print(len(dist), len(cost))
    # for key in dist:
    #    combined_cost[key] = dist[key] + cost[key]

    graph = Graph(g, dist, cost, cord)
    graph.uniform_cost_search(1, 50)
