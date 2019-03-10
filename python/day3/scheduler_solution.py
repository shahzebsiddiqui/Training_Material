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
        bsub = "#BSUB"
        self.script = "#!/bin/bash \n"
        self.script += f"{bsub} -W {self.walltime} \n"
        self.script += f"{bsub} -N {self.nodes} \n"
        if args.tasks:
            self.script += f"{bsub} -n {self.tasks} \n"

        if args.resource:
            self.script+= f"{bsub} -R {self.resource} \n"
        if args.command:
            self.script+= f"{args.command}\n"
    def write(self):

        print(f"Writing to file: {self.file}")
        fd = open(self.file,"w")
        fd.write(self.script)
        fd.close()

        print(f"Content of File {self.file} is the following:")
        os.system(f"cat {self.file}")
    def submit(self):
        cmd = f"bsub < {self.file}"
        print(f"Executing Command: {cmd}")
        os.system(cmd)


class SLURM(Scheduler):
    def generate(self):
        sbatch = "#SBATCH"
        self.script = "#!/bin/bash \n"
        self.script += f"{sbatch} -t {self.walltime} \n"
        self.script += f"{sbatch} -N {self.nodes} \n"
        if args.tasks:
            self.script += f"{sbatch} -n {self.tasks} \n"

        if args.resource:
            self.script += f"{sbatch} -C {self.resource} \n"
        if args.command:
            self.script += f"{args.command}\n"

    def write(self):
        print(f"Writing to file: {self.file}")
        fd = open(self.file, "w")
        fd.write(self.script)
        fd.close()

        print(f"Content of File {self.file} is the following:")
        os.system(f"cat {self.file}")

    def submit(self):
        cmd = f"sbatch {self.file}"
        print(f"Executing Command: {cmd}")
        os.system(cmd)

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
