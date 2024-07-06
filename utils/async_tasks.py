import asyncio
from tasks import tasks

async def long_running_task(task_id):
    print(f"Task {task_id} started")
    await asyncio.sleep(20)
    print(f"Task {task_id} completed sleep")
    tasks[task_id]['status'] = 'completed'
    tasks[task_id]['result'] = 'Task result data'
    print(f"Task {task_id} updated status")

def run_long_running_task(task_id):
    print(f"Running task {task_id} in new thread")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(long_running_task(task_id))
    loop.close()
