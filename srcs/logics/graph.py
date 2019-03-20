from .devises import Devises
import networkx as nx

class Graph:

    GRAPH = None

    def __init__(self):
        self.GRAPH = nx.Graph()

    def build(self, devises):
        for devises_nodes, devises_nodes_value in devises.RATE.items():
            if self.GRAPH.has_node(devises_nodes) is False:
                self.GRAPH.add_node(devises_nodes)
            for devises_edges, devises_edges_value in devises_nodes_value.items():
                if self.GRAPH.has_node(devises_edges) is False:
                    self.GRAPH.add_node(devises_edges)
                self.GRAPH.add_edge(devises_nodes, devises_edges)
                self.GRAPH[devises_nodes][devises_edges][(devises_nodes, devises_edges)] = round(float(devises_edges_value), 4)
                self.GRAPH[devises_nodes][devises_edges][(devises_edges, devises_nodes)] = round(1 / float(devises_edges_value), 4)

    def get_step(self, D1, D2, AMOUNT):
        i = 0
        path = nx.shortest_path(self.GRAPH, D1, D2)
        rate = 0
        print("You have {} {} and want to have {}".format(round(AMOUNT), D1.decode('utf-8'), D2.decode('utf-8')))
        while i < (len(path) - 1):
            edge = self.GRAPH.edges[path[i], path[i+1]]
            rate = edge[(path[i], path[i+1])]
            tmp = round(AMOUNT * rate, 4)
            print("{} -> {} = {} * {} = {}".format(\
            path[i].decode('utf-8'), path[i+1].decode('utf-8'), AMOUNT, rate, tmp))
            AMOUNT = tmp
            i += 1
        print("You have {} {}".format(round(AMOUNT), D2.decode('utf-8')))

    def process(self, devises):
        self.build(devises)
        self.get_step(devises.D1, devises.D2, devises.AMOUNT)