from flask_restful import Resource
import threading
import uuid
from utils.async_tasks import run_long_running_task, long_running_task, another_long_running_task
from tasks import tasks

class StartTask(Resource):
    def get(self):
        task_id_1 = str(uuid.uuid4())
        tasks[task_id_1] = {'status': 'in process', 'result': None}
        print(f"Starting task {task_id_1}")
        threading.Thread(target=run_long_running_task, args=(task_id_1, long_running_task)).start()

        task_id_2 = str(uuid.uuid4())
        tasks[task_id_2] = {'status': 'in process', 'result': None}
        print(f"Starting task {task_id_2}")
        threading.Thread(target=run_long_running_task, args=(task_id_2, another_long_running_task)).start()

        return {'task_id_1': task_id_1, 'task_id_2': task_id_2, 'status': 'Tasks are in process'}, 202