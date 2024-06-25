import celery.states as states
from flask import Flask, Response
from flask import url_for, jsonify
from worker import celery

app = Flask(__name__)


@app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
    task = celery.send_task('tasks.add', args=[param1, param2], kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response


@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        print('-------PENDING--------')
        return res.state
    elif res.state != states.FAILURE:
        print('------------NO FAILURE--------')
        result = res.result
        return f"Task result: {result}"
    else:
        print('-----------_ELSE--------')
        return str(res.result)


@app.route('/')
def home() -> Response:
    return jsonify("Welcome!!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)