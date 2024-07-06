from flask_restful import Resource
from tasks import tasks

class TaskStatus(Resource):
    def get(self, task_id):
        task = tasks.get(task_id)
        if not task:
            return {'message': 'Task not found'}, 404
        return task
