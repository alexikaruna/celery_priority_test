import time
import datetime
from tasks import test_priority_task

def write_to_log(data):
    with open('/rabbitmq/celery/priority_test_output', 'a') as output_log:
        output_log.write(data + '\n')

for i in range(10):
  for i in range(5):
      test_priority_task.apply_async(('low priority', 5), queue='tasks', priority=5)
      write_to_log('Enqueued one low priority task...')
  time.sleep(3)
