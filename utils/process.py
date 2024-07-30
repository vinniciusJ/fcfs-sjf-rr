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