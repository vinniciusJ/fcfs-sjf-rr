from utils.process import start_non_preemptive_scheduler

def start_sjf_scheduler(processes):
    start_non_preemptive_scheduler(processes, True)