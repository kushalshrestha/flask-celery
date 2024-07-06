# Flask Celery Project with Redis and Flower

This is a simple Python Flask project that utilizes Celery for asynchronous task processing, Redis as a message broker and result backend, and Flower for monitoring Celery tasks.



### Prerequisites

Make sure you have Python and pip installed on your system.

### Setup Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
python -m venv venv
```
Activate the virtual environment:

```bash
On Unix or MacOS:
source venv/bin/activate

On Windows:
venv\Scripts\activate
```



### Install Dependencies
Install the required Python packages listed in requirements.txt:

```bash
pip install -r requirements.txt
``` 
### Running the Application
#### Start the Flask application:

```bash
python app.py
```

#### Start the Celery worker:
```bash
celery -A tasks worker --loglevel=debug
```

#### (Optional) Start Celery Flower for monitoring:

```bash
celery -A tasks flower --port=5555
```
#### Usage
Once the application is running, you can access it at http://localhost:5000/. Here are the available endpoints:

- `/add/<int:param1>/<int:param2>`: This endpoint triggers a Celery task to add two numbers. It returns a link to check the status of the task.
- `/check/<string:task_id>`: This endpoint checks the status of a specific task identified by its ID.
- `/`: Home endpoint displaying a welcome message.

#### Celery Configuration
Celery is configured to use Redis as the message broker and result backend. The configuration can be found in worker.py and tasks.py.

#### Notes

Installing and Running Redis:
```bash
brew install redis
brew services start redis

# testing redis
redis-cli ping  # should return PONG
```

### PID and Killing Process
```bash
lsof -i tcp:<PORT_NUMBER>

kill -15 <PID>
```