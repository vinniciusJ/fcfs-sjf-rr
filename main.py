from utils.process import read_processes_from_file
from schedulers import fcfs, sjf, rr

if __name__ == '__main__':
   fcfs.start_scheduler(read_processes_from_file('processes.txt'))
   sjf.start_scheduler(read_processes_from_file('processes.txt'))
   rr.start_scheduler(read_processes_from_file('processes.txt'))
