import os
import sys


def name():
    return os.path.splitext(os.path.basename(sys.argv[0]))[0]


def table_name():
    return name().replace("-", "_")


def dir():
    return os.getcwd()


def run_x_times(x, f):
    for i in range(0, x):
        print("===== RUN %s/%s =====" % (i, x))
        f()