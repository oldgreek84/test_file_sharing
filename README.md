# test_file_sharing
Test file sharing service on flask framework

## to run app

- clone repository
- enter in dir
```bash
cd test_file_sharing
```
- create or run virtual enviroment
```bash
source env/bin/activate
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

after ends time of life file, his will be deleted from server and database.
