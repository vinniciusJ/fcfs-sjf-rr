from utils.process import start_non_preemptive_scheduler
from colorama import Fore

from utils.log import log
def start_scheduler(processes):
    log(f'Inicializando scheduler SJF', Fore.YELLOW)
    start_non_preemptive_scheduler(processes, True)