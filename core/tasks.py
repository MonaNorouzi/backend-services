import time 
import random
from celery import shared_task
import time
import random
from celery import shared_task

@shared_task
def simulate_task():
    time.sleep(60)
    if random.random() < 0.5:
        raise Exception("simulated task failed")
    return {"status": "success","message": "task completed"}
