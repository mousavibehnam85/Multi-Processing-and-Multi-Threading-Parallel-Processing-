# tasks.py
import os
import time

def cpu_task(task_id):
    print(f"Task {task_id} running in process ID {os.getpid()}")
    start_time = time.time()
    for _ in range(10 ** 7):
        pass
    end_time = time.time()
    print(f"Task {task_id} finished in {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    # You can add any testing code here if needed
    pass