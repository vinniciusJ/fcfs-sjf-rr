import threading
import time
from utils.log import log
from colorama import Fore

from utils.queue import Queue


def add_process_to_queue(processes, process_queue):
    def add_process(process):
        process_queue.enqueue(process)
        log(f'{process.name} entrou na fila de execução', Fore.BLUE)

    for process in processes:
        timer = threading.Timer(process.arrival_time, add_process, args=[process])
        timer.start()


def execute_process(process_queue):
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


def start_fcfs_scheduler(processes):
    queue = Queue()

    add_process_thread = threading.Thread(target=add_process_to_queue, args=(processes, queue))
    execute_process_thread = threading.Thread(target=execute_process, args=(queue,))

    add_process_thread.start()
    execute_process_thread.start()

    add_process_thread.join()
    execute_process_thread.join()