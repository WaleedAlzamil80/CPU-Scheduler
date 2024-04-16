class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.original_burst_time = burst_time
        self.priority = priority
        self.done = False

    @staticmethod
    def print_process(processes: list, avg_waiting_time, avg_turnaround_time):
        print("\nProcess_ID\tArrival_Time\tBurst_Time\tCompletion_Time\tTurnaround_Time\tWaiting_Time\tPriority")
        for process in processes:
            print(f"{process.pid}\t\t{process.arrival_time}\t\t{process.original_burst_time}\t\t"
                  f"{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}\t\t"
                  f"{process.priority}")
        print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
        print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
        print("---------------------------------------------------------------------------------------------")
