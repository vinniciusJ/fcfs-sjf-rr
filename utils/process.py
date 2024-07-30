import threading
import time
from colorama import Fore

from utils.log import log
from utils.queue import Queue
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

    def __lt__(self, other):
        return self.runtime < other.runtime

    def __le__(self, other):
        return self.runtime <= other.runtime

    def __gt__(self, other):
        return self.runtime > other.runtime

    def __ge__(self, other):
        return self.runtime >= other.runtime

    def __eq__(self, other):
        return self.runtime == other.runtime

    def __ne__(self, other):
        return self.runtime != other.runtime

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

def add_process_to_queue(processes, process_queue, sorted=False):
    def add_process(process):
        process_queue.enqueue(process)
        log(f'{process.name} entrou na fila de execução', Fore.BLUE)

        if sorted:
            process_queue.sort()

    for process in processes:
        timer = threading.Timer(process.arrival_time, add_process, args=[process])
        timer.start()

def execute_non_preemptive_processes(process_queue):
    while True:
        if not process_queue.is_empty():
            process = process_queue.dequeue()

            while process.runtime > 0:
                process.runtime -= 1
                log(f'{process.name} executando...')

                time.sleep(1)

            log(f'{process.name} finalizado com sucesso!', Fore.GREEN)
            process.set_finished()
        else:
            time.sleep(1)

def start_non_preemptive_scheduler(processes, sorted=False):
    queue = Queue()

    add_process_thread = threading.Thread(target=add_process_to_queue, args=(processes, queue, sorted))
    execute_process_thread = threading.Thread(target=execute_non_preemptive_processes, args=(queue,))

    add_process_thread.start()
    execute_process_thread.start()

    add_process_thread.join()
    execute_process_thread.join()