class Param_Pars:
    def __init__(self, in_data='input/in_data', out_data='input/parsed.dat'):
        self.in_data = in_data
        self.out_data = out_data
        self.parser(self.in_data, self.out_data)

    def parser(self, in_data, out_data):
        """ Create flat text file form input """
        # LIKE GLOBAL VARS
        user = ''
        G_USER = ''
        G_PASS = ''
        HOST = ''
        COMMAND_ARR = []
        result = []

        with open(in_data, 'r') as data:
            for line in data:
                if 'USER:' in line:
                    G_USER = (line.split(':')[1]).strip()
                if 'PASS:' in line:
                    G_PASS = (line.split(':')[1]).strip()
                if 'host:' in line:
                    HOST = (line.split(':')[1]).strip()
                if 'user:' in line:
                    user = (line.split(':')[1]).strip()
                if '#' not in line and '--' in line:
                    COMMAND_ARR.append(line.strip()[2:])
                if '}' in line:
                    result.append(HOST)
                    if user != '':
                        result.append(user)
                    else:
                        result.append(G_USER)

                    result.append(G_PASS)
                    result.append(COMMAND_ARR)

                    out = open(out_data, 'a')
                    print(result, file=out)
                    out.close()

                    result = []
                    COMMAND_ARR = []
                    user = ''
        return result


if __name__ == '__main__':
    print(Param_Pars())
