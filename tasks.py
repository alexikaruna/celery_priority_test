# to run the worker:
# celery -A tasks worker --loglevel=info

from celery import Celery
import time

celery_app = Celery()
celeryconfig = {}
celeryconfig['BROKER_URL'] = 'amqp://localhost'
celeryconfig['CELERY_RESULT_BACKEND'] = 'rpc://localhost'
celeryconfig['CELERY_QUEUES'] = {"tasks": {"exchange": "tasks", "binding_key": "tasks", "routing_key": "tasks"}}
celeryconfig['CELERY_DEFAULT_QUEUE'] = "tasks"
celeryconfig['CELERY_ACKS_LATE'] = True
celeryconfig['CELERYD_PREFETCH_MULTIPLIER'] = 1
#celeryconfig['TASK_DEFAULT_PRIORITY'] = 2
celery_app.config_from_object(celeryconfig)

@celery_app.task
def test_priority_task(name, priority):
    output = "Job executed, priority: {}, name: {}".format(priority, name)
    with open('/rabbitmq/celery/priority_test_output', 'a') as output_log:
        output_log.write(output + '\n')
    time.sleep(3)
  
@celery_app.task
def add(x, y):
    return x + y
