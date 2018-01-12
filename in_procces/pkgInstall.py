import os
import platform
from subprocess import call


class pkgInstall:
    """
    Class for installing pakgase from list;
    Chek os and select install method
    """
    def __init__(self, pkgList):
        self.pkgList = pkgList
        c_os = self.checkOS()
        self.doInstall(c_os, pkgList)

    def checkOS(slef):
        tmp = platform.dist()
        if tmp[0] == '':
            tmp = platform.uname()
        # ------
        if tmp[0] == "Darwin":
            print("OSX")
            return "brew"
        elif tmp[0] == "centos":
            print("Centos")
            return "yum"
        elif tmp[0] == "ubuntu" | tmp[0] == "debian":
            print("Deb based")
            return "apt"
        else:
            return 1

    def doInstall(self, c_os, pkgInstall):
        commanD = c_os + " install -y " + pkgInstall
        try:
            call(commanD.split(" "))
        except:
            print("Cannot install")
            return 1


if __name__ == '__main__':
    pkgInstall('1')
