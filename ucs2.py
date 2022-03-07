
from dis import dis
import json
from collections import deque

# implementation of question 2 with Uniform cost search


class Graph:

    BUDGET_CONSTRAINT = 287932

    def __init__(self, graph, dist, cost):
        # graph -> disctionary => graph["node"] = ["node1","node2"]
        self.graph = graph
        # dist -> dictionary => dist["node,node2"]
        self.dist = dist
        self.cost = cost
        self.V = len(graph)

    def uniform_cost_search(self, start, goal):
        # start and goal are string of node index
        # assuming only 1 goal

        total_nodes_expanded_counter = 0

        # initialisation
        start = str(start)
        goal = str(goal)
        parent = {}
        final_cost = 10**8
        visited = []

        pq = []
        # [cost to this node,total budget to this node, node_index, parent_node]
        pq_node = [0, 0, start, "-1"]

        pq.append(pq_node)

        while (len(pq) > 0):  # while pq is not empty
            pq.sort()
            current_pq_node = pq.pop(0)
            cost_to_this_node = current_pq_node[0]
            total_budget_to_this_node = current_pq_node[1]
            node_index = current_pq_node[2]
            parent_node_index = current_pq_node[3]

            if (node_index == goal):
                budget = total_budget_to_this_node
                final_cost = cost_to_this_node
                parent[node_index] = parent_node_index
                self.get_path(parent, start, goal)
                print("\nShortest distance: ", final_cost)
                print("\nTotal energy cost: ", budget)
                print("\nTotal nodes expanded: ", total_nodes_expanded_counter)
                return
            elif (node_index not in visited):
                total_nodes_expanded_counter += 1

                visited.append(node_index)
                parent[node_index] = parent_node_index

                for child in self.graph[node_index]:
                    string_param = node_index+','+child

                    total_budget_to_child = self.cost[string_param] + \
                        total_budget_to_this_node

                    if total_budget_to_child > self.BUDGET_CONSTRAINT:  # if budget too high, do not add this node to the pq
                        continue

                    cost_to_child = self.dist[string_param] + cost_to_this_node

                    pq_node = [cost_to_child,
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


if __name__ == "__main__":
    g = json.load(open("G.json"))
    dist = json.load(open("Dist.json"))
    cost = json.load(open("Cost.json"))
    # combined_cost = {}
    # print(len(dist),len(cost))
    # for key in dist:
    #     combined_cost[key] = dist[key] + cost[key]

    graph = Graph(g, dist, cost)
    graph.uniform_cost_search(1, 50)
