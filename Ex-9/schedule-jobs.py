class Job:
    
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs, max_deadline):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    schedule = [-1] * max_deadline  # -1 indicates the slot is free
    total_profit = 0

    for job in jobs:
        for j in range(min(max_deadline - 1, job.deadline - 1), -1, -1):
            if schedule[j] == -1:
                schedule[j] = job.job_id
                total_profit += job.profit
                break

    scheduled_jobs = [job_id for job_id in schedule if job_id != -1]
    return scheduled_jobs, total_profit

jobs = [
    Job('a', 2, 100),
    Job('b', 1, 19),
    Job('c', 2, 27),
    Job('d', 1, 25),
    Job('e', 3, 15)
]

max_deadline = max(job.deadline for job in jobs)
scheduled_jobs, total_profit = job_scheduling(jobs, max_deadline)
print(f"Scheduled Jobs: {scheduled_jobs}")
print(f"Total Profit: {total_profit}")
