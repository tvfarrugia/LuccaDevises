import argparse
from logics.devises import Devises
from logics.graph import Graph

class LuccaConverter:

    DEVISES = None
    GRAPH = None

    def __init__(self, f):
        self.DEVISES = Devises(f)
        self.GRAPH = Graph()

    def process(self):
        self.GRAPH.process(self.DEVISES)

if __name__ == '__main__':
    lc = None
    argumentparser = argparse.ArgumentParser(description="LuccaDevise.py <file contains devises>")
    argumentparser.add_argument('-f', '--file', help='--file <file>')
    
    args = argumentparser.parse_args()
    try:
        lc = LuccaConverter(args.file)
        lc.process()
    except Exception as e:
        print("You raise an exception:\n{}".format(e))
    