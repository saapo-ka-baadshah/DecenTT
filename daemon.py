#!venv/bin/python3
import os
import time

from DecenTT.IPFS import Daemon
import sys


def daemon(detatched=False):
    d = Daemon(shell=False).daemon
    if not detatched:
        d.communicate()
    else:
        return


if __name__ == "__main__":
    if "-d" in list(sys.argv):
        print("Running in Detached mode!")
        daemon(detatched=True)
        time.sleep(2)
        exit()
    else:
        daemon()

