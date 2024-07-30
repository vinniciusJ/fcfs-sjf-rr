import threading
import time
from colorama import Fore

from utils.log import log
from utils.queue import Queue
from utils.process import add_process_to_queue

def execute_processes(process_queue):
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
    execute_process_thread = threading.Thread(target=execute_processes, args=(queue,))

    add_process_thread.start()
    execute_process_thread.start()

    add_process_thread.join()
    execute_process_thread.join()