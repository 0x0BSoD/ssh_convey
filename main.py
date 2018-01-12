#!/usr/local/bin/python3
from data import worker
from data import param_pars
from data import bc
import os
import sys


def main():
    # Where I
    tmp = os.path.realpath(__file__).split("/")
    del(tmp[0], tmp[-1])
    rPath = ''
    for i in tmp:
        rPath += '/' + i

    if (len(sys.argv) > 2):
        in_data = sys.argv[1]
        verbose = sys.argv[2]
    else:
        in_data = rPath + "/input/in_data"
        verbose = ''

    path = rPath + "/input/parsed.dat"
    if os.path.exists(path):
        os.remove(path)

    bc.ok("Alex SSH!")

    # ==
    param_pars.Param_Pars(in_data, path)
    worker.Sconveer(path, rPath, verbose)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye...")
