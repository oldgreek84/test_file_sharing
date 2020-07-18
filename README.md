# test_file_sharing
Test file sharing service on flask framework

Link to deloyed app:

 - [link to app on Heroku](https://test-sharing-app.herokuapp.com/)

## to run app

- clone repository
- enter in dir
```bash
cd test_file_sharing
```
- create and run virtual enviroment
```bash
virualenv env
source env/bin/activate
pip3 install -r requirements.txt
```
- run migration of database
```bash
flask db init
flask db migrate
flask db upgrade
```
- run app
```bash
python3 main.py
```

## work with tasks

task work with celery and redis.

- install celery and redis
```bash
pip3 install celery redis
```

- run celery worker:
```bash
celery worker -A app.client --loglevel=info
```
- run celery for periodic tasks in new terminal:
```bash
celery -A app.client beat -s celerybeat-schedule
```
- or run in one worker:
```bash
celery worker -A app.client -B -s ./celerybeat-schedule --loglevel=info -E
```

- for app for monitoring tasks - flower:
```bash
celery -A app.client flower
```

After ends time of life file, his will be deleted from server and database.
Check all old files every day at 00:00 on UTC. 
