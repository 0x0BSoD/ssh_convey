import multiprocessing
import time


class Threadconnect:
    def __init__(self, task):
        self.task = task
        self.makeThreads(task)

    def makeThreads(self, task):
        cpus = multiprocessing.cpu_count()
        jobs = []
        print("Cores: {0}".format(cpus))
        i = 1
        while cpus != 0:
            tmp = multiprocessing.Process(target=task)
            jobs.append(tmp)
            tmp.start()
            print("Job {0} start on {1}".format(i, time.ctime(time.time())))
            i += 1
            cpus -= 1
