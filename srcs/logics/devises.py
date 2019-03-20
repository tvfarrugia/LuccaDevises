class Devises:
    D1 = None
    D2 = None
    M = None
    AMOUNT = 0

    RATE = dict()
    def __init__(self, f):
        self.process(f)

    # Parse the the line and store rate of currency
    def get_rate(self, line, is_start=False):
        data = line.strip().replace(b'\n', b'').split(b';')
        if is_start is True:
            self.D1 = data[0]
            self.M = data[1]
            self.AMOUNT = float(self.M)
            self.D2 = data[2]
        elif len(data) > 1:
            if data[0] in self.RATE:
                self.RATE[data[0]][data[1]] = data[2]
            else:
                self.RATE[data[0]] = {
                    data[1]: data[2],
                }
    
    # Read the file and call the parser get_rate.
    def process(self, f):
        line = None
        
        with open(f, 'rb') as f:
            while line is not b'':
                line = f.readline()
                if self.D1 is None:
                    self.get_rate(line, True)
                else:
                    self.get_rate(line)