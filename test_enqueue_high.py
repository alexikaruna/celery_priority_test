import time
import datetime
from tasks import test_priority_task

def write_to_log(data):
    with open('/rabbitmq/celery/priority_test_output', 'a') as output_log:
        output_log.write(data + '\n')

test_priority_task.apply_async(('high priority', 8), queue='tasks', priority=8)
write_to_log('Enqueued high priority task...')
