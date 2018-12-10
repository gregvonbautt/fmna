#!/usr/bin/python

import os
import random
import subprocess
import sys


def collect():
    os.system("%s/collect.sh %s %s &> /dev/null" % (this_path, experiment, experiment_output))


def cleanup():
    os.system("rm %s &> /dev/null" % experiment_output)


experiment = sys.argv[1]
total = int(sys.argv[2])
case = sys.argv[3]

this_path = os.path.dirname(os.path.realpath(__file__))

exp_dir = "%s/../%s" % (this_path, experiment)
command = "%s/single_run.py" % exp_dir
experiment_output_dir = "%s/results" % exp_dir
experiment_output = "%s/raw_%s.csv" % (experiment_output_dir, case)

collect()
cleanup()

parallelism = 100

for i in range(0, total / parallelism):
    processes = []
    files = []
    for j in range(0, parallelism):
        outfilename = "/var/tmp/%s_%s.txt" % (experiment, random.randint(1e15, 1e16 - 1))
        outfile = open(outfilename, "wb", 0)
        processes.append(subprocess.Popen(command, stdout=outfile, stderr=None))
        files.append(outfile)

    for p in processes:
        os.waitpid(p.pid, 0)
    for f in files:
        f.close()

    collect()
    print(i + 1)

# os.system("%s/build_results.py %s" % (exp_dir, experiment_output))
