import argparse
from logics.devises import Devises
from logics.graph import Graph

class LuccaConverter:

    DEVISES = None
    GRAPH = None

    # Initialize main variable and parse the file pass in parameter.
    def __init__(self, f):
        self.DEVISES = Devises(f)
        self.GRAPH = Graph()

    # Create and render
    # Call our two main function:
    # -  Build who build the graph and get_step who
    # solve the shortest path and print the result
    def process(self):
        self.GRAPH.build(self.DEVISES)
        self.GRAPH.get_step(self.DEVISES)

if __name__ == '__main__':
    lc = None
    argumentparser = argparse.ArgumentParser(description="LuccaDevise.py -f <file contains devises>")
    argumentparser.add_argument('-f', '--file', help='--file <file>')
    args = argumentparser.parse_args()
    try:
        lc = LuccaConverter(args.file)
        lc.process()
    except Exception as e:
        print("You raise an exception:\n{}".format(e))
    
