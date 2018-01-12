class Parser:
    def __init__(self, in_data='input/in_data_new', out_data='input/parsed.dat'):
        self.in_data = in_data
        self.out_data = out_data
        self.parse(self.in_data, self.out_data)

    def parse(self, in_data, out_data):


        with open(in_data, 'r') as data:
            for line in data:
                if line.strip()[:1] == "#":
                    pass
                else:
                    if line[:4] == 'USER':
                        print("Global user: ", line.strip()[5:])
                    if line[:4] == 'PASS':
                        print("Global password: ", line.strip()[5:])
                    if line[:4] == 'host':
                        print("Host: ", line.strip()[5:])
                    if line[:4] == 'user':
                        print("Local user: ", line.strip()[5:])
                    if line[:12] == '    commands':
                        print("Commands start: ")
                    if line[:11] == '    install':
                        print("Install start: ")

    def commands(self, line):
        print(line.rstrip())

Parser()
