import time
from instance import job_manager


@job_manager.job
def long_running_task():
    print("Starting long running task")
    time.sleep(10)
    print("Task completed")

def test_long_running_task():
    for _ in range(5):
        long_running_task()

    with job_manager.wait():
        print("Waiting for task to complete")

test_long_running_task()