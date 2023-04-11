import os
import django
from celery import Celery
from celery.schedules import crontab


# Initialise l'application Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_blog.settings')
django.setup()

app = Celery('my_blog')
from app.models import NewsLetter
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=0, minute=1, day_of_week=0),
        check_valide_mail.s(),
        name='Check valide mail for news letter'
    )


@app.task
def check_valide_mail():
    emails = NewsLetter.objects.filter(abonnement=False)
    for email in emails:
        email.delete()
        email.save()