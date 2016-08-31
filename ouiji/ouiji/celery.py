from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ouiji.settings')
app = Celery('ouiji')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(['ouiji_finance'], force=True)
print(app.tasks.periodic())
print(app.tasks.regular())
@app.task(bind=True)
def debug_task(self):
	print('Request: {0!r}'.format(self.request))
