class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def sjf_scheduling(processes):
    current_time = 0
    total_waiting_time = 0
    num_processes = len(processes)

    while processes:
        ready_processes = [p for p in processes if p.arrival_time <= current_time]
        
        if not ready_processes:
            current_time += 1
            continue
        
        shortest_job = min(ready_processes, key=lambda x: x.burst_time)
        processes.remove(shortest_job)
        
        waiting_time = current_time - shortest_job.arrival_time
        total_waiting_time += waiting_time
        
        print(f"{shortest_job.name}\t{shortest_job.arrival_time}\t\t{shortest_job.burst_time}\t\t{waiting_time}")
        
        current_time += shortest_job.burst_time  # Update current time

    average_waiting_time = total_waiting_time / num_processes  # Calculate average waiting time
    print(f"\nAverage Waiting Time: {average_waiting_time:.2f}")

if __name__ == "__main__":
    processes = [
        Process("P1", 0, 6),
        Process("P2", 1, 8),
        Process("P3", 2, 7),
        Process("P4", 3, 3),
    ]

    sjf_scheduling(processes)