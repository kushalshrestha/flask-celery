from flask_restful import Resource
import threading
import uuid
from utils.async_tasks import run_long_running_task
from tasks import tasks

class StartTask(Resource):
    def get(self):
        task_id = str(uuid.uuid4())
        tasks[task_id] = {'status': 'in process', 'result': None}
        print(f"Starting task {task_id}")
        threading.Thread(target=run_long_running_task, args=(task_id,)).start()
        return {'task_id': task_id, 'status': 'Task is in process'}, 202
