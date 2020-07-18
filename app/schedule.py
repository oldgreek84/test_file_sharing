from datetime import timedelta

from celery.schedules import crontab
from app import client
from app.tasks import clear_all


# for run tasks:

# run only worker:
# $ celery worker -A app.client --loglevel=info -E

# run periodic task:
# $ celery -A app.client -B -s celerybeat-schedule 


client.conf.beat_schedule= {
   'clean_all_day': {
     'task': 'app.tasks.clear_all',
     'schedule': crontab(hour=0, minute=0),
  },
}
client.conf.timezone = 'UTC'
