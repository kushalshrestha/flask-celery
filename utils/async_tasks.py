import asyncio
from tasks import tasks

async def long_running_task(task_id):
    # Simulate a task that takes 20 seconds
    print(f"Task {task_id} started")
    await asyncio.sleep(20)
    print(f"Task {task_id} completed sleep")
    tasks[task_id]['status'] = 'completed'
    tasks[task_id]['result'] = 'Task result data'
    print(f"Task {task_id} updated status")

async def another_long_running_task(task_id):
    # Simulate another task that takes 30 seconds
    print(f"Another Task {task_id} started")
    await asyncio.sleep(30)
    print(f"Another Task {task_id} completed sleep")
    tasks[task_id]['status'] = 'completed'
    tasks[task_id]['result'] = 'Another Task result data'
    print(f"Another Task {task_id} updated status")

def run_long_running_task(task_id, task_function):
    # Function to run any given task function with its own event loop
    print(f"Running {task_function.__name__} for task {task_id} in new thread")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(task_function(task_id))
    loop.close()