import threading
from colorama import Fore

from utils.log import log
class Process:
    def __init__(self, name, arrival_time, runtime):
        self.name = name
        self.arrival_time = arrival_time
        self.runtime = runtime
        self.is_finished = False

    def set_finished(self):
        self.is_finished = True

    def __str__(self):
        return f'[{self.name} = ({self.arrival_time}, {self.runtime})]'

def read_processes_from_file(filename):
    processes = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            parts = line.strip().split(':')

            name = parts[0].strip()
            times = parts[1].strip().strip('()').split(',')
            arrival_time = int(times[0].strip())
            runtime = int(times[1].strip())

            processes.append(Process(name, arrival_time, runtime))

    return processes

def add_process_to_queue(processes, process_queue):
    def add_process(process):
        process_queue.enqueue(process)
        log(f'{process.name} entrou na fila de execução', Fore.BLUE)

    for process in processes:
        timer = threading.Timer(process.arrival_time, add_process, args=[process])
        timer.start()