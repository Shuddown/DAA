from random import randint

def cost(cost_matrix: list[list[float]] | list[list[int]]) -> float:
    n = len(cost_matrix)
    sorted_matrix = [sorted(list(enumerate(cost_matrix[i])), 
                            key = lambda x: x[1]) for i in range(n)]
    
    min_values = [sorted_matrix[0][0][1] for _ in range(n)]
    initial_cost = sum(min_values)
    initial_person = 0
    bound = float('inf')
    chosen_jobs = {job : False for job in range(n)}
    
    def min_cost(prev_cost: float, person: int) -> None:
        nonlocal bound
        if(prev_cost >= bound): return
        if(person == n): 
            bound = prev_cost
            return
        
        num_jobs = n
        sorted_jobs = sorted_matrix[person]

        for i in range(num_jobs):
            job_no = sorted_jobs[i][0]
            if chosen_jobs[job_no] == True: continue
            chosen_jobs[job_no] = True
            new_cost = prev_cost - min_values[person] + sorted_jobs[i][1]
            min_cost(new_cost, person + 1)
            chosen_jobs[job_no] = False
    
    min_cost(initial_cost, initial_person)
    return bound


if __name__ == "__main__":
    n = 5 
    costs = [[randint(n, n*n) for _ in range(n)] for _ in range(n)]
    print("Input")
    print(costs)
    print("Output:")
    print("Minimum cost: ", cost(costs))

        
    

    