from colorama import Fore

from utils.log import log
from utils.process import start_non_preemptive_scheduler

def start_scheduler(processes):
    log(f'Inicializando scheduler FCFS', Fore.YELLOW)
    start_non_preemptive_scheduler(processes)