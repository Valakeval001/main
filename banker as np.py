#123
import numpy as np

num_processes = 5
num_resources = 3


allocation = np.array([[1, 2, 2], [2, 1, 1], [1, 3, 5], [0, 6, 3], [2, 1, 1]])
maximum = np.array([[6, 4, 3], [4, 3, 2], [7, 5, 6], [3, 7, 5], [5, 4, 3]])
available = np.array([4, 3, 2])

need = maximum - allocation
print("need data",need)
def is_safe():
    work = available.copy()
    finish = [False] * num_processes
    safe_sequence = []
    while len(safe_sequence) < num_processes:
        found_process = False
        for i in range(num_processes):
            if not finish[i] and all(need[i] <= work):
                work += allocation[i]
                safe_sequence.append(i)
                finish[i] = True
                found_process = True

        if not found_process:
            return False, []

    return True, safe_sequence

def request_resources(process_num, request):
    
    global available, allocation, need

    if any(request > need[process_num]):
        print("Error: Process has exceeded its maximum claim.")
        return False

    if all(request <= available):
        available -= request
        allocation[process_num] += request
        need[process_num] -= request

        safe, sequence = is_safe()
        if safe:
            print(f"Request granted. Safe sequence: {sequence}")
            return True
        else:
            print("Request denied to avoid unsafe state.")
            available += request
            allocation[process_num] -= request
            need[process_num] += request
            return False
    else:
        print("Error: Not enough resources available.")
        return False


print("Initial system state:")
print("Allocation matrix:\n", allocation)
print("Maximum matrix:\n", maximum)
print("Available resources:", available)
print("Need matrix:\n", need)


safe, sequence = is_safe()
if safe:
    print("System is in a safe state. Safe sequence:", sequence)
else:
    print("System is not in a safe state.")


process_num = 1
for i in allocation:
     request = np.array(i)
     print(f"\nProcess {process_num} requesting resources: {request}")
     
request_resources(process_num, request)
