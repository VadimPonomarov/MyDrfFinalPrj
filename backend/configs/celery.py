import os

from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

app = Celery('configs')
app.config_from_object('django.conf.settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'send_spam_every_minutes': {
    #     "task": "core.services.email_services.spam",
    #     "schedule": crontab(minute='*/5')
    # }
}
