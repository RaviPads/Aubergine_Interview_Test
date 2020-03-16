from __future__ import absolute_import
from aubergine.celery import app


@app.task(bind=True, ignore_result=True, queue='aubergine')
def print_hello(self):
    print('hello there')


@app.task(bind=True, queue='aubergine')
def add(self, x, y):
    return x + y
