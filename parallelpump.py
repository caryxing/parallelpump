#!/usr/bin/python
# Pump the items in a list with multi processes.

import sys
import os
import multiprocessing
from multiprocessing import Process, Value, Manager

class Parapump:
    def __init__(self, func, listToParallelize, numJobs, sharedInfo = None):
        manager = Manager()
        sharedItems = manager.list(listToParallelize)
        computedCount = Value('i', -1)

        mutex = multiprocessing.Lock()
        mutexCnt = multiprocessing.Lock()

        self.subprocs = []
        for i in xrange(numJobs):
            procArgs = (i, sharedItems, sharedInfo, computedCount, mutex, mutexCnt, func, )
            proc = Process(target = subprocWorker, args = procArgs)
            self.subprocs.append(proc)


    def printError(self, text):
        sys.stderr.write(text+"\n")


    def run(self):
        startedProcs = []
        for (idx, proc) in enumerate(self.subprocs):
            try:
                proc.start()
                startedProcs.append(proc)
            except Exception, e:
                self.printError("Error: unable to start sub process-" + str(idx))

        for proc in startedProcs:
            proc.join()


def subprocWorker(id, sharedItems, sharedInfo, computedCount, mutex, mutexCnt, func):
    total = len(sharedItems)

    while True:
        mutexCnt.acquire()
        computedCount.value += 1
        idx = computedCount.value
        mutexCnt.release()
        if idx >= total:
            break

        item = sharedItems[idx]
        func(item, mutex, sharedInfo)

