import paramiko
import time
import getpass
from subprocess import call


class Sconveer:
    def __init__(self, in_data, rPath, verbose):
        self.in_data = in_data
        self.verbose = verbose
        self.rPath = rPath
        output = []
        self.start_conveer(in_data, verbose, output)
        if verbose != '-v':
            self.write_log(output, rPath)

    def start_conveer(self, in_data, verbose, output):
        pwd = getpass.getpass()
        with open(in_data, 'r') as data:
            for raw_line in data:
                line = raw_line.split(',')
                hostN = line[0][2:-1]
                userN = line[1][2:-1]
                commands = line[3:]
                for s in commands:
                    command = s.split('\'')[1]
                    print(hostN, command)
                    self.connect_ssh(hostN, userN, pwd, command,
                                     verbose, output)

    def connect_ssh(self, hostN, userN, pwd, commanD, verbose, output):
        #  ==connect block==
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostN, username=userN, password=pwd)
        if "sudo" in commanD:
            stdin, stdout, stderr = ssh.exec_command(commanD, get_pty=True)
            time.sleep(1)
            stdin.write(pwd + "\n")
            stdin.flush()
        else:
            stdin, stdout, stderr = ssh.exec_command(commanD)
        #  ==end connect block==

        data = stdout.readlines()  # get data from paramiko pipe

        #  ==output==
        if verbose == '-v':
            for line in data:
                print("\t\t//=>", line, end="")
                time.sleep(0.1)
            print("*"*15)
        else:
            tmpfile = "/tmp/sconv_{0}_{1}.tmp".format(time.ctime(
                                     time.time()).replace(" ", ""), hostN)
            with open(tmpfile, 'w') as f:
                print("Start == [{0}] ==".format(hostN), file=f)
                for line in data:
                    if "Reading package lists" in line:
                        line = ''
                    if "[sudo] password for" in line:
                        line = ''
                    if "Reading state information" in line:
                        line = ''
                    if "Building dependency tree" in line:
                        line = ''
                    print(line, end="", file=f)
                print("End   == [{0}] ==\n\n".format(hostN), file=f)
            output.append(tmpfile)
        #  ==end output==

    def write_log(self, output, rPath):
        filename = rPath + "/output/sconv_res_{0}.log".format(time.ctime(
                                     time.time()).replace(" ", ""))
        with open(filename, 'w') as outfile:
            for fname in output:
                with open(fname) as infile:
                    outfile.write(infile.read())
        with open(filename, 'r') as log:
            for line in log:
                print(line, end="")
