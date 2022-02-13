
from dis import dis
import json

# implementation of question 1 with Uniform cost search


class Graph:

    def __init__(self, graph, dist):

        # graph -> disctionary => graph["node"] = ["node1","node2"]
        self.graph = graph
        # dist -> dictionary => dist["node,node2"]
        self.dist = dist
        self.V = len(graph)

    def uniform_cost_search(self, start, goal):
        # start and goal are string of node index
        # assuming only 1 goal

        # initialisation
        start = str(start)
        goal = str(goal)
        parent = {}
        final_cost = 0
        visited = []

        pq = []
        # [cost to this node, node_index, parent_node]
        pq_node = [0, start, "-1"]

        pq.append(pq_node)

        while (len(pq) > 0):  # while pq is not empty
            pq.sort()
            current_pq_node = pq.pop(0)

            cost_to_this_node = current_pq_node[0]
            node_index = current_pq_node[1]
            parent_node_index = current_pq_node[2]

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
                    print(string_param)
                    cost_to_child = self.dist[string_param] + cost_to_this_node

                    pq_node = [cost_to_child, child, node_index]
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
    graph = Graph(g, dist)
    graph.uniform_cost_search(1, 50)
