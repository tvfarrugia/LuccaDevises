from .devises import Devises
import networkx as nx

class Graph:

    GRAPH = None

    def __init__(self):
        self.GRAPH = nx.Graph()

    # As the name talk this method will build our graph
    # with the help of the networkx api: https://networkx.github.io/
    # The graph is construct like this:
    # Currency->edge->Currency->edge ....:
    # Each edge has an attribute who contains two variable:
    #   - CurrencyA to CurrencyB
    #   - CurrencyB to CurrencyA
    def build(self, devises):
        for devises_nodes, devises_nodes_value in devises.RATE.items():
            if self.GRAPH.has_node(devises_nodes) is False:
                self.GRAPH.add_node(devises_nodes)
            for devises_edges, devises_edges_value in devises_nodes_value.items():
                if self.GRAPH.has_node(devises_edges) is False:
                    self.GRAPH.add_node(devises_edges)
                self.GRAPH.add_edge(devises_nodes, devises_edges)
                self.GRAPH[devises_nodes][devises_edges][(devises_nodes, devises_edges)] =\
                    round(float(devises_edges_value), 4)
                self.GRAPH[devises_nodes][devises_edges][(devises_edges, devises_nodes)] =\
                    round(1 / float(devises_edges_value), 4)

    # Get step is our algorithm and print who calculate the amount of
    # currency converted and print the step.
    def get_step(self, devises):
        i = 0
        path = nx.shortest_path(self.GRAPH, devises.D1, devises.D2)
        rate = 0
        print("You have {} {} and want to have {}".format(round(devises.AMOUNT),\
        devises.D1.decode('utf-8'), devises.D2.decode('utf-8')))
        while i < (len(path) - 1):
            edge = self.GRAPH.edges[path[i], path[i+1]]
            rate = edge[(path[i], path[i+1])]
            tmp = round(devises.AMOUNT * rate, 4)
            print("{} -> {} = {} * {} = {}".format(\
            path[i].decode('utf-8'), path[i+1].decode('utf-8'), devises.AMOUNT, rate, tmp))
            devises.AMOUNT = tmp
            i += 1
        print("You have {} {}".format(round(devises.AMOUNT), devises.D2.decode('utf-8')))