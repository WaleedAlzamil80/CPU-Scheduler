from process import Process


def fcfs(pro: list[Process]):
    pro.sort(key=lambda x: x.arrival_time)
    elapsed, waiting, turnar = 0, 0, 0
    gantt = []
    for p in pro:
        p.waiting_time = max(0, elapsed - p.arrival_time)
        waiting += p.waiting_time
        elapsed += p.burst_time
        p.completion_time = elapsed
        p.turnaround_time = elapsed - p.arrival_time
        p.done = True
        turnar += p.turnaround_time
        gantt += [(p.pid, p.burst_time, p.completion_time)]

    avg_turnaround_time = turnar / len(pro)
    avg_waiting_time = waiting / len(pro)
    #Process.print_process(pro , avg_waiting_time , avg_turnaround_time )

    return gantt



# testing
process_list = []
process_list.append(Process(1, 0, 7))
process_list.append(Process(2, 2, 4))
process_list.append(Process(3, 4, 1))
process_list.append(Process(4, 5, 4))
fcfs(process_list)
