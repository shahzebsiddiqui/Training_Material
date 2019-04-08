import argparse
import os

class Scheduler:
    def __init__(self,args):
        self.type = args.type
        self.walltime = args.walltime
        self.nodes = args.nodes
        self.tasks = args.tasks
        self.resource = args.resource
        self.command = args.command
        self.file = f"{args.file}.{args.type}"


class LSF(Scheduler):

    def generate(self):
        """ generate the jobscript content"""

        bsub = "#BSUB"
        self.script = "#!/bin/bash \n"

        # TODO: build the string self.script that contains content of job script 

    def write(self):
        """ write the content to file """

        print(f"Writing to file: {self.file}")
        # TODO: Write the content to file

        print(f"Content of File {self.file} is the following:")
        # run cat against the file. use os.system

    def submit(self):
        """ submit job to scheduler """
        
        # TODO: send job to scheduler 


class SLURM(Scheduler):
    def generate(self):
        """ generate the jobscript content"""

        sbatch = "#SBATCH"
        self.script = "#!/bin/bash \n"

        # TODO: build the string self.script that contains content of job script 

    def write(self):
        """ write the content to file """

        print(f"Writing to file: {self.file}")
        # TODO: Write the content to file

        print(f"Content of File {self.file} is the following:")
        # run cat against the file. use os.system

    def submit(self):
        """ submit job to scheduler """

parser = argparse.ArgumentParser(description="scheduler script generator")
parser.add_argument("-t", "--type", help="scheduler type", choices=["slurm","lsf"], default="lsf")
parser.add_argument("-W", "--walltime", help="wall time", required=True)
parser.add_argument("-N", "--nodes", help="number of nodes to allocate", type=int, required=True)
parser.add_argument("-T", "--tasks", help="number of tasks to allocate", type=int)
parser.add_argument("-R", "--resource", help="specify resource flag")
parser.add_argument("-c", "--command", help="specify resource flag", choices=["uptime","hostname"], default="uptime")
parser.add_argument("-f", "--file", help="specify file to write job script", default="job")
parser.add_argument("-s", "--submit", help="submit job to scheduler",action='store_true')
args = parser.parse_args()

if args.type == "lsf":
    job = LSF(args)
    job.generate()

    if args.file:
        job.write()

    if args.submit:
        job.submit()
else:
    job = SLURM(args)
    job.generate()

    if args.file:
        job.write()

    if args.submit:
        job.submit()
