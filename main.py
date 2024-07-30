from utils.process import read_processes_from_file
from schedulers import fcfs, sjf
def start_process_scheduler():
    processes = read_processes_from_file('processes.txt')

    # start_fcfs_scheduler(processes)
    sjf.start_sjf_scheduler(processes)

if __name__ == '__main__':
   start_process_scheduler()


