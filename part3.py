
from dis import dis
import json
import math

# implementation of question 2 with Uniform cost search


class Graph:

    BUDGET_CONSTRAINT = 287932

    def __init__(self, graph, dist, cost, coord):
        # graph -> disctionary => graph["node"] = ["node1","node2"]
        self.graph = graph
        # dist -> dictionary => dist["node,node2"]
        self.dist = dist
        self.cost = cost
        self.coord = coord
        self.V = len(graph)

    def uniform_cost_search(self, start, goal):
        # start and goal are string of node index
        # assuming only 1 goal

        # initialisation
        start = str(start)
        goal = str(goal)
        xyCoord = self.coord[goal]
        xCoordGoal = xyCoord[0]
        yCoordGoal = xyCoord[1]
        #print('xcoordGoal' + str(xCoordGoal) + 'xcoordGoal' + str(yCoordGoal))
        parent = {}
        final_cost = 10**8
        visited = []

        pq = []
        # [heuristic(straight line distance to goal + cost to this node),
        # cost to this node, total budget to this node, node_index, parent_node]
        pq_node = [0, 0, 0, start, "-1"]

        pq.append(pq_node)

        while (len(pq) > 0):  # while pq is not empty
            pq.sort()
            current_pq_node = pq.pop(0)

            cost_to_this_node = current_pq_node[1]
            total_budget_to_this_node = current_pq_node[2]
            node_index = current_pq_node[3]
            parent_node_index = current_pq_node[4]

            if (node_index == goal):
                final_cost = cost_to_this_node
                parent[node_index] = parent_node_index
                self.get_path(parent, start, goal)
                print("\ncost to travel =", final_cost)
                return
            elif (node_index not in visited):
                visited.append(node_index)
                parent[node_index] = parent_node_index

                for child in self.graph[node_index]:
                    string_param = node_index+','+child

                    total_budget_to_child = self.cost[string_param] + \
                        total_budget_to_this_node

                    if total_budget_to_child > self.BUDGET_CONSTRAINT:  # if budget too high, do not add this node to the pq
                        continue

                    cost_to_child = self.dist[string_param] + cost_to_this_node

                    # calculate heuristic
                    xCoord = self.coord[child][0]
                    yCoord = self.coord[child][1]

                    straightlineDist = math.hypot(
                        xCoord - xCoordGoal, yCoord - yCoordGoal)
                    heuristic = cost_to_child + straightlineDist

                    pq_node = [heuristic, cost_to_child,
                               total_budget_to_child, child, node_index]
                    pq.append(pq_node)

    def get_path(self, parent, start, goal):
        # assuming start , goal are strings
        # parent is a dictionary
        temp = goal
        print(goal, "<-", end="")
        while parent[temp] != start:
            print(parent[temp], "<-", end="")
            temp = parent[temp]
        print(start, end="")


if __name__ == "__main__":
    g = json.load(open("G.json"))
    dist = json.load(open("Dist.json"))
    cost = json.load(open("Cost.json"))
    coord = json.load(open("Coord.json"))
    # combined_cost = {}
    # print(len(dist),len(cost))
    # for key in dist:
    #     combined_cost[key] = dist[key] + cost[key]

    graph = Graph(g, dist, cost, coord)
    graph.uniform_cost_search(1, 50)
