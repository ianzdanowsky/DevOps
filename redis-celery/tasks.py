# pylint: disable-all

from celery import Celery
import time
app = Celery('tasks', broker='redis://10.26.70.83:6379')

@app.task
def running(runner, vel):
    dist = 0
    while 1:
        time.sleep(2)
        dist += vel
        print("Corredor {0} esta em {1} metros".format(runner, dist))