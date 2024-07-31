import threading
import time
from colorama import Fore

from utils.process import add_process_to_queue, handle_processes_finished, is_finished_flag
from utils.queue import Queue
from utils.log import log

quantum = 2

def execute_process(processes_queue):
    timer = threading.Timer(5, handle_processes_finished)
    timer.start()

    while not is_finished_flag.is_set():
        if not processes_queue.is_empty():
            timer.cancel()

            process = processes_queue.dequeue()
            quantum_counter = 0

            while quantum_counter < quantum and process.runtime != 0:
                process.runtime -= 1
                quantum_counter += 1

                log(f'{process.name} executando...')

                time.sleep(1)

            if process.runtime == 0:
                process.set_finished()
                log(f'{process.name} finalizado com sucesso!', Fore.GREEN)
            else:
                processes_queue.enqueue(process)

            timer = threading.Timer(5, handle_processes_finished)
            timer.start()
        else:
            time.sleep(1)

    log(f'Finalizando scheduler pois não há mais processos na fila', Fore.YELLOW)
    is_finished_flag.clear()

def start_scheduler(processes):
    queue = Queue()

    add_process_thread = threading.Thread(target=add_process_to_queue, args=(processes, queue))
    execute_process_thread = threading.Thread(target=execute_process, args=(queue,))

    log('Inicializando scheduler round robin', Fore.YELLOW)

    add_process_thread.start()
    execute_process_thread.start()

    add_process_thread.join()
    execute_process_thread.join()