import os
import sys


def name():
    return os.path.splitext(os.path.basename(sys.argv[0]))[0]
