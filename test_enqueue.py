import time
import datetime
from tasks import test_priority_task

def write_to_log(data):
    with open('/rabbitmq/celery/priority_test_output', 'a') as output_log:
        output_log.write(data + '\n')

# TEST 1 - correct prioritization
write_to_log('TEST 1: Enqueue 10 low priority tasks and immediately a high priority task. Ensure the high priority task runs before the low prior ones finish.')
write_to_log('TEST 1: Enqueueing 10 low priority tasks now...')
for i in range(10):
    test_priority_task.apply_async(('low priority', 5), queue='tasks', priority=5)

# put a high priority task and see if it runs sooner than the low pr tasks finish
write_to_log('TEST 1: Enqueueing priority task now...')
test_priority_task.apply_async(('high priority', 1), queue='tasks', priority=1)

write_to_log('Sleeping 60 seconds to ensure that queue flushes before second test...')
time.sleep(60)

# TEST 2 - default task priority
write_to_log('TEST 2: Test that the default priority set (2) holds for unprioritizd tasks, i.e. that setting TASK_DEFAULT_PRIORITY works.')
write_to_log('TEST 2: Enqueueing 10 low priority tasks now...')
for i in range(10):
    test_priority_task.apply_async(('low priority', 'NO PRIORITY')) # note no actual prior, just the param to the task for logging
write_to_log('TEST 2: Enqueueing priority task now...')
test_priority_task.apply_async(('high priority', 1), queue='tasks', priority=1)
