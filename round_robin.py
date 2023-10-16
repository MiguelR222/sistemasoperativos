class Process:
    def __init__(self, name, burst_time):
        self.name = name
        self.burst_time = burst_time
        self.remaining_time = burst_time

def round_robin_scheduling(processes, time_quantum):
    queue = processes.copy()
    timeline = []
    current_time = 0

    while queue:
        current_process = queue.pop(0)
        if current_process.remaining_time <= time_quantum:
            timeline.append((current_process.name, current_time, current_time + current_process.remaining_time))
            current_time += current_process.remaining_time
            current_process.remaining_time = 0
        else:
            timeline.append((current_process.name, current_time, current_time + time_quantum))
            current_time += time_quantum
            current_process.remaining_time -= time_quantum
            queue.append(current_process)

    return timeline

if __name__ == "__main__":
    processes = [
        Process("P1", 10),
        Process("P2", 5),
        Process("P3", 8),
        Process("P4", 4),
    ]
    time_quantum = 3

    timeline = round_robin_scheduling(processes, time_quantum)

    print("Round Robin Scheduling Timeline:")
    for entry in timeline:
        print(f"Process {entry[0]} - [{entry[1]} - {entry[2]}]")

