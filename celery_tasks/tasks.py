from celery import Celery

# Initialize Celery
celery = Celery('tasks', broker='redis://localhost:6379/0')

# Define a Celery task
@celery.task
def add(x, y):
    return x + y
